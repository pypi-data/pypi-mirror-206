import calendar
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta
from getpass import getpass
from threading import Thread
from time import sleep
from grpc import StatusCode
import dataclasses
import importlib.util
import locale
import os
import platform
import json
import pkg_resources
import re
import subprocess
from subprocess import DEVNULL, STDOUT, CompletedProcess
import sys
from typing import Any, Callable, Tuple
import colorama
from colorama import Back, Style, Fore
from prettytable import PrettyTable
import requests
from requests import ConnectTimeout, Response
import traceback
from contextlib import contextmanager
import base64
import uuid

try:
    from packaging.version import parse
except ImportError:
    from pip._vendor.packaging.version import parse

pih_is_exists = importlib.util.find_spec("pih") is not None
if not pih_is_exists:
    sys.path.append("//pih/facade")
from pih.tools import DataTool, EnumTool, PathTool, ResultTool, FullNameTool, PasswordTools, ResultUnpack, DateTimeTool, BitMask as BM, ParameterList, StringTool, ListTool, NetworkTool
from pih.collection import ActionValue, T, FieldItem, FieldItemList, FullName, InventoryReportItem, LogCommandDescription, LoginPasswordPair, Mark, MarkDivision, MarkGroup, MarkGroupStatistics, ParamItem, PasswordSettings, PolibasePerson, PrinterADInformation, PrinterReport, PrinterStatus, Result, ServiceRoleInformation, ServiceRoleDescription, TemporaryMark, TimeTrackingEntity, TimeTrackingResultByDate, TimeTrackingResultByDivision, TimeTrackingResultByPerson, User, UserContainer, Workstation, WhatsAppMessage, WhatsAppMessageListPayload, WhatsAppMessageButtonsPayload, WorkstationDescription, SettingsValue, PolibasePersonVisitDS, PolibasePersonVisitNotification, PolibasePersonVisitNotificationDS, DelayedMessage, MessageSearchCritery, DelayedMessageDS, PolibasePersonInformationQuest, PolibasePersonVisitSearchCritery, RobocopyJobStatus, PolibasePersonNotificationConfirmation, ResourceDescription, ResourceStatus, SiteResourceStatus, CTIndicationItem, CTIndicationValue, PolibaseScannedDocument, OGRN, Message
from pih.const import CONST, URLS, DATA, FIELD_NAME_COLLECTION, FIELD_COLLECTION, FILE, FIELD_COLLECTION_ALIAS, PASSWORD, PATHS, HOSTS, USER_PROPERTY, WorkstationMessageMethodTypes, LogChannels, LogCommands, LogLevels, MarkType, ServiceCommands, ServiceRoles, SETTINGS, MessageTypes, MessageStatuses, RESOURCE, CheckableSections, AD, MEDICAl_DOCUMENT, FONT
from pih.rpc_collection import Subscriber
from pih.rpc import RPC, Error, SubscribtionTypes

class IClosable:

    def close() -> None:
        raise NotImplemented()

class ServiceListener:
    
    def __init__(self):
        self.service: RPC.Service | None = None
        self.service_command_list: list[ServiceCommands] = None
        self.host: str = A.OS.host()
        self.port: int = NetworkTool.next_free_port()

    def listen_for(self, service_command_list: list[ServiceCommands], handler: Callable[[str, ParameterList, IClosable], Any]) -> None:     
        self.service_command_list = service_command_list
  
        def service_started_handler(service: RPC.Service) -> None:
            self.service = service
            for service_command in service_command_list:
                service.subscribe_on(service_command)

        service_description: ServiceRoleDescription = ServiceRoleDescription(
            name=f"Subscriber_{self.host}_{ self.port}",
            description="Subscriber",
            host=self.host,
            port=self.port,
            weak_subscribtion=True)
        
        PIH.SERVICE.ADMIN.serve(service_description, lambda command_name, parameter_list, _: handler(command_name, parameter_list, self), False, service_started_handler)
        
    def close(self) -> None:
        self.service.unsubscribe(self.service_command_list)
        self.service.stop()    


class MarkOutputAbstract:

    def by_any(self, value: str) -> None:
        raise NotImplemented()

    def result(self, result: Result[list[Mark]], caption: str, use_index: bool = False) -> None:
        raise NotImplemented()

class OutputAbstract:
    
    def indent(self, count: int = 1) -> None:
        raise NotImplemented()
    
    def bold(self, value: str) -> str:
        raise NotImplemented()

    def header(self, caption: str) -> None:
        raise NotImplemented()

    def reset_indent(self) -> None:
        raise NotImplemented()

    def restore_indent(self) -> None:
        raise NotImplemented()

    def init(self) -> None:
        raise NotImplemented()

    def text_color(self, color: int, text: str) -> str:
        raise NotImplemented()

    def text_black(self, text: str) -> str:
        raise NotImplemented()

    def color_str(self, color: int, text: str, text_before: str = None, text_after: str = None) -> str:
        raise NotImplemented()

    def color(self, color: int, text: str, text_before: str = None, text_after: str = None) -> None:
        raise NotImplemented()

    def write_line(self, text: str) -> None:
        raise NotImplemented()

    def index(self, index: int, text: str, max_index: int = None) -> None:
        raise NotImplemented()

    def input(self, caption: str) -> None:
        raise NotImplemented()

    def input_str(self, caption: str, text_before: str = None, text_after: str = None) -> str:
        raise NotImplemented()

    def value(self, caption: str, value: str, text_before: str = None) -> None:
        raise NotImplemented()

    def get_action_value(self, caption: str, value: str, show: bool = True) -> ActionValue:
        raise NotImplemented()

    def head(self, caption: str) -> None:
        raise NotImplemented()

    def head1(self, caption: str) -> None:
        raise NotImplemented()

    def head2(self, caption: str) -> None:
        raise NotImplemented()

    def new_line(self) -> None:
        raise NotImplemented()

    def separated_line(self) -> None:
        self.new_line()

    def error_str(self, caption: str) -> str:
        raise NotImplemented()

    def error(self, caption: str) -> None:
        raise NotImplemented()

    def notify_str(self, caption: str) -> str:
        raise NotImplemented()

    def notify(self, caption: str) -> None:
        raise NotImplemented()

    def good_str(self, caption: str) -> str:
        raise NotImplemented()

    def good(self, caption: str) -> None:
        raise NotImplemented()

    def green_str(self, text: str, text_before: str = None, text_after: str = None) -> str:
        raise NotImplemented()

    def green(self, text: str, text_before: str = None, text_after: str = None) -> None:
        raise NotImplemented()

    def yellow_str(self, text: str, text_before: str = None, text_after: str = None) -> str:
        raise NotImplemented()

    def yellow(self, text: str, text_before: str = None, text_after: str = None) -> None:
        raise NotImplemented()

    def black_str(self, text: str, text_before: str = None, text_after: str = None) -> str:
        raise NotImplemented()

    def black(self, text: str, text_before: str = None, text_after: str = None) -> None:
        raise NotImplemented()

    def white_str(self, text: str, text_before: str = None, text_after: str = None) -> str:
        raise NotImplemented()

    def white(self, text: str, text_before: str = None, text_after: str = None) -> None:
        raise NotImplemented()

    def draw_line(self, color: str = Back.LIGHTBLUE_EX, char: str = " ", width: int = 80) -> None:
        raise NotImplemented()

    def line(self) -> None:
        raise NotImplemented()

    def magenta_str(self, text: str, text_before: str = None, text_after: str = None) -> str:
        raise NotImplemented()

    def magenta(self, text: str, text_before: str = None, text_after: str = None) -> None:
        raise NotImplemented()

    def cyan(self, text: str, text_before: str = None, text_after: str = None) -> None:
        raise NotImplemented()

    def cyan_str(self, text: str, text_before: str = None, text_after: str = None) -> str:
        raise NotImplemented()

    def red(self, text: str, text_before: str = None, text_after: str = None) -> None:
        raise NotImplemented()

    def red_str(self, text: str, text_before: str = None, text_after: str = None) -> str:
        raise NotImplemented()

    def blue(self, text: str, text_before: str = None, text_after: str = None) -> None:
        raise NotImplemented()

    def blue_str(self, text: str, text_before: str = None, text_after: str = None) -> str:
        raise NotImplemented()

    def bright(self, text: str, text_before: str = None, text_after: str = None) -> None:
        raise NotImplemented()

    def bright_str(self, text: str, text_before: str = None, text_after: str = None) -> str:
        raise NotImplemented()

    def get_number(self, value: int) -> str:
        raise NotImplemented()

    def write_result(self, result: Result[T], use_index: bool = True, item_separator: str = "\n", empty_result_text: str = "Не найдено", separated_result_item: bool = True, label_function:  Callable[[Any, int], str] = None, data_label_function: Callable[[int, FieldItem, Result[T], Any], Tuple[bool, str]] = None, title: str = None) -> None:
        raise NotImplemented()

    @contextmanager
    def send_to_group(self, group: CONST.MESSAGE.WHATSAPP.GROUP) -> bool:
        raise NotImplemented()

class MarkOutputBase(MarkOutputAbstract):

    def __init__(self):
        self.parent: OutputBase


class MarkOutput(MarkOutputBase):

    def by_any(self, value: str) -> None:
        try:
            self.result(PIH.RESULT.MARK.by_any(value) , "Найденные карты доступа:", True)
        except NotFound as error:
            self.parent.error(error.get_details())

           

    def result(self, result: Result[list[Mark]], caption: str, use_index: bool = False) -> None:
        self.parent.table_with_caption_first_title_is_centered(result, caption, use_index)


class UserOutputAbstract:

    def result(self, result: Result[list[User]], caption: str = None, use_index: bool = False, root_location: str = AD.ACTIVE_USERS_CONTAINER_DN) -> None:
        raise NotImplemented()

    def get_formatted_given_name(self, value: str | None = None) -> str:
        return value

class OutputExtendedAbstract:

    def pih_title(self) -> None:
        raise NotImplemented()  

    def rpc_service_header(self, host: str, port: int, description: str) -> None:
        raise NotImplemented()  

    def service_header(self, service_role_description: ServiceRoleDescription) -> None:
        raise NotImplemented()  

    def free_marks(self, show_guest_marks: bool, use_index: bool = False) -> None:
        raise NotImplemented()  

    def guest_marks(self, use_index: bool = False) -> None:
        raise NotImplemented()

    def temporary_candidate_for_mark(self, mark: Mark) -> None:
        raise NotImplemented()  

    def free_marks_group_statistics(self, use_index: bool = False, show_guest_marks: bool = None) -> None:
        raise NotImplemented()  

    def free_marks_by_group(self, group: dict, use_index: bool = False) -> None:
        raise NotImplemented()  

    def free_marks_group_statistics_for_result(self, result: Result, use_index: bool) -> None:
        raise NotImplemented()  

    def free_marks_by_group_for_result(self, group: MarkGroup, result: Result, use_index: bool) -> None:
        raise NotImplemented()  

    def temporary_marks(self, use_index: bool = False,) -> None:
        raise NotImplemented()  

    def containers_for_result(self, result: Result, use_index: bool = False) -> None:
        raise NotImplemented()  

    def table_with_caption_first_title_is_centered(self, result: Result, caption: str, use_index: bool = False, label_function: Callable = None) -> None:
        raise NotImplemented()  

    def table_with_caption_last_title_is_centered(self, result: Result, caption: str, use_index: bool = False, label_function: Callable = None) -> None:
        raise NotImplemented()  

    def table_with_caption(self, result: Any, caption: str = None, use_index: bool = False, modify_table_function: Callable = None, label_function: Callable = None) -> None:
        raise NotImplemented()  

    def template_users_for_result(self, data: dict, use_index: bool = False) -> None:
        raise NotImplemented()  

    def clear_screen(self) -> None:
        raise NotImplemented()
    
    def write_video(self, caption: str, video_content: str) -> None:
            raise NotImplemented()

    def write_image(self, caption: str, image_content: str) -> None:
        raise NotImplemented()

class UserOutputBase(UserOutputAbstract):

    def __init__(self):
        self.parent: OutputBase

class UserOutput(UserOutputBase):

    def result(self, result: Result[list[User]], caption: str = None, use_index: bool = False, root_location: str = AD.ACTIVE_USERS_CONTAINER_DN) -> None:
        data: list = DataTool.as_list(result.data)
        fields: FieldItemList = result.fields
        base_location_list = PIH.DATA.FORMAT.location_list(
            root_location, False)
        root_base_location = base_location_list[0:2]
        root_base_location.reverse()
        base_location = AD.LOCATION_JOINER.join([".".join(
            root_base_location), AD.LOCATION_JOINER.join(base_location_list[2:])])
        location_field = fields.get_item_by_name(
            FIELD_NAME_COLLECTION.DN)
        pevious_caption: str = location_field.caption
        location_field.caption = f"{location_field.caption} ({base_location})"
        def modify_data(field: FieldItem, user: User) -> str:
            if field.name == USER_PROPERTY.DN:
                return AD.LOCATION_JOINER.join(filter(
                    lambda x: x not in base_location_list, PIH.DATA.FORMAT.location_list(user.distinguishedName)))
            if field.name == USER_PROPERTY.USER_ACCOUNT_CONTROL:
                return "\n".join(PIH.DATA.FORMAT.get_user_account_control_values(user.userAccountControl))
            if field.name == USER_PROPERTY.DESCRIPTION:
                return user.description
            if field.name == USER_PROPERTY.NAME:
                return "\n".join(user.name.split(" "))
            return None
        self.parent.table_with_caption(
            result, "Пользватели:" if len(data) > 1 else "Пользватель:", False, None, modify_data)
        location_field.caption = pevious_caption


class InputAbstract:

    def input(self, caption: str = None, new_line: bool = True, check_function: Callable[[str], str] = None) -> str:
        raise NotImplemented()

    def polibase_person_card_registry_folder(self) -> str:
        raise NotImplemented()

    def telephone_number(self, format: bool = True, telephone_prefix: str = CONST.TELEPHONE_NUMBER_PREFIX) -> str:
        raise NotImplemented()

    def email(self) -> str:
        raise NotImplemented()

    def message(self, caption: str = None, prefix: str = None) -> str:
        raise NotImplemented()

    def description(self) -> str:
        raise NotImplemented()

    def login(self, check_on_exists: bool = False) -> str:
        raise NotImplemented()

    def indexed_list(self, caption: str, name_list: list[Any], caption_list: list[str], by_index: bool = False) -> str:
        raise NotImplemented()

    def indexed_field_list(self, caption: str, list: FieldItemList) -> str:
        raise NotImplemented()

    def index(self, caption: str, data: list, label_function: Callable[[Any, int], str] = None, use_zero_index: bool = False) -> int:
        raise NotImplemented()

    def item_by_index(self, caption: str, data: list[Any], label_function: Callable[[Any, int], str] = None, use_zero_index: bool = False) -> Any:
        raise NotImplemented()

    def tab_number(self, check: bool = True) -> str:
        raise NotImplemented()

    def password(self, secret: bool = True, check: bool = False, settings: PasswordSettings = None, is_new: bool = True) -> str:
        raise NotImplemented()

    def same_if_empty(self, caption: str, src_value: str) -> str:
        raise NotImplemented()

    def name(self) -> str:
        raise NotImplemented()

    def full_name(self, one_line: bool = False) -> FullName:
        raise NotImplemented()

    def yes_no(self, text: str = " ", enter_for_yes: bool = False, yes_label: str = None, no_label: str = None, yes_checker: Callable[[str], bool] = None) -> bool:
        raise NotImplemented()

    def message_for_user_by_login(self, login: str) -> str:
        raise NotImplemented()

    def polibase_person_any(self, title: str | None = None) -> str:
        raise NotImplemented()


class UserInputAbstract:

    def container(self) -> UserContainer:
        raise NotImplemented()

    def by_name(self) -> User:
        raise NotImplemented()

    def title_any(self, title: str = None) -> str:
        raise NotImplemented()

    def by_any(self, value: str = None, active: bool = None, title: str = None, use_all: bool = False) -> list[User]:
        raise NotImplemented()

    def telephone_number(self, value: str = None, active: bool = None, title: str = None) -> User:
        raise NotImplemented()

    def template(self) -> dict:
        raise NotImplemented()

    def search_attribute(self) -> str:
        raise NotImplemented()

    def search_value(self, search_attribute: str) -> str:
        raise NotImplemented()

    def generate_login(self, full_name: FullName, ask_for_remove_inactive_user_if_login_is_exists: bool = True, ask_for_use: bool = True) -> str:
        raise NotImplemented()

    def generate_password(self, once: bool = False, settings: PasswordSettings = PASSWORD.SETTINGS.DEFAULT) -> str:
        raise NotImplemented()


class UserInputBase(UserInputAbstract):

    def __init__(self):
        self.parent: InputBase = None


class MarkInputAbstract:

    def free(self, group: MarkGroup = None) -> Mark:
        raise NotImplemented()

    def person_division(self) -> MarkDivision:
        raise NotImplemented()

    def by_name(self) -> Mark:
        raise NotImplemented()

    def by_any(self, value: str = None) -> Mark:
        raise NotImplemented()

    def any(self) -> str:
        raise NotImplemented()


class MarkInputBase(MarkInputAbstract):

    def __init__(self):
        self.parent: InputBase


class InputBase(InputAbstract):

    def __init__(self):
        self.output: OutputBase
        self.mark: MarkInputBase
        self.user: UserInputBase


class OutputBase(OutputAbstract, OutputExtendedAbstract):

    def __init__(self, user_output: UserOutputBase = None, mark_output: MarkOutputBase = None):
        self.TEXT_BEFORE: str = ""
        self.TEXT_AFTER: str = ""
        self.INDEX: str = "  "
        self.INDEX_COUNT: int = 0
        self.user: UserOutputBase = user_output
        self.user.parent = self
        self.mark: MarkOutputBase = mark_output
        self.mark.parent = self
        self.personalize = False


class SessionAbstract:

    def run_forever_untill_enter_not_pressed(self) -> None:
        raise NotImplemented()

    def exit(self, timeout: int = None, message: str = None) -> None:
        raise NotImplemented()

    def get_login(self) -> str:
        raise NotImplemented()

    def get_user(self) -> User:
        raise NotImplemented()

    def user_given_name(self) -> str:
        raise NotImplemented()

    def start(self, login: str, notify: bool = True) -> None:
        raise NotImplemented()

    def say_hello(self) -> None:
        raise NotImplemented()
    
    @property
    def argv(self) -> list[str]:
        raise NotImplemented()

    def arg(self, index: int = None, default_value: str = None) -> str:
        raise NotImplemented()

    def get_file_path(self) -> str:
        raise NotImplemented()

    @property
    def file_name(self) -> str:
        raise NotImplemented()

    def authenticate(self, exit_on_fail: bool = True) -> bool:
        raise NotImplemented()

    def add_allowed_group(self, value: AD.Groups) -> None:
        raise NotImplemented()

class SessionBase(SessionAbstract):

    def __init__(self, input: InputBase = None, output: OutputBase = None):
        self.allowed_groups: list[AD.Groups] = []
        self.login: str = None
        self.user: User = None
        self.input: InputBase = input
        self.output: OutputBase = output

    def add_allowed_group(self, value: AD.Groups) -> None:
        self.allowed_groups.append(value)


class Session(SessionBase):

    def __init__(self, input: InputBase = None, output: OutputBase = None):
        super().__init__(input, output)
        self.authenticated: bool = False
       
    def run_forever_untill_enter_not_pressed(self) -> None:
        try:
            self.output.green("Нажмите Ввод для выхода...")
            input()
        except KeyboardInterrupt:
            pass

    def exit(self, timeout: int = None, message: str = None) -> None:
        if message is not None:
            self.output.error(message)
        if timeout is None:
            timeout = 5
        sleep(timeout)
        exit()

    def get_login(self) -> str:
        if self.login is None:
            self.start(PIH.OS.get_login())
        return self.login

    def get_user(self) -> User:
        if self.user is None:
            self.user = PIH.RESULT.USER.by_login(
                self.get_login()).data
        return self.user

    @property
    def user_given_name(self) -> str:
        return FullNameTool.to_given_name(self.get_user().name)

    def start(self, login: str, notify: bool = True) -> None:
        if self.login is None:
            self.login = login
            if notify:
                PIH.LOG.COMMAND.start_session()

    def say_hello(self) -> None:
        user: User = self.get_user()
        if user is not None:
            self.output.good(f"Добро пожаловать, {user.name}")
            self.output.new_line()
            return
        self.output.error(f"Ты кто такой? Давай, до свидания...")
        self.exit()

    @property
    def argv(self) -> list[str]:
        return sys.argv[1:] if len(sys.argv) > 1 else None
    
    def arg(self, index: int = 0, default_value: Any = None) -> str:
        return DataTool.by_index(self.argv, index, default_value)

    def get_file_path(self) -> str:
        return sys.argv[0]

    @property
    def file_name(self) -> str:
        return PathTool.get_file_name(self.get_file_path())

    def authenticate(self, exit_on_fail: bool = True, once: bool = True) -> bool:
        try:
            if once and self.authenticated:
                return True
            self.output.green("Инициализация...")
            self.output.clear_screen()
            self.output.pih_title()
            if PIH.SERVICE.check_accessibility(ServiceRoles.AD): 
                login: str = PIH.OS.get_login()
                self.output.head1(f"{FullNameTool.to_given_name(A.R_U.by_login(login, cached=False).data.name)}, пожалуйста, пройдите аутентификацию...")
                self.output.new_line()
                if not self.input.yes_no(f"Использовать логин '{login}'", True):
                    login = PIH.input.login()
                password: str = PIH.input.password(is_new=False)
                if DataTool.rpc_unrepresent(RPC.call(ServiceCommands.authenticate, (login, password))):
                    self.authenticated = True
                    self.start(login, False)
                    PIH.LOG.COMMAND.login()
                    self.output.good(self.output.text_black(
                        f"Добро пожаловать, {self.get_user().name}..."))
                    return True
                else:
                    if exit_on_fail:
                        self.exit(
                            5, "Неверный пароль или логин. До свидания...")
                    else:
                        return False
            else:
                self.output.error(
                    "Сервис аутентификации недоступен. До свидания...")
        except KeyboardInterrupt:
            self.exit(0, "Выход")



class Stdin:

    def __init__(self):
        self.data: str = None
        self.wait_for_data_input: bool = False
        self.interrupt_type: int = False

    def is_empty(self) -> bool:
        return DataTool.is_empty(self.data)

    def set_default_state(self) -> None:
        self.interrupt_type = False
        self.wait_for_data_input = False
        self.data = None


