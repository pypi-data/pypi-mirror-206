import importlib.util
import sys

pih_is_exists = importlib.util.find_spec("pih") is not None
if not pih_is_exists:
    sys.path.append("//pih/facade")
from pih import A
from pih.const import ServiceRoles

#version 1.0

ROLE: ServiceRoles = ServiceRoles.DEVELOPER
if A.U.update_for_service(ROLE, False, True, True):

    from typing import Any
    from pih.const import ServiceCommands as SC
    from pih.tools import EnumTool, ParameterList

    def handler_or_server_name(command_name: str, parameter_list: ParameterList, context) -> Any:
        sc: SC = EnumTool.get(SC, command_name)       
        return None
    

    def service_started_handler() -> None:
        pass
       
    A.SRV_A.serve(ROLE, handler_or_server_name, False, service_started_handler)
