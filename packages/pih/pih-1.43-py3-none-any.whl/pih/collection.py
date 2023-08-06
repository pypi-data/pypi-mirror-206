from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any, Generic, Tuple, TypeVar, List


@dataclass
class FieldItem:
    name: str | None = None
    caption: str | None = None
    visible: bool = True
    class_type: Any | None = None
    default_value: str | None = None
    data_formatter: str = "{data}"


@dataclass
class FullName:
    last_name: str = ""
    first_name: str = ""
    middle_name: str = ""

@dataclass
class ActionValue:
    caption: str
    value: str


@dataclass
class LoginPasswordPair:
    login: str | None = None
    password: str | None = None


@dataclass
class ServiceRoleDescriptionBase:
    name: str | None = None
    description: str | None = None
    host: str | None = None
    login: str | None = None
    password: str | None = None
    port: str | None = None
    service_path: str | None = None
    pid: int = -1
    pih_version: str | None = None
    isolated: bool = False
    visible_for_admin: bool = True
    auto_restart: bool = True
    weak_subscribtion: bool = False
    auto_start: bool = True
    start_once: bool = False


@dataclass
class ServiceRoleInformation(ServiceRoleDescriptionBase):
    subscribers: list | None = None


@dataclass
class ServiceRoleDescription(ServiceRoleDescriptionBase):
    #from pih.const import ServiceCommands
    #list[ServiceCommands]
    commands: list = field(default_factory=list)
    modules: list[str] = field(default_factory=list)

    def __hash__(self) -> int:
        return hash(self.name)
    
    def __eq__(self, another):
         return self.name == another.name


class FieldItemList:

    list: list[FieldItem]

    def copy_field_item(self, value: FieldItem) -> FieldItem:
        return FieldItem(
            value.name, value.caption, value.visible, value.class_type, value.default_value, value.data_formatter)

    def __init__(self, *args):
        self.list = []
        arg_list = list(args)
        for arg_item in arg_list:
            if isinstance(arg_item, FieldItem):
                item: FieldItem = self.copy_field_item(arg_item)
                self.list.append(item)
            elif isinstance(arg_item, FieldItemList):
                for item in arg_item.list:
                    self.list.append(self.copy_field_item(item))
            elif isinstance(arg_item, list):
                self.list.extend(arg_item)

    def get_list(self) -> list[FieldItem]:
        return self.list

    def get_item_and_index_by_name(self, value: str) -> Tuple[FieldItem, int]:
        index: int = -1
        result: FieldItem | None = None
        for item in self.list:
            index += 1
            if item.name == value:
                result = item
                break
        return result, -1 if result is None else index

    def get_item_by_name(self, value: str) -> FieldItem:
        result, _ = self.get_item_and_index_by_name(value)
        return result

    def position(self, name: str, position: int):
        _, index = self.get_item_and_index_by_name(name)
        if index != -1:
            self.list.insert(position, self.list.pop(index))
        return self

    def get_name_list(self):
        return list(map(lambda x: str(x.name), self.list))

    def get_caption_list(self):
        return list(map(lambda x: str(x.caption), filter(lambda y: y.visible, self.list)))

    def visible(self, name: str, value: bool):
        item, _ = self.get_item_and_index_by_name(name)
        if item is not None:
            item.visible = value
        return self

    def caption(self, name: str, value: bool):
        item, _ = self.get_item_and_index_by_name(name)
        if item is not None:
            item.caption = value
        return self

    def length(self) -> int:
        return len(self.list)


T = TypeVar("T")
R = TypeVar("R")


@dataclass
class Result(Generic[T]):
    fields: FieldItemList | None = None
    data: T | None = None


@dataclass
class OGRN:
    name: str | None = None
    code: str | None = None
    data: dict | None = None


@dataclass
class UserContainer:
    name: str | None = None
    description: str | None = None
    distinguishedName: str | None = None


@dataclass
class User(UserContainer):
    samAccountName: str | None = None
    mail: str | None = None
    telephoneNumber: str | None = None
    userAccountControl: int | None = None


@dataclass
class WorkstationDescription:
    name: str | None = None
    properties: int  = 0
    description: str | None = None


@dataclass
class Workstation(WorkstationDescription):
    samAccountName: str | None = None
    accessable: bool | None = None


@dataclass
class ResourceDescription:
    address: str | None = None
    name: str | None = None
    inaccessibility_check_values: Tuple[int] = (2, 20, 15)

@dataclass
class SiteResourceDescription(ResourceDescription):
    check_certificate_status: bool = False
    check_free_space_status: bool = False
    driver_name: str | None = None
   

@dataclass
class ResourceStatus(ResourceDescription):
    accessable: bool | None = None
    inaccessibility_counter: int = 0

@dataclass
class WSResourceStatus(ResourceStatus):
    
    pass