class Output(OutputBase):

    def indent(self, count: int = 1) -> None:
        self.INDEX_COUNT = count
        self.TEXT_BEFORE = self.INDEX*count

    def bold(self, value: str) -> str:
        return self.text_color(Fore.RED, value)

    def italic(self, value: str) -> str:
        return value

    def reset_indent(self) -> None:
        self.TEXT_BEFORE = ""

    def restore_indent(self) -> None:
        self.indent(self.INDEX_COUNT)

    def init(self) -> None:
        colorama.init()

    def text_color(self, color: int, text: str) -> str:
        return f"{color}{text}{Fore.RESET}"

    def text_black(self, text: str) -> str:
        return self.text_color(Fore.BLACK, text)

    def color_str(self, color: int, text: str, text_before: str = None, text_after: str = None) -> str:
        text = f" {text} "
        text_before = text_before if text_before is not None else self.TEXT_BEFORE
        text_after = text_after if text_after is not None else self.TEXT_AFTER
        return f"{text_before}{color}{text}{Back.RESET}{text_after}"

    def color(self, color: int, text: str, text_before: str = None, text_after: str = None) -> None:
        self.write_line(self.color_str(
            color, text, text_before, text_after))

    def write_line(self, text: str) -> None:
        print(text)

    @contextmanager
    def personalized(self) -> bool:
        pass

    def index(self, index: int, text: str, max_index: int = None) -> None:
        indent: str = ""
        if max_index is not None:
            indent = " " * 2 * (len(str(max_index)) - len(str(index)))
        if index is None:
            self.write_line(f"{indent}{text}")
        else:
            self.write_line(f"{index}. {indent}{text}")

    def input(self, caption: str) -> None:
        self.write_line(self.input_str(
            caption, self.TEXT_BEFORE, text_after=":"))

    def input_str(self, caption: str, text_before: str = None, text_after: str = None) -> str:
        return self.white_str(f"{Fore.BLACK}{caption}{Fore.RESET}", text_before, text_after)

    def value(self, caption: str, value: str, text_before: str = None) -> None:
        text_before = text_before or self.TEXT_BEFORE
        self.cyan(caption, text_before, f": {value}")

    def get_action_value(self, caption: str, value: str, show: bool = True) -> ActionValue:
        if show:
            self.value(caption, value)
        return ActionValue(caption, value)

    def head(self, caption: str) -> None:
        self.cyan(caption)

    def head1(self, caption: str) -> None:
        self.magenta(caption)

    def head2(self, caption: str) -> None:
        self.yellow(self.text_color(Fore.BLACK, caption))

    def new_line(self) -> None:
        print()

    def separated_line(self) -> None:
        self.new_line()

    def error_str(self, caption: str) -> str:
        return self.red_str(caption)

    def error(self, caption: str) -> None:
        self.write_line(self.error_str(caption))

    def notify_str(self, caption: str) -> str:
        return self.yellow_str(caption)

    def notify(self, caption: str) -> None:
        self.write_line(self.notify_str(caption))

    def good_str(self, caption: str) -> str:
        return self.green_str(caption)

    def good(self, caption: str) -> str:
        self.write_line(self.good_str(self.text_black(caption)))

    def green_str(self, text: str, text_before: str = None, text_after: str = None) -> str:
        return self.color_str(Back.GREEN, text, text_before, text_after)

    def green(self, text: str, text_before: str = None, text_after: str = None) -> None:
        self.write_line(self.green_str(text, text_before, text_after))

    def yellow_str(self, text: str, text_before: str = None, text_after: str = None) -> str:
        return self.color_str(Back.YELLOW, text, text_before, text_after)

    def yellow(self, text: str, text_before: str = None, text_after: str = None) -> None:
        text_before = text_before or self.TEXT_BEFORE
        text_after = text_after or self.TEXT_AFTER
        self.write_line(self.yellow_str(text, text_before, text_after))

    def black_str(self, text: str, text_before: str = None, text_after: str = None) -> str:
        return self.color_str(Back.BLACK, text, text_before, text_after)

    def black(self, text: str, text_before: str = None, text_after: str = None) -> None:
        self.write_line(self.black_str(text, text_before, text_after))

    def white_str(self, text: str, text_before: str = None, text_after: str = None) -> str:
        return self.color_str(Back.WHITE, text, text_before, text_after)

    def white(self, text: str, text_before: str = None, text_after: str = None) -> None:
        self.write_line(self.white_str(text, text_before, text_after))

    def draw_line(self, color: str = Back.LIGHTBLUE_EX, char: str = " ", width: int = 80) -> None:
        self.write_line("") if color is None else self.color(
            color, char*width)

    def line(self) -> None:
        self.new_line()
        self.draw_line(Back.WHITE, self.text_color(
            Fore.BLACK, "_"), width=128)
        self.new_line()

    def magenta_str(self, text: str, text_before: str = None, text_after: str = None) -> str:
        return self.color_str(Back.LIGHTMAGENTA_EX, text, text_before, text_after)

    def magenta(self, text: str, text_before: str = None, text_after: str = None) -> None:
        self.write_line(self.magenta_str(text, text_before, text_after))

    def cyan(self, text: str, text_before: str = None, text_after: str = None) -> None:
        self.write_line(self.cyan_str(text, text_before, text_after))

    def cyan_str(self, text: str, text_before: str = None, text_after: str = None) -> str:
        return self.color_str(Back.CYAN, text, text_before, text_after)

    def red(self, text: str, text_before: str = None, text_after: str = None) -> None:
        self.write_line(self.red_str(text, text_before, text_after))

    def red_str(self, text: str, text_before: str = None, text_after: str = None) -> str:
        return self.color_str(Back.LIGHTRED_EX, text, text_before, text_after)

    def blue(self, text: str, text_before: str = None, text_after: str = None) -> None:
        self.write_line(self.blue_str(text, text_before, text_after))

    def blue_str(self, text: str, text_before: str = None, text_after: str = None) -> str:
        return self.color_str(Back.BLUE, text, text_before, text_after)

    def bright(self, text: str, text_before: str = None, text_after: str = None) -> None:
        self.write_line(self.bright_str(text, text_before, text_after))

    def bright_str(self, text: str, text_before: str = None, text_after: str = None) -> str:
        return self.color_str(Style.BRIGHT, text, text_before, text_after)

    def get_number(self, value: int) -> str:
        return CONST.VISUAL.NUMBER_SYMBOLS[value - 1]

    def header(self, caption: str) -> None:
        self.head2(caption)

    def write_result(self, result: Result[T], use_index: bool = True, item_separator: str = "\n", empty_result_text: str = "Не найдено", separated_result_item: bool = True, label_function: Callable[[Any, int], str] = None, data_label_function: Callable[[int, FieldItem, Result, Any], Tuple[bool, str]] = None, title: str = None) -> None:
        data: list = DataTool.as_list(result.data)
        result_string_list: list[str] = None
        if DataTool.is_empty(data):
            self.new_line()
            self.write_line(empty_result_text)
        else:
            if not DataTool.is_empty(title):
                self.write_line(title)
            for index, data_item in enumerate(data):
                result_string_list = []
                if use_index and len(data) > 1:
                    result_string_list.append(f"{str(index + 1)}:")
                if label_function is None:
                    for field_item in result.fields.list:
                        field: FieldItem = field_item
                        if not field.visible:
                            continue
                        item_data_value: str = None
                        if isinstance(data_item, dict):
                            item_data_value = data_item[field.name]
                        elif dataclasses.is_dataclass(data_item):
                            item_data_value = data_item.__getattribute__(field.name)
                        item_data_value = item_data_value if DataTool.is_empty(item_data_value) else PIH.DATA.FORMAT.by_name(field.data_formatter, item_data_value) or field.data_formatter.format(data=item_data_value) 
                        if DataTool.is_empty(item_data_value):
                            if data_label_function is None:
                                continue
                        default_value_label_function: Callable[[int, FieldItem, Result[T], Any], (
                            bool, str)] = lambda _1, field, _2, data_value: (True, f"{self.bold(field.caption)}: {data_value}")
                        result_data_label_function: Callable[[int, FieldItem, Result[T], Any], (bool, str)] = data_label_function or default_value_label_function 
                        label_value_result: tuple[bool, str] = result_data_label_function(index, field, data_item, item_data_value)
                        label_value: str = None
                        if label_value_result[0] == True:
                            label_value = label_value_result[1]
                            if label_value is None and field.default_value is not None:
                                label_value = field_item.default_value
                        else:
                            label_value = default_value_label_function(index, field, data_item, item_data_value)[1]
                        if not DataTool.is_empty(label_value):
                            result_string_list.append(label_value)
                else:
                    result_string_list.append(label_function(data_item, index))  
                if separated_result_item:
                    self.separated_line()
                self.write_line(item_separator.join(result_string_list))

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def pih_title(self) -> None:
        self.cyan(self.text_color(Fore.WHITE, "███ ███ █┼█"))
        self.cyan(
            self.text_color(Fore.WHITE, "█▄█ ┼█┼ █▄█"))
        self.cyan(self.text_color(Fore.WHITE, "█┼┼ ▄█▄ █┼█") +
                         self.text_color(Fore.BLACK, f" {PIH.VERSION.local()}"))
        self.new_line()

    def rpc_service_header(self, host: str, port: int, description: str) -> None:
        self.blue("PIH service")
        self.blue(f"Version: {PIH.VERSION.local()}")
        self.blue(f"PyPi Version: {PIH.VERSION.remote()}")
        self.green(f"Service host: {host}")
        self.green(f"Service port: {port}")
        self.green(f"Service name: {description}")

    def service_header(self, service_role_description: ServiceRoleDescription) -> None:
        if service_role_description.isolated:
            self.blue(f"[Isolate]")
        self.blue("Запуск сервиса")
        self.blue(f"PIH версия: {PIH.VERSION.remote()}")
        self.green(f"Хост: {service_role_description.host}")
        self.green(f"Порт: {service_role_description.port}")
        self.green(f"Имя сервиса: {service_role_description.name}")
        self.green(
            f"Описание сервиса: {service_role_description.description}")
        self.green(
            f"Идентификатор процесса: {service_role_description.pid}")

    def free_marks(self, show_guest_marks: bool, use_index: bool = False, sort_by_tab_number: bool = True) -> None:
        def sort_function(item: Mark) -> Any:
            return item.TabNumber if sort_by_tab_number else item.GroupName
        self.table_with_caption_first_title_is_centered(ResultTool.sort(PIH.RESULT.MARK.free_list(show_guest_marks), sort_function), "Свободные карты доступа:", use_index)

    def guest_marks(self, use_index: bool = False) -> None:
        mark_list_result: Result[list[Mark]] = PIH.RESULT.MARK.free_list(True)
        mark_list_result.fields.visible(
            FIELD_NAME_COLLECTION.GROUP_NAME, False)
        def filter_function(item: Mark) -> bool:
            return EnumTool.get(MarkType, item.type) == MarkType.GUEST
        ResultTool.filter(mark_list_result, filter_function)
        self.table_with_caption_first_title_is_centered(
            mark_list_result, "Гостевые карты доступа:", use_index)

    def temporary_candidate_for_mark(self, mark: Mark) -> None:
        self.mark.result(
            Result(FIELD_COLLECTION.ORION.FREE_MARK, [mark]), "Временная карта")

    def free_marks_group_statistics(self, use_index: bool = False, show_guest_marks: bool = None) -> None:
        self.free_marks_group_statistics_for_result(
            PIH.RESULT.MARK.free_marks_group_statistics(show_guest_marks), use_index)

    def free_marks_by_group(self, group: dict, use_index: bool = False) -> None:
        self.free_marks_by_group_for_result(PIH.RESULT.MARK.free_marks_by_group_id(group), group, use_index)

    def free_marks_group_statistics_for_result(self, result: Result, use_index: bool) -> None:
        self.table_with_caption_last_title_is_centered(
            result, "Свободные карты доступа:", use_index)

    def free_marks_by_group_for_result(self, group: MarkGroup, result: Result, use_index: bool) -> None:
        group_name: str = group.GroupName
        self.table_with_caption_last_title_is_centered(
            result, f"Свободные карты доступа для группы доступа '{group_name}':", use_index)

    def temporary_marks(self, use_index: bool = False,) -> None:
        def modify_table(table: PrettyTable, caption_list: list[str]):
            table.align[caption_list[0]] = "c"
            table.align[caption_list[1]] = "c"
        self.table_with_caption(
            PIH.RESULT.MARK.temporary_list(), "Список временных карт:", use_index, modify_table)

    def containers_for_result(self, result: Result, use_index: bool = False) -> None:
        self.table_with_caption(result, "Подразделение:", use_index)

    def table_with_caption_first_title_is_centered(self, result: Result, caption: str, use_index: bool = False, label_function: Callable = None) -> None:
        def modify_table(table: PrettyTable, caption_list: list[str]):
            table.align[caption_list[int(use_index)]] = "c"
        self.table_with_caption(
            result, caption, use_index, modify_table, label_function)

    def table_with_caption_last_title_is_centered(self, result: Result, caption: str, use_index: bool = False, label_function: Callable = None) -> None:
        def modify_table(table: PrettyTable, caption_list: list[str]):
            table.align[caption_list[-1]] = "c"
        self.table_with_caption(
            result, caption, use_index, modify_table, label_function)

    def table_with_caption(self, result: Any, caption: str = None, use_index: bool = False, modify_table_function: Callable = None, label_function: Callable = None) -> None:
        if caption is not None:
            self.cyan(caption)
        is_result_type: bool = isinstance(result, Result)
        field_list = result.fields if is_result_type else ResultUnpack.unpack_fields(
            result)
        data: Any = result.data if is_result_type else ResultUnpack.unpack_data(result)
        if DataTool.is_empty(data):
            self.error("Не найдено!")
        else:
            if not isinstance(data, list):
                data = [data]
            if len(data) == 1:
                use_index = False
            if use_index:
                field_list.list.insert(0, FIELD_COLLECTION.INDEX)
            caption_list: list = field_list.get_caption_list()
            def create_table(caption_list: list[str]) -> PrettyTable:
                from prettytable.colortable import ColorTable, Themes
                table: ColorTable = ColorTable(
                    caption_list, theme=Themes.OCEAN)
                table.align = "l"
                if use_index:
                    table.align[caption_list[0]] = "c"
                return table
            table: PrettyTable = create_table(caption_list)
            if modify_table_function is not None:
                modify_table_function(table, caption_list)
            for index, item in enumerate(data):
                row_data: list = []
                for field_item_obj in field_list.get_list():
                    field_item: FieldItem = field_item_obj
                    if field_item.visible:
                        if field_item.name == FIELD_COLLECTION.INDEX.name:
                            row_data.append(str(index + 1))
                        elif not isinstance(item, dict):
                            if label_function is not None:
                                modified_item_data = label_function(
                                    field_item, item)
                                if modified_item_data is None:
                                    modified_item_data = getattr(
                                        item, field_item.name)
                                row_data.append(DataTool.check(
                                    modified_item_data, lambda: modified_item_data, "") if modified_item_data is None else modified_item_data)
                            else:
                                item_data = getattr(item, field_item.name)
                                row_data.append(DataTool.check(
                                    item_data, lambda: item_data, ""))
                        elif field_item.name in item:
                            item_data = item[field_item.name]
                            if label_function is not None:
                                modified_item_data = label_function(
                                    field_item, item)
                                row_data.append(
                                    item_data if modified_item_data is None else modified_item_data)
                            else:
                                row_data.append(item_data)
                table.add_row(row_data)
            print(table)
            table.clear()

    def template_users_for_result(self, data: dict, use_index: bool = False) -> None:
        def data_handler(field_item: FieldItem, item: User) -> Any:
            filed_name = field_item.name
            if filed_name == FIELD_NAME_COLLECTION.DESCRIPTION:
                return item.description
            return None
        self.table_with_caption(
            data, "Шаблоны для создания аккаунта пользователя:", use_index, None, data_handler)

class Input(InputBase):

    def __init__(self, user_input: UserInputBase, mark_input: MarkInputBase, output: OutputBase):
        self.output: OutputBase = output
        self.answer: str = None
        if user_input is not None:
            self.user: UserInputBase = user_input
            self.user.parent = self
        if mark_input is not None:
            self.mark: MarkInputBase = mark_input
            self.mark.parent = self

    def input(self, caption: str = None, new_line: bool = True, check_function: Callable[[str], str] = None) -> str:
        try:
            while True:
                if new_line and caption is not None:
                    self.output.input(caption)
                value: str = input(self.output.TEXT_BEFORE) if new_line else input(self.output.TEXT_BEFORE + caption)
                if check_function is not None: 
                    value_after: str = check_function(value)
                    if value_after is not None:
                        return value_after
                else:
                    return value
        except KeyboardInterrupt:
            raise KeyboardInterrupt()

    def telephone_number(self, format: bool = True, telephone_prefix: str = CONST.TELEPHONE_NUMBER_PREFIX) -> str:
        while True:
            self.output.input("Номер телефона")
            use_telephone_prefix: bool = telephone_prefix is not None
            telephone_number: str = self.input(
                telephone_prefix if use_telephone_prefix else "", False)
            if use_telephone_prefix:
                if not telephone_number.startswith(telephone_prefix):
                    telephone_number = telephone_prefix + telephone_number
            check: bool = None
            if format:
                telehone_number_after_fix = PIH.DATA.FORMAT.telephone_number(
                    telephone_number, telephone_prefix)
                check = PIH.CHECK.telephone_number(telehone_number_after_fix)
                if check and telehone_number_after_fix != telephone_number:
                    telephone_number = telehone_number_after_fix
                    self.output.value("Телефон отформатирован", telephone_number)
            if check or PIH.CHECK.telephone_number(telephone_number):
                return telephone_number
            else:
                self.output.error("Неверный формат номера телефона!")

    def email(self, title: str | None = None) -> str:
        email: str = None
        while True:
            email = self.input(title or "Адресс электронная почта")
            if PIH.CHECK.email(email):
                return email
            else:
                self.output.error("Неверный формат адресса электронной почты!")

    def polibase_person_card_registry_folder(self) -> str:
        value: str = None
        while True:
            value = self.input("Введите название папки с картами пациентов")
            if PIH.CHECK.POLIBASE.person_card_registry_folder_name(value):
                return PIH.DATA.FORMAT.polibase_person_card_registry_folder(value)
            else:
                self.output.error("Неверный формат названия папки с картами пациентов!")

    def message(self, caption: str = None, prefix: str = None) -> str:
        caption = caption or "Введите сообщение"
        self.output.input(caption)
        return (prefix or "") + self.input(prefix, False)

    def description(self) -> str:
        self.output.input("Введите описание")
        return self.input()

    def login(self, check_on_exists: bool = False) -> str:
        login: str = None
        while True:
            login = self.input("Введите логин")
            if PIH.CHECK.login(login):
                if check_on_exists and PIH.CHECK.USER.exists_by_login(login):
                    self.output.error("Логин занят!")
                else:
                    return login
            else:
                self.output.error("Неверный формат логина!")

    def indexed_list(self, caption: str, name_list: list[Any], caption_list: list[str], by_index: bool = False) -> str:
        return self.item_by_index(caption, name_list, lambda item, index: caption_list[index if by_index else item])

    def indexed_field_list(self, caption: str, list: FieldItemList) -> str:
        name_list = list.get_name_list()
        return self.item_by_index(caption, name_list, lambda item, _: list.get_item_by_name(item).caption)

    def index(self, caption: str, data: list, label_function: Callable[[Any, int], str] = None, use_zero_index: bool = False) -> int:
        selected_index: int = -1
        length: int = len(data)
        has_error: bool = False
        while True:
            min_value: int = 1 - int(use_zero_index)
            max_value: int = length - int(use_zero_index)
            if not has_error and label_function is not None and length > 1:
                for index, item in enumerate(data):
                    self.output.index(
                            index + 1 - int(use_zero_index) if length > 1 else None, label_function(item, index), max_value)
            if length == 1:
                return 0
            selected_index = PIH.DATA.EXTRACT.decimal(self.input(
                caption + f" (от {min_value} до {max_value})"))
            if DataTool.is_empty(selected_index):
                selected_index = min_value
            try:
                selected_index = int(selected_index) - min_value
                if selected_index >= 0 and selected_index < length:
                    return selected_index
            except ValueError:
                has_error = True
                continue

    def item_by_index(self, caption: str, data: list[Any], label_function: Callable[[Any, int], str] = None, use_zero_index: bool = False) -> Any:
        return data[self.index(caption, data, label_function, use_zero_index)]

    def tab_number(self, check: bool = True) -> str:
        tab_number: str = None
        while True:
            tab_number = self.input("Введите номер карты доступа")
            if check:
                if PIH.CHECK.MARK.tab_number(tab_number):
                    return tab_number
                else:
                    self.output.error(
                        "Неправильный формат номера карты доступа")
                    #return None
            else:
                return tab_number

    def password(self, secret: bool = True, check: bool = False, settings: PasswordSettings = None, is_new: bool = True) -> str:
        self.output.input(
            "Введите новый пароль" if is_new else "Введите пароль")
        while True:
            value = getpass("") if secret else self.input()
            if not check or PIH.CHECK.password(value, settings):
                return value
            else:
                self.output.error(
                    "Пароль не соответствует требованием безопасности")

    def same_if_empty(self, caption: str, src_value: str) -> str:
        value = self.input(caption)
        if value == "":
            value = src_value
        return value

    def name(self) -> str:
        return self.input("Введите часть имени")

    def full_name(self, one_line: bool = False) -> FullName:
        if one_line:
            while(True):
                value: str = self.input("Введите полное имя")
                if PIH.CHECK.full_name(value):
                    return FullNameTool.from_string(PIH.DATA.FORMAT.name(value))
                else:
                    pass
        else:
            def full_name_part(caption: str) -> str:
                while(True):
                    value: str = self.input(caption)
                    value = value.strip()
                    if PIH.CHECK.name(value):
                        return PIH.DATA.FORMAT.name(value)
                    else:
                        pass
            return FullName(full_name_part("Введите фамилию"), full_name_part("Введите имя"), full_name_part("Введите отчество"))

    def yes_no(self, text: str = " ", enter_for_yes: bool = False, yes_label: str = None, no_label: str = None, yes_checker: Callable[[str], bool] = None) -> bool:
        text = self.output.blue_str(self.output.text_color(Fore.WHITE, text))
        self.output.write_line(f"{text}? \n{self.output.green_str(self.output.text_black('Да (1 или Ввод)'))} / {self.output.red_str(self.output.text_black('Нет (Остальное)'), '')}" if enter_for_yes else
                               f"{text}? \n{self.output.red_str('Да (1)')} / {self.output.green_str(self.output.text_black('Нет (Остальное или Ввод)'), '')}")
        answer: str = self.input()
        answer = answer.lower()
        self.answer = answer
        return answer == "y" or answer == "yes" or answer == "1" or (answer == "" and enter_for_yes)

    def message_for_user_by_login(self, login: str) -> str:
        user: User = PIH.RESULT.USER.by_login(login).data
        if user is not None:
            head_string = f"Здравствуйте, {FullNameTool.to_given_name(user.name)}, "
            self.output.green(head_string)
            message = self.input("Введите сообщениеt: ")
            return head_string + message
        else:
            pass

    def polibase_person_any(self, title: str | None = None) -> str:
        return self.input(title or "Введите персональный номер или часть имени пациента")


class MarkInput(MarkInputBase):

    def __init__(self, input: Input = None):
        self.parent = input

    def free(self, group: MarkGroup = None) -> Mark:
        result: Result[list[Mark]] = None
        while True:
            if group is None:
                if self.parent.yes_no("Выбрать группы доступа для карты доступа, введя имени пользователя из этой группы"):
                    result = PIH.RESULT.MARK.by_name(self.parent.name())
                    mark_list: list[Mark] = result.data
                    length = len(mark_list)
                    if length > 0:
                        if length > 1:
                            self.parent.output.table_with_caption_first_title_is_centered(
                                result, "Найденные пользователи:", True)
                        group = self.parent.item_by_index(
                            "Выберите группу доступа", mark_list)
                    else:
                        self.parent.output.error(
                            "Пользователь с введенным именем не найден")
                else:
                    result = PIH.RESULT.MARK.free_marks_group_statistics(False)
                    data = result.data
                    length = len(data)
                    if length > 0:
                        if length > 1:
                            self.parent.output.free_marks_group_statistics_for_result(
                                result, True)
                        group = self.parent.item_by_index(
                            "Выберите группу доступа введя индекс", data)
                    else:
                        self.parent.output.error("Свободный карт доступа нет!")
                        return None
            else:
                result = PIH.RESULT.MARK.free_marks_by_group_id(group.GroupID)
                data = result.data
                length = len(data)
                if length > 0:
                    if length > 1:
                        self.parent.output.free_marks_by_group_for_result(
                            group, result, True)
                    return self.parent.item_by_index(
                        "Выберите карту доступа введя индекс", data)
                else:
                    self.parent.output.error(
                        f"Нет свободных карт для группы доступа '{group.GroupName}'!")
                    return self.free()

    def person_division(self) -> MarkDivision:
        division_list: list[MarkDivision] = PIH.RESULT.MARK.person_divisions().data
        division_list.insert(0, MarkDivision(0, "Без подразделения"))
        return self.parent.item_by_index("Выберите подразделение для персоны, которой принадлежит карта доступа", division_list, lambda item, _: item.name )

    def by_name(self) -> Mark:
        self.parent.output.head2("Введите имя персоны")
        result: Result[list[Mark]] = None
        while result is None:
            try:
                result = PIH.RESULT.MARK.by_name(
                    self.parent.name())
            except NotFound as error:
                self.parent.output.error(error.get_details())
        self.parent.output.mark.result(result, "Карты доступа", True)
        return self.parent.item_by_index("Выберите карточку, введя индекс", result.data)

    def by_any(self, value: str = None) -> Mark:
        result: Result[list[Mark]] = None
        while result is None:
            try:
                result = PIH.RESULT.MARK.by_any(value or self.any())
            except NotFound as error:
                self.parent.output.error(error.get_details())
        self.parent.output.mark.result(result, "Карты доступа", True)
        return self.parent.item_by_index("Выберите карточку, введя индекс", result.data)

    def any(self) -> str:
        return self.parent.input(
            "Введите часть имени или табельный номер держателя карты")


