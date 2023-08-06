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


from qrisp.interface.circuit_converter import convert_circuit
from qrisp.interface.openapi_interface.codegen.client.openapi_client import (
    ApiClient,
    Configuration,
)
from qrisp.interface.openapi_interface.codegen.client.openapi_client.api.default_api \
    import DefaultApi
from qrisp.interface.openapi_interface.codegen.client.openapi_client.models import (
    InlineObject,
)


class BackendClient(DefaultApi):
    def __init__(self, socket_ip, port):
        if socket_ip.find(":") != -1:
            socket_ip = "[" + socket_ip + "]"

        if port is None:
            port = 8080

        # TO-DO Allow API token/Secure connections ...
        # check Configuration class definition
        config = Configuration(host="http://" + socket_ip + ":" + str(port))
        client = ApiClient(configuration=config)

        super().__init__(client)

    def run(self, qc, shots, token=""):
        request_object = InlineObject(
            qc=convert_circuit(qc, "open_api"), shots=shots, token=token
        )
        return super().run(inline_object=request_object)