@dataclass
class SiteResourceStatus(ResourceStatus, SiteResourceDescription):
    certificate_status: str | None = None
    free_space_status: str | None = None

@dataclass
class MarkBase:
    FullName: str | None = None
    TabNumber: str | None = None


@dataclass
class MarkSimple(MarkBase):
    DivisionName: str | None = None


@dataclass
class TemporaryMark(MarkBase):
    OwnerTabNumber: str | None = None


@dataclass
class PolibasePersonBase:
    pin: int | None = None
    FullName: str | None = None
    telephoneNumber: str | None = None


@dataclass
class PolibasePerson(PolibasePersonBase):
    Birth: datetime | None = None
    Comment: str | None = None
    ChartFolder: str | None = None
    mail: str | None = None


@dataclass
class PolibasePersonVisitDS(PolibasePersonBase):
    id: int | None = None
    registrationDate: str | None = None
    beginDate: str | None = None
    completeDate: str | None = None
    status: int | None = None
    cabinetID: int | None = None
    doctorID: int | None = None
    doctorFullName: str | None = None
    serviceGroupID: int | None = None


@dataclass
class PolibasePersonVisitSearchCritery:
    vis_no: Any | None = None
    vis_pat_no: Any | None = None
    vis_pat_name: Any | None = None
    vis_place: Any | None = None
    vis_reg_date: Any | None = None
    vis_date_ps: Any | None = None
    vis_date_pf: Any | None = None
    vis_date_fs: Any | None = None
    vis_date_ff: Any | None = None


@dataclass
class PolibasePersonVisitNotificationDS:
    visitID: int | None = None
    messageID: int | None = None
    type: int | None = None

@dataclass
class Message:
    message: str | None = None
    recipient: str | None = None
    sender: str | None = None

@dataclass
class DelayedMessage(Message):
    date: Any | None = None
    type: int | None = None
    
@dataclass
class DelayedMessageDS(DelayedMessage):
    id: int | None = None
    status: int | None = None

@dataclass
class MessageSearchCritery:
    id: Any | None = None
    recipient: str | None = None
    date: str | None = None
    type: Any | None = None
    status: int | None = None
    sender: str | None = None


@dataclass
class PolibasePersonNotificationConfirmation:
    recipient: str | None = None
    sender: str | None = None
    status: int = 0

@dataclass
class PolibasePersonVisitNotification(PolibasePersonVisitDS, PolibasePersonVisitNotificationDS):
    pass

@dataclass
class PolibasePersonVisit(PolibasePersonVisitDS):
    registrationDate: datetime | None = None
    beginDate: datetime | None = None
    completeDate: datetime | None = None
    beginDate2: datetime | None = None
    completeDate2: datetime | None = None
   

@dataclass
class PolibasePersonQuest:
    step: int | None = None
    stepConfirmed: bool | None = None
    timestamp: int | None = None


@dataclass
class PolibasePersonInformationQuest(PolibasePersonBase):
    confirmed: int | None = None
    errors: int | None = None


@dataclass
class PolibasePersonReviewQuest(PolibasePersonQuest):
    beginDate: str | None = None
    completeDate: str | None = None
    grade: int | None = None
    message: str | None = None
    informationWay: int | None = None
    feedbackCallStatus: int | None = None


@dataclass
class Mark(MarkSimple):
    pID: int | None = None
    mID: int | None = None
    GroupName: str | None = None
    GroupID: int | None = None
    Comment: str | None = None
    telephoneNumber: str | None = None
    type: int | None = None


@dataclass
class MarkDivision:
    id: int | None = None
    name: str | None = None


@dataclass
class TimeTrackingEntity(MarkSimple):
    TimeVal: str | None = None
    Mode: int | None = None


@dataclass
class TimeTrackingResultByDate:
    date: str | None = None
    enter_time: str | None = None
    exit_time: str | None = None
    duration: int | None = None


@dataclass
class TimeTrackingResultByPerson:
    tab_number: str | None = None
    full_name: str | None = None
    duration: int = 0
    list: List[TimeTrackingResultByDate] = field(
        default_factory=list)


@dataclass
class WhatsAppMessage:
    message: str | None = None
    from_me: bool | None = None
    sender: str | None = None
    recipient: str | None = None
    profile_id: str | None = None
    time: int | None = None
    chatId: str | None = None


@dataclass
class WhatsAppMessagePayload:
    title: str
    body: str


@dataclass
class WhatsAppMessageListPayload(WhatsAppMessagePayload):
    btn_text: str
    list: dict


@dataclass
class WhatsAppMessageButtonsPayload(WhatsAppMessagePayload):
    buttons: list | None = None


@dataclass
class TimeTrackingResultByDivision:
    name: str
    list: List[TimeTrackingResultByPerson] = field(
        default_factory=list)

