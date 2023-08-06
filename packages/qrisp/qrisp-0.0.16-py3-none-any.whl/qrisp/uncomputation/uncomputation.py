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


import numpy as np


def auto_uncompute(*args, recompute=False):
    if len(args):
        return auto_uncompute_inner(args[0])
    else:
        if recompute:
            from qrisp import gate_wrap

            def auto_uncompute_helper(function):
                return gate_wrap(auto_uncompute_inner(function))

            return auto_uncompute_helper
        else:
            return auto_uncompute_inner(args[0])


# Decorator for auto uncomputed function
def auto_uncompute_inner(function):
    # Create auto uncomputed function
    def auto_uncomputed_function(*args, **kwargs):
        from qrisp.core import (
            QuantumVariable,
            multi_session_merge,
            recursive_qs_search,
            recursive_qv_search,
        )

        # Acquire quantum session

        qs_list = recursive_qs_search([args, kwargs])
        multi_session_merge(qs_list)

        if not len(qs_list):
            return function(*args, **kwargs)

        qs = qs_list[0]

        # Determine quantum variables to uncompute
        initial_qvs = set([hash(qv()) for qv in QuantumVariable.live_qvs])

        # Execute function
        result = function(*args, **kwargs)

        result_vars = set([hash(qv) for qv in recursive_qv_search(result)])

        uncomp_vars = []

        for qv in qs.qv_list:
            if not hash(qv) in initial_qvs.union(result_vars):
                uncomp_vars.append(qv)

        uncompute(qs, uncomp_vars)

        return result

    auto_uncomputed_function.__name__ = function.__name__ + "_auto_uncomputed"

    # Return result
    return auto_uncomputed_function


verify = np.zeros(1)


def uncompute(qs, uncomp_vars, recompute=False):
    from qrisp import QuantumEnvironment

    qubits_to_uncompute = sum([qv.reg for qv in uncomp_vars], [])

    i = 0
    while i < len(qs.data):
        if isinstance(qs.data[i], QuantumEnvironment):
            env = qs.data.pop(i)
            env.compile()
            continue
        i += 1

    alloc_gates_remaining = list(qubits_to_uncompute)

    for i in range(len(qs.data)):
        instr = qs.data[i]
        if isinstance(instr, QuantumEnvironment):
            continue
        if instr.op.name == "qb_alloc" and instr.qubits[0] in alloc_gates_remaining:
            alloc_gates_remaining.remove(instr.qubits[0])

    if len(alloc_gates_remaining):
        incorrectly_allocated_qvs = []

        for qv in uncomp_vars:
            if set(alloc_gates_remaining).intersection(list(qv)):
                incorrectly_allocated_qvs.append(qv)

        incorrectly_allocated_qvs = [qv.name for qv in incorrectly_allocated_qvs]
        raise Exception(
            f"Could not uncompute QuantumVariables {incorrectly_allocated_qvs} "
            f"because they were not created within this QuantumEnvironment"
        )

    qc_to_uncompute = qs.copy()

    recompute_qubits = []

    for qb in qc_to_uncompute.qubits:
        if hasattr(qb, "recompute"):
            recompute_qubits.append(qb)

    from qrisp.uncomputation.unqomp import uncompute_qc

    uncomputed_qc = uncompute_qc(qc_to_uncompute, qubits_to_uncompute, recompute_qubits)

    from qrisp import QuantumCircuit

    qs.data = []
    QuantumCircuit.fast_append = True

    qs.data = uncomputed_qc.data

    for qv in uncomp_vars:
        # if recompute:
        # for qb in qv:
        # qb.recompute = True

        qv.delete(verify=bool(verify), recompute=recompute)

        # The uncomputation algorithm already added deallocation gates
        # Therefore we remove the deallocation gates
        for i in range(len(qv)):
            qv.qs.data.pop(-1)

    QuantumCircuit.fast_append = False
