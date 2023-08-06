import importlib.util
import sys

pih_is_exists = importlib.util.find_spec("pih") is not None
if not pih_is_exists:
    sys.path.append("//pih/facade")
from pih.collection import ServiceRoleInformation, ServiceRoleDescription
from pih.rpc_collection import Subscriber, Subscribtion
from pih.tools import DataTool, EnumTool, ParameterList, BitMask as BM
from pih.const import CONST, ServiceCommands as SC, ServiceRoles, SubscribtionTypes
import pih.rpcCommandCall_pb2_grpc as pb2_grpc
import pih.rpcCommandCall_pb2 as pb2
import threading
from typing import Any, Callable
import grpc
from grpc import Server
from concurrent import futures
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime, timedelta
import psutil

@dataclass
class Error(BaseException):
    details: str
    code: tuple

@dataclass
class RoleStub:
    name: str = "stub"

class RPC:

    server: Server | None = None

    class SESSION:

        start_time: datetime
        life_time: timedelta
       

    @staticmethod
    def create_error(context, message: str = "", code: Any = None) -> Any:
        context.set_details(message)
        context.set_code(code)
        return pb2.rpcCommandResult()

    class UnaryService(pb2_grpc.UnaryServicer):

        def __init__(self, role_description: ServiceRoleDescription, call_handler: Callable[[str, ParameterList, Any], Any] | None = None, *args, **kwargs):
            self.role_description = role_description
            self.call_handler = call_handler
            self.subscriber_map: dict[SC,
                                      dict[ServiceRoleDescription, Subscriber]] = defaultdict(dict)

        def internal_handler(self, command_name: str, parameters: str, context) -> Any:
            try:
                print(f"rpc call: {command_name} {parameters}")
                sc: SC = EnumTool.get(SC, command_name)
                parameter_list: ParameterList = ParameterList(parameters)
                if sc is not None:
                    if sc == SC.stop:
                        RPC.server.stop(0)
                        A = sys.modules["pih.pih"].A
                        pid: int = A.OS.get_pid()
                        parent = psutil.Process(pid)
                        for child in parent.children(recursive=True):
                            child.kill()
                    if sc == SC.ping:
                        return DataTool.fill_data_from_source(ServiceRoleInformation(
                            subscribers=self.get_subscriber_list()), self.role_description)
                    if sc == SC.subscribe:
                        return self.subscribe(parameter_list)
                    if sc == SC.unsubscribe:
                        return self.unsubscribe(parameter_list)
                    if sc == SC.unsubscribe_all:
                        self.unsubscribe_all()
                        return True
                    if sc == SC.heat_beat:
                        date_string: str = parameter_list.get()
                        date: datetime = datetime.strptime(
                            date_string, CONST.DATE_TIME_FORMAT)
                        parameter_list.set(0, date)
                        RPC.SESSION.life_time = date - RPC.SESSION.start_time
                return None if DataTool.is_empty(self.call_handler) else self.call_subscribers_after(sc, parameter_list, self.call_handler(
                    command_name, self.call_subscribers_before(sc, parameter_list), context))
            except Exception as error:
                A = sys.modules["pih.pih"].A
                A.E.global_except_hook(type(error), error, error.__traceback__)
           
        def get_subscriber_list(self) -> dict:
            subscriber_list: list[Subscriber] = []
            for service_command in self.subscriber_map:
                for role_description in self.subscriber_map[service_command]:
                    subscriber_list.append(self.subscriber_map[service_command][role_description])
            return subscriber_list

        def unsubscribe_all(self) -> None:
            def unsubscribe_all_internal() -> None:
                for service_command in self.subscriber_map:
                    for role_description in self.subscriber_map[service_command]:
                        subscriber: Subscriber = self.subscriber_map[service_command][role_description]
                        DataTool.rpc_unrepresent(RPC.internal_call(
                            subscriber.service_role_description, SC.unsubscribe, (service_command, subscriber.name)))
                self.subscriber_map = {}
            threading.Thread(target=unsubscribe_all_internal).start()

        def unsubscribe(self, parameter_list: ParameterList) -> None:
            role_description: ServiceRoleDescription = parameter_list.next(
                ServiceRoleDescription())
            for service_command in self.subscriber_map:
                if role_description in self.subscriber_map[service_command]:
                    del self.subscriber_map[service_command][role_description]
                 
        def subscribe(self, parameter_list: ParameterList) -> bool:
            role_description: ServiceRoleDescription = parameter_list.next(ServiceRoleDescription())
            service_command: SC = EnumTool.get(
                SC, parameter_list.next())
            type: int = parameter_list.next()
            name: str = parameter_list.next()
            if service_command in self.subscriber_map:
                if role_description in self.subscriber_map[service_command]:
                    subscriber: Subscriber = self.subscriber_map[service_command][role_description]
                    if subscriber.service_role_description == role_description and BM.has(subscriber.type, type):
                        self.subscriber_map[service_command][role_description].enabled = True
                else:
                    self.subscriber_map[service_command][role_description] = Subscriber(
                        role_description, type, name)
            else:
                self.subscriber_map[service_command][role_description] = Subscriber(role_description, type, name)
            return True

        def call_subscribers_before(self, service_command: SC, in_result: ParameterList):
            out_result: ParameterList = in_result
            if service_command in self.subscriber_map:
                for role_item in self.subscriber_map[service_command]:
                    subscriber: Subscriber = self.subscriber_map[service_command][role_item]
                    role_description: ServiceRoleDescription = subscriber.service_role_description
                    if BM.has(subscriber.type, SubscribtionTypes.BEFORE) and subscriber.enabled:
                        subscriber.available = RPC.check_availability(role_description)
                        if subscriber.available:
                            out_result = ParameterList(DataTool.rpc_unrepresent(RPC.internal_call(
                                role_description, service_command, in_result)))
                        else:
                            if role_description.weak_subscribtion:
                                subscriber.enabled = False
            return out_result

        def call_subscribers_after(self, service_command: SC, parameter_list: ParameterList, result: Any) -> Any:
            def internal_call_subscribers_after(service_command: SC, role_description_item: ServiceRoleDescription):
                subscriber: Subscriber = self.subscriber_map[service_command][role_description_item]
                if BM.has(subscriber.type, SubscribtionTypes.AFTER) and subscriber.enabled:
                    role_description: ServiceRoleDescription = subscriber.service_role_description
                    subscriber.available = RPC.check_availability(role_description)
                    if subscriber.available:
                        RPC.internal_call(role_description, service_command, (result, parameter_list))
                    else:
                        if role_description.weak_subscribtion:
                            subscriber.enabled = False
            if service_command in self.subscriber_map:
                for role_description_item in list(self.subscriber_map[service_command]):
                    threading.Thread(target=internal_call_subscribers_after, args=(service_command, role_description_item)).start()
            return result

        """
            def internal_call_subscribers_after(service_command: SC, role_description_item: ServiceRoleDescription):
            subscriber: Subscriber = self.subscriber_map[service_command][role_description_item]
            if BM.has(subscriber.type, SubscribtionTypes.AFTER) and subscriber.enabled:
                role_description: ServiceRoleDescription = subscriber.service_role_description
                subscriber.available = RPC.check_availability(role_description)
                if subscriber.available:
                    RPC.internal_call(role_description, service_command, (result, parameter_list))
                else:
                    if role_description.weak_subscribtion:
                        subscriber.enabled = False
        if service_command in self.subscriber_map:
            for role_description_item in list(self.subscriber_map[service_command]):
                threading.Thread(target=internal_call_subscribers_after, args=(service_command, role_description_item)).start()
        return result
        """

        def rpcCallCommand(self, command, context):
            parameters = command.parameters
            if not DataTool.is_empty(parameters):
                parameters = DataTool.rpc_unrepresent(parameters)
            result: Any = self.internal_handler(command.name, parameters, context)
            if context.code() is None:
                return pb2.rpcCommandResult(data=DataTool.rpc_represent(result))
            return result

    class Service:

        MAX_WORKERS: int = 10
        role_description: ServiceRoleDescription = None
        service: Any | None = None

        def __init__(self):
            self.role_description: ServiceRoleDescription | None = None
            self.subscribtion_map: dict[ServiceRoleDescription,
                               list[Subscribtion]] = defaultdict(dict)
            self.server: Server | None = None


        def serve(self, role_or_description: ServiceRoles | ServiceRoleDescription, call_handler: Callable[[str, ParameterList, Any], Any] | None = None, isolate: bool = False, service_started_handler: Callable[[None], None] = None, depends_on_list: list[ServiceRoles | ServiceRoleDescription] = [], max_workers: int | None = None) -> None:
            A = sys.modules["pih.pih"].A
            A.O.init()
            A.SRV.init()
            max_workers = max_workers or RPC.Service.MAX_WORKERS
            role_description: ServiceRoleDescription = role_or_description if isinstance(role_or_description, ServiceRoleDescription) else role_or_description.value
            if  RPC.Service.service is None:
                RPC.Service.role_description = role_description
                RPC.Service.service = self
            self.role_description = role_description
            isolate_arg: str = A.SE.arg(1, None)
            if isolate_arg is not None:
                isolate = isolate_arg.lower() in ["true", "1", "yes"]
            role_description.isolated = isolate
            service_host: str = A.SRV.get_host(role_description)
            service_port: int = A.SRV.get_port(role_description)
            role_description.pih_version = A.V.local()
            role_description.pid = A.OS.get_pid()
            A.O.service_header(role_description)
            A.O.good(f"Сервис был запущен!")
            self.server = grpc.server(
                futures.ThreadPoolExecutor(max_workers=max_workers))
            pb2_grpc.add_UnaryServicer_to_server(
                RPC.UnaryService(role_description, call_handler), self.server)
            try:
                self.server.add_insecure_port(f"{service_host}:{service_port}") 
                RPC.SESSION.start_time = datetime.now().replace(second=0, microsecond=0)
                A.L_C.service_starts(role_description)
                self.server.start() 
                A.L_C.service_started(role_description)
                if not DataTool.is_empty(depends_on_list): 
                    from pih import while_not_do
                    A.O.write_line("Dependency availability check...")
                    while_not_do(lambda: len(list(filter(lambda item: A.SRV.check_accessibility(item if isinstance(item, ServiceRoleDescription) else item.value), depends_on_list))) == len(depends_on_list), sleep_time=1)
                    A.O.write_line("All dependencies online")
                if service_started_handler is not None:
                    if service_started_handler.__code__.co_argcount == 1:
                        service_started_handler(self)
                    else:
                        service_started_handler()
                self.create_subscribtions()
                if RPC.server is None:
                    RPC.server = self.server
                self.server.wait_for_termination()
            except RuntimeError as error:
                A.L_C.service_not_started(
                    role_description, "".join(error.args))

        def create_subscribtions(self) -> None:
            def create_subscribtions_internal() -> None:
                subscribtion_map: dict[ServiceRoleDescription, list[Subscribtion]] = self.subscribtion_map
                for role_description in subscribtion_map:
                    if RPC.check_availability(role_description):
                        for service_command in subscribtion_map[role_description]:
                            subscribtion: Subscribtion = subscribtion_map[role_description][service_command]
                            if not subscribtion.actiated:
                                if DataTool.rpc_unrepresent(RPC.internal_call(role_description, SC.subscribe, (self.role_description, subscribtion.service_command, subscribtion.type, subscribtion.name))):
                                    subscribtion.actiated = True
                    else:
                        pass
            threading.Thread(target=create_subscribtions_internal).start()


        def subscribe_on(self, service_command: SC, type: int = SubscribtionTypes.AFTER, name: str = None) -> bool:
            service_role_description: ServiceRoleDescription = self.role_description
            if service_role_description is not None:
                if not service_role_description.isolated:
                    A = sys.modules["pih.pih"].A
                    subscriber_service_role: ServiceRoleDescription = A.SRV.get_role_description_by_command(service_command)
                    if subscriber_service_role is not None:
                        if subscriber_service_role.name != service_role_description.name:
                            subscribtion_map: dict[ServiceRoleDescription,
                                                   list[Subscribtion]] = self.subscribtion_map
                            if service_command not in subscribtion_map[subscriber_service_role]:
                                subscribtion_map[subscriber_service_role][service_command] = Subscribtion(service_command, type, name)
                            else:
                                subscribtion: Subscribtion = subscribtion_map[subscriber_service_role][service_command]
                                subscribtion.enabled = True
                                subscribtion.type |= type
                            return True
            return False


        def unsubscribe(self, commnad_list: list[SC] = None, type: int = None) -> bool:
            for role_description in self.subscribtion_map:
                for service_command in self.subscribtion_map[role_description]:
                    if service_command in commnad_list:
                        DataTool.rpc_unrepresent(RPC.internal_call(role_description, SC.unsubscribe, (self.role_description, )))


        def unsubscribe_all(self, role_or_description: ServiceRoles | ServiceRoleDescription) -> bool:
            pass
            #return self.unsubscribe(role_or_description)

        def stop(self) -> None:
            self.server.stop(0)
    
    class CommandClient():

        def __init__(self, host: str, port: int):
            self.stub = pb2_grpc.UnaryStub(grpc.insecure_channel(f"{host}:{port}"))

        def call_command(self, name: str, parameters: str = None, timeout: int = None):
            return self.stub.rpcCallCommand(pb2.rpcCommand(name=name, parameters=parameters), timeout=timeout)

    @staticmethod
    def ping(role_or_description: ServiceRoles | ServiceRoleDescription) -> ServiceRoleInformation:
        try:
            role_description: ServiceRoleDescription = role_or_description if isinstance(role_or_description, ServiceRoleDescription) else role_or_description.value
            return DataTool.fill_data_from_rpc_str(ServiceRoleInformation(), RPC.internal_call(role_description, SC.ping, ((RPC.Service.role_description or RoleStub()).name), ))
        except Error:
            return None
        
    @staticmethod
    def stop(role_or_description: ServiceRoles | ServiceRoleDescription) -> ServiceRoleInformation:
        role_description: ServiceRoleDescription = role_or_description if isinstance(role_or_description, ServiceRoleDescription) else role_or_description.value
        return RPC.internal_call(role_description, SC.stop)

    @staticmethod
    def check_availability(role_or_description: ServiceRoles | ServiceRoleDescription) -> bool:
        return not DataTool.is_empty(RPC.ping(role_or_description))
    
    @staticmethod
    def internal_call(role_or_description: ServiceRoles | ServiceRoleDescription, sc: SC, parameters: Any = None) -> str:
        A = sys.modules["pih.pih"].A
        A.SRV.init()
        role_description: ServiceRoleDescription | None = role_or_description if role_or_description is None else (
            role_or_description if isinstance(role_or_description, ServiceRoleDescription) else role_or_description.value)
        try:
            if role_description is None:
                role_description = A.SRV.get_role_description_by_command(sc)
            service_host: str = A.SRV.get_host(role_description)
            service_port: int = A.SRV.get_port(role_description)
            timeout: int = None 
            if RPC.Service.role_description is None or RPC.Service.role_description.isolated or role_description.isolated:
                if sc == SC.ping:
                    timeout = CONST.RPC.TIMEOUT_FOR_PING
                else:
                    timeout = CONST.RPC.TIMEOUT
            return RPC.CommandClient(service_host, service_port).call_command(sc.name, DataTool.rpc_represent(parameters), timeout).data
        except grpc.RpcError as error:
            code: tuple = error.code()
            details: str = f"Service role:{role_description.name}\nHost: {service_host}:{service_port}\nCommand: {sc.name}\nDetails: {error.details()}\nCode: {code}"
            A.E.rpc_error_handler(details, code, role_description, sc)

    @staticmethod
    def call(command: SC, parameters: Any = None) -> str:
        return RPC.internal_call(None, command, parameters)