class UserInput(UserInputBase):

    def __init__(self, input: Input = None):
        self.parent = input

    def container(self) -> UserContainer:
        result: Result[list[UserContainer]] = PIH.RESULT.USER.containers()
        self.parent.output.containers_for_result(result, True)
        return self.parent.item_by_index("Выберите контейнер пользователя, введя индекс", result.data)

    def by_name(self) -> User:
        result: Result[list[User]] = PIH.RESULT.USER.by_name(
            self.parent.name())
        result.fields = FIELD_COLLECTION.AD.USER_NAME
        self.parent.output.table_with_caption(
            result, "Список пользователей", True)
        return self.parent.item_by_index("Выберите пользователя, введя индекс", result.data)

    def title_any(self, title: str = None) -> str:
        return self.parent.input(title or "Введите логин, часть имени или другой поисковый запрос")

    def by_any(self, value: str = None, active: bool = None, title: str = None, use_all: bool = False) -> list[User]:
        result: Result[list[User]] = PIH.RESULT.USER.by_any(value or self.title_any(title), active)
        label_function: Callable[[Any, int], str] = (lambda item, _: "Все" if item is None else item.name) if len(
            result.data) > 1 else None
        if use_all and len(result.data) > 1:
            result.data.append(None)
        result_data: User = self.parent.item_by_index("Выберите пользователя, введя индекс", result.data, label_function)
        return result.data if result_data is None else [result_data]

    def telephone_number(self, value: str = None, active: bool = None, title: str = None) -> User:
        try:
            return self.by_any(value, active, title)
        except NotFound:
            return None


    def template(self) -> dict:
        result: Result[list[User]] = PIH.RESULT.USER.template_list()
        self.parent.output.template_users_for_result(result, True)
        return self.parent.item_by_index("Выберите шаблон пользователя, введя индекс", result.data)

    def search_attribute(self) -> str:
        return self.parent.indexed_field_list("Выберите по какому критерию искать, введя индекс",
                                             FIELD_COLLECTION.AD.SEARCH_ATTRIBUTE)

    def search_value(self, search_attribute: str) -> str:
        field_item = FIELD_COLLECTION.AD.SEARCH_ATTRIBUTE.get_item_by_name(
            search_attribute)
        return self.parent.input(f"Введите {field_item.caption.lower()}")

    def generate_password(self, once: bool = False, settings: PasswordSettings = PASSWORD.SETTINGS.DEFAULT) -> str:
        def internal_generate_password(settings: PasswordSettings = None) -> str:
            return PasswordTools.generate_random_password(settings.length, settings.special_characters,
                                                          settings.order_list, settings.special_characters_count,
                                                          settings.alphabets_lowercase_count, settings.alphabets_uppercase_count,
                                                          settings.digits_count, settings.shuffled)
        while True:
            password = internal_generate_password(settings)
            if once or self.parent.yes_no(f"Использовать пароль {password}", True):
                return password
            else:
                pass

    def generate_login(self, full_name: FullName, ask_for_remove_inactive_user_if_login_is_exists: bool = True, ask_for_use: bool = True) -> str:
        login_list: list[str] = []
        inactive_user_list: list[User] = []
        login_is_exists: bool = False

        def show_user_which_login_is_exists_and_return_user_if_it_inactive(login_string: str) -> User:
            user: User = PIH.RESULT.USER.by_login(login_string).data
            is_active: bool = PIH.CHECK.USER.active(user)
            self.parent.output.error(
                f"Логин '{login_string}' занят {'активным' if is_active else 'неактивным'} пользователем: {user.name}")
            self.parent.output.new_line()
            return user if not is_active else None
        login: FullName = NamePolicy.convert_to_login(full_name)
        login_string: str = FullNameTool.to_string(login, "")
        login_list.append(login_string)
        need_enter_login: bool = False

        def remove_inactive_user_action():
            login_string: str = None
            need_enter_login: bool = False
            if self.parent.yes_no("Удалить неактивных пользователей, чтобы освободить логин", True):
                user_for_remove: User = self.parent.item_by_index(
                    "Выберите пользователя для удаления, выбрав индекс", inactive_user_list, lambda item, _: f"{item.name} ({item.samAccountName})")
                self.parent.output.new_line()
                self.parent.output.value(f"Пользователь для удаления",
                                        user_for_remove.name)
                if self.parent.yes_no("Удалить неактивного пользователя", True):
                    if PIH.ACTION.USER.remove(user_for_remove):
                        self.parent.output.good("Удален")
                        login_string = user_for_remove.samAccountName
                        inactive_user_list.remove(user_for_remove)
                    else:
                        self.parent.output.error("Ошибка")
                else:
                    need_enter_login = True
            else:
                need_enter_login = True
            return need_enter_login, login_string
        if PIH.CHECK.USER.exists_by_login(login_string):
            user: User = show_user_which_login_is_exists_and_return_user_if_it_inactive(login_string)
            if user is not None:
                inactive_user_list.append(user)
            login_alt: FullName = NamePolicy.convert_to_alternative_login(login)
            login_string = FullNameTool.to_string(login_alt, "")
            login_is_exists = login_string in login_list
            if not login_is_exists:
                login_list.append(login_string)
            if login_is_exists or PIH.CHECK.USER.exists_by_login(login_string):
                if not login_is_exists:
                    user = show_user_which_login_is_exists_and_return_user_if_it_inactive(
                        login_string)
                    if user is not None:
                        inactive_user_list.append(user)
                login_reversed: FullName = NamePolicy.convert_to_reverse_login(login)
                login_is_exists = login_string in login_list
                login_string = FullNameTool.to_string(login_reversed, "")
                if not login_is_exists:
                    login_list.append(login_string)
                if login_is_exists or PIH.CHECK.USER.exists_by_login(login_string):
                    login_last: FullName = NamePolicy.convert_to_last_login(login)
                    login_string = FullNameTool.to_string(login_last, "")
                    if not login_is_exists:
                        user = show_user_which_login_is_exists_and_return_user_if_it_inactive(login_string)
                        if user is not None:
                            inactive_user_list.append(user)
                    if ask_for_remove_inactive_user_if_login_is_exists and len(inactive_user_list) > 0:
                        need_enter_login, login_string = remove_inactive_user_action()
                    if need_enter_login:
                        while True:
                            login_string = self.parent.login()
                            if PIH.CHECK.USER.exists_by_login(login_string):
                                show_user_which_login_is_exists_and_return_user_if_it_inactive(
                                    login_string)
                            else:
                                break
        if not need_enter_login and ask_for_remove_inactive_user_if_login_is_exists and len(inactive_user_list) > 0:
            need_enter_login, login_string = remove_inactive_user_action()
            if need_enter_login:
                return self.generate_login(full_name, False)
        else:
            if ask_for_use and not self.parent.yes_no(f"Использовать логин '{login_string}' для аккаунта пользователя", True):
                login_string = self.parent.login(True)

        return login_string


def while_not_do(check_action: Callable[[None], bool], attemp_count: int = None, success_handler: Callable[[None], None] = None, start_handler: Callable[[None], None] = None, sleep_time: int = None, action: Callable[[None], None] = None) -> None:
    while not check_action():
        if start_handler is not None:
            start_handler()
            start_handler = None
        if action is not None:
            action()
        if attemp_count is not None:
            if attemp_count == 0:
                break
            attemp_count -= 1
        if sleep_time is not None:
            sleep(sleep_time)
    if success_handler is not None:
        success_handler()


class NotImplemented(BaseException):
    pass


class ZeroReached(BaseException):
    pass


class NotFound(BaseException):

    def get_details(self) -> str:
        return self.args[0]

    def get_value(self) -> str:
        return DataTool.by_index(self.args, 1)


class IncorrectInputFile(BaseException):
    pass


class NotAccesable(BaseException):
    pass


class NamePolicy:

    @staticmethod
    def get_first_letter(name: str) -> str:
        from transliterate import translit
        letter = name[0]
        if letter.lower() == "ю":
            return "yu"
        return translit(letter, "ru", reversed=True).lower()

    @staticmethod
    def convert_to_login(full_name: FullName) -> FullName:
        return FullName(
            NamePolicy.get_first_letter(
                full_name.last_name),
            NamePolicy.get_first_letter(
                full_name.first_name),
            NamePolicy.get_first_letter(full_name.middle_name))

    @staticmethod
    def convert_to_alternative_login(login_list: FullName) -> FullName:
        return FullName(login_list.first_name, login_list.middle_name, login_list.last_name)

    @staticmethod
    def convert_to_last_login(login_list: FullName) -> FullName:
        return FullName(login_list.first_name, login_list.last_name, login_list.middle_name)

    @staticmethod
    def convert_to_reverse_login(login_list: FullName) -> FullName:
        return FullName(login_list.middle_name, login_list.first_name, login_list.last_name)