@dataclass
class RobocopyJobDescription:
    name: str | None = None
    start_datetime: str | None = None
    host: str | None = None
    run_from_system_account: bool = False
    run_with_elevetion: bool = False
   
    def clone(self, job_name: str, start_datetime: str | None = None, host: str | None = None):
        return RobocopyJobDescription(job_name, start_datetime, host or self.host, self.run_from_system_account, self.run_with_elevetion)


@dataclass
class RobocopyJobItem(RobocopyJobDescription):
    source: str | None = None
    destination: str | None = None


@dataclass
class RobocopyJobStatus:
    name: str | None = None
    source: str | None = None
    destination: str | None = None
    active: bool = False
    last_created: str | None = None
    last_status: int | None = None


@dataclass
class PrinterADInformation:
    driverName: str | None = None
    adminDescription: str | None = None
    description: str | None = None
    portName: str | None = None
    serverName: str | None = None
    name: str | None = None

@dataclass
class IndicationItem:
    timestamp: datetime | None = None

@dataclass
class THIndicationValue:
    temperature: float | None = None
    humidity: float | None = None

@dataclass
class CTIndicationValue(THIndicationValue):
    pass

@dataclass
class CTIndicationItem(CTIndicationValue, IndicationItem):
    pass


@dataclass
class InventoryReportItem:
    name: str | None = None
    inventory_number: str | None = None
    row: str | None = None
    quantity: int | None = None
    name_column: int | None = None
    inventory_number_column: int | None = None
    quantity_column: int | None = None


@dataclass
class PrinterStatus:
    ip: str | None = None
    desc: str | None = None
    variant: str | None = None
    port: int | None = None
    community: str | None = None 
    accessable: bool | None = None


@dataclass
class PrinterReport(PrinterStatus):
    name: str | None = None
    model: str | None = None
    serial: int | None = None
    meta: str | None = None
    printsOverall: int | None = None
    printsColor: int | None = None
    printsMonochrome: int | None = None
    fuserType: int | None = None
    fuserCapacity: int | None = None
    fuserRemaining: int | None = None
    wasteType: int | None = None
    wasteCapacity: int | None = None
    wasteRemaining: int | None = None
    cleanerType: int | None = None
    cleanerCapacity: int | None = None
    cleanerRemaining: int | None = None
    transferType: int | None = None
    transferCapacity: int | None = None
    transferRemaining: int | None = None
    blackTonerType: str | None = None
    blackTonerCapacity: int | None = None
    blackTonerRemaining: int | None = None
    cyanTonerType: int | None = None
    cyanTonerCapacity: int | None = None
    cyanTonerRemaining: int | None = None
    magentaTonerType: int | None = None
    magentaTonerCapacity: int | None = None
    magentaTonerRemaining: int | None = None
    yellowTonerType: int | None = None
    yellowTonerCapacity: int | None = None
    yellowTonerRemaining: int | None = None
    blackDrumType: str | None = None
    blackDrumCapacity: int | None = None
    blackDrumRemaining: int | None = None
    cyanDrumType: int | None = None
    cyanDrumCapacity: int | None = None
    cyanDrumRemaining: int | None = None
    magentaDrumType: int | None = None
    magentaDrumCapacity: int | None = None
    magentaDrumRemaining: int | None = None
    yellowDrumType: int | None = None
    yellowDrumCapacity: int | None = None
    yellowDrumRemaining: int | None = None


@dataclass
class MarkGroup:
    GroupName: str | None = None
    GroupID: int | None = None


@dataclass
class MarkGroupStatistics(MarkGroup):
    Comment: str | None = None 
    Count: int | None = None


@dataclass
class PasswordSettings:
    length: int
    special_characters: str
    order_list: list[str]
    special_characters_count: int
    alphabets_lowercase_count: int
    alphabets_uppercase_count: int
    digits_count: int = 1
    shuffled: bool = False


@dataclass
class LogCommandDescription:
    message: str
    log_channel: Enum
    log_level: int
    params: Tuple | None = None


@dataclass
class ParamItem:
    name: str
    caption: str
    description: str | None = None


@dataclass
class SettingsValue:
    key_name: str
    default_value: Any
    description: str | None = None
    auto_init: bool = True


@dataclass
class PolibaseScannedDocument:
    file_path: str
    pin: int
    document_name: str

@dataclass
class ThresholdedText:
    title: str
    threshold: float


@dataclass
class PolibaseDocumentDescription(ThresholdedText):
    title_top: int = 0
    title_height: int = 0
    page_count: int = 1

@dataclass
class DocumentDescription(ThresholdedText):
    left: float
    top: float
    right: float
    bottom: float


@dataclass
class MedicalDirectionDescription:
    title_list: tuple[str]
    alias: str