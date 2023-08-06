"""
/*********************************************************************
* Copyright (c) 2023 the Qrisp Authors
*
* This program and the accompanying materials are made
* available under the terms of the Eclipse Public License 2.0
* which is available at https://www.eclipse.org/legal/epl-2.0/
*
* SPDX-License-Identifier: EPL-2.0
**********************************************************************/
"""


from qrisp.circuit.qubit import Qubit
from qrisp.core.library import mcx, p, rz, x
from qrisp.core.session_merging_tools import merge
from qrisp.environments import QuantumEnvironment
from qrisp.misc import perm_lock, perm_unlock


class ControlEnvironment(QuantumEnvironment):
    """
    This class behaves similarly to ConditionEnvironment but instead of a function
    calculating a truth value, we supply a list of qubits.
    The environment's content is then controlled on these qubits.

    An alias for this QuantumEnvironment is "control".


    Parameters
    ----------
    ctrl_qubits : list[Qubit]
        A list of qubits on which to control the environment's content.
    ctrl_state : int/str, optional
        The computational basis state which is supposed to activate the environment.
        Can be supplied as a bitstring or integer. The default is "1111..".


    Examples
    --------

    We create a QuantumVariable and control on some of it's qubits
    using the control alias ::

        from qrisp import QuantumVariable, QuantumString, multi_measurement, control, h

        qv = QuantumVariable(3)
        q_str = QuantumString()

        qv[:] = "011"
        h(qv[0])

        with control(qv[:2], "11"):
            q_str += "hello world"


    >>> print(multi_measurement([qv, q_str]))
    {('011', 'aaaaaaaaaaa'): 0.5, ('111', 'hello world'): 0.5}


    """

    def __init__(self, ctrl_qubits, ctrl_state=-1, ctrl_method=None):
        self.arg_qs = merge(ctrl_qubits)

        self.ctrl_method = ctrl_method
        if isinstance(ctrl_qubits, Qubit):
            ctrl_qubits = [ctrl_qubits]
        self.ctrl_qubits = ctrl_qubits
        self.ctrl_state = ctrl_state

        self.manual_allocation_management = True

        # For more information on why this attribute is neccessary check the comment
        # on the line containing subcondition_truth_values = []
        self.sub_condition_envs = []

        QuantumEnvironment.__init__(self)

    # Method to enter the environment
    def __enter__(self):
        from qrisp.qtypes.quantum_bool import QuantumBool

        if len(self.ctrl_qubits) == 1:
            self.condition_truth_value = self.ctrl_qubits[0]
        else:
            self.qbool = QuantumBool(name="ctrl env*", qs=self.arg_qs)
            self.condition_truth_value = self.qbool[0]

        QuantumEnvironment.__enter__(self)

        merge(self.env_qs, self.arg_qs)

        return self.condition_truth_value

    def __exit__(self, exception_type, exception_value, traceback):
        from qrisp.environments import (
            ConditionEnvironment,
            ControlEnvironment,
            InversionEnvironment,
        )

        self.parent_cond_env = None

        QuantumEnvironment.__exit__(self, exception_type, exception_value, traceback)

        # Determine the parent environment
        for env in self.env_qs.env_stack[::-1]:
            if isinstance(env, (ControlEnvironment, ConditionEnvironment)):
                self.parent_cond_env = env
                break
            if not isinstance(env, (QuantumEnvironment, InversionEnvironment)):
                break

    def compile(self):
        from qrisp import QuantumBool
        from qrisp.environments import ConditionEnvironment

        # Create the quantum variable where the condition truth value should be saved
        # Incase we have a parent environment we create two qubits because
        # we use the second qubit to compute the toffoli of this one and the parent
        # environments truth value in order to not have the environment operations
        # controlled on two qubits

        if len(self.env_data):
            # The first step we have to perform is calculating the truth value of the
            # environments quantum condition. For this we differentiate between
            # the case that this condition is embedded in another condition or not

            ctrl_qubits = list(self.ctrl_qubits)

            if self.parent_cond_env is not None:
                # In the parent case we also need to make sure that the code is executed
                # if the parent environment is executed. A possible approach would be
                # to control the content on both, the parent and the chield truth value.
                # However, for each nesting level the gate count to generate
                # the controlled-controlled-controlled... version of the gates inside
                # the environment increases exponentially. Because of this we compute
                # the toffoli of the parent and child truth value
                # and controll the environment gates on this qubit.

                # Synthesize the condition of the environment
                # into the condition truth value qubit
                if len(ctrl_qubits) == 1:
                    from qrisp.misc import retarget_instructions

                    self.qbool = QuantumBool(name="ctrl env*")
                    retarget_instructions(
                        self.env_data, [self.condition_truth_value], [self.qbool[0]]
                    )

                    if isinstance(self.env_qs.data[-1], QuantumEnvironment):
                        env = self.env_qs.data.pop(-1)
                        env.compile()

                    self.condition_truth_value = self.qbool[0]

                ctrl_qubits.append(self.parent_cond_env.condition_truth_value)

                if self.ctrl_state != -1:
                    self.ctrl_state += 2 ** (len(ctrl_qubits) - 1)

            if len(ctrl_qubits) > 1:
                mcx(
                    ctrl_qubits,
                    self.condition_truth_value,
                    ctrl_state=self.ctrl_state,
                    method="gray_pt",
                )

            perm_lock(ctrl_qubits)
            # unlock(self.condition_truth_value)

            # This list will contain the qubits holding the truth values of
            # conditional/control environments within this environment.
            # The instruction from the subcondition environments do not need to be
            # controlled, since their compile method compiles their condition
            # truth value based on the truth value of the parent environment.
            subcondition_truth_values = [
                env.condition_truth_value for env in self.sub_condition_envs
            ]
            inversion_tracker = 1
            # Now we need to recover the instructions from the data list
            # and perform their controlled version on the condition_truth_value qubit
            while self.env_data:
                instruction = self.env_data.pop(0)

                # If the instruction == conditional environment, compile the environment
                if isinstance(instruction, (ControlEnvironment, ConditionEnvironment)):
                    instruction.compile()

                    subcondition_truth_values = [
                        env.condition_truth_value for env in self.sub_condition_envs
                    ]
                    continue

                # If the instruction is a general environment, compile the instruction
                # and add the compilation result to the list of instructions
                # that need to be conditionally executed.
                elif issubclass(instruction.__class__, QuantumEnvironment):
                    temp_data_list = list(self.env_qs.data)
                    self.env_qs.clear_data()
                    instruction.compile()
                    self.env_data = list(self.env_qs.data) + self.env_data
                    self.env_qs.clear_data()
                    self.env_qs.data.extend(temp_data_list)

                    subcondition_truth_values = [
                        env.condition_truth_value for env in self.sub_condition_envs
                    ]
                    continue

                if (
                    instruction.op.name in ["qb_alloc", "qb_dealloc"]
                    and instruction.qubits[0] != self.condition_truth_value
                ) or instruction.op.name == "barrier":
                    self.env_qs.append(instruction)
                    continue

                if set(instruction.qubits).intersection(subcondition_truth_values):
                    self.env_qs.append(instruction)
                    continue

                # Support for inversion of the condition without opening a new
                # environment
                # if set(instruction.qubits).issubset(self.user_exposed_qbool):
                if set(instruction.qubits).issubset([self.condition_truth_value]):
                    if instruction.op.name == "x":
                        inversion_tracker *= -1
                        x(self.condition_truth_value)
                    elif instruction.op.name == "p":
                        p(instruction.op.params[0], self.condition_truth_value)
                    elif instruction.op.name == "rz":
                        rz(instruction.op.params[0], self.condition_truth_value)
                    else:
                        raise Exception(
                            "Tried to perform invalid operations"
                            "on condition truth value (allowed are x, p, rz)"
                        )
                    continue

                # Create controlled instruction
                instruction.op = instruction.op.control(
                    num_ctrl_qubits=1, method=self.ctrl_method
                )

                # Add condition truth value qubit to the instruction qubit list
                instruction.qubits = [self.condition_truth_value] + list(
                    instruction.qubits
                )
                # Append instruction
                self.env_qs.append(instruction)

            perm_unlock(ctrl_qubits)

            if inversion_tracker == -1:
                x(self.condition_truth_value)

            if len(ctrl_qubits) > 1:
                mcx(
                    ctrl_qubits,
                    self.qbool,
                    method="gray_pt_inv",
                    ctrl_state=self.ctrl_state,
                )
                self.qbool.delete()

        if self.parent_cond_env is not None:
            self.parent_cond_env.sub_condition_envs.extend(
                self.sub_condition_envs + [self]
            )


control = ControlEnvironment