class PIH:

    NAME: str = "pih"
    NAME_ALT: str = "пих"

    def __init__(self, input: InputBase = None, output: OutputBase = None, session: SessionBase = None): 
        if output is None:
            output = Output(UserOutput(), MarkOutput())
            PIH.output: Output = output
        else:
            self.output: Output = output
        if input is None:
            input = Input(
                UserInput(), MarkInput(), PIH.output)
            PIH.input: Input = input
        else:
            self.input: Input = input
        if session is None: 
            PIH.session: Session = Session(input, output)
        else:
            self.session: Session = session
        
    class MOBILE_HELPER:

        ANSWER: dict[str, list[str]] = defaultdict(list)

        @staticmethod
        def create_output(recipient: str) -> Output:
            return PIH.MESSAGE.WHATSAPP.create_output(recipient)

        @staticmethod
        def waiting_for_input_from(recipient: str, handler: Callable[[str, Callable[[None], None]], None] | None = None) -> str | None:
            def internal_handler(message: str, close_handler: Callable[[None], None]) -> None:
                PIH.MOBILE_HELPER.ANSWER[recipient].append(message)
                if DataTool.is_empty(handler):
                    close_handler()
                else:
                    handler(message, close_handler)  
            PIH.EVENT.waiting_for_mobile_helper_message_input(
                recipient, internal_handler)
            return PIH.MOBILE_HELPER.ANSWER[recipient][-1] 

    class VERSION:

        @staticmethod
        def local() -> str:
            return "1.43"

        @staticmethod
        def need_update() -> bool:
            return importlib.util.find_spec(PIH.NAME) is not None and PIH.VERSION.local() < PIH.VERSION.remote()

        @staticmethod
        def remote() -> str:
            try:
                req = requests.get(URLS.PYPI)
                version = parse("0")
                if req.status_code == requests.codes.ok:
                    data = json.loads(req.text.encode(req.encoding))
                    releases = data.get("releases", [])
                    for release in releases:
                        ver = parse(release)
                        if not ver.is_prerelease:
                            version = max(version, ver)
                return str(version)
            except ConnectionError:
                return 

    class ERROR:

        notify_about_error: bool = True

        @staticmethod
        def create_error_header(details: str) -> str:
            return f"\nВерсия: {PIH.VERSION.local()}/{PIH.VERSION.remote()}\nПользователь: {PIH.OS.get_login()}\nКомпьютер: {PIH.OS.host()}\n{details}"

        @staticmethod
        def rpc_error_handler(details: str, code: Tuple, service_role_description: ServiceRoles, command: ServiceCommands) -> None:
            if isinstance(command, ServiceCommands):
                if code == StatusCode.UNAVAILABLE:
                    PIH.output.error(f"Error: {details}")
                    return
                elif code == StatusCode.DEADLINE_EXCEEDED or details.lower().find("stream removed") != -1:
                    return
                else:
                    if PIH.ERROR.notify_about_error:
                        PIH.LOG.debug(
                            PIH.ERROR.create_error_header(details), LogLevels.ERROR)
            raise Error(details, code) from None

        @staticmethod
        def global_except_hook(exctype, value, __traceback__):
            details_list: list[str] = []
            for item in value.args:
                if isinstance(item, str):
                    details_list.append(item)
            details: str = "\n".join(traceback.format_exception(value))
            if PIH.ERROR.notify_about_error:
                PIH.LOG.debug(
                    PIH.ERROR.create_error_header(details), LogLevels.ERROR)
            sys.__excepthook__(exctype, value, traceback)

        sys.excepthook = global_except_hook

        class POLIBASE:

            @staticmethod
            def create_not_found_error(title: str, value: str, start: str = "Пациент/Клиент") -> str:
                return NotFound(f"{start} с {title} '{value}' не найден", value)

        
        class USER:

            @staticmethod
            def get_not_found_error(title: str, active: bool, value: str) -> str:
                start: str = None
                if active is None:
                    start = "Пользователь"
                elif active:
                    start = "Активный пользователь"
                else:
                    start = "Неактивный пользователь"
                return NotFound(f"{start} с {title} '{value}' не найден", value)

    class UPDATER:

        @staticmethod
        def update_for_service(service_role: ServiceRoles, pih_update: bool = True, modules_update: bool = True, show_output: bool = False) -> bool:
            service_role_description: ServiceRoleDescription = service_role.value
            returncode: int = 0
            if pih_update:
                remote_executor_command_list: list[str] = PIH.PSTOOLS.create_remote_process_executor_for_service(service_role_description, True)
                command_list: list[str] = remote_executor_command_list + \
                    PIH.UPDATER.get_module_updater_command_list(PIH.NAME, None)
                process_result: CompletedProcess = PIH.PSTOOLS.execute_command_list(
                    command_list, show_output)
                returncode = process_result.returncode
            result: bool = returncode == 0
            if modules_update and result:
                installed_module_list: list[str] = {
                    pkg.key.lower() for pkg in pkg_resources.working_set}
                for module_name in [item.lower() for item in service_role_description.modules]:
                    if module_name not in installed_module_list:
                        result = result and PIH.UPDATER.install_module(
                            module_name, show_output=show_output)
                        if result:
                            pkg_resources.working_set.add_entry(module_name)
                        else:
                            break
            return result

        @staticmethod
        def get_module_updater_command_list(module_name: str, version: str = None) -> list[str]:
            return ["-m", CONST.PYTHON.PYPI, "install"] + ([f"{module_name}=={version}"] if version is not None else [module_name, "-U"])

        @staticmethod
        def update_localy(version: str = None, show_output: bool = False) -> bool:
            return PIH.UPDATER.install_module(PIH.NAME, version, show_output)

        @staticmethod
        def install_module(module_name: str, version: str = None, show_output: bool = False) -> bool:
            command_list = PIH.UPDATER.get_module_updater_command_list(
                module_name, version)
            command_list.pop(0)
            process_result: CompletedProcess = PIH.PSTOOLS.execute_command_list(
                command_list, show_output)
            returncode = process_result.returncode
            return returncode == 0

        @staticmethod
        def update_remote(host: str, show_output: bool = False) -> bool:
            remote_executor_command_list: list[str] = PIH.PSTOOLS.create_command_list_for_psexec_command(
                host)
            command_list: list[str] = remote_executor_command_list + \
                PIH.UPDATER.get_module_updater_command_list()
            process_result: CompletedProcess = PIH.PSTOOLS.execute_command_list(
                command_list, show_output)
            returncode = process_result.returncode
            return returncode == 0

        @staticmethod
        def update_action(start_handler: Callable, update_start_handler: Callable, update_complete_handler: Callable) -> None:
            need_update: bool = PIH.VERSION.need_update()

            def internal_update_action(need_update: bool, start_handler: Callable, update_start_handler: Callable, update_complete_handler: Callable):
                if need_update:
                    update_start_handler()
                    if PIH.UPDATER.update_localy():
                        import importlib
                        importlib.reload(sys.modules[PIH.NAME])
                        importlib.reload(sys.modules[f"{PIH.NAME}.{PIH.NAME}"])
                        update_complete_handler()
                        start_handler()
                else:
                    start_handler()
            Thread(target=internal_update_action, args=(
                need_update, start_handler, update_start_handler, update_complete_handler,)).start()

    class SETTINGS:

        @staticmethod
        def to_datetime(value: SETTINGS) -> datetime:
            return PIH.DATA.CONVERT.settings_to_datetime(value)
        
        @staticmethod
        def to_datetime_list(value: SETTINGS) -> list[datetime]:
            return PIH.DATA.CONVERT.settings_to_datetime_list(value)

        @staticmethod
        def set(settings_item: SETTINGS, value: Any) -> bool:
            return PIH.ACTION.SETTINGS.set(settings_item, value)

        @staticmethod
        def set_default(settings_item: SETTINGS) -> bool:
            return PIH.ACTION.SETTINGS.set_default(settings_item)

        @staticmethod
        def get(settings_item: SETTINGS) -> Any:
            return PIH.RESULT.SETTINGS.get(settings_item).data

        @staticmethod
        def init() -> None:
            for setting_item in SETTINGS:
                if setting_item.value.auto_init:
                    PIH.SETTINGS.set_default(setting_item)

        class WORKSTATION:

            @staticmethod
            def shutdown_time() -> datetime:
                return PIH.DATA.CONVERT.settings_to_datetime(SETTINGS.WORKSTATION_SHUTDOWN_TIME)
            
            @staticmethod
            def reboot_time() -> datetime:
                return PIH.DATA.CONVERT.settings_to_datetime(SETTINGS.WORKSTATION_REBOOT_TIME)

        class USER:

            @staticmethod
            def use_cache() -> bool:
                return PIH.SETTINGS.get(SETTINGS.USER_USE_CACHE)
            
        class INDICATION:

            @staticmethod
            def ct_notification_start_time() -> list[datetime]:
                return PIH.DATA.CONVERT.settings_to_datetime(SETTINGS.INDICATION_CT_NOTIFICATION_START_TIME)
            
        class RESOURCE:
    
            @staticmethod
            def site_check_certificate_start_time() -> datetime:
                return PIH.DATA.CONVERT.settings_to_datetime(
                    SETTINGS.RESOURCE_MANAGER_CHECK_SITE_CERTIFICATE_START_TIME)
            
            @staticmethod
            def site_check_free_spcae_perion_in_minutes() -> int:
                return PIH.SETTINGS.get(SETTINGS.RESOURCE_MANAGER_CHECK_SITE_FREE_SPACE_PERIOD_IN_MINUTES)


        class POLIBASE:

            @staticmethod
            def test_recipient(sender: Any) -> str | None:
                if sender == CONST.MESSAGE.WHATSAPP.WAPPI.PROFILE.CALL_CENTRE.value:
                    return PIH.SETTINGS.get(SETTINGS.POLIBASE_PERSON_VISIT_NOTIFICATION_TEST_TELEPHONE_NUMBER)
                if sender == CONST.MESSAGE.WHATSAPP.WAPPI.PROFILE.MARKETER.value:
                    return PIH.SETTINGS.get(SETTINGS.POLIBASE_PERSON_REVIEW_NOTIFICATION_TEST_TELEPHONE_NUMBER)
                return None
            
            class REVIEW_NOTIFICATION:

                @staticmethod
                def start_time() -> datetime:
                    return PIH.DATA.CONVERT.settings_to_datetime(SETTINGS.POLIBASE_PERSON_REVIEW_NOTIFICATION_START_TIME)

                @staticmethod
                def is_on() -> bool:
                    return PIH.SETTINGS.get(SETTINGS.POLIBASE_PERSON_REVIEW_NOTIFICATION_IS_ON)

                @staticmethod
                def day_delta() -> int:
                    return PIH.SETTINGS.get(SETTINGS.POLIBASE_PERSON_REVIEW_NOTIFICATION_DAY_DELTA)

                @staticmethod
                def notification_text(person: PolibasePerson, notification_confirmed: bool) -> str:
                    return str(PIH.SETTINGS.get(SETTINGS.POLIBASE_PERSON_REVIEW_NOTIFICATION_TEXT_FOR_CONFIRMED_NOTIFICATION if notification_confirmed else SETTINGS.POLIBASE_PERSON_REVIEW_NOTIFICATION_TEXT)).format(name=FullNameTool.to_given_name(person))

            class VISIT:

                @staticmethod
                def offer_telegram_bot_url_text(person_full_name: str) -> str:
                    return str(PIH.SETTINGS.get(SETTINGS.POLIBASE_PERSON_TAKE_TELEGRAM_BOT_URL_TEXT)).format(name=FullNameTool.to_given_name(person_full_name)) 

    class PSTOOLS:

        @staticmethod
        def ping(address_or_ip: str, host: str, count: int = 1, timeout: int = 100):
            command_list: list[str] = ["ping", "-4",  address_or_ip, "-n",
                                       str(count), "-w", str(timeout)]
            result: CompletedProcess = PIH.PSTOOLS.execute_command_list(PIH.PSTOOLS.create_command_list_for_psexec_command(command_list, host, interactive=True), True, True)
            out: str = result.stdout
            return result.returncode == 0 and out.count("(TTL)") < count
          
        @staticmethod
        def get_executor_path(executor_name: str) -> str:
            return os.path.join(
                PATHS.WS.PATH, CONST.PSTOOLS.NAME, executor_name)

        @staticmethod
        def as_host(value: str) -> str:
            host_start: str = r"\\"
            return ("" if value.startswith(host_start) else host_start) + value 

        @staticmethod
        def create_command_list_for_command(executor_name: str, command_list: list[str], login: str = None, password: str = None) -> list[str]:
            login = "\\".join([AD.DOMAIN_NAME, AD.ADMINISTRATOR if DataTool.is_empty(login) else login])
            password = password or AD.ADMINISTRATOR_PASSOWORD
            return [PIH.PSTOOLS.get_executor_path(executor_name), CONST.PSTOOLS.NO_BANNER, CONST.PSTOOLS.ACCEPTEULA, "-u", login, "-p", password]  + command_list
        
        @staticmethod
        def create_command_list_for_psexec_command(command_list: list[str], host: str = None, login: str = None, password: str = None, interactive: bool = False, run_from_system_account: bool = False, run_with_elevetion: bool = False) -> list[str]:
            result_command_list: list[str] = ["-i" if interactive else "-d"]
            host_start: str = r"\\"
            if not DataTool.is_empty(host):
                result_command_list.append(("" if host.startswith(host_start) else host_start) + host)
            if run_from_system_account:
                result_command_list.append("-s")
            if run_with_elevetion:
                result_command_list.append("-h")
            return PIH.PSTOOLS.create_command_list_for_command(CONST.PSTOOLS.PS_EXECUTOR, result_command_list + command_list, login, password)

        @staticmethod
        def create_remote_process_executor_for_service(service_role_or_description: ServiceRoles | ServiceRoleDescription, interactive: bool = False) -> list[str]:
            service_role_description: ServiceRoleDescription = service_role_or_description if isinstance(service_role_or_description, ServiceRoleDescription) else service_role_or_description.value
            return PIH.PSTOOLS.create_command_list_for_psexec_command([CONST.PYTHON.EXECUTOR], PIH.SERVICE.get_host(service_role_description), service_role_description.login, service_role_description.password, interactive)

        @staticmethod
        def execute_command_list(command_list: list[str], show_output: bool, capture_output: bool = False) -> CompletedProcess:
            if show_output:
                if capture_output:
                    process_result = subprocess.run(
                        command_list, capture_output=True, text=True)
                else:
                    process_result = subprocess.run(
                        command_list, text=True)
            else:
                process_result = subprocess.run(
                    command_list, stdout=DEVNULL, stderr=STDOUT, text=True)
            return process_result
       
        @staticmethod
        def kill_process(name_or_pid: str | int, host: str, show_output: bool = False) -> bool:
           return PIH.PSTOOLS.execute_command_list(PIH.PSTOOLS.create_command_list_for_command(CONST.PSTOOLS.PS_KILL_EXECUTOR, ["-t", str(name_or_pid), PIH.PSTOOLS.as_host(host)]), show_output).returncode == 0

        @staticmethod
        def kill_process_via_windows(name_or_pid: str | int, host: str, show_output: bool = False) -> bool:
           is_string : bool = isinstance(name_or_pid, str)
           return PIH.PSTOOLS.execute_command_list(["taskkill", "/S", PIH.PSTOOLS.as_host(host), "/F", "/IM" if is_string else "/PID", PIH.PATH.add_extension(name_or_pid, FILE.EXTENSION.EXE) if is_string else str(name_or_pid)], show_output).returncode == 0

        @staticmethod
        def reboot(host: str, show_output: bool = False) -> bool:
            return PIH.PSTOOLS.execute_command_list(A.PS.create_command_list_for_psexec_command(
                ["shutdown", "/r", "/t", "0"], host), show_output).returncode == 0

        @staticmethod
        def shutdown(host: str, show_output: bool = False) -> bool:
            return PIH.PSTOOLS.execute_command_list(A.PS.create_command_list_for_psexec_command(
                ["shutdown", "/s", "/t", "0"], host), show_output).returncode == 0
        
    class EVENT:

        @staticmethod
        def on_log_command(handler: Callable[[ParameterList, ServiceListener], None]) -> None:
            ServiceListener().listen_for([ServiceCommands.send_log_command], lambda _, parameter_list, service_listener: handler(parameter_list, service_listener))

        @staticmethod
        def wait_server_start(handler_or_server_name: Callable[[str, Callable[[None], None]], None] | str) -> None:
            def internal_handler(parameter_list: ParameterList, listener: ServiceListener) -> None:
                log_command, parameters = PIH.DATA.EXTRACT.SERVICE_PARAMETER_LIST.log_command_parameters(parameter_list)
                if log_command == LogCommands.SERVER_WAS_STARTED:
                    server_name: str = parameters[0]
                    if callable(handler_or_server_name):
                        handler_or_server_name(server_name, listener.close)
                    else:
                        if handler_or_server_name.startswith(server_name):
                            listener.close()
            PIH.EVENT.on_log_command(internal_handler)

        @staticmethod
        def wait_robocopy_job_complete(handler_or_robocopy_job_name: Callable[[ParameterList, ServiceListener], None] | str) -> None:
            def internal_handler(parameter_list: ParameterList, listener: ServiceListener) -> None:
                log_command, parameters = PIH.DATA.EXTRACT.SERVICE_PARAMETER_LIST.log_command_parameters(parameter_list)
                if log_command ==  A.CT_LC.BACKUP_NOTIFY_ABOUT_ROBOCOPY_JOB_COMPLETED:
                    robocopy_job_status: str = parameters[0]
                    if callable(handler_or_robocopy_job_name):
                        handler_or_robocopy_job_name(
                            robocopy_job_status, listener.close)
                    else:
                        if robocopy_job_status.startswith(handler_or_robocopy_job_name):
                            listener.close()
            PIH.EVENT.on_log_command(internal_handler)

        @staticmethod
        def waiting_for_mobile_helper_message_input(recipient: str, handler: Callable[[str, Callable[[None], None]], None]) -> None:
            def internal_handler(parameter_list: ParameterList, listener: ServiceListener) -> None:
                message: WhatsAppMessage = PIH.DATA.EXTRACT.SERVICE_PARAMETER_LIST.whatsapp_message(parameter_list)
                if not DataTool.is_empty(message) and PIH.DATA.FORMAT.telephone_number(message.sender) == PIH.DATA.FORMAT.telephone_number(recipient):
                    handler(message.message, listener.close)
            PIH.EVENT.on_log_command(internal_handler)

            
    class SERVICE:

        command_map: dict[str, ServiceRoleDescription] = None

        class ADMIN:

            @staticmethod
            def call(service_command: ServiceCommands, parameters: Any) -> str:
                return RPC.call(service_command, parameters)

            @staticmethod
            def subscribe_on(service_command: ServiceCommands, type: int = SubscribtionTypes.AFTER, name: str = None) -> bool:
                return RPC.Service.service.subscribe_on(service_command, type, name)

            @staticmethod
            def unsubscribe(service_command: ServiceCommands, type: int) -> bool:
                return RPC.Service.service.unsubscribe(service_command, type)

            @staticmethod
            def create_developer_service_role_description(port: int = None) -> ServiceRoleDescription:
                if port is None or port == ServiceRoles.DEVELOPER.value.port:
                    return ServiceRoles.DEVELOPER.value
                return ServiceRoleDescription(f"Developer{port}", host=CONST.HOST.DEVELOPER.NAME, port=CONST.RPC.PORT(port))

            @staticmethod
            def develope(service_role: ServiceRoles, port: int = None) -> None:
                developer_service_role_description: ServiceRoleDescription = PIH.SERVICE.ADMIN.create_developer_service_role_description(port)
                service_role_description: ServiceRoleDescription = service_role.value
                service_role_description.auto_restart = False
                service_role_description.host = developer_service_role_description.host
                service_role_description.port = developer_service_role_description.port

            @staticmethod
            def isolate(service_role: ServiceRoles) -> None:
                service_role_description: ServiceRoleDescription = service_role.value
                service_role_description.isolated = True

            @staticmethod
            def start(service_role_or_description: ServiceRoles | ServiceRoleDescription, check_if_started: bool = True, show_output: bool = False) -> bool:
                service_role_description: ServiceRoleDescription = service_role_or_description if isinstance(service_role_or_description, ServiceRoleDescription) else service_role_or_description.value
                if check_if_started:
                    if PIH.SERVICE.check_accessibility(service_role_description):
                        return None
                remote_executor_command_list: list[str] = PIH.PSTOOLS.create_remote_process_executor_for_service(service_role_description)
                service_file_path: str = None
                if service_role_description.service_path is None:
                    service_file_path = os.path.join(
                        CONST.FACADE.PATH, f"{service_role_description.name}{CONST.FACADE.SERVICE_FOLDER_SUFFIX}", PathTool.add_extension(CONST.SERVICE.NAME, FILE.EXTENSION.PYTHON))
                else:
                    service_file_path = os.path.join(
                        service_role_description.service_path, PathTool.add_extension(CONST.SERVICE.NAME, FILE.EXTENSION.PYTHON))
                remote_executor_command_list.append(service_file_path)
                #debug = False
                remote_executor_command_list.append("False")
                process_result = PIH.PSTOOLS.execute_command_list(
                    remote_executor_command_list, show_output)
                returncode = process_result.returncode
                if returncode == 2:
                    return False
                service_role_description.pid = returncode
                return True

            @staticmethod
            def kill_via_pstools(service_role_or_description: ServiceRoles | ServiceRoleDescription) -> bool | None:
                service_role_description: ServiceRoleDescription = service_role_or_description if isinstance(service_role_or_description, ServiceRoleDescription) else service_role_or_description.value
                if PIH.SERVICE.check_accessibility(service_role_description):
                    return PIH.PSTOOLS.kill_process(service_role_description.pid, PIH.PSTOOLS.as_host(PIH.SERVICE.get_host(service_role_description)))
                return None
            
            @staticmethod
            def kill(service_role_or_description: ServiceRoles | ServiceRoleDescription) -> bool: # | None:
                service_role_description: ServiceRoleDescription = service_role_or_description if isinstance(service_role_or_description, ServiceRoleDescription) else service_role_or_description.value
                #if PIH.SERVICE.check_accessibility(service_role_description):
                return PIH.PSTOOLS.kill_process_via_windows(service_role_description.pid, PIH.PSTOOLS.as_host(PIH.SERVICE.get_host(service_role_description)))
                #return None
            
            @staticmethod
            def serve(service_role_or_description: ServiceRoles | ServiceRoleDescription, call_handler: Callable[[str, ParameterList, Any], Any], isolate: bool = False, service_started_handler: Callable[[None], None] = None, depends_on_list: list[ServiceRoles | ServiceRoleDescription] = [], max_workers=None, stop_before: bool = False) -> RPC.Service:
                if stop_before:
                    if PIH.SERVICE.check_accessibility(service_role_or_description):
                        PIH.SERVICE.ADMIN.stop(service_role_or_description)
                service: RPC.Service = RPC.Service()
                service.serve(service_role_or_description, call_handler, isolate, service_started_handler, depends_on_list, max_workers)

            @staticmethod
            def stop(service_role_or_description: ServiceRoles | ServiceRoleDescription) -> None:
                service_role_description: ServiceRoleDescription = service_role_or_description if isinstance(
                            service_role_or_description, ServiceRoleDescription) else service_role_or_description.value
                if PIH.SERVICE.check_accessibility(service_role_description):
                    RPC.stop(service_role_description)  
                    PIH.SERVICE.ADMIN.kill(service_role_description)   
            
            @staticmethod
            def publish(service_role_or_description: ServiceRoles | ServiceRoleDescription) -> bool:
                role_descrption: ServiceRoleDescription = service_role_or_description if isinstance(
                    service_role_or_description, ServiceRoleDescription) else service_role_or_description.value
                return PIH.ACTION.DATA_STORAGE.value(role_descrption)
            
            @staticmethod
            def receive(name: str) -> ServiceRoleDescription:
                return PIH.RESULT.DATA_STORAGE.value(name, ServiceRoleDescription)

        @staticmethod
        def check_accessibility(service_role_or_description: ServiceRoles | ServiceRoleDescription) -> bool:
            role_descrption: ServiceRoleDescription = service_role_or_description if isinstance(
                    service_role_or_description, ServiceRoleDescription) else service_role_or_description.value
            return not DataTool.is_empty(PIH.SERVICE.ping(role_descrption))

        @staticmethod
        def ping(service_role_or_description: ServiceRoles | ServiceRoleDescription) -> ServiceRoleInformation:
            service_role_description: ServiceRoleDescription = service_role_or_description if isinstance(
                    service_role_or_description, ServiceRoleDescription) else service_role_or_description.value
            service_role_informaion: ServiceRoleInformation = RPC.ping(service_role_or_description)
            if service_role_informaion is not None:
                DataTool.fill_data_from_source(
                    service_role_description, service_role_informaion)
                service_role_informaion.subscribers = list(map(lambda item: DataTool.fill_data_from_source(
                    Subscriber(), item), service_role_informaion.subscribers))
            return service_role_informaion
        
        @staticmethod
        def init() -> None:
            if PIH.SERVICE.command_map is None:
                PIH.SERVICE.command_map = {}
                for service_role in ServiceRoles:
                    service_role_description: ServiceRoleDescription = service_role.value
                    for service_command in service_role_description.commands:
                        PIH.SERVICE.command_map[service_command.name] = service_role_description

        @staticmethod
        def get_role_description_by_command(value: ServiceCommands) -> ServiceRoleDescription:
            return PIH.SERVICE.command_map[value.name] if value.name in PIH.SERVICE.command_map else None

        @staticmethod
        def get_host(service_role_or_description: ServiceRoles | ServiceRoleDescription) -> str:
            service_role_description: ServiceRoleDescription = service_role_or_description if isinstance(service_role_or_description, ServiceRoleDescription) else service_role_or_description.value
            if service_role_description.isolated:
                service_role_description.host = PIH.OS.host()
            return service_role_description.host

        @staticmethod
        def get_port(service_role_or_description: ServiceRoles | ServiceRoleDescription) -> str:
            service_role_description: ServiceRoleDescription = service_role_or_description if isinstance(service_role_or_description, ServiceRoleDescription) else service_role_or_description.value
            return service_role_description.port

    class PATH(PATHS, PathTool):

        @staticmethod
        def resolve(value: str) -> str:
            if value[0] == "{" and value[-1] == "}":
                value = value[1: -1]
            return PathTool.resolve(value, PIH.OS.host())
        
        def join(path: str, *paths) -> str:
            return os.path.join(path, *paths)
        
        class QR_CODE:

            @staticmethod
            def polibase_person_card_registry_folder(name: str) -> str:
                name = PIH.DATA.FORMAT.polibase_person_card_registry_folder(name)
                return os.path.join(PATHS.POLIBASE_APP_DATA.PERSON_CARD_FOLDER, PathTool.replace_prohibited_symbols_from_path_with_symbol(PathTool.add_extension(name, FILE.EXTENSION.PNG)))

            @staticmethod
            def mobile_helper_command(name: str) -> str:
                name = PIH.DATA.FORMAT.mobile_helper_command(name)
                return os.path.join(PATHS.MOBILE_HELPER.QR_CODE_FOLDER, PathTool.replace_prohibited_symbols_from_path_with_symbol(PathTool.add_extension(name, FILE.EXTENSION.PNG)))
  

    class DATA(DataTool, StringTool, ListTool, DateTimeTool, EnumTool):

        @staticmethod
        def save_base64_as_image(path: str, content: str) -> bool:
            with open(path, "wb") as file:
                file.write(base64.decodebytes(bytes(content, "utf-8")))
                return True 
            return False

        @staticmethod
        def uuid() -> str:
            return str(uuid.uuid4().hex)
        
        @staticmethod
        def create_email(login: str) -> str:
            return "@".join((login, CONST.SITE_ADDRESS))

        @staticmethod
        def create_user_principal_name(login: str) -> str:
            return "@".join((login, AD.DOMAIN_MAIN))

        class USER:

            @staticmethod
            def by_login(value: str) -> User:
                return PIH.RESULT.USER.by_login(value).data

            @staticmethod
            def by_name(value: str) -> User:
                return PIH.RESULT.USER.by_name(value).data

        class MARK:

            @staticmethod
            def by_tab_number(value: str) -> User:
                return PIH.RESULT.MARK.by_tab_number(value).data

        class SETTINGS:

            @staticmethod
            def get(value: SETTINGS) -> Any:
                return PIH.RESULT.SETTINGS.get(value).data

        class FILTER:

            @staticmethod
            def symbols_only_in(value: str, check_value: str) -> str:
                return "".join(c for c in value if c in check_value)

            @staticmethod
            def users_by_dn(data: list[User], dn: str) -> list:
                return list(filter(lambda x: x.distinguishedName.find(dn) != -1, data))

        class EXTRACT:

            @staticmethod
            def date(value: str, format: str) -> datetime | None:
                result: datetime | None = None
                try:
                    result = DateTimeTool.from_string(value, format)
                except ValueError as error:
                    date_extract_pattern = "[0-9]{1,2}\\.[0-9]{1,2}\\.[0-9]{4}"
                    date_list: list[str] = re.findall(date_extract_pattern, value)
                    if not DataTool.is_empty(date_list):
                        result = PIH.DATA.EXTRACT.date(date_list[0], format)
                return result
            
            @staticmethod
            def wappi_telephone_number(value: any) -> str:
                if isinstance(value, str):
                    return PIH.DATA.FORMAT.telephone_number(value.split(CONST.MESSAGE.WHATSAPP.WAPPI.CONTACT_SUFFIX)[0])
                if isinstance(value, dict):
                    return PIH.DATA.FORMAT.telephone_number(value["user"])

            class SERVICE_PARAMETER_LIST:

                @staticmethod
                def whatsapp_message(parameter_list: ParameterList) -> WhatsAppMessage:
                    result: bool = parameter_list.next()
                    message: WhatsAppMessage = None
                    if result:
                        message_parameters: list[Any] = parameter_list.next()
                        message_command: LogCommands = LogCommands.WHATSAPP_MESSAGE_RECEIVED
                        if EnumTool.get(LogCommands, message_parameters[0]) == message_command:
                            param_item: ParamItem = message_command.value.params[0]
                            message = DataTool.fill_data_from_source(
                                WhatsAppMessage(), message_parameters[1][param_item.name])
                    return message
                
                @staticmethod
                def log_command_parameters(parameter_list: ParameterList) -> tuple[LogCommands, list[Any]]:
                    log_command_content: dict[str, Any] = parameter_list.list[1]
                    log_command: LogCommands = EnumTool.get(LogCommands, log_command_content[0])
                    log_command_parameters: dict[str, Any] = log_command_content[1]
                    result: list[Any] = []
                    if not A.D_C.empty(log_command.value.params):
                        for log_command_parameters_description in log_command.value.params:
                            result.append(log_command_parameters[log_command_parameters_description.name])
                    return log_command, result

            @staticmethod
            def email(value: str) -> str:
                emails: list[str] = re.findall(
                    r"[A-Za-z0-9_%+-.]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,5}", value)
                if len(emails) > 0:
                    return emails[0]
                return None
            
            @staticmethod
            def float(value: str) -> float:
                if not DataTool.is_empty(value):
                    floats: list[str] = re.findall(
                        r"\d+[\.\,]*\d+", value)
                    if len(floats) > 0:
                        return float(floats[0].replace(",", "."))
                return None

            @staticmethod
            def decimal(value: str, min: int = None, max: int = None) -> int | None:
                value = value.strip()
                result: int | None = None
                numbers: list[str] = re.findall(r"\d+", value)
                if len(numbers) > 0:
                    result = int(numbers[0])
                    if min is not None and max is not None and (result < min or result > max):
                        result = None
                return result

            @staticmethod
            def parameter(object: dict, name: str) -> str:
                return object[name] if name in object else ""

            @staticmethod
            def tab_number(mark_object: dict) -> str:
                return PIH.DATA.EXTRACT.parameter(mark_object, FIELD_NAME_COLLECTION.TAB_NUMBER)

            @staticmethod
            def telephone(user_object: dict) -> str:
                return PIH.DATA.EXTRACT.parameter(user_object, FIELD_NAME_COLLECTION.TELEPHONE_NUMBER)

            @staticmethod
            def login(user_object: dict) -> str:
                return PIH.DATA.EXTRACT.parameter(user_object, FIELD_NAME_COLLECTION.LOGIN)

            @staticmethod
            def name(mark_object: dict) -> str:
                return PIH.DATA.EXTRACT.parameter(mark_object, FIELD_NAME_COLLECTION.NAME)

            @staticmethod
            def dn(user_object: dict) -> str:
                return PIH.DATA.EXTRACT.parameter(user_object, FIELD_NAME_COLLECTION.DN)

            @staticmethod
            def group_name(mark_object: dict) -> str:
                return PIH.DATA.EXTRACT.parameter(mark_object, FIELD_NAME_COLLECTION.GROUP_NAME)

            @staticmethod
            def group_id(mark_object: dict) -> str:
                return PIH.DATA.EXTRACT.parameter(mark_object, FIELD_NAME_COLLECTION.GROUP_ID)

            @staticmethod
            def as_full_name(mark_object: dict) -> FullName:
                return FullNameTool.from_string(PIH.DATA.EXTRACT.full_name(mark_object))

            @staticmethod
            def full_name(mark_object: dict) -> str:
                return PIH.DATA.EXTRACT.parameter(mark_object, FIELD_NAME_COLLECTION.FULL_NAME)

            @staticmethod
            def person_id(mark_object: dict) -> str:
                return PIH.DATA.EXTRACT.parameter(mark_object, FIELD_NAME_COLLECTION.PERSON_ID)

            @staticmethod
            def mark_id(mark_object: dict) -> str:
                return PIH.DATA.EXTRACT.parameter(mark_object, FIELD_NAME_COLLECTION.MARK_ID)

            @staticmethod
            def description(object: dict) -> str:
                result = PIH.DATA.EXTRACT.parameter(
                    object, FIELD_NAME_COLLECTION.DESCRIPTION)
                if isinstance(result, Tuple) or isinstance(result, list):
                    return result[0]

            @staticmethod
            def container_dn(user_object: dict) -> str:
                return PIH.DATA.EXTRACT.container_dn_from_dn(PIH.DATA.EXTRACT.dn(user_object))

            @staticmethod
            def container_dn_from_dn(dn: str) -> str:
                return ",".join(dn.split(",")[1:])
            
        class CONVERT:

            @staticmethod
            def settings_to_datetime(item: SETTINGS, format: str = CONST.SECONDLESS_TIME_FORMAT) -> datetime | list[datetime]:
                settings_value: str | list[str] = A.S.get(item)
                return  PIH.DATA.CONVERT.settings_to_datetime_list(item, format) if isinstance(settings_value, list) else DateTimeTool.from_string(settings_value, format)
            
            @staticmethod
            def settings_to_datetime_list(item: SETTINGS, format: str = CONST.SECONDLESS_TIME_FORMAT) -> list[datetime]:
                return list(map( lambda item: DateTimeTool.from_string(item, format), A.S.get(item)))

            @staticmethod
            def file_to_base64(path: str) -> str | None:
                with open(path, "rb") as file:
                    return PIH.DATA.CONVERT.bytes_to_base64(file.read())
                return None
                
            @staticmethod
            def bytes_to_base64(value: bytes) -> str:
                return PIH.DATA.CONVERT.bytes_to_string(PIH.DATA.CONVERT.to_base64(value))
            
            @staticmethod
            def to_base64(value: Any) -> str:
                return base64.b64encode(value)

            @staticmethod 
            def bytes_to_string(value: bytes) -> str:
                return value.decode('utf-8')
            
            
        class CHECK:

            @staticmethod
            def by_secondless_time(value_datetime: datetime, value_str: str) -> bool:
                return False if DataTool.is_empty(value_str) else DateTimeTool.is_equal_by_time(value_datetime, DateTimeTool.from_string(value_str, CONST.SECONDLESS_TIME_FORMAT)) 
            
            @staticmethod
            def empty(value) -> bool:
                return DataTool.is_empty(value)

            @staticmethod
            def decimal(value: int | str) -> bool:
                return isinstance(value, int) or (isinstance(value, str) and value.isdecimal())

        class FORMAT:

            @staticmethod
            def by_name(value: str, data: Any) -> str | None:
                if value == DATA.FORMATTER.MY_DATETIME:
                    return PIH.DATA.FORMAT.datetime(data)
                return None

            @staticmethod
            def polibase_person_card_registry_folder(value: str) -> str:
                return value.upper()

            @staticmethod
            def mobile_helper_command(value: str) -> str:
                return value.lower()

            @staticmethod
            def mobile_helper_qr_code_text(value: str) -> str:
                return PIH.DATA.FORMAT.whatsapp_send_message_to(PIH.DATA.FORMAT.telephone_number_international(PIH.DATA.TELEPHONE_NUMBER.it_administrator()), f"{PIH.NAME} {value}".replace(" ", "+"))
            
            @staticmethod
            def whatsapp_send_message_to(telephone_number: str, message: str) -> str:
                return CONST.MESSAGE.WHATSAPP.SEND_MESSAGE_TO_TEMPLATE.format(telephone_number, message)

            @staticmethod
            def string(value: str) -> str:
                return ("" or value).lower().replace('"', '')
            
            @staticmethod
            def telephone_number(value: str, prefix: str = CONST.TELEPHONE_NUMBER_PREFIX) -> str:
                if DataTool.is_empty(value):
                    return value
                if prefix != CONST.TELEPHONE_NUMBER_PREFIX:
                    value = value[value.find(prefix):]
                src_value: str = value
                if value is not None and len(value) > 0:
                    value = re.sub("[\-\(\) ]", "", value)
                    if value.startswith(prefix):
                        value = value[len(prefix):]
                    if len(value) == 0:
                        return src_value
                    value = prefix + \
                        (value[1:] if (value[0] ==
                         "8" or value[0] == CONST.INTERNATIONAL_TELEPHONE_NUMBER_PREFIX) else value)
                    pattern: str = ("^\\" if prefix[0] == "+" else "^") + prefix + "[0-9]{10}"
                    matcher: re.Match = re.match(pattern, value)
                    if matcher is not None:
                        return matcher.group(0)
                    else:
                        return src_value
                else:
                    return src_value

            @staticmethod
            def telephone_number_international(value: str) -> str:
                return PIH.DATA.FORMAT.telephone_number(value, CONST.INTERNATIONAL_TELEPHONE_NUMBER_PREFIX)

            @staticmethod
            def email(value: str) -> str:
                return value.lower()

            @staticmethod
            def name(value: str, remove_non_alpha: bool = False, name_part_minimal_length: int | None = None) -> str:
                name_part_list: list[str] = list(
                    filter(lambda item: len(item) > (0 if name_part_minimal_length is None else name_part_minimal_length - 1), value.split(" ")))
                if len(name_part_list) == 1:
                    value = value.lower()
                    value = re.sub("[^а-я]+", "",
                                   value) if remove_non_alpha else value
                    if len(value) > 1:
                        value = StringTool.capitalize(value)
                    return value
                return " ".join(list(map(lambda item: PIH.DATA.FORMAT.name(item, remove_non_alpha), name_part_list)))

            @staticmethod
            def location_list(value: str, remove_first: bool = True, reversed: bool = True) -> list[str]:
                location_list: list[str] = value.split(
                    ",")[1 if remove_first else 0:]
                if reversed:
                    location_list.reverse()
                return list(map(
                    lambda item: item.split("=")[-1], location_list))

            @staticmethod
            def get_user_account_control_values(uac: int) -> list[str]:
                result: list[str] = []
                for count, item in enumerate(AD.USER_ACCOUNT_CONTROL):
                    if (pow(2, count) & uac) != 0:
                        result.append(item)
                return result
            
            @staticmethod
            def description(value: str) -> str:
                return (value.split("|")[0]).rstrip()
            
            def datetime(iso_datetime_string: str) -> str:
                return DateTimeTool.datetime_to_string(datetime.fromisoformat(iso_datetime_string), CONST.MY_DATE_FORMAT)

        class TELEPHONE_NUMBER:

            wappi_profile_TO_TELEPHONE_NUMBER_MAP: dict = None

            @staticmethod
            def all(active: bool = True) -> list[str]:
                def filter_function(user: User) -> str:
                    return user.telephoneNumber is not None
                def map_function(user: User) -> str:
                    return PIH.DATA.FORMAT.telephone_number(user.telephoneNumber)
                return ResultTool.map(ResultTool.filter(PIH.RESULT.USER.by_name(AD.SEARCH_ALL_PATTERN, active=active), filter_function), map_function).data

            @staticmethod
            def it_administrator() -> str:
                return PIH.DATA.TELEPHONE_NUMBER.by_login(AD.ADMINISTRATOR)

            @staticmethod
            def call_centre_administrator() -> str:
                return PIH.DATA.TELEPHONE_NUMBER.by_login(AD.CALL_CENTRE_ADMINISTRATOR)

            @staticmethod
            def marketer() -> str:
                return PIH.DATA.TELEPHONE_NUMBER.by_login(AD.MARKETER)

            @staticmethod
            def for_wappi(value: Any) -> str:
                WP = CONST.MESSAGE.WHATSAPP.WAPPI.PROFILE
                value = EnumTool.get_by_value_or_key(WP, value)
                map: dict = PIH.DATA.TELEPHONE_NUMBER.wappi_profile_TO_TELEPHONE_NUMBER_MAP
                if map is None:
                    map = {
                        WP.CALL_CENTRE: PIH.DATA.TELEPHONE_NUMBER.call_centre_administrator(),
                        WP.IT: PIH.DATA.TELEPHONE_NUMBER.it_administrator(),
                        WP.MARKETER: PIH.DATA.TELEPHONE_NUMBER.marketer(),
                    }
                    PIH.DATA.TELEPHONE_NUMBER.wappi_profile_TO_TELEPHONE_NUMBER_MAP = map
                return map[value] if value in map else None

            @staticmethod
            def by_login(value: str, format: bool = True) -> str:
                result: str = PIH.DATA.USER.by_login(value).telephoneNumber
                return PIH.DATA.FORMAT.telephone_number(result) if format else result

            @staticmethod
            def by_workstation_name(value: str) -> str:
                workstation: Workstation = PIH.RESULT.WORKSTATION.by_name(value).data
                return PIH.DATA.TELEPHONE_NUMBER.by_login(workstation.samAccountName)

            @staticmethod
            def by_mark_tab_number(value: str, format: bool = True) -> str:
                result: str = PIH.DATA.MARK.by_tab_number(
                    value).telephoneNumber
                return PIH.DATA.FORMAT.telephone_number(result) if format else result

            @staticmethod
            def by_polibase_person_pin(value: int, format: bool = True) -> bool:
                result: str = PIH.DATA.POLIBASE.person_by_pin(
                    value).telephoneNumber
                return PIH.DATA.FORMAT.telephone_number(result) if format else result

            @staticmethod
            def by_full_name(value: Any, format: bool = True) -> str:
                value_string: str = None
                if isinstance(value, str):
                    value_string = value
                    value = FullNameTool.from_string(value)
                else:
                    value_string = FullNameTool.to_string(value)
                telephone_number: str = PIH.RESULT.MARK.by_full_name(
                    value_string, True).data.telephoneNumber
                if PIH.CHECK.telephone_number(telephone_number):
                    return PIH.DATA.FORMAT.telephone_number(telephone_number) if format else telephone_number
                telephone_number = PIH.RESULT.USER.by_full_name(
                    value_string, True).data.telephoneNumber
                if PIH.CHECK.telephone_number(telephone_number):
                    return PIH.DATA.FORMAT.telephone_number(telephone_number) if format else telephone_number
                details: str = f"Телефон для {value_string} не найден"
                raise NotFound(details)

        class POLIBASE:

            @staticmethod
            def person_by_pin(value: int, test: bool = None) -> PolibasePerson:
                return PIH.RESULT.POLIBASE.person_by_pin(value, test).data

            @staticmethod
            def duplicate_persons_by_person(person: PolibasePerson, check_birth: bool = True) -> list[PolibasePerson]:
                def check_function(check_person: PolibasePerson) -> bool:
                    return check_person.pin != person.pin and (not check_birth or check_person.Birth == person.Birth)
                return ResultTool.get_first_element(ResultTool.filter(PIH.RESULT.POLIBASE.persons_by_full_name(person.FullName), lambda item: check_function(item)))
            
            @staticmethod
            def unique_by_telephone(value: str) -> PolibasePerson:
                value = PIH.DATA.FORMAT.telephone_number(value)
                def check_function(check_person: PolibasePerson) -> bool:
                    return PIH.DATA.FORMAT.telephone_number(check_person.telephoneNumber) == value
                return ResultTool.get_first_element(ResultTool.filter(PIH.RESULT.POLIBASE.person_by_telephone_number(value), lambda item: check_function(item)))

            @staticmethod
            def duplicate_persons_by_person_pin(value: int, check_birth: bool = True) -> list[PolibasePerson]:
                try:
                    return PIH.DATA.POLIBASE.duplicate_persons_by_person(PIH.RESULT.POLIBASE.person_by_pin(value).data, check_birth)
                except NotFound as error:
                    return None

            @staticmethod
            def sort_person_list(value: list[PolibasePerson]) -> None:
                value.sort(key=lambda item: item.pin)

    class OS:

        @staticmethod
        def get_login() -> str:
            return os.getlogin()

        @staticmethod
        def host() -> str:
            return platform.node()

        @staticmethod
        def get_pid() -> int:
            return os.getppid()

    class RESULT(ResultTool):

        class SSH:

            @staticmethod
            def execute(command: str, host: str, username: str | None = None, password: str | None = None) -> Result[list[str]]:
                return DataTool.to_result(
                    RPC.call(ServiceCommands.execute_ssh_command, (command, host, username, password)))

            @staticmethod
            def get_certificate_information(host: str, username: str | None = None, password: str | None = None) -> Result[str | None]:
                return DataTool.to_result(
                    RPC.call(ServiceCommands.get_certificate_information, (host, username, password)))
            
            @staticmethod
            def get_unix_free_space_information_by_drive_name(drive_name: str, host: str, username: str | None = None, password: str | None = None) -> Result[str | None]:
                return DataTool.to_result(
                    RPC.call(ServiceCommands.get_unix_free_space_information_by_drive_name, (drive_name, host, username, password)))

        class DATA_STORAGE:

            @staticmethod
            def value(name: str, class_type: T, section: str = None) -> Result[T]:
                return DataTool.to_result(
                    RPC.call(ServiceCommands.get_storage_value, (name, section)), class_type)
            
            @staticmethod
            def ogrn(code: str) -> Result[OGRN]:
                return DataTool.to_result(
                    RPC.call(ServiceCommands.get_ogrn_value, (code, )), OGRN)
            
            @staticmethod
            def fms_unit_name(code: str) -> Result[str]:
                return DataTool.to_result(
                    RPC.call(ServiceCommands.get_fms_unit_name, (code, )))

        class MESSAGE:

            class DELAYED:

                @staticmethod
                def get(search_condition: MessageSearchCritery = None, take_to_work: bool = False) -> Result[list[DelayedMessageDS]]:
                    return DataTool.to_result(
                        RPC.call(ServiceCommands.search_delayed_messages, (search_condition, take_to_work)), DelayedMessageDS)

        class RESOURCES:

            @staticmethod
            def get_status_list(checkable_section_list: list[CheckableSections] = None, force_update: bool = False, all: bool = False) -> Result[list[ResourceStatus]]:
                def get_type(data: dict) -> ResourceStatus:
                    if "check_certificate_status" in data:
                        return SiteResourceStatus()
                    return ResourceStatus()
                return DataTool.to_result(RPC.call(ServiceCommands.get_resource_status_list, (None if DataTool.is_empty(checkable_section_list) else list(map(lambda item: item.name, checkable_section_list)), force_update, all)), get_type)

            @staticmethod
            def get_resource_status_list(force_update: bool = False, all: bool = False) -> Result[list[ResourceStatus]]:
                return PIH.RESULT.RESOURCES.get_status_list([CheckableSections.RESOURCES], force_update, all)

            @staticmethod
            def get_status(checkable_section_list: list[CheckableSections], resource_desription_or_address: Any, force: bool = False) -> ResourceStatus:
                address: str = None
                if isinstance(resource_desription_or_address, ResourceDescription):
                    address = resource_desription_or_address.address
                elif isinstance(resource_desription_or_address, str):
                    address = resource_desription_or_address
                if not DataTool.is_empty(address):
                    resource_list: list[ResourceStatus] = PIH.RESULT.RESOURCES.get_status_list(checkable_section_list, force).data
                    for item in resource_list:
                        if item.address == address:
                            return item
                return None
            
            @staticmethod
            def get_resource_status(resource_desription_or_address: Any, force: bool = False) -> ResourceStatus:
                return PIH.RESULT.RESOURCES.get_status([CheckableSections.RESOURCES], resource_desription_or_address, force)
            
        class INDICATIONS:

            @staticmethod
            def get_last_items(count: int = 1) -> Result[list[CTIndicationItem]]:
                return DataTool.to_result(RPC.call(ServiceCommands.get_last_ct_indications_value_list, (count, )), CTIndicationItem)


        class BACKUP:

            @staticmethod
            def robocopy_job_status_list() -> Result[list[RobocopyJobStatus]]:
                return DataTool.to_result(RPC.call(ServiceCommands.robocopy_get_job_status_list), RobocopyJobStatus)

        class SETTINGS:

            @staticmethod
            def key(key: str, default_value: Any = None) -> Result[Any]:
                return DataTool.to_result(
                    RPC.call(ServiceCommands.get_settings_value, (key, default_value)))

            @staticmethod
            def get(settings_item: SETTINGS) -> Result[Any]:
                settings_value: SettingsValue = settings_item.value
                return PIH.RESULT.SETTINGS.key(settings_value.key_name or settings_item.name, settings_value.default_value)

        class SERVER:

            pass

        class WORKSTATION:

            @staticmethod
            def all_description() -> Result[list[WorkstationDescription]]:
                return DataTool.to_result(
                    RPC.call(ServiceCommands.get_all_workstation_description), WorkstationDescription)

            @staticmethod
            def all_with_prooperty(value: AD.WSProperies) -> Result[list[Workstation]]:
                def filter_function(workstation: Workstation) -> bool:
                    return BM.has(workstation.properties, value.value)
                return ResultTool.filter(PIH.RESULT.WORKSTATION.all(), filter_function)

            @staticmethod
            def by_login(value: str) -> Result[list[Workstation]]:
                value = PIH.DATA.FORMAT.string(value)
                if PIH.CHECK.USER.exists_by_login(value):
                    return DataTool.to_result(
                        RPC.call(ServiceCommands.get_workstation_by_user, value), Workstation)
                else:
                    details: str = f"Пользователь с логином {value} не найден"
                    raise NotFound(details)

            @staticmethod
            def by_internal_telephone_number(value: int) -> Result[Workstation]:
                result: Result[list[Workstation]] = PIH.RESULT.WORKSTATION.all()
                workstation_list: list[Workstation] = result.data
                result_worksation: Workstation = None
                for workstation in workstation_list:
                    if not DataTool.is_empty(workstation.description):
                        index: int = workstation.description.find(CONST.INTERNAL_TELEPHONE_NUMBER_PREFIX)
                        if index != -1:
                            internal_telephone_number_text: str = workstation.description[index:]
                            internal_telephone_number: int = PIH.DATA.EXTRACT.decimal(internal_telephone_number_text)
                            if internal_telephone_number == value:
                                result_worksation = workstation
                                break
                if result_worksation is not None:#and result_worksation.accessable and not DataTool.is_empty(result_worksation.samAccountName):
                    return Result(result.fields, workstation)
                else:
                    raise PIH.ERROR.USER.get_not_found_error(
                        "внутренним номером телефона", True, str(value))

            @staticmethod
            def by_any(value: Any) -> Result[list[Workstation]]:
                if PIH.DATA.CHECK.decimal(value):
                    return ResultTool.as_list(PIH.RESULT.WORKSTATION.by_internal_telephone_number(int(value)))
                if PIH.CHECK.WORKSTATION.name(value):
                    return ResultTool.as_list(PIH.RESULT.WORKSTATION.by_name(value))
                try:
                    return PIH.RESULT.WORKSTATION.by_login(value)
                except NotFound:
                    detail: str = f"Компьютер с параметром поиска {value} не найден"
                    raise NotFound(detail)

            @staticmethod
            def by_name(value: str) -> Result[Workstation]:
                value = PIH.DATA.FORMAT.string(value)
                result: Result[Workstation] = ResultTool.with_first_element(ResultTool.filter(
                    PIH.RESULT.WORKSTATION.all(), lambda item: item.name.lower() == value.lower()))
                if ResultTool.is_empty(result):
                    raise NotFound(f"Компьютер с именем {value} не найден")
                return result

            @staticmethod
            def all() -> Result[list[Workstation]]:
                def every_action(workstation: Workstation) -> None:
                    workstation.name = workstation.name.lower()
                return ResultTool.every(DataTool.to_result(
                    RPC.call(ServiceCommands.get_all_workstations), Workstation), every_action)

        class INVENTORY:

            @staticmethod
            def report(report_file_path: str, open_for_edit: bool = False) -> Result[list[InventoryReportItem]]:
                return DataTool.to_result(
                    RPC.call(ServiceCommands.get_inventory_report, (report_file_path, open_for_edit)), InventoryReportItem)

        class TIME_TRACKING:

            @staticmethod
            def today(tab_number_list: list[str] = None) -> Result[list[TimeTrackingResultByPerson]]:
                return PIH.RESULT.TIME_TRACKING.create(tab_number_list=tab_number_list)

            def yesterday(tab_number_list: list[str] = None) -> Result[list[TimeTrackingResultByPerson]]:
                yesterday: datetime = DateTimeTool.yesterday()
                return PIH.RESULT.TIME_TRACKING.create(DateTimeTool.start_date(yesterday), DateTimeTool.start_date(yesterday), tab_number_list)

            @staticmethod
            def in_period(day_start: int = 1, day_end: int = None, month: int = None, tab_number: list[str] = None) -> Result[list[TimeTrackingResultByPerson]]:
                now: datetime = datetime.now()
                if month is not None:
                    now = now.replace(month=month)
                start_date: datetime = DateTimeTool.start_date(now)
                end_date: datetime = DateTimeTool.end_date(now)
                if day_start < 0:
                    start_date -= timedelta(days=abs(day_start))
                else:
                    start_date = start_date.replace(day=day_start)
                if day_end is not None:
                    if day_end < 0:
                        day_end -= timedelta(days=abs(day_start))
                    else:
                        day_end = start_date.replace(day=day_start)
                return PIH.RESULT.TIME_TRACKING.create(start_date, end_date, tab_number)

            @staticmethod
            def create(start_date: datetime = None, end_date: datetime = None, tab_number_list: list[str] = None) -> Result[list[TimeTrackingResultByPerson]]:
                now: datetime = datetime.now() if start_date is None or end_date is None else None
                start_date = start_date or DateTimeTool.start_date(now)
                end_date = end_date or DateTimeTool.end_date(now)

                def get_date_or_time(entity: TimeTrackingEntity, date: bool) -> str:
                    return DataTool.not_none_check(entity, lambda: entity.TimeVal.split(CONST.DATE_TIME_SPLITTER)[not date])
                result_data: dict = {}
                full_name_by_tab_number_map: dict = {}
                result_data = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
                data: list[TimeTrackingEntity] = DataTool.to_result(RPC.call(
                    ServiceCommands.get_time_tracking, (start_date, end_date, tab_number_list)), TimeTrackingEntity).data
                for time_tracking_entity in data:
                    tab_number: str = time_tracking_entity.TabNumber
                    full_name_by_tab_number_map[tab_number] = time_tracking_entity.FullName
                    result_data[time_tracking_entity.DivisionName][tab_number][get_date_or_time(time_tracking_entity, True)].append(
                        time_tracking_entity)
                result: list[TimeTrackingResultByDivision] = []
                for division_name in result_data:
                    if division_name is None:
                        continue
                    result_division_item: TimeTrackingResultByDivision = TimeTrackingResultByDivision(
                        division_name)
                    result.append(result_division_item)
                    for tab_number in result_data[division_name]:
                        result_person_item: TimeTrackingResultByPerson = TimeTrackingResultByPerson(
                            tab_number, full_name_by_tab_number_map[tab_number])
                        result_division_item.list.append(result_person_item)
                        for date in result_data[division_name][tab_number]:
                            time_tracking_entity_list: list[TimeTrackingEntity] = result_data[division_name][tab_number][date]
                            time_tracking_enter_entity: TimeTrackingEntity = None
                            time_tracking_exit_entity: TimeTrackingEntity = None
                            for time_tracking_entity_list_item in time_tracking_entity_list:
                                if time_tracking_entity_list_item.Mode == 1:
                                    time_tracking_enter_entity = time_tracking_entity_list_item
                                if time_tracking_entity_list_item.Mode == 2:
                                    time_tracking_exit_entity = time_tracking_entity_list_item
                            duration: int = 0
                            if time_tracking_enter_entity is not None:
                                if time_tracking_exit_entity is not None:
                                    enter_time: datetime = datetime.fromisoformat(
                                        time_tracking_enter_entity.TimeVal).timestamp()
                                    exit_time: datetime = datetime.fromisoformat(
                                        time_tracking_exit_entity.TimeVal).timestamp()
                                    if enter_time < exit_time:
                                        #    enter_time, exit_time = exit_time, enter_time
                                        #    time_tracking_enter_entity, time_tracking_exit_entity = time_tracking_exit_entity, time_tracking_enter_entity
                                        duration = int(exit_time - enter_time)
                                    result_person_item.duration += duration
                            result_person_item.list.append(
                                TimeTrackingResultByDate(date, get_date_or_time(time_tracking_enter_entity, False),
                                                         get_date_or_time(time_tracking_exit_entity, False), duration))
                for division in result:
                    for person in division.list:
                        index: int = 0
                        length: int = len(person.list)
                        for _ in range(length):
                            item: TimeTrackingResultByDate = person.list[index]
                            if item.duration == 0:
                                # if item.enter_time is None and item.exit_time is not None:
                                if index < length - 1:
                                    item_next: TimeTrackingResultByDate = person.list[index + 1]
                                    if item.exit_time is not None:
                                        if item_next.enter_time is not None:
                                            duration = int(datetime.fromisoformat(item.date + CONST.DATE_TIME_SPLITTER + item.exit_time).timestamp(
                                            ) - datetime.fromisoformat(item_next.date + CONST.DATE_TIME_SPLITTER + item_next.enter_time).timestamp())
                                            item.duration = duration
                                            person.duration += duration
                                            if item_next.exit_time is None:
                                                index += 1
                            index += 1
                            if index >= length - 1:
                                break

                return Result(FIELD_COLLECTION.ORION.TIME_TRACKING_RESULT, result)

        class PRINTER:

            @staticmethod
            def all() -> Result[list[PrinterADInformation]]:
                def filter_by_server_name(printer_list: list[PrinterADInformation]) -> list[PrinterADInformation]:
                    return list(filter(lambda item: item.serverName == CONST.HOST.PRINTER_SERVER.NAME, printer_list))
                result: Result[list[PrinterADInformation]] = DataTool.to_result(
                    RPC.call(ServiceCommands.get_printers), PrinterADInformation)
                return Result(result.fields, filter_by_server_name(result.data))

            @staticmethod
            def report(redirect_to_log: bool = True) -> Result[list[PrinterReport]]:
                return DataTool.to_result(
                    RPC.call(ServiceCommands.printers_report, redirect_to_log), PrinterReport)

            @staticmethod
            def status(redirect_to_log: bool = True) -> Result[list[PrinterStatus]]:
                return DataTool.to_result(
                    RPC.call(ServiceCommands.printers_status, redirect_to_log), PrinterStatus)

        class MARK:

            @staticmethod
            def by_tab_number(value: str) -> Result[Mark]:
                result: Result[Mark] = DataTool.to_result(
                    RPC.call(ServiceCommands.get_mark_by_tab_number, value), Mark)
                if ResultTool.is_empty(result):
                    details: str = f"Карта доступа с номером '{value}' не найдена"
                    raise NotFound(details)
                return result

            @staticmethod
            def person_divisions() -> Result[list[Mark]]:
                return DataTool.to_result(RPC.call(ServiceCommands.get_person_divisions), MarkDivision)

            @staticmethod
            def by_name(value: str, first_item: bool = False) -> Result[list[Mark]]:
                return DataTool.to_result(RPC.call(ServiceCommands.get_mark_by_person_name, value), Mark, first_item)

            @staticmethod
            def by_full_name(value: FullName, first_item: bool = False) -> Result[list[Mark]]:
                return PIH.RESULT.MARK.by_name(FullNameTool.from_string(value), first_item)

            @staticmethod
            def temporary_list() -> Result[list[TemporaryMark]]:
                return DataTool.to_result(RPC.call(ServiceCommands.get_temporary_marks), TemporaryMark)

            @staticmethod
            def by_any(value: str) -> Result[list[Mark]]:
                if PIH.CHECK.MARK.tab_number(value):
                    return ResultTool.as_list(PIH.RESULT.MARK.by_tab_number(value))
                elif PIH.CHECK.name(value, True):
                    return PIH.RESULT.MARK.by_name(value)
                return Result()

            @staticmethod
            def free_list(show_with_guest_marks: bool = False) -> Result[list[Mark]]:
                result: Result[list[Mark]] = DataTool.to_result(
                    RPC.call(ServiceCommands.get_free_marks), Mark)

                def filter_function(item: Mark) -> bool:
                    return EnumTool.get(MarkType, item.type) != MarkType.GUEST
                return result if show_with_guest_marks else ResultTool.filter(result, filter_function)

            @staticmethod
            def free_marks_by_group_id(value: int) -> Result[list[Mark]]:
                return DataTool.to_result(RPC.call(ServiceCommands.get_free_marks_by_group_id, value), Mark)

            @staticmethod
            def free_marks_group_statistics(show_guest_marks: bool = None) -> Result[list[MarkGroupStatistics]]:
                return DataTool.to_result(RPC.call(ServiceCommands.get_free_marks_group_statistics, show_guest_marks), MarkGroupStatistics)

            @staticmethod
            def all() -> Result[list[Mark]]:
                return DataTool.to_result(RPC.call(ServiceCommands.get_all_persons), Mark)

            @staticmethod
            def temporary_mark_owner(mark: Mark) -> Result[Mark]:
                return DataTool.check(mark is not None and EnumTool.get(MarkType, mark.type) == MarkType.TEMPORARY, lambda: DataTool.to_result(RPC.call(ServiceCommands.get_owner_mark_for_temporary_mark, mark.TabNumber), Mark), None)

            @staticmethod
            def temporary_mark_owner_by_tab_number(value: str) -> Result[Mark]:
                return PIH.RESULT.MARK.temporary_mark_owner(PIH.RESULT.MARK.by_tab_number(value).data)

        class POLIBASE:

            class NOTIFICATION:

                @staticmethod
                def by(value: PolibasePersonVisitNotification) -> Result[list[PolibasePersonVisitNotification]]:
                    return DataTool.to_result(RPC.call(ServiceCommands.search_polibase_person_visit_notifications, value), PolibasePersonVisitNotification)

                @staticmethod
                def by_message_id(value: int) -> Result[PolibasePersonVisitNotification]:
                    return ResultTool.with_first_element(PIH.RESULT.POLIBASE.NOTIFICATION.by(PolibasePersonVisitNotification(messageID=value)))

                class CONFIRMATION:
                    
                    @staticmethod
                    def by(recipient: str, sender: str) -> Result[PolibasePersonNotificationConfirmation]:
                        return DataTool.to_result(RPC.call(ServiceCommands.search_polibase_person_notification_confirmation, PolibasePersonNotificationConfirmation(recipient, sender)), PolibasePersonNotificationConfirmation)

            class INFORMATION_QUEST:

                @staticmethod
                def get(search_critery: PolibasePersonInformationQuest) -> Result[list[PolibasePersonInformationQuest]]:
                    return DataTool.to_result(
                        RPC.call(ServiceCommands.search_polibase_person_information_quests, search_critery), PolibasePersonInformationQuest)

            class VISIT:

                @staticmethod
                def after_id(value: int, test: bool = None) -> Result[list[PolibasePersonVisitDS]]:
                    return DataTool.to_result(RPC.call(ServiceCommands.search_polibase_person_visits, (PolibasePersonVisitSearchCritery(vis_no=f">{value}"), test)), PolibasePersonVisitDS)

                @staticmethod
                def by_id(value: int, test: bool = None) -> Result[PolibasePersonVisitDS]:
                    return DataTool.to_result(RPC.call(ServiceCommands.search_polibase_person_visits, (PolibasePersonVisitSearchCritery(vis_no=value), test)), PolibasePersonVisitDS, True)

                @staticmethod
                def last_id(test: bool = None) -> Result[int]:
                    return DataTool.to_result(RPC.call(ServiceCommands.get_polibase_person_visits_last_id, test))

                @staticmethod
                def today(test: bool = None) -> Result[list[PolibasePersonVisitDS]]:
                    return PIH.RESULT.POLIBASE.VISIT.by_registration_date(DateTimeTool.today(), test)

                @staticmethod
                def prerecording_today(test: bool = None) -> Result[list[PolibasePersonVisitDS]]:
                    return PIH.RESULT.POLIBASE.VISIT.prerecording_by_registration_date(DateTimeTool.today(), test)

                @staticmethod
                def by_registration_date(value: datetime, test: bool = None) -> Result[list[PolibasePersonVisitDS]]:
                    return DataTool.to_result(RPC.call(ServiceCommands.search_polibase_person_visits, (PolibasePersonVisitSearchCritery(vis_reg_date=DateTimeTool.date_to_string(value, CONST.POLIBASE.DATE_FORMAT)), test)), PolibasePersonVisitDS)

                @staticmethod
                def prerecording_by_registration_date(value: datetime = None, test: bool = None) -> Result[list[PolibasePersonVisitDS]]:
                    def filter_function(value: PolibasePersonVisitDS) -> bool:
                        return value.pin == CONST.POLIBASE.PRERECORDING_PIN
                    return ResultTool.filter(PIH.RESULT.POLIBASE.VISIT.by_registration_date(value, test), filter_function)

                class DATA_STORAGE:

                    @staticmethod
                    def search(value: PolibasePersonVisitDS) -> Result[PolibasePersonVisitDS]:
                        return DataTool.to_result(RPC.call(ServiceCommands.search_polibase_person_visits_in_data_storage, (value, )), PolibasePersonVisitDS, True)

                    @staticmethod
                    def last() -> Result[PolibasePersonVisitDS]:
                        return PIH.RESULT.POLIBASE.VISIT.DATA_STORAGE.search(PolibasePersonVisitDS(id=-1))


            def person_by_telephone_number(value: str, test: bool = None) -> Result[list[PolibasePerson]]:
                value = PIH.DATA.FORMAT.telephone_number_international(value)
                result: Result[PolibasePerson] = DataTool.to_result(RPC.call(
                    ServiceCommands.get_polibase_persons_by_telephone_number, (value, test)), PolibasePerson)
                if ResultTool.is_empty(result):
                    raise PIH.ERROR.POLIBASE.create_not_found_error("идентификационным номером", value)
                return result

            @staticmethod
            def person_by_pin(value: int, test: bool = None) -> Result[PolibasePerson]:
                result: Result[PolibasePerson] = DataTool.to_result(RPC.call(
                    ServiceCommands.get_polibase_person_by_pin, (value, test)), PolibasePerson)
                if ResultTool.is_empty(result):
                    raise PIH.ERROR.POLIBASE.create_not_found_error("идентификационным номером", value)
                return result

            @staticmethod
            def persons_pin_by_visit_date(date: datetime, test: bool = None) -> Result[list[int]]:
                if test:
                    return Result(None, [100310])
                return DataTool.to_result(RPC.call(ServiceCommands.get_polibase_persons_pin_by_visit_date, (date.strftime(CONST.DATE_FORMAT), test)))

            @staticmethod
            def person_creator_by_pin(value: int, test: bool = None) -> Result[PolibasePerson]:
                result: Result[list[PolibasePerson]] = DataTool.to_result(RPC.call(ServiceCommands.get_polibase_person_registrator_by_pin, (value, test)), PolibasePerson)
                if ResultTool.is_empty(result):
                    raise PIH.ERROR.POLIBASE.create_not_found_error(
                        "идентификационным номером", value)
                return result

            @staticmethod
            def persons_by_full_name(value: str, test: bool = None) -> Result[list[PolibasePerson]]:
                result: Result[list[PolibasePerson]] = DataTool.to_result(RPC.call(ServiceCommands.get_polibase_persons_by_full_name, (value, test)), PolibasePerson)
                if ResultTool.is_empty(result):
                    raise PIH.ERROR.POLIBASE.create_not_found_error("именем", value)
                return result

            @staticmethod
            def persons_by_pin(value: list[int], test: bool = None) -> Result[list[PolibasePerson]]:
                result: Result[list[PolibasePerson]] = DataTool.to_result(RPC.call(ServiceCommands.get_polibase_persons_by_pin, (value, test)), PolibasePerson)
                if ResultTool.is_empty(result):
                    raise PIH.ERROR.POLIBASE.create_not_found_error("идентификационным номером", value)
                return result

            @staticmethod
            def persons_by_card_registry_folder_name(value: str, test: bool = None) -> Result[list[PolibasePerson]]:
                return DataTool.to_result(RPC.call(ServiceCommands.get_polibase_persons_by_card_registry_folder_name, (value, test)), PolibasePerson)

            @staticmethod
            def person_pin_list_with_old_format_barcode(test: bool = None) -> Result[list[int]]:
                return DataTool.to_result(RPC.call(ServiceCommands.get_polibase_person_pin_list_with_old_format_barcode, (test, )))

            @staticmethod
            def persons_by_any(value: str, test: bool = None) -> Result[list[PolibasePerson]]:
                if PIH.CHECK.telephone_number(value) or PIH.CHECK.telephone_number_international(value):
                    return ResultTool.as_list(PIH.RESULT.POLIBASE.person_by_telephone_number(value, test))
                if PIH.CHECK.POLIBASE.person_pin(value):
                    return ResultTool.as_list(PIH.RESULT.POLIBASE.person_by_pin(int(value), test))
                if PIH.CHECK.POLIBASE.person_card_registry_folder_name(value):
                    return PIH.RESULT.POLIBASE.persons_by_card_registry_folder_name(value, test)
                return ResultTool.as_list(PIH.RESULT.POLIBASE.persons_by_full_name(value))

        class USER:

            @staticmethod
            def by_login(value: str, active: bool = None, cached: bool = None) -> Result[User]:
                result: Result[User] = DataTool.to_result(RPC.call(ServiceCommands.get_user_by_login, (value, active, PIH.SETTINGS.USER.use_cache() if cached is None else cached)), User)
                if ResultTool.is_empty(result):
                    raise PIH.ERROR.USER.get_not_found_error("логином", active, value)
                return result

            @staticmethod
            def by_telephone_number(value: str, active: bool = None) -> Result[User]:
                result: Result[User] = DataTool.to_result(
                    RPC.call(ServiceCommands.get_user_by_telephone_number, (value, active)), User, True)
                if ResultTool.is_empty(result):
                    raise PIH.ERROR.USER.get_not_found_error("номером телефона", active, value)
                return result

            @staticmethod
            def by_internal_telephone_number(value: int) -> Result[User]:
                workstation_list: list[Workstation] = PIH.RESULT.WORKSTATION.all().data
                result_worksation: Workstation = None
                for workstation in workstation_list:
                    if not DataTool.is_empty(workstation.description):
                        index: int = workstation.description.find(CONST.INTERNAL_TELEPHONE_NUMBER_PREFIX)
                        if index != -1:
                            internal_telephone_number_text: str = workstation.description[index:]
                            internal_telephone_number: int = PIH.DATA.EXTRACT.decimal(internal_telephone_number_text)
                            if internal_telephone_number == value:
                                result_worksation = workstation
                                break
                if result_worksation is not None and result_worksation.accessable and not DataTool.is_empty(result_worksation.samAccountName):
                    return PIH.RESULT.USER.by_login(workstation.samAccountName)
                else:
                    raise PIH.ERROR.USER.get_not_found_error(
                        "внутренним номером телефона", True, str(value))

            @staticmethod
            def by_polibase_pin(value: int) -> Result[User]:
                return PIH.RESULT.USER.by_name(PIH.RESULT.POLIBASE.person_by_pin(value).data.FullName)

            @staticmethod
            def by_workstation_name(name: str) -> Result[User]:
                name = name.lower()
                user_workstation: Workstation = DataTool.to_result(RPC.call(
                    ServiceCommands.get_user_by_workstation, name), Workstation, True).data
                if user_workstation is None:
                    details: str = f"Компьютер с именем '{name}' не найден!"
                    raise NotFound(details)
                if user_workstation.samAccountName is None:
                    raise NotFound(f"За компьютером {name} нет залогиненного пользователя", name)
                return PIH.RESULT.USER.by_login(user_workstation.samAccountName)

            @staticmethod
            def by_any(value: Any, active: bool = None) -> Result[list[User]]:
                def by_number(value: int) -> Result[list[User]]:
                    try:
                        return ResultTool.as_list(PIH.RESULT.USER.by_tab_number(value))
                    except NotFound:
                        try:
                            return ResultTool.as_list(PIH.RESULT.USER.by_login(PIH.RESULT.WORKSTATION.by_internal_telephone_number(value).data.samAccountName))
                        except:
                            return ResultTool.as_list(PIH.RESULT.USER.by_polibase_pin(value))
                if isinstance(value, Mark):
                    return PIH.RESULT.USER.by_name(value.FullName)
                elif isinstance(value, FullName):
                    return PIH.RESULT.USER.by_full_name(value, False, active)
                elif isinstance(value, (WorkstationDescription, Workstation)):
                    return PIH.RESULT.USER.by_any(value.name, active)
                elif isinstance(value, str):
                    if value.lower().startswith(CONST.GROUP_PREFIX):
                        value = str(value[len(CONST.GROUP_PREFIX):])
                        return PIH.RESULT.USER.by_group_name(value)
                    try:
                        value_as_telephone_number: str = PIH.DATA.FORMAT.telephone_number(value)
                        if PIH.CHECK.telephone_number(value_as_telephone_number):
                            return ResultTool.as_list(PIH.RESULT.USER.by_telephone_number(value_as_telephone_number, active))
                    except Exception:
                        pass
                    if PIH.DATA.CHECK.decimal(value):
                       return by_number(value)
                    if PIH.CHECK.WORKSTATION.name(value):
                        return ResultTool.as_list(PIH.RESULT.USER.by_workstation_name(value))
                    if PIH.CHECK.login(value):
                        return ResultTool.as_list(PIH.RESULT.USER.by_login(value, active))
                    if value == "" or PIH.CHECK.name(value):
                        return PIH.RESULT.USER.by_name(value, active)
                elif isinstance(value, int):
                    return by_number(value)
                raise PIH.ERROR.USER.get_not_found_error("поисковым значением", active, value)

            @staticmethod
            def by_job_position(value: AD.JobPisitions) -> Result[list[User]]:
                return DataTool.to_result(RPC.call(ServiceCommands.get_users_by_job_position, value.name), User)

            @staticmethod
            def by_group(value: AD.Groups) -> Result[list[User]]:
                return PIH.RESULT.USER.by_group_name(value.name)

            @staticmethod
            def by_group_name(value: str) -> Result[list[User]]:
                return DataTool.to_result(RPC.call(ServiceCommands.get_users_by_group, value), User)


            @staticmethod
            def template_list() -> Result[list[User]]:
                return DataTool.to_result(RPC.call(ServiceCommands.get_template_users), User)

            @staticmethod
            def containers() -> Result[list[UserContainer]]:
                return DataTool.to_result(RPC.call(
                    ServiceCommands.get_containers), UserContainer)

            @staticmethod
            def by_full_name(value: FullName, get_first: bool = False, active: bool = None) -> Result[list[User]]:
                return DataTool.to_result(RPC.call(ServiceCommands.get_user_by_full_name, (value, active)), User, get_first)

            @staticmethod
            def by_name(value: str, active: bool = None) -> Result[list[User]]:
                result: Result[list[User]] = DataTool.to_result(
                    RPC.call(ServiceCommands.get_users_by_name, (value, active)), User)
                if ResultTool.is_empty(result):
                    raise PIH.ERROR.USER.get_not_found_error("именем", active, value)
                return result

            @staticmethod
            def all(active: bool = None) -> Result[list[User]]:
                return PIH.RESULT.USER.by_name(AD.SEARCH_ALL_PATTERN, active)

            @staticmethod
            def list_with_telephone_number(active: bool = None) -> Result[list[User]]:
                def user_with_telephone_number(user: User) -> bool:
                    return PIH.CHECK.telephone_number(user.telephoneNumber)
                return ResultTool.filter(PIH.RESULT.USER.all(active), lambda user: user_with_telephone_number(user))

            @staticmethod
            def by_tab_number(value: str) -> Result[User]:
                result: Result[Mark] = PIH.RESULT.MARK.by_tab_number(value)
                if ResultTool.is_empty(result):
                    details: str = f"Карта доступа с номером {value} не найдена"
                    raise NotFound(details)
                return PIH.RESULT.USER.by_mark(result.data)

            @staticmethod
            def by_mark(value: Mark) -> Result[User]:
                return Result(FIELD_COLLECTION.AD.USER, DataTool.check(value, lambda: DataTool.get_first_item(PIH.RESULT.USER.by_full_name(FullNameTool.from_string(value.FullName)).data)))

    class CHECK:

        class SETTINGS:
    
            @staticmethod
            def by_time(current: datetime, settings: SETTINGS) -> bool:
                return DateTimeTool.is_equal_by_time(current, PIH.SETTINGS.to_datetime(settings))

        class INDICATION:

            @staticmethod
            def ct_notification_start_time(current: datetime) -> bool:
                start_time_list: list[datetime] = PIH.SETTINGS.INDICATION.ct_notification_start_time()
                for start_time in start_time_list:
                    if DateTimeTool.is_equal_by_time(current, start_time):
                        return True
                return False

        class RESOURCE:
        
            @staticmethod
            def accessibility_by_ping(address_or_ip: str, host: str = None, count: int = None, check_for_all: bool = True) -> bool:
                count = count or 4
                local_ping_commnad_list: list[str] = [PIH.PSTOOLS.get_executor_path(
                    CONST.PSTOOLS.PS_PING), CONST.PSTOOLS.ACCEPTEULA, "-4", "-n", str(count), address_or_ip]
                pocess_result: CompletedProcess = A.PS.execute_command_list(local_ping_commnad_list if host is None else A.PS.create_command_list_for_psexec_command(local_ping_commnad_list, host, interactive=True), True, True)
                if pocess_result.returncode == 0:
                    out: str = pocess_result.stdout
                    lost_marker: str = "Lost = "
                    index: int = out.find(lost_marker)
                    if index != -1:
                        lost_count: int = int(out[index +
                                                len(lost_marker): out.find(" (", index)])
                        if check_for_all:
                            return lost_count == 0
                        return lost_count < count
                return False

            @staticmethod
            def accessibility(resource_status_or_address: Any) -> bool:
                resource_status: ResourceStatus = None
                if isinstance(resource_status_or_address, ResourceDescription):
                    resource_status = resource_status_or_address
                else:
                    resource_status = PIH.RESULT.RESOURCES.get_resource_status(
                        resource_status_or_address)
                return None if resource_status is None else resource_status.inaccessibility_counter < resource_status.inaccessibility_check_values[0]
                
            @staticmethod
            def vpn_pacs_accessibility(count: int = 2) -> bool:
                return PIH.PSTOOLS.ping(RESOURCE.DESCRIPTIONS.VPN_PACS_SPB.address, CONST.HOST.WS255.NAME, count)
            
            @staticmethod
            def pacs_accessibility(count: int = 2) -> bool:
                return PIH.CHECK.RESOURCE.accessibility_by_ping(RESOURCE.DESCRIPTIONS.PACS_SPB.address, CONST.HOST.WS255.NAME, count)
           
            @staticmethod
            def wappi_profile_accessibility(value: Any, cached: bool = False) -> bool:
                return PIH.CHECK.RESOURCE.accessibility(PIH.RESULT.RESOURCES.get_resource_status(EnumTool.get_value(value, CONST.MESSAGE.WHATSAPP.WAPPI.PROFILE.DEFAULT.value))) if cached else PIH.CHECK.MESSAGE.WHATSAPP.WAPPI.accessibility(value, False)

            @staticmethod
            def ws_accessibility(name: str) -> bool:
                result: Result[Workstation] = PIH.RESULT.WORKSTATION.by_name(name)
                return not ResultTool.is_empty(result) and result.data.accessable
            
            @staticmethod
            def polibase_accessibility(cached: bool = False) -> bool:
                try:
                    if cached:
                        return PIH.RESULT.RESOURCES.get_resource_status(RESOURCE.DESCRIPTIONS.POLIBASE).accessable
                    result_by_ping: bool = PIH.SERVICE.check_accessibility(ServiceRoles.POLIBASE)    
                    result_by_pin : bool = PIH.CHECK.POLIBASE.person_exists_by_pin(CONST.POLIBASE.PRERECORDING_PIN)
                    print("POLIBASE", result_by_ping, result_by_pin)
                    return result_by_ping and result_by_pin
                except NotFound:
                    print("POLIBASE BY PIN")
                    pass
                return False

        class EMAIL:

            @staticmethod
            def accessability(value: str) -> bool:
                return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.check_email_accessibility, value))

        class FILE:

            @staticmethod
            def excel_file(path: str) -> bool:
                return os.path.isfile(path) and PathTool.get_extension(path) in [FILE.EXTENSION.EXCEL_OLD, FILE.EXTENSION.EXCEL_NEW]

        class ACCESS:

            @staticmethod
            def by_group(group: AD.Groups, exit_on_access_denied: bool = False, session: SessionBase = None, notify_on_fail: bool = True, notify_on_success: bool = True) -> bool:
                session = session or PIH.session
                user: User = session.get_user()
                result: bool = False
                notify: bool = notify_on_success or notify_on_fail
                if group in session.allowed_groups:
                    result = True
                    notify = False
                else:
                    result = PIH.CHECK.USER.by_group(user, group)
                    if result:
                        session.add_allowed_group(group)
                if notify:
                    PIH.LOG.it(
                        f"Запрос на доступа к группе: {group.name} от пользователя {user.name} ({user.samAccountName}). Доступ {'разрешен' if result else 'отклонен'}.", LogLevels.NORMAL if result else LogLevels.ERROR)
                if not result and exit_on_access_denied:
                    session.exit(5, "Функционал недоступен...")
                return result

            @staticmethod
            def admin(exit_on_access_denied: bool = False, session: SessionBase = None, notify_on_fail: bool = True, notify_on_success: bool = True) -> bool:
                return PIH.CHECK.ACCESS.by_group(AD.Groups.Admin, exit_on_access_denied, session, notify_on_fail, notify_on_success)

            @staticmethod
            def service_admin(session: SessionBase = None, notify_on_fail: bool = True, notify_on_success: bool = True) -> bool:
                return PIH.CHECK.ACCESS.by_group(AD.Groups.ServiceAdmin, False, session, notify_on_fail, notify_on_success)

            @staticmethod
            def inventory(session: SessionBase = None, notify_on_fail: bool = True, notify_on_success: bool = True) -> bool:
                return PIH.CHECK.ACCESS.by_group(AD.Groups.Inventory, False, session, notify_on_fail, notify_on_success)

            @staticmethod
            def polibase(session: SessionBase = None, notify_on_fail: bool = True, notify_on_success: bool = True) -> bool:
                return PIH.CHECK.ACCESS.by_group(AD.Groups.Polibase, False, session, notify_on_fail, notify_on_success)

            @staticmethod
            def card_registry(session: SessionBase = None, notify_on_fail: bool = True, notify_on_success: bool = True) -> bool:
                return PIH.CHECK.ACCESS.by_group(AD.Groups.CardRegistry, False, session, notify_on_fail, notify_on_success)

        class USER:

            @staticmethod
            def by_group(user: User, group: AD.Groups) -> bool:
                return not DataTool.is_empty(ResultTool.do_while(PIH.RESULT.USER.by_group(group), lambda check_user: check_user.samAccountName == user.samAccountName))

            @staticmethod
            def exists_by_login(value: str) -> bool:
                return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.check_user_exists_by_login, value))

            @staticmethod
            def user(user: User) -> bool:
                return PIH.CHECK.full_name(user.name)

            @staticmethod
            def active(user: User) -> bool:
                return user.distinguishedName.find(AD.ACTIVE_USERS_CONTAINER_DN) != -1

            @staticmethod
            def exists_by_full_name(full_name: FullName) -> bool:
                return not ResultTool.is_empty(PIH.RESULT.USER.by_full_name(full_name))

            @staticmethod
            def search_attribute(value: str) -> bool:
                return value in AD.SEARCH_ATTRIBUTES

            @staticmethod
            def property(value: str | None, default_value: str = USER_PROPERTY.PASSWORD) -> str:
                return value or default_value

            @staticmethod
            def accessibility() -> bool:
                return PIH.SERVICE.check_accessibility(ServiceRoles.AD)

        class MESSAGE:

            class WHATSAPP:

                class WAPPI:

                    @staticmethod
                    def from_me(value: str) -> bool:
                        value = PIH.DATA.FORMAT.telephone_number(value)
                        return value in [PIH.DATA.TELEPHONE_NUMBER.it_administrator(), PIH.DATA.TELEPHONE_NUMBER.call_centre_administrator(), PIH.DATA.TELEPHONE_NUMBER.marketer()]

                    @staticmethod
                    def accessibility(profile: Any, cached: bool = True) -> bool:
                        def internal_accessibility(profile: Any = None) -> bool:
                            profile = EnumTool.get_value(profile, CONST.MESSAGE.WHATSAPP.WAPPI.PROFILE.DEFAULT.value)
                            url: str = f"{CONST.MESSAGE.WHATSAPP.WAPPI.URL_GET_STATUS}{profile}"
                            headers: dict = {
                                "Authorization": CONST.MESSAGE.WHATSAPP.WAPPI.AUTHORIZATION,
                                "Content-Type": "application/json"
                            }
                            response_result: dict = None
                            try:
                                response: Response = requests.get(url, headers=headers)
                                response_result = json.loads(response.text)
                            except Exception:
                                return False
                            if "status" in response_result:
                                if response_result["status"] == "error":
                                    return False
                            return response_result["app_status"] == "open"
                        return PIH.CHECK.RESOURCE.wappi_profile_accessibility(profile, True) if cached else internal_accessibility(profile)

        class MARK:

            @staticmethod
            def free(tab_number: str) -> bool:
                return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.check_mark_free, tab_number))

            @staticmethod
            def exists_by_full_name(full_name: FullName) -> bool:
                result: Result[list[Mark]] = PIH.RESULT.MARK.by_name(
                    FullNameTool.to_string(full_name))
                return ResultTool.is_empty(result)

            @staticmethod
            def accessibility() -> bool:
                return PIH.SERVICE.check_accessibility(ServiceRoles.MARK)

            @staticmethod
            def tab_number(value: str) -> bool:
                return value.isdecimal()

        class TIME_TRACKING:

            @staticmethod
            def accessibility() -> bool:
                return PIH.CHECK.ACCESS.by_group(AD.Groups.TimeTrackingReport)

        class INVENTORY:

            @staticmethod
            def is_report_file(file_path: str) -> bool:
                return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.check_inventory_report, file_path))

            @staticmethod
            def accessibility() -> bool:
                return PIH.SERVICE.check_accessibility(ServiceRoles.DOCS) and PIH.CHECK.ACCESS.inventory()

        class POLIBASE:

            @staticmethod
            def accessibility() -> bool:
                return PIH.SERVICE.check_accessibility(ServiceRoles.POLIBASE) and PIH.CHECK.ACCESS.polibase()

            @staticmethod
            def person_card_registry_folder_name(value: str) -> bool:
                return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.check_polibase_person_card_registry_folder_name, value))

            @staticmethod
            def person_exists_by_pin(pin: int) -> bool:
                try:
                    return not ResultTool.is_empty(PIH.RESULT.POLIBASE.person_by_pin(pin))
                except NotFound:
                    return False

            @staticmethod
            def person_pin(value: str) -> bool:
                return value.isnumeric()

            class NOTIFICATION:

                @staticmethod
                def exists(value: PolibasePersonVisitNotification) -> bool:
                    return not ResultTool.is_empty(PIH.RESULT.POLIBASE.NOTIFICATION.by(value))

                class CONFIRMATION:

                    @staticmethod
                    def exists(recipient: str, sender: str, state: int = None) -> bool:
                        result: Result[PolibasePersonNotificationConfirmation] = PIH.RESULT.POLIBASE.NOTIFICATION.CONFIRMATION.by(
                            recipient, sender)
                        return not ResultTool.is_empty(result) and (True if state is None else result.data.status == state)
            
            class DATABASE:

                def creation_start_time(value: datetime) -> bool:
                    return DateTimeTool.is_equal_by_time(value, PIH.SETTINGS.to_datetime(SETTINGS.POLIBASE_CREATION_DB_DUMP_START_TIME))

        @staticmethod
        def login(value: str) -> bool:
            pattern: str = r"^[a-z]+[a-z_0-9]{"+str(CONST.NAME_POLICY.PART_ITEM_MIN_LENGTH - 1) + ",}"
            return re.fullmatch(pattern, value, re.IGNORECASE) is not None

        class WORKSTATION:

            @staticmethod
            def name(value: str) -> bool:
                value = PIH.DATA.FORMAT.string(value)
                for prefix in AD.WORKSTATION_PREFIX_LIST:
                    if value.startswith(prefix):
                        return True
                return False

            @staticmethod
            def exists(name: str) -> bool:
                return not ResultTool.is_empty(ResultTool.filter(PIH.RESULT.WORKSTATION.all_description(), lambda workstation: name.lower() == workstation.name.lower()))

            @staticmethod
            def has_property(workstation: WorkstationDescription, property: AD.WSProperies) -> bool:
                return BM.has(workstation.properties, property)

            @staticmethod
            def watchable(workstation: WorkstationDescription) -> bool:
                return PIH.CHECK.WORKSTATION.has_property(workstation, AD.WSProperies.Watchable)

            @staticmethod
            def shutdownable(workstation: WorkstationDescription) -> bool:
                return PIH.CHECK.WORKSTATION.has_property(workstation, AD.WSProperies.Shutdownable)

            @staticmethod
            def rebootable(workstation: WorkstationDescription) -> bool:
                return PIH.CHECK.WORKSTATION.has_property(workstation, AD.WSProperies.Rebootable)

        @staticmethod
        def telephone_number(value: str, international: bool = False) -> bool:
            return not DataTool.is_empty(value) and re.fullmatch(("" if international else r"^\+") + "[0-9]{11,13}$", value) is not None

        @staticmethod
        def telephone_number_international(value: str) -> bool:
            return PIH.CHECK.telephone_number(value, True)

        @staticmethod
        def email(value: str, check_accesability: bool = False) -> bool:
            return re.fullmatch(r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+", value) is not None and (not check_accesability or PIH.CHECK.EMAIL.accessability(value))

        @staticmethod
        def name(value: str, use_space: bool = False) -> bool:
            pattern = r"[а-яА-ЯёЁ" + (" " if use_space else "") + \
                "]{" + str(CONST.NAME_POLICY.PART_ITEM_MIN_LENGTH) + ",}$"
            return re.fullmatch(pattern, value) is not None

        @staticmethod
        def full_name(value: str) -> bool:
            pattern = r"[а-яА-ЯёЁ]{" + str(CONST.NAME_POLICY.PART_ITEM_MIN_LENGTH) + ",} [а-яА-ЯёЁ]{" + str(
                CONST.NAME_POLICY.PART_ITEM_MIN_LENGTH) + ",} [а-яА-ЯёЁ]{" + str(CONST.NAME_POLICY.PART_ITEM_MIN_LENGTH) + ",}$"
            return re.fullmatch(pattern, value) is not None

        @staticmethod
        def password(value: str, settings: PasswordSettings = None) -> bool:
            settings = settings or PASSWORD.SETTINGS.DEFAULT
            return PasswordTools.check_password(value, settings.length, settings.special_characters)


    class LOG:

        executor = ThreadPoolExecutor(max_workers=1)

        @staticmethod
        def send_message(value: str, channel: LogChannels = LogChannels.DEFAULT, level: Any = LogLevels.DEFAULT) -> str:
            level_value: int = None
            level_list: list[LogLevels] = None
            if isinstance(level, LogLevels):
                level_list = [level]
            if isinstance(level, int):
                level_value = level
            if level_value is None:
                level_value = 0
                for level_item in level_list:
                    level_value = level_value | level_item.value

            def internal_send_message(message: str, channel_name: str, level_value: int) -> None:
                try:
                    RPC.call(ServiceCommands.send_log_message,
                            (message, channel_name, level_value))
                except Error as error:
                    PIH.output.error("Log send error")
            PIH.LOG.executor.submit(internal_send_message, value,
                                        channel.name, level_value)
            return value

        @staticmethod
        def send_command(value: LogCommands, parameters: Tuple = None) -> None:
            message_commnad_description: LogCommandDescription = value.value
            parameter_pattern_list: list = DataTool.as_list(
                message_commnad_description.params)
            parameters = parameters or ()
            parameters_dict: dict = {}
            if len(parameter_pattern_list) > len(parameters):
                raise Exception(
                    "Income parameter list length is less that parameter list length of command")
            for index, parameter_pattern_item in enumerate(parameter_pattern_list):
                parameter_pattern: ParamItem = parameter_pattern_item
                parameters_dict[parameter_pattern.name] = parameters[index]

            def internal_send_command(command_name: str, parameters: dict) -> None:
                try:
                    RPC.call(ServiceCommands.send_log_command,
                            (command_name, parameters))
                except Error as error:
                    PIH.output.error("Log send error")
            PIH.LOG.executor.submit(internal_send_command,
                                        value.name, parameters_dict)

        class COMMAND:

            @staticmethod
            def send(value: LogCommands, parameters: Tuple = None) -> None:
                PIH.LOG.send_command(value, parameters)


            @staticmethod
            def computer_was_started(name: str) -> None:
                PIH.LOG.send_command(
                    LogCommands.COMPUTER_WAS_STARTED, (name,))
                
            @staticmethod
            def server_was_started(name: str) -> None:
                PIH.LOG.send_command(
                    LogCommands.SERVER_WAS_STARTED, (name,))
    
            @staticmethod
            def polibase_persons_with_old_format_barcode_was_detected(persons_pin: list[int]) -> None:
                PIH.LOG.send_command(
                    LogCommands.POLIBASE_PERSONS_WITH_OLD_FORMAT_BARCODE_WAS_DETECTED, (len(persons_pin), persons_pin))

            @staticmethod
            def all_polibase_persons_barcode_with_old_format_was_created(persons_pin: list[int]) -> None:
                PIH.LOG.send_command(
                    LogCommands.POLIBASE_ALL_PERSON_BARCODES_WITH_OLD_FORMAT_WAS_CREATED, (persons_pin,))

            @staticmethod
            def polibase_person_visit_was_registered(value: PolibasePersonVisitDS) -> None:
                PIH.LOG.send_command(LogCommands.POLIBASE_PERSON_VISIT_WAS_REGISTERED, (
                    value.FullName, "Предзапись" if value.pin == CONST.POLIBASE.PRERECORDING_PIN else value.pin, value))
                
            @staticmethod
            def resource_accessible(resource: ResourceStatus, at_first_time: bool) -> None:
                PIH.LOG.send_command(LogCommands.RESOURCE_ACCESSABLE, (resource.name, resource, at_first_time))

            @staticmethod
            def resource_inaccessible(resource: ResourceStatus, at_first_time: bool, reason: RESOURCE.INACCESSABLE_REASON | None = None) -> None:
                reason_string: str = ""
                reason_name: str | None = None
                if not DataTool.is_empty(reason):
                    reason_string = f"Причина: {reason.value}"
                    reason_name =  reason.name
                PIH.LOG.send_command(LogCommands.RESOURCE_INACCESSABLE, (resource.name, resource, at_first_time, reason_string, reason_name))

            @staticmethod
            def polibase_person_visit_notification_was_registered(visit: PolibasePersonVisitDS, notification: PolibasePersonVisitNotificationDS) -> None:
                PIH.LOG.send_command(LogCommands.POLIBASE_PERSON_VISIT_NOTIFICATION_WAS_REGISTERED, (
                    visit.FullName, "Предзапись" if visit.pin == CONST.POLIBASE.PRERECORDING_PIN else visit.pin, notification))

            @staticmethod
            def login() -> None:
                login: str = PIH.session.get_login()
                user: User = PIH.RESULT.USER.by_login(login).data
                PIH.LOG.send_command(
                    LogCommands.LOG_IN, (user.name, login, PIH.OS.host()))

            @staticmethod
            def whatsapp_message_received(message: WhatsAppMessage) -> None:
                PIH.LOG.send_command(
                    LogCommands.WHATSAPP_MESSAGE_RECEIVED, (message,))

            @staticmethod
            def new_file_detected(path: str) -> None:
                PIH.LOG.send_command(
                    LogCommands.NEW_FILE_DETECTED, (path,))
                
            @staticmethod
            def new_polibase_scanned_document_detected(value: PolibaseScannedDocument):
                PIH.LOG.send_command(LogCommands.NEW_POLIBASE_DOCUMENT_DETECTED, (value.file_path, value.pin, value.document_name))

            @staticmethod
            def start_session() -> None:
                argv: list[str] = PIH.session.argv
                argv_str: str = ""
                if not DataTool.is_empty(argv):
                    argv_str = " ".join(argv)
                    argv_str = f"({argv_str})"
                login: str = PIH.session.get_login()
                user: User = PIH.RESULT.USER.by_login(login).data
                PIH.LOG.send_command(LogCommands.SESSION_STARTED, (user.name, login,
                                         f"{PIH.session.file_name} {argv_str}", f"{PIH.VERSION.local()}/{PIH.VERSION.remote()}", PIH.OS.host()))

            @staticmethod
            def backup_notify_about_robocopy_job_started(status: str) -> None:
                PIH.LOG.send_command(
                    LogCommands.BACKUP_NOTIFY_ABOUT_ROBOCOPY_JOB_STARTED, (status, ))

            @staticmethod
            def backup_notify_about_robocopy_job_completed(status: str) -> None:
                PIH.LOG.send_command(
                    LogCommands.BACKUP_NOTIFY_ABOUT_ROBOCOPY_JOB_COMPLETED, (status, ))

            @staticmethod
            def service_action(service_role_description: ServiceRoleDescription, log_command: LogCommands) -> None:
                PIH.LOG.send_command(log_command, (service_role_description.name, service_role_description.description,
                                         service_role_description.host, service_role_description.port, service_role_description.pid))

            @staticmethod
            def service_started(service_role_description: ServiceRoleDescription) -> None:
                PIH.LOG.COMMAND.service_action(service_role_description, LogCommands.SERVICE_STARTED)
            
            @staticmethod
            def service_starts(service_role_description: ServiceRoleDescription) -> None:
                PIH.LOG.COMMAND.service_action(service_role_description, LogCommands.SERVICE_STARTS)

            @staticmethod
            def service_is_inaccessable_and_waiting_to_be_restarted(service_role_description: ServiceRoleDescription) -> None:
                PIH.LOG.COMMAND.service_action(service_role_description, LogCommands.SERVICE_IS_INACCESIBLE_AND_WAITING_TO_BE_RESTARTED)

            @staticmethod
            def service_not_started(service_role_description: ServiceRoleDescription, error: str) -> None:
                PIH.LOG.send_command(LogCommands.SERVICE_NOT_STARTED, (service_role_description.name, service_role_description.description,
                                                                       service_role_description.host, service_role_description.port, error))

            @staticmethod
            def hr_notify_about_new_employee(login: User) -> None:
                user: User = PIH.RESULT.USER.by_login(login).data
                hr_user: User = ResultTool.get_first_element(
                    PIH.RESULT.USER.by_job_position(AD.JobPisitions.HR))
                PIH.LOG.send_command(LogCommands.HR_NOTIFY_ABOUT_NEW_EMPLOYEE, (FullNameTool.to_given_name(hr_user.name),
                                                                                        user.name, user.mail))

            @staticmethod
            def it_notify_about_user_creation(login: str, password: str) -> None:
                it_user_list: list[User] = PIH.RESULT.USER.by_job_position(
                    AD.JobPisitions.IT).data
                me_user_login: str = PIH.session.get_login()
                it_user_list = list(
                    filter(lambda user: user.samAccountName != me_user_login, it_user_list))
                it_user: User = it_user_list[0]
                user: User = PIH.RESULT.USER.by_login(login).data
                PIH.LOG.send_command(LogCommands.IT_NOTIFY_ABOUT_CREATE_USER, (
                    user.name, user.description, user.samAccountName, password, user.telephoneNumber, user.mail))
                PIH.LOG.send_command(LogCommands.IT_TASK_AFTER_CREATE_NEW_USER, (FullNameTool.to_given_name(
                    it_user.name), user.name, user.mail, password))

            @staticmethod
            def it_notify_about_mark_creation(temporary: bool, full_name: Any, tab_number: str = None) -> None:
                name: str = FullNameTool.to_string(full_name) if isinstance(
                    full_name, FullName) else full_name
                mark: Mark = PIH.RESULT.MARK.by_name(name, True).data
                telephone_number: str = PIH.DATA.FORMAT.telephone_number(
                    mark.telephoneNumber)
                if temporary:
                    PIH.LOG.send_command(LogCommands.IT_NOTIFY_ABOUT_CREATE_TEMPORARY_MARK,
                                             (name, tab_number, telephone_number))
                else:
                    PIH.LOG.send_command(LogCommands.IT_NOTIFY_ABOUT_CREATE_NEW_MARK, (
                        name, telephone_number, mark.TabNumber, mark.GroupName))

            @staticmethod
            def it_notify_about_temporary_mark_return(mark: Mark, temporary_tab_number: int) -> None:
                PIH.LOG.send_command(
                    LogCommands.IT_NOTIFY_ABOUT_TEMPORARY_MARK_RETURN, (mark.FullName, temporary_tab_number))

            @staticmethod
            def backup_notify_about_polibase_creation_db_dumb_start() -> None:
                PIH.LOG.send_command(
                    LogCommands.POLIBASE_CREATION_DB_DUMP_START)
                
            @staticmethod
            def backup_notify_about_polibase_creation_db_dumb_complete() -> None:
                PIH.LOG.send_command(
                    LogCommands.POLIBASE_CREATION_DB_DUMP_COMPLETE)
                
            @staticmethod
            def backup_notify_about_polibase_creation_archived_db_dumb_start() -> None:
                PIH.LOG.send_command(
                    LogCommands.POLIBASE_CREATION_ARCHIVED_DB_DUMP_START)
                
            @staticmethod
            def backup_notify_about_polibase_creation_archived_db_dumb_complete() -> None:
                PIH.LOG.send_command(
                    LogCommands.POLIBASE_CREATION_ARCHIVED_DB_DUMP_COMPLETE)
                
            @staticmethod
            def backup_notify_about_polibase_coping_archived_db_dumb_start(destination: str) -> None:
                PIH.LOG.send_command(
                    LogCommands.POLIBASE_COPING_ARCHIVED_DB_DUMP_START, (destination,))

            @staticmethod
            def backup_notify_about_polibase_coping_archived_db_dumb_complete(destination: str) -> None:
                PIH.LOG.send_command(
                    LogCommands.POLIBASE_COPING_ARCHIVED_DB_DUMP_COMPLETE, (destination,))
                
            @staticmethod
            def backup_notify_about_polibase_coping_db_dumb_start(destination: str) -> None:
                PIH.LOG.send_command(
                    LogCommands.POLIBASE_COPING_DB_DUMP_START, (destination,))

            @staticmethod
            def backup_notify_about_polibase_coping_db_dumb_complete(destination: str) -> None:
                PIH.LOG.send_command(
                    LogCommands.POLIBASE_COPING_DB_DUMP_COMPLETE, (destination,))

            @staticmethod
            def it_notify_about_mark_return(mark: Mark) -> None:
                PIH.LOG.send_command(
                    LogCommands.IT_NOTIFY_ABOUT_MARK_RETURN, (mark.FullName, mark.TabNumber))

            @staticmethod
            def it_notify_about_create_new_mark(full_name: Any) -> None:
                PIH.LOG.COMMAND.it_notify_about_mark_creation(
                    False, full_name)

            @staticmethod
            def it_notify_about_create_temporary_mark(full_name: Any, tab_number: str) -> None:
                PIH.LOG.COMMAND.it_notify_about_mark_creation(
                    True, full_name, tab_number)

            @staticmethod
            def printer_report(name: str, location: str, report: str) -> bool:
                return PIH.LOG.send_command(LogCommands.PRINTER_REPORT, (name, location, report))

        @staticmethod
        def debug_bot(message: str, level: Any = LogLevels.DEFAULT) -> str:
            return PIH.LOG.send_message(message, LogChannels.DEBUG_BOT, level)

        @staticmethod
        def debug(message: str, level: Any = LogLevels.DEFAULT) -> str:
            return PIH.LOG.send_message(message, LogChannels.DEBUG, level)

        @staticmethod
        def services(message: str, level: Any = LogLevels.DEFAULT) -> str:
            return PIH.LOG.send_message(message, LogChannels.SERVICE, level)

        @staticmethod
        def resources(message: str, level: Any = LogLevels.DEFAULT) -> str:
            return PIH.LOG.send_message(message, LogChannels.RESOURCES, level)
        
        @staticmethod
        def printers(message: str, level: Any = LogLevels.DEFAULT) -> str:
            return PIH.LOG.send_message(message, LogChannels.PRINTER, level)

        @staticmethod
        def services_bot(message: str, level: Any = LogLevels.DEFAULT) -> str:
            return PIH.LOG.send_message(message, LogChannels.SERVICE_BOT, level)

        @staticmethod
        def backup(message: str, level: Any = LogLevels.DEFAULT) -> str:
            return PIH.LOG.send_message(message, LogChannels.BACKUP, level)

        @staticmethod
        def notification(message: str, level: Any = LogLevels.DEFAULT) -> str:
            return PIH.LOG.send_message(message, LogChannels.NOTIFICATION, level)

        @staticmethod
        def notification_bot(message: str, level: Any = LogLevels.DEFAULT) -> str:
            return PIH.LOG.send_message(message, LogChannels.NOTIFICATION_BOT, level)

        @staticmethod
        def it(message: str, level: Any = LogLevels.DEFAULT) -> str:
            return PIH.LOG.send_message(message, LogChannels.IT, level)

        @staticmethod
        def from_feedback_call_bot(message: str, level: Any = LogLevels.DEFAULT) -> str:
            return PIH.LOG.send_message(message, LogChannels.POLIBASE_PERSON_FEEDBACK_CALL, level)

        @staticmethod
        def from_review_request_result(message: str, level: Any = LogLevels.DEFAULT) -> str:
            return PIH.LOG.send_message(message, LogChannels.POLIBASE_PERSON_REVIEW_QUEST_RESULT, level)

        @staticmethod
        def it_bot(message: str, level: Any = LogLevels.DEFAULT) -> str:
            return PIH.LOG.send_message(message, LogChannels.IT_BOT, level)


    class MESSAGE:

        class POLIBASE:

            @staticmethod
            def notify(message: str, test: bool = True) -> None:
                PIH.MESSAGE.WORKSTATION.to_all_workstations(message, AD.Groups.PolibaseUsers, [CONST.HOST.WS255.NAME], None, test, 180)

            @staticmethod
            def notify_about_polibase_closing(message: str | None = None, test: bool = True) -> None:
                PIH.MESSAGE.POLIBASE.notify(message or PIH.SETTINGS.get(
                    SETTINGS.POLIBASE_WAS_EMERGENCY_CLOSED_NOTIFICATION_TEXT), test)
                
            @staticmethod
            def notify_about_polibase_restarted(test: bool = True) -> None:
                PIH.MESSAGE.POLIBASE.notify(PIH.SETTINGS.get(
                    SETTINGS.POLIBASE_WAS_RESTARTED_NOTIFICATION_TEXT), test)


        class WORKSTATION:
              
            executor = ThreadPoolExecutor(max_workers=10)

            @staticmethod
            def to_all_workstations(message: str, filter_group: AD.Groups = None, to_all_user_workstation_name_list: list[str] = None, session: Session = None, test: bool = True, timeout: int = 60) -> None:
                session = session or PIH.session
                filter_user_login_list: list[str] = None if filter_group is None else ResultTool.map(PIH.RESULT.USER.by_group(filter_group), lambda item: item.samAccountName.lower()).data
                filter_user_login_list_is_empty: bool = DataTool.is_empty(filter_user_login_list)
                to_all_user_workstation_name_list_is_empty: bool = DataTool.is_empty(
                    to_all_user_workstation_name_list)
                def filter_function(workstation: Workstation) -> bool:
                    workstation_name: str = workstation.name.lower()
                    if test:
                        return workstation_name == CONST.TEST.WS
                    return workstation.accessable and ((filter_user_login_list_is_empty or workstation.samAccountName in filter_user_login_list) or (to_all_user_workstation_name_list_is_empty or workstation_name in to_all_user_workstation_name_list))
                def every_action(workstation: Workstation) -> None:
                    def internal_send_message(user_login: str | None, workstation_name: str, message: str) -> None:
                        if not DataTool.is_empty(to_all_user_workstation_name_list) and workstation_name in to_all_user_workstation_name_list:
                            if not test:
                                PIH.MESSAGE.WORKSTATION.to_user_or_workstation(None, workstation_name, message, timeout)
                        else:
                            if DataTool.is_empty(user_login):
                                if test:
                                    PIH.MESSAGE.WORKSTATION.to_user_or_workstation(user_login, workstation_name, message, timeout)
                                else:
                                    pass
                                #dont send message - cause workstation is on but no one user is logged
                            else:
                                if test:
                                    if workstation_name == CONST.TEST.WS:
                                        PIH.MESSAGE.WORKSTATION.to_user_or_workstation(user_login, workstation_name, message, timeout)
                                else:
                                    PIH.MESSAGE.WORKSTATION.to_user_or_workstation(user_login, workstation_name, message, timeout)
                    result_message: str = f"Сообщение от {session.user_given_name} ({A.D_F.description(session.get_user().description)}):"
                    result_message += f" День добрый, "
                    user_data: dict = {"user" : None}
                    def obtain_user_action() -> User:
                        user: User = None
                        try:
                            user = A.R_U.by_login(workstation.samAccountName).data
                            user_data["user"] = user
                        except NotFound:
                            pass
                        return user
                    if workstation.samAccountName:
                        while_not_do(lambda: obtain_user_action() is not None)
                    user: User | None = user_data["user"]
                    result_message += "" if A.D_C.empty(workstation.samAccountName) else f"{FullNameTool.to_given_name(user)}, "
                    result_message += message
                    PIH.MESSAGE.WORKSTATION.executor.submit(
                        internal_send_message, workstation.samAccountName, workstation.name.lower(), result_message)
                ResultTool.every(ResultTool.filter(PIH.RESULT.WORKSTATION.all(), filter_function), every_action)

            @staticmethod
            def to_user(value: Any, message: str, timeout: int = 60, method_type: WorkstationMessageMethodTypes = WorkstationMessageMethodTypes.REMOTE) -> bool:
                return PIH.MESSAGE.WORKSTATION.to_user_or_workstation(value.samAccountName if isinstance(value, User) else value, None, message, timeout, method_type)

            @staticmethod
            def to_workstation(value: Any, message: str, timeout: int = 60, method_type: WorkstationMessageMethodTypes = WorkstationMessageMethodTypes.REMOTE) -> bool:
                return PIH.MESSAGE.WORKSTATION.by_workstation_name(value.name if isinstance(value, WorkstationDescription) else value, message, timeout, method_type)

            @staticmethod
            def by_workstation_name(value: str, message: str, timeout: int = 60, method_type: WorkstationMessageMethodTypes = WorkstationMessageMethodTypes.REMOTE) -> bool:
                user: User = None
                try:
                    user = PIH.RESULT.USER.by_workstation_name(value).data
                except NotFound:
                    pass
                return PIH.MESSAGE.WORKSTATION.to_user_or_workstation(user.samAccountName if user is not None else None, value, message, timeout, method_type)

            @staticmethod
            def to_user_or_workstation(user_login: str, workstation_name: str, message: str, timeout: int = 60, method_type: WorkstationMessageMethodTypes = WorkstationMessageMethodTypes.REMOTE) -> bool:
                if RPC.Service.role_description is not None and RPC.Service.role_description.name == ServiceRoles.WS.value.name:
                    method_type = WorkstationMessageMethodTypes.LOCAL_PSTOOL_MSG
                if method_type == WorkstationMessageMethodTypes.REMOTE:
                    return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.send_message_to_user_or_workstation, (user_login, workstation_name, message, timeout)))
                def internal_send_by_login_and_workstation_name(login: str, workstation_name: str) -> None:
                    if method_type == WorkstationMessageMethodTypes.LOCAL_PSTOOL_MSG:
                        PIH.PSTOOLS.execute_command_list(PIH.PSTOOLS.create_command_list_for_psexec_command(
                            [CONST.MSG.EXECUTOR, f"/time:{timeout}", login, message], workstation_name), False)
                    if method_type == WorkstationMessageMethodTypes.LOCAL_MSG:
                        PIH.PSTOOLS.execute_command_list(
                            [CONST.MSG.EXECUTOR, f"/time:{timeout}", login, f"/server:{workstation_name}", message], False)
                if workstation_name is None:
                    ResultTool.every(PIH.RESULT.WORKSTATION.by_login(
                        user_login), lambda workstation: internal_send_by_login_and_workstation_name(user_login, workstation.name))
                else:
                    if user_login is None:
                        internal_send_by_login_and_workstation_name(
                            "*", workstation_name)
                    else:
                        internal_send_by_login_and_workstation_name(
                            user_login, workstation_name)
                return True

            @staticmethod
            def by_login(login: str, message: str, timeout: int = 60, method_type: WorkstationMessageMethodTypes = WorkstationMessageMethodTypes.REMOTE) -> bool:
                return PIH.MESSAGE.WORKSTATION.to_user_or_workstation(login, None, message, timeout, method_type)

        class WHATSAPP:

            class WAPPI:

                class QUEUE:
    
                    @staticmethod
                    def add(message: Message, recipient: str, sender: CONST.MESSAGE.WHATSAPP.WAPPI.PROFILE, high_priority: bool = False) -> bool:
                        return PIH.MESSAGE.WHATSAPP.WAPPI.QUEUE.add_message(Message(message, recipient, sender.value), high_priority)
                    
                    @staticmethod
                    def add_message(message: Message, high_priority: bool = False) -> bool:
                        return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.add_message_to_queue, (message, high_priority)))


                WAPPI_PROFILE_MAP: dict = None 

                @staticmethod
                def get_wappi_collection() -> dict:
                    WP = CONST.MESSAGE.WHATSAPP.WAPPI.PROFILE
                    result: dict = PIH.MESSAGE.WHATSAPP.WAPPI.WAPPI_PROFILE_MAP or {
                        WP.IT: PIH.DATA.TELEPHONE_NUMBER.it_administrator(),
                        WP.CALL_CENTRE: PIH.DATA.TELEPHONE_NUMBER.call_centre_administrator(),
                        WP.MARKETER: PIH.DATA.TELEPHONE_NUMBER.marketer()
                    }
                    if PIH.MESSAGE.WHATSAPP.WAPPI.WAPPI_PROFILE_MAP is None:
                        PIH.MESSAGE.WHATSAPP.WAPPI.WAPPI_PROFILE_MAP = result
                    return result


                @staticmethod
                def send_to_group(group: CONST.MESSAGE.WHATSAPP.GROUP, message: str, profile: CONST.MESSAGE.WHATSAPP.WAPPI.PROFILE = CONST.MESSAGE.WHATSAPP.WAPPI.PROFILE.IT) -> bool:
                    return PIH.MESSAGE.WHATSAPP.WAPPI.send(group.value, message, profile)

                @staticmethod
                def get_profile_id(telephone_number: str) -> CONST.MESSAGE.WHATSAPP.WAPPI.PROFILE:
                    if PIH.CHECK.telephone_number_international(telephone_number):
                        telephone_number = PIH.DATA.FORMAT.telephone_number(telephone_number)
                    profile_id_collection = PIH.MESSAGE.WHATSAPP.WAPPI.get_wappi_collection()
                    for item in profile_id_collection:
                        if profile_id_collection[item] == telephone_number:
                            return item
                    return None

                @staticmethod
                def get_message_list(telephone_number: str, profile: Any = None) -> list[WhatsAppMessage]:
                    profile = EnumTool.get_value(profile, CONST.MESSAGE.WHATSAPP.WAPPI.PROFILE.DEFAULT.value)
                    url: str = f"{CONST.MESSAGE.WHATSAPP.WAPPI.URL_GET_MESSAGES}{profile}&chat_id={telephone_number}{CONST.MESSAGE.WHATSAPP.WAPPI.CONTACT_SUFFIX}"
                    headers: dict = {
                        "Authorization": CONST.MESSAGE.WHATSAPP.WAPPI.AUTHORIZATION,
                        "Content-Type": "application/json"
                    }
                    result: list[WhatsAppMessage] = []
                    try:
                        response: Response = requests.get(url, headers=headers)
                    except Exception:
                        return result
                    response_result: dict = json.loads(response.text)
                    has_error: bool = response_result["status"] == "error" or ("detail" in response_result and response_result["detail"] == "Messages not found")
                    if not has_error:
                        for message_item in response_result["messages"]:
                            if message_item["type"] == "chat":
                                result.append(WhatsAppMessage(message_item["body"], message_item["fromMe"], str(message_item["from"]).split("@")[0], 
                                   str(message_item["to"]).split("@")[0], profile, message_item["time"]))
                    return result 
                
                @staticmethod
                def send(telephone_number: str, message: Any, profile: Any = None) -> bool:
                    #print(message)
                    profile = EnumTool.get_value(profile, CONST.MESSAGE.WHATSAPP.WAPPI.PROFILE.DEFAULT.value)
                    url: str = None
                    payload: dict = {"recipient": telephone_number}
                    if isinstance(message, str):
                        payload["body"] = message
                        url: str = CONST.MESSAGE.WHATSAPP.WAPPI.URL_SEND_MESSAGE
                    elif isinstance(message, (WhatsAppMessageListPayload, WhatsAppMessageButtonsPayload)):
                        for item in message.__dataclass_fields__:
                            item_value: Any = message.__getattribute__(item)
                            if not DataTool.is_empty(item_value):
                                payload[item] = item_value
                        if isinstance(message, WhatsAppMessageListPayload):
                            url = CONST.MESSAGE.WHATSAPP.WAPPI.URL_SEND_LIST_MESSAGE
                        else:
                            url = CONST.MESSAGE.WHATSAPP.WAPPI.URL_SEND_BUTTONS_MESSAGE
                    url += profile
                    headers: dict = {"accept": "application/json",
                                     "Authorization": CONST.MESSAGE.WHATSAPP.WAPPI.AUTHORIZATION, "Content-Type": "application/json"}
                    try:
                        response: Response = requests.post(
                            url, data=json.dumps(payload), headers=headers)
                    except ConnectTimeout:
                        #print("ConnectTimeout")
                        return False
                    if response.status_code == CONST.ERROR.WAPPI.PROFILE_NOT_PAID:
                        PIH.LOG.resources(
                            "Аккаунт Wappi (сервис для отправики сообщений в WhatsApp) не оплачен", LogLevels.ERROR)
                    status_code: int = response.status_code
                    #print(status_code)
                    return status_code == 200

                @staticmethod
                def send_base64_file(url: str, telephone_number: str, caption: str, base64_content: str,  profile: Any = None) -> bool:
                    profile = EnumTool.get_value(
                        profile, CONST.MESSAGE.WHATSAPP.WAPPI.PROFILE.DEFAULT.value)
                    payload: dict = {"recipient": telephone_number,
                                     "caption": caption,
                                     "b64_file": base64_content}
                    headers: dict = {"accept": "application/json",
                                     "Authorization": CONST.MESSAGE.WHATSAPP.WAPPI.AUTHORIZATION, "Content-Type": "application/json"}
                    url = url + profile
                    try:
                        response: Response = requests.post(
                            url, data=json.dumps(payload), headers=headers)
                    except ConnectTimeout:
                        return False
                    if response.status_code == CONST.ERROR.WAPPI.PROFILE_NOT_PAID:
                        PIH.LOG.resources(
                            "Аккаунт Wappi (сервис для отправики сообщений в WhatsApp) не оплачен", LogLevels.ERROR)
                    return response.status_code == 200

                @staticmethod
                def send_video(telephone_number: str, caption: str, base64_content: str, profile: Any = None) -> bool:
                    return PIH.MESSAGE.WHATSAPP.WAPPI.send_base64_file(CONST.MESSAGE.WHATSAPP.WAPPI.URL_SEND_VIDEO, telephone_number, caption, base64_content, profile)

                @staticmethod
                def send_image(telephone_number: str, caption: str, base64_content: str, profile: Any = None) -> bool:
                    return PIH.MESSAGE.WHATSAPP.WAPPI.send_base64_file(CONST.MESSAGE.WHATSAPP.WAPPI.URL_SEND_IMAGE, telephone_number, caption, base64_content, profile)

                @staticmethod
                def send_document(telephone_number: str, caption: str, base64_content: str, profile: Any = None) -> bool:
                    return PIH.MESSAGE.WHATSAPP.WAPPI.send_base64_file(CONST.MESSAGE.WHATSAPP.WAPPI.URL_SEND_DOCUMENT, telephone_number, caption, base64_content, profile)

            @staticmethod
            def create_output(recipient: str) -> Output:
                from MobileHelperCore.api import WappiOutput, WappiSession
                return WappiOutput(WappiSession(recipient))
            
            @staticmethod
            def send_via_browser(telephone_number: str, message: str) -> bool:
                pywhatkit_is_exists: bool = importlib.util.find_spec(
                    "pywhatkit") is not None
                if not pywhatkit_is_exists:
                    PIH.output.green(
                        "Установка библиотеки для отправки сообщения. Ожидайте...")
                    if not PIH.UPDATER.install_module("pywhatkit"):
                        PIH.output.error(
                            "Ошибка при установке библиотеки для отправки сообщений!")
                try:
                    import pywhatkit as pwk
                    pwk.sendwhatmsg_instantly(telephone_number, message)
                except Exception as уrror:
                    PIH.output.error("Ошибка при отправке сообщения!")

            @staticmethod
            def send(telephone_number: str, message: Any, via_wappi: bool = True, use_alternative: bool = True, wappi_profile: Any = None) -> bool:
                wappi_profile = EnumTool.get_value(
                    wappi_profile, CONST.MESSAGE.WHATSAPP.WAPPI.PROFILE.DEFAULT.value)
                result: bool = False
                telephone_number = PIH.DATA.FORMAT.telephone_number(
                    telephone_number)
                if via_wappi:
                    result = PIH.MESSAGE.WHATSAPP.WAPPI.send(
                        telephone_number, message, wappi_profile)
                if result:
                    return result
                if use_alternative or not via_wappi:
                    return PIH.MESSAGE.WHATSAPP.send_via_browser(telephone_number, message)
                return False

            @staticmethod
            def send_video(telephone_number: str, caption: str, base64_value: str, wappi_profile: Any = None) -> bool:
                wappi_profile = EnumTool.get_value(
                    wappi_profile, CONST.MESSAGE.WHATSAPP.WAPPI.PROFILE.DEFAULT.value)
                telephone_number = PIH.DATA.FORMAT.telephone_number(telephone_number)
                return PIH.MESSAGE.WHATSAPP.WAPPI.send_video(telephone_number, caption, base64_value, wappi_profile)

            @staticmethod
            def send_image(telephone_number: str, caption: str, base64_value: str, wappi_profile: Any = None) -> bool:
                wappi_profile = EnumTool.get_value(
                    wappi_profile, CONST.MESSAGE.WHATSAPP.WAPPI.PROFILE.DEFAULT.value)
                telephone_number = PIH.DATA.FORMAT.telephone_number(
                    telephone_number)
                return PIH.MESSAGE.WHATSAPP.WAPPI.send_image(telephone_number, caption, base64_value, wappi_profile)
        
            @staticmethod
            def send_document(telephone_number: str, caption: str, base64_value: str, wappi_profile: Any = None) -> bool:
                wappi_profile = EnumTool.get_value(
                    wappi_profile, CONST.MESSAGE.WHATSAPP.WAPPI.PROFILE.DEFAULT.value)
                telephone_number = PIH.DATA.FORMAT.telephone_number(
                    telephone_number)
                return PIH.MESSAGE.WHATSAPP.WAPPI.send_document(telephone_number, caption, base64_value, wappi_profile)

            @staticmethod
            def send_to_user(user: User, message: Any, via_wappi: bool = True, use_alternative: bool = True, wappi_profile: Any = None) -> bool:
                return PIH.MESSAGE.WHATSAPP.send(user.telephoneNumber, message, via_wappi, use_alternative, EnumTool.get_value(
                    wappi_profile, CONST.MESSAGE.WHATSAPP.WAPPI.PROFILE.DEFAULT.value))

        class DELAYED:

            @staticmethod
            def register(message: DelayedMessage) -> int:
                return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.register_delayed_message, PIH.ACTION.MESSAGE.DELAYED.prepeare_message(message)))

            @staticmethod
            def send(message: DelayedMessage, high_priority: bool = True) -> bool:
                return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.send_delayed_message, (PIH.ACTION.MESSAGE.DELAYED.prepeare_message(message), high_priority)))
            
    
    class ACTION:

        class QR_CODE:

            @staticmethod
            def titled(data: str, title, path: str, font_size: int | None = None) -> bool:
                return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.create_qr_code, (data, title, path, font_size)))

            @staticmethod
            def print(path: str) -> bool:
                return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.print_image, (path, )))

            @staticmethod
            def for_mobile_helper_command(value: str, title: str, path: str, font_size: int | None = None) -> bool:
                return PIH.ACTION.QR_CODE.titled(PIH.DATA.FORMAT.mobile_helper_qr_code_text(PIH.DATA.FORMAT.mobile_helper_command(value)), title, path, font_size)
            
            @staticmethod
            def for_polibase_person_card_registry_folder(name: str) -> bool:
                name = A.D_F.polibase_person_card_registry_folder(name)
                return PIH.ACTION.QR_CODE.for_mobile_helper_command(" ".join(["card", "registry", name]), name, PIH.PATH.QR_CODE.polibase_person_card_registry_folder(name), 80)

        class INDICATION:

            class CT:

                @staticmethod
                def register(value: CTIndicationValue) -> bool:
                    return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.register_ct_indications_value, (value), ))

        class MOBILE_HELPER:

            @staticmethod
            def send_message(name: str, telephone_number: str) -> None:
                return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.send_mobile_helper_message, (name, telephone_number)))

        class BACKUP:

            @staticmethod
            def start_robocopy_job(name: str = None, source: str = None, destination: str = None, force: bool = False) -> bool:
                return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.robocopy_start_job, (name, source, destination, force)))

            @staticmethod
            def start_robocopy_job_by_name(value: str, force: bool = False) -> bool:
                return PIH.ACTION.BACKUP.start_robocopy_job(value, force=force)

        class DATA_STORAGE:

            @staticmethod
            def value(value: object, name: str = None, section: str = None) -> bool:
                try:
                    name = name or value.__getattribute__("name")
                except AttributeError as error:
                    pass
                else:
                    return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.set_storage_value, (name, value, section)))

        class MESSAGE:

            class DELAYED:

                @staticmethod
                def update(value: DelayedMessageDS, search_critery: MessageSearchCritery) -> bool:
                    return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.update_delayed_message, (value, search_critery)))

                @staticmethod
                def update_status(value: DelayedMessageDS, status: MessageStatuses) -> bool:
                    return PIH.ACTION.MESSAGE.DELAYED.update(DelayedMessageDS(status=status.value), MessageSearchCritery(id=value.id))

                @staticmethod
                def complete(value: DelayedMessageDS) -> bool:
                    return PIH.ACTION.MESSAGE.DELAYED.update_status(value, MessageStatuses.COMPLETE)

                @staticmethod
                def abort(value: DelayedMessageDS) -> bool:
                    return PIH.ACTION.MESSAGE.DELAYED.update_status(value, MessageStatuses.ABORT)

                @staticmethod
                def prepeare_message(message: DelayedMessage) -> DelayedMessage:
                    if message.type is None:
                        message.type = MessageTypes.WHATSAPP.value
                    if message.date is not None:
                        if isinstance(message.date, datetime):
                            message.date = DateTimeTool.datetime_to_string(
                                message.date, CONST.DATA_STORAGE.DATE_TIME_FORMAT)
                    if message.sender is not None:
                        message.sender = EnumTool.get_value(message.sender)
                    if  message.type == MessageTypes.WHATSAPP.value and not DataTool.is_empty(message.recipient):
                        if PIH.CHECK.telephone_number(message.recipient):
                            #+7 -> 7
                            message.recipient = PIH.DATA.FORMAT.telephone_number(message.recipient, CONST.INTERNATIONAL_TELEPHONE_NUMBER_PREFIX)
                    return message
        
        class SETTINGS:

            @staticmethod
            def key(key: str, value: Any) -> bool:
                return DataTool.rpc_unrepresent(
                    RPC.call(ServiceCommands.set_settings_value, (key, value)))

            @staticmethod
            def set(settings_item: SETTINGS, value: Any) -> bool:
                return PIH.ACTION.SETTINGS.key(settings_item.value.key_name or settings_item.name, value)

            @staticmethod
            def set_default(settings_item: SETTINGS) -> bool:
                return PIH.ACTION.SETTINGS.set(settings_item, settings_item.value.default_value)

        class USER:

            @staticmethod
            def create_from_template(container_dn: str,
                                     full_name: FullName, login: str, password: str, description: str, telephone: str, email: str) -> bool:
                return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.create_user_by_template, (container_dn, full_name, login, password, description, telephone, email)))

            @staticmethod
            def create_in_container(container_dn: str,
                                    full_name: FullName, login: str, password: str, description: str, telephone: str, email: str) -> bool:
                return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.create_user_in_container, (container_dn, full_name, login, password, description, telephone, email)))

            @staticmethod
            def set_telephone_number(user: User, telephone: str) -> bool:
                return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.set_user_telephone, (user.distinguishedName, telephone)))

            @staticmethod
            def set_password(user: User, password: str) -> bool:
                return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.set_user_password, (user.distinguishedName, password)))

            @staticmethod
            def set_status(user: User, status: str, container: UserContainer) -> bool:
                return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.set_user_status, (user.distinguishedName, status, DataTool.check(container, lambda: container.distinguishedName))))

            @staticmethod
            def remove(user: User) -> bool:
                return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.remove_user, user.distinguishedName))

        class TIME_TRACKING:

            @staticmethod
            def save_report(path: str, start_date: datetime, end_date: datetime, tab_number_list: list[str] = None, plain_format: bool = False) -> bool:
                return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.save_time_tracking_report, (path, DateTimeTool.start_date(start_date), DateTimeTool.end_date(end_date), tab_number_list, plain_format)))

        class INVENTORY:

            @staticmethod
            def create_barcodes(report_file_path: str, result_directory: str) -> bool:
                return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.create_barcodes_for_inventory, (report_file_path, result_directory)))

            @staticmethod
            def save_report_item(report_file_path: str, item: InventoryReportItem) -> bool:
                return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.save_inventory_report_item, (report_file_path, item)))

            @staticmethod
            def close_report(report_file_path: str) -> bool:
                return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.close_inventory_report, report_file_path))

        class PRINTER:

            @staticmethod
            def report() -> bool:
                return not ResultTool.is_empty(PIH.RESULT.PRINTER.report())

            @staticmethod
            def status() -> bool:
                return not ResultTool.is_empty(PIH.RESULT.PRINTER.status())

        class POLIBASE:

            executor: ThreadPoolExecutor = ThreadPoolExecutor(max_workers=10)

            @staticmethod
            def program_close_for_all(notify: bool = True, notification_message: str | None = None, test: bool = True) -> None:
                def close_action(workstation: Workstation) -> None:
                    PIH.ACTION.POLIBASE.client_program_close_for_workstation(workstation)
                def filter_function(workstation: Workstation) -> bool:
                    return workstation.name == CONST.TEST.WS if test else workstation.accessable 
                def every_action(workstation: Workstation) -> None:
                    PIH.ACTION.POLIBASE.executor.submit(close_action, workstation)
                if notify:
                    PIH.MESSAGE.POLIBASE.notify_about_polibase_closing(notification_message, test)
                ResultTool.every(ResultTool.filter(PIH.RESULT.WORKSTATION.all(), filter_function), every_action)

            @staticmethod
            def client_program_close_for_workstation(workstation: Workstation) -> bool:
                return PIH.ACTION.WORKSTATION.kill_process(
                    CONST.POLIBASE.PROCESS_NAME, workstation.name)

            def restart(test: bool = True) -> None:
                PIH.PSTOOLS.reboot(HOSTS.POLIBASE_TEST.NAME if test else HOSTS.POLIBASE.NAME)

            class NOTIFICATION:

                @staticmethod
                def register(value: PolibasePersonVisitNotificationDS) -> bool:
                    return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.register_polibase_person_visit_notification, value))

                class CONFIRMATION:

                    @staticmethod
                    def update(recepient: str, sender: str, status: int) -> bool:
                        return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.update_polibase_person_notification_confirmation, PolibasePersonNotificationConfirmation(recepient, sender, status)))

            class INFORMATION_QUEST:

                @staticmethod
                def register(person: PolibasePerson) -> bool:
                    return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.register_polibase_person_information_quest, PolibasePersonInformationQuest(person.pin, person.FullName, person.telephoneNumber)))
                
                @staticmethod
                def start(person: PolibasePerson) -> bool:
                    return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.start_polibase_person_information_quest, (person.pin, )))

                @staticmethod
                def update(value: PolibasePersonInformationQuest, search_critery: PolibasePersonInformationQuest) -> bool:
                    return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.update_polibase_person_information_quest, (value, search_critery)))

            @staticmethod
            def create_barcode_for_person(pid: int, test: bool = None) -> bool:
                return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.create_barcode_for_polibase_person, (pid, test)))

            @staticmethod
            def set_card_folder_for_person(name: str, pid: int, test: bool = None) -> bool:
                return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.set_polibase_person_card_folder_name, (name, pid, test)))

            @staticmethod
            def set_email(value: str, pin: int, test: bool = None) -> bool:
                return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.set_polibase_person_email, (value, pin, test)))

            @staticmethod
            def set_person_barcode_by_pin(barcode_file_name: str, pin: int, test: bool = None) -> bool:
                return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.set_polibase_person_barcode_by_pin, (barcode_file_name, pin, test)))

            class DB:

                @staticmethod
                def backup(dump_file_name: str = None, test: bool = None) -> bool:
                    return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.create_polibase_database_backup, (dump_file_name, test)))

            class VISIT:

                class DATA_STORAGE:

                    @staticmethod
                    def update(value: PolibasePersonVisitDS) -> bool:
                        return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.update_polibase_person_visit_to_data_stogare, value))

        class MARK:

            @staticmethod
            def create(full_name: FullName, person_division_id: int,  tab_number: str, telephone: str = None) -> bool:
                return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.create_mark, (full_name, person_division_id, tab_number, telephone)))

            @staticmethod
            def set_full_name_by_tab_number(full_name: FullName, tab_number: str) -> bool:
                return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.set_full_name_by_tab_number, (full_name, tab_number)))

            @staticmethod
            def set_telephone_by_tab_number(telephone: str, tab_number: str) -> bool:
                return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.set_telephone_by_tab_number, (telephone, tab_number)))

            @staticmethod
            def make_as_free_by_tab_number(tab_number: str) -> bool:
                return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.make_mark_as_free_by_tab_number, tab_number))

            @staticmethod
            def make_as_temporary(temporary_mark: Mark, owner_mark: Mark) -> bool:
                return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.make_mark_as_temporary, (temporary_mark.TabNumber, owner_mark.TabNumber)))

            @staticmethod
            def remove(mark: Mark) -> bool:
                return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.remove_mark_by_tab_number, mark.TabNumber))

        class DOCUMENTS:

            @staticmethod 
            def save_base64_as_image(path: str, content: str) -> bool:
                return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.save_base64_as_image, (path, content)))

            @staticmethod
            def create_for_user(path: str, full_name: FullName, tab_number: str, pc: LoginPasswordPair, polibase: LoginPasswordPair, email: LoginPasswordPair) -> bool:
                locale.setlocale(locale.LC_ALL, 'ru_RU')
                date_now = datetime.now().date()
                date_now_string = f"{date_now.day} {calendar.month_name[date_now.month]} {date_now.year}"
                return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.create_user_document, (path, date_now_string, CONST.SITE_ADDRESS, CONST.SITE_PROTOCOL + CONST.SITE_ADDRESS, CONST.MAIL_ADDRESS, full_name, tab_number, pc, polibase, email)))

        class WORKSTATION:
    
            @staticmethod
            def reboot(host: str = None, force: bool = False) -> bool:
                return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.reboot, (host, force)))

            @staticmethod
            def shutdown(host: str = None, force: bool = False) -> bool:
                return DataTool.rpc_unrepresent(RPC.call(ServiceCommands.shutdown, (host, force)))
            
            @staticmethod
            def kill_process(process_name: str, host: str) -> bool:
                return PIH.PSTOOLS.kill_process(process_name, host)

            @staticmethod
            def kill_process_via_windows(process_name: str, host: str) -> bool:
                return PIH.PSTOOLS.kill_process_via_windows(process_name, host)

class ActionStack(list):

    def __init__(self, caption: str = "", *argv, input: InputBase = None, output: OutputBase = None):
        self.input = input or PIH.input
        self.output = output or PIH.output
        self.acion_value_list: list[ActionValue] = []
        self.caption = caption
        for arg in argv:
            self.append(arg)
        self.start()

    def call_actions_by_index(self, index: int = 0, change: bool = False):
        previous_change: bool = False
        while True:
            try:
                action_value: ActionValue = self[index]()
                if action_value:
                    if change or previous_change:
                        previous_change = False
                        if index < len(self.acion_value_list):
                            self.acion_value_list[index] = action_value
                        else:
                            self.acion_value_list.append(action_value)
                    else:
                        self.acion_value_list.append(action_value)
                index = index + 1
                if index == len(self) or change:
                    break
            except KeyboardInterrupt:
                self.output.new_line()
                self.output.error("Повтор предыдущих действия")
                self.output.new_line()
                if index > 0:
                    previous_change = True
                    # self.show_action_values()
                    #index = index - 1
                else:
                    continue

    def show_action_values(self) -> None:
        def label(item: ActionValue, _):
            return item.caption
        self.call_actions_by_index(self.input.index(
            "Выберите свойство для изменения, введя индекс", self.acion_value_list, label), True)

    def start(self):
        self.call_actions_by_index()
        while True:
            self.output.new_line()
            self.output.head2(self.caption)
            for action_value in self.acion_value_list:
                self.output.value(action_value.caption, action_value.value)
            if self.input.yes_no("Данные верны", True):
                break
            else:
                self.show_action_values()


class A:

    root = PIH()

    MH = root.MOBILE_HELPER

    R = root.RESULT
    D = root.DATA
    D_TN = D.TELEPHONE_NUMBER
    D_FL = D.FILTER
    D_E = D.EXTRACT
    D_E_SPL = D_E.SERVICE_PARAMETER_LIST
    D_M = D.MARK
    D_C = D.CHECK
    A = root.ACTION
    A_D = A.DOCUMENTS
    A_QR = A.QR_CODE
    A_I = A.INDICATION
    A_I_CT = A_I.CT
    ME = root.MESSAGE
    ME_P = ME.POLIBASE
    A_WS = A.WORKSTATION
    R_ME = R.MESSAGE
    R_R = R.RESOURCES
    R_SSH = R.SSH
    R_I = R.INDICATIONS
    #
    A_ME = A.MESSAGE
    A_TT = A.TIME_TRACKING
    A_MH = A.MOBILE_HELPER
    R_ME_D = R_ME.DELAYED
    A_ME_D = A_ME.DELAYED
    
    #
    ME_WS = ME.WORKSTATION
    ME_P = ME.POLIBASE
    ME_WH = ME.WHATSAPP
    ME_D = ME.DELAYED
    ME_WH_W = ME_WH.WAPPI
    ME_WH_W_Q = ME_WH_W.QUEUE
    A_ME_WH_W_Q = ME_WH_W.QUEUE
    #
    S = root.SETTINGS
    S_U = S.USER
    S_P = S.POLIBASE
    S_R = S.RESOURCE
    S_WS = S.WORKSTATION
    S_P_V = S_P.VISIT
    S_P_RN = S_P.REVIEW_NOTIFICATION
    #
    C = root.CHECK
    C_R = C.RESOURCE
    C_I = C.INDICATION
    C_M = C.MARK
    C_TT = C.TIME_TRACKING
    C_A = C.ACCESS
    C_S = C.SETTINGS
    C_WS = C.WORKSTATION
    C_ME = C.MESSAGE
    C_ME_WH = C_ME.WHATSAPP
    C_ME_WH_W = C_ME_WH.WAPPI
    #
    A_M = A.MARK
    R_M = R.MARK
    R_U = R.USER
    R_TT = R.TIME_TRACKING
    A_U = A.USER
    C_U = C.USER
    D_F = D.FORMAT
    D_CO = D.CONVERT
    A_P = A.POLIBASE
    C_P = C.POLIBASE
    C_P_DB = C_P.DATABASE
    D_P = D.POLIBASE
    R_P = R.POLIBASE
    R_PR = R.PRINTER
    #
    A_P_V = A_P.VISIT
    A_P_V_DS = A_P_V.DATA_STORAGE
    R_P_V = R_P.VISIT
    R_P_V_DS = R_P_V.DATA_STORAGE
    A_P_N = A_P.NOTIFICATION
    A_P_N_C = A_P_N.CONFIRMATION
    R_P_N = R_P.NOTIFICATION
    R_P_N_C = R_P_N.CONFIRMATION
    C_P_N = C_P.NOTIFICATION
    C_P_N_С = C_P_N.CONFIRMATION
    R_WS = R.WORKSTATION
    C_WS = C.WORKSTATION
    A_P_IQ = A_P.INFORMATION_QUEST
    R_P_IQ = R_P.INFORMATION_QUEST
    SRV = root.SERVICE
    SRV_A = SRV.ADMIN
    I = root.input
    I_U = I.user
    A_B = A.BACKUP
    R_B = R.BACKUP
    O = root.output
    SE = root.session
    A_DS = A.DATA_STORAGE
    R_DS = R.DATA_STORAGE
    V = root.VERSION
    OS = root.OS
    U = root.UPDATER
    PS = root.PSTOOLS
    E = root.ERROR
    EV = root.EVENT
    PTH = root.PATH
    PTH_U = PTH.USER
    PTH_QR = PTH.QR_CODE
    PTH_FNT = PTH.FONTS
    L = root.LOG
    L_C = L.COMMAND

    CT = CONST
    CT_FNT = FONT
    CT_SR = ServiceRoles
    CT_SC = ServiceCommands
    CT_F = FILE
    CT_R = RESOURCE
    CT_R_D = CT_R.DESCRIPTIONS
    CT_R_IR = CT_R.INACCESSABLE_REASON
    CT_F_E = CT_F.EXTENSION
    CT_P = CT.POLIBASE
    CT_P_DD = CT_P.DOCUMENT_DESCRIPTIONS
    CT_S = SETTINGS
    CT_ME = CT.MESSAGE
    CT_ME_WH = CT_ME.WHATSAPP
    CT_ME_WH_W = CT_ME_WH.WAPPI
    CT_V = CT.VISUAL
    CT_LC = LogCommands
    CT_MD = MEDICAl_DOCUMENT
    CT_MD_DT = CT_MD.DIRECTION_TYPES
    CT_DS = CT.DATA_STORAGE
    CT_FNC = FIELD_NAME_COLLECTION
    CT_FCA = FIELD_COLLECTION_ALIAS
    CT_LL = LogLevels
    CT_AD = AD