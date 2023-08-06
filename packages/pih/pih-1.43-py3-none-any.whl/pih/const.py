from enum import *
import os

from pih.collection import FieldItem, FieldItemList, LogCommandDescription, ParamItem, PasswordSettings, ServiceRoleDescription, SettingsValue, ResourceDescription, SiteResourceDescription, PolibaseDocumentDescription, MedicalDirectionDescription

class DATA:

    #deprecated
    class EXTRACTOR:

        USER_NAME_FULL: str = "user_name_full"
        USER_NAME: str = "user_name"
        AS_IS: str = "as_is"

    class FORMATTER:

        MY_DATETIME: str = "my_datetime"


class USER_PROPERTY:

    TELEPHONE_NUMBER: str = "telephoneNumber"
    EMAIL: str = "mail"
    DN: str = "distinguishedName"
    USER_ACCOUNT_CONTROL: str = "userAccountControl"
    LOGIN: str = "samAccountName"
    DESCRIPTION: str = "description"
    PASSWORD: str = "password"
    USER_STATUS: str = "userStatus"
    NAME: str = "name"

class BARCODE:

    CODE128: str = "code128"
    I25: str = "i25"

class AD:

    SEARCH_ATTRIBUTES: list[str] = [
        USER_PROPERTY.LOGIN, USER_PROPERTY.NAME]
    SEARCH_ATTRIBUTE_DEFAULT: str = SEARCH_ATTRIBUTES[0]
    DOMAIN_NAME: str = "fmv"
    DOMAIN_ALIAS: str = "pih"
    DOMAIN_SUFFIX: str = "lan"
    DOMAIN: str = f"{DOMAIN_NAME}.{DOMAIN_SUFFIX}"
    DOMAIN_MAIN: str = DOMAIN
    USER_HOME_FOLDER_DISK: str = "U:"
    OU: str = "OU="
    ROOT_CONTAINER_DN: str = f"{OU}Unit,DC={DOMAIN_NAME},DC={DOMAIN_SUFFIX}"
    WORKSTATIONS_CONTAINER_DN: str = f"{OU}Workstations,{ROOT_CONTAINER_DN}"
    USERS_CONTAINER_DN_SUFFIX: str = f"Users,{ROOT_CONTAINER_DN}"
    ACTIVE_USERS_CONTAINER_DN: str = f"{OU}{USERS_CONTAINER_DN_SUFFIX}"
    INACTIVE_USERS_CONTAINER_DN: str = f"{OU}dead{USERS_CONTAINER_DN_SUFFIX}"
    PATH_ROOT: str = f"\\\{DOMAIN_MAIN}"
    SEARCH_ALL_PATTERN: str = "*"
    GROUP_CONTAINER_DN: str = f"{OU}Groups,{ROOT_CONTAINER_DN}"
    JOB_POSITION_CONTAINER_DN: str = f"{OU}Job positions,{GROUP_CONTAINER_DN}"
    LOCATION_JOINER: str = ":"
    TEMPLATED_USER_SERACH_TEMPLATE: str = "_*_"
    PROPERTY_ROOT_DN: str = f"{OU}Property,{GROUP_CONTAINER_DN}"
    PROPERTY_WS_DN: str = f"{OU}WS,{PROPERTY_ROOT_DN}"

    USER_ACCOUNT_CONTROL: list[str] = [
        "SCRIPT",
        "ACCOUNTDISABLE",
        "RESERVED",
        "HOMEDIR_REQUIRED",
        "LOCKOUT",
        "PASSWD_NOTREQD",
        "PASSWD_CANT_CHANGE",
        "ENCRYPTED_TEXT_PWD_ALLOWED",
        "TEMP_DUPLICATE_ACCOUNT",
        "NORMAL_ACCOUNT",
        "RESERVED",
        "INTERDOMAIN_TRUST_ACCOUNT",
        "WORKSTATION_TRUST_ACCOUNT",
        "SERVER_TRUST_ACCOUNT",
        "RESERVED",
        "RESERVED",
        "DONT_EXPIRE_PASSWORD",
        "MNS_LOGON_ACCOUNT",
        "SMARTCARD_REQUIRED",
        "TRUSTED_FOR_DELEGATION",
        "NOT_DELEGATED",
        "USE_DES_KEY_ONLY",
        "DONT_REQ_PREAUTH",
        "PASSWORD_EXPIRED",
        "TRUSTED_TO_AUTH_FOR_DELEGATION",
        "RESERVED",
        "PARTIAL_SECRETS_ACCOUNT"
    ]

    WORKSTATION_PREFIX_LIST: list[str] = [
        "ws-", "nb-", "fmvulianna"]

    ADMINISTRATOR: str = "Administrator"
    ADMINISTRATOR_PASSOWORD: str = "Fortun@90"

    CALL_CENTRE_ADMINISTRATOR: str = "callCentreAdmin"

    MARKETER: str = "marketer"

    class JobPisitions(Enum):
        HR: int = auto()
        IT: int = auto()
        CALL_CENTRE: int = auto()
        REGISTRATOR: int = auto()
        RD: int = auto()

    class Groups(Enum):
        TimeTrackingReport: int = auto()
        Inventory: int = auto()
        Polibase: int = auto()
        Admin: int = auto()
        ServiceAdmin: int = auto()
        CardRegistry: int = auto()
        PolibaseUsers: int = auto()
        RD: int = auto()
        IndicationWatcher: int = auto()

    class WSProperies(Enum):

        Watchable: int = 1
        Shutdownable: int = 2
        Rebootable: int = 4

class FONT:

    FOR_PDF: str = "DejaVuSerif"

class FILE:

    class EXTENSION:

        EXCEL_OLD: str = "xls"
        EXCEL_NEW: str = "xlsx"
        JPEG: str = "jpeg"
        JPG: str = "jpg"
        PNG: str = "png"
        PDF: str = "pdf"
        TXT: str = "txt"
        PYTHON: str = "py"
        BASE64: str = "base64"
        EXE: str = "exe"
        TRUE_TYPE_FONT: str = "ttf"

class HOSTS:

    class BACKUP_WORKER:
    
        NAME: str = "backup_worker"
        ALIAS: str = "backup_worker"
        IP: str = "192.168.100.11"
    
    class DEVELOPER:

        NAME: str = "ws-735"
        IP: str = "192.168.254.102"

    class WS255:
    
        NAME: str = "ws-255"
        IP: str = "192.168.100.138"

    class WS816:
        
        NAME: str = "ws-816"
        IP: str = "192.168.254.81"

    class WS735:
        
        NAME: str = "ws-735"
        IP: str = "192.168.254.102"
        ALIAS: str = "shared_disk_owner"

    class DC1:
    
        NAME: str = "fmvdc1.fmv.lan"
        ALIAS: str = "dc1"
        IP: str = "192.168.100.4"

    class DC2:

        NAME: str = "fmvdc2.fmv.lan"
        ALIAS: str = "dc2"
        IP: str = "192.168.100.23"
    
    class PRINTER_SERVER:

        NAME: str = "fmvdc1.fmv.lan"

    class POLIBASE:

        #shit - cause polibase is not accessable
        NAME: str = "fmvpolibase1.fmv.lan"
        ALIAS: str = "polibase"
        IP: str = "192.168.100.3"

    class POLIBASE_TEST:

        NAME: str = "fmvpolibase2.fmv.lan"
        ALIAS: str = "polibase_test"
        IP: str = "192.168.110.140"

    class _1C:

        NAME: str = "1c"
        ALIAS: str = "1c"
        IP: str = "192.168.100.22"

    class NAS:
    
        NAME: str = "nas"
        ALIAS: str = "nas"
        IP: str = "192.168.100.200"

    class PACS_ARCHVE:

        NAME: str = "pacs_archive"
        ALIAS: str = "ea_archive"
        IP: str = "192.168.110.108"

class URLS:

    PYPI: str = "https://pypi.python.org/pypi/pih/json"


class CONST:

    class TEST:

        WS: str = HOSTS.DEVELOPER.NAME

    GROUP_PREFIX: str = "group:"

    SITE_PROTOCOL: str = "https://"
    UNTRUST_SITE_PROTOCOL: str = "http://" 
    
    SITE_ADDRESS: str = "pacifichosp.com"
    MAIL_ADDRESS: str = f"mail.{SITE_ADDRESS}"
    WIKI_ADDRESS: str = f"{UNTRUST_SITE_PROTOCOL}wiki"

    INTERNATIONAL_TELEPHONE_NUMBER_PREFIX: str = "7"
    TELEPHONE_NUMBER_PREFIX: str = "+" + INTERNATIONAL_TELEPHONE_NUMBER_PREFIX
    INTERNAL_TELEPHONE_NUMBER_PREFIX: str = "тел."

    DATE_TIME_SPLITTER: str = "T"
    TIME_FORMAT: str = "%H:%M:00"
    SECONDLESS_TIME_FORMAT: str = "%H:%M"
    DATE_TIME_FORMAT: str = f"%Y-%m-%d{DATE_TIME_SPLITTER}{TIME_FORMAT}"
    DATE_FORMAT: str = "%d.%m.%Y"

    YEARLESS_DATE_FORMAT: str = "%d.%m"

    MY_DATE_FORMAT: str = "%d.%m.%Y %H:%M:%S"

    API_SITE_ADDRESS: str = f"api.{SITE_ADDRESS}"

    BITRIX_SITE_URL: str = "bitrix.cmrt.ru"

    class DATA_STORAGE:

        DADATA_TOKEN: str = "147c0cd53d67fb4e48e379336c5794ae146c9621"
        DATE_TIME_SPLITTER: str = " "
        DATE_FORMAT: str = "%Y-%m-%d"
        TIME_FORMAT: str = "%H:%M:00"
        DATE_TIME_FORMAT: str = f"{DATE_FORMAT}{DATE_TIME_SPLITTER}{TIME_FORMAT}"

    class CACHE:
        
        class TTL:
            
            WORKSTATIONS: int = 60

    class ERROR:

        class WAPPI:

            PROFILE_NOT_PAID: int = 402

    class TIME_TRACKING:

        REPORT_DAY_PERIOD_DEFAULT: int = 15

    class MESSAGE:

        class WHATSAPP:

            SITE_NAME: str = "https://wa.me/"
            SEND_MESSAGE_TO_TEMPLATE: str = SITE_NAME + "{}?text={}"

            GROUP_SUFFIX: str = "@g.us"

            class GROUP(Enum):

                RD: str = "79146947050-1595848245@g.us"
                CT_INDICATIONS: str = "120363084280723039@g.us"
                DOCUMENTS_WORK_STACK: str = '120363115241877592@g.us'
                DOCUMENTS_WORK_STACK_TEST: str = '120363128816931482@g.us'

            class WAPPI:

                PROFILE_SUFFIX: str = "profile_id="
                URL_API: str = "https://wappi.pro/api"
                URL_API_SYNC: str = f"{URL_API}/sync"
                URL_MESSAGE: str = f"{URL_API_SYNC}/message"
                URL_SEND_MESSAGE: str = f"{URL_MESSAGE}/send?{PROFILE_SUFFIX}"
                URL_SEND_VIDEO: str = f"{URL_MESSAGE}/video/send?{PROFILE_SUFFIX}"
                URL_SEND_IMAGE: str = f"{URL_MESSAGE}/img/send?{PROFILE_SUFFIX}"
                URL_SEND_DOCUMENT: str = f"{URL_MESSAGE}/document/send?{PROFILE_SUFFIX}"
                URL_SEND_LIST_MESSAGE: str = f"{URL_MESSAGE}/list/send?{PROFILE_SUFFIX}"
                URL_SEND_BUTTONS_MESSAGE: str = f"{URL_MESSAGE}/buttons/send?{PROFILE_SUFFIX}"
                URL_GET_MESSAGES: str = f"{URL_MESSAGE}s/get?{PROFILE_SUFFIX}"
                URL_GET_STATUS: str = f"{URL_API_SYNC}/get/status?{PROFILE_SUFFIX}"
                CONTACT_SUFFIX: str = "@c.us"

                class PROFILE(Enum):
                    IT: str = "e6706eaf-ae17"
                    CALL_CENTRE: str = "56ad2cb1-a5ac"
                    MARKETER: str = "c31db01c-b6d6"
                    DEFAULT: str = CALL_CENTRE
                    
                AUTHORIZATION: str = "6b356d3f53124af3078707163fdaebca3580dc38"
            
    class PYTHON:

        EXECUTOR: str = "py"
        PYPI: str = "pip"

    class SERVICE:

        NAME: str = "service"

    class FACADE:

        SERVICE_FOLDER_SUFFIX: str = "Core"
        PATH: str = "\\\\pih\\facade\\"

    class VALENTA:

        PROCESS_NAME: str = "Vlwin"

    class PSTOOLS:

        NAME: str = "pstools"
        PS_EXECUTOR: str = "psexec"
        PS_KILL_EXECUTOR: str = "pskill"
        PS_PING: str = "psping"

        COMMAND_LIST: list[str] = [
            PS_KILL_EXECUTOR,
            "psfile",
            "psgetsid",
            "psinfo",
            "pslist",
            "psloggedon",
            "psloglist",
            "pspasswd",
            PS_PING,
            "psservice",
            "psshutdown",
            "pssuspend"
        ]

        NO_BANNER: str = "-nobanner"
        ACCEPTEULA: str = "-accepteula"

    class MSG:

        NAME: str = "msg"
        EXECUTOR: str = NAME

    class DOCS:

        EXCEL_TITLE_MAX_LENGTH: int = 31

        class INVENTORY:

            NAME_COLUMN_NAME: str = "наименование, назначение и краткая характеристика объекта"
            NUMBER_COLUMN_NAME: str = "инвентарный"
            QUANTITY_COLUMN_NAME: str = "фактическое наличие"
            NAME_MAX_LENTH: int = 120
            QUANTITY_NOT_SET: str = "-"

    class BARCODE_READER:

        PREFIX: str = "("
        SUFFIX: str = ")"

    class MOBILE_HELPER:

        USER_DATA_INPUT_TIMEOUT: int = 180

        class InteraptionTypes:

            INTERNAL: int = 1
            TIMEOUT: int = 2

   
    class NAME_POLICY:

        PARTS_LIST_MIN_LENGTH: int = 3
        PART_ITEM_MIN_LENGTH: int = 3

    class RPC:

        PING_COMMAND: str = "__ping__"
        EVENT_COMMAND: str = "__event__"
        SUBSCRIBE_COMMAND: str = "__subscribe__"

        @staticmethod
        def PORT(add: int = 0) -> int:
            return 50051 + add

        TIMEOUT: int = None
        TIMEOUT_FOR_PING: int = 2

    HOST = HOSTS()

    class POLIBASE:

        NAME: str = "Polibase"

        PROCESS_NAME: str = "Polibase ODAC"

        PRERECORDING_PIN: int = 10
        RESERVED_TIME_A_PIN: int = 5
        RESERVED_TIME_B_PIN: int = 6
        RESERVED_TIME_C_PIN: int = 7

        CARD_REGISTRY_FOLDER_NAME_CHECK_PATTERN: list[str] = [
        "п", "т", "b", "p", "t", "б"]
    
        #145 - Средний Медицинский Персонал
        #300 - Реанимация
        #361 - Операционная блок
        #421 - СМП
        #221 -
        #229 -
        CABINET_NO_EXCLUDE_FROM_VISIT_RESULT: list[int] = [145, 221, 229, 300, 361, 421]
        
        #147 - УЗИ
        #201 - ЭНДОСКОПИЯ
        #202 - МРТ
        #203 - КТ

        class APPOINTMENT_SERVICE_GROUP_ID(Enum):
            ULTRASOUND: int = 147
            ENDOSCOPY: int = 201
            MRI: int = 202
            CT: int = 203

        APPOINTMENT_SERVICE_GROUP_NAME: dict = {
            APPOINTMENT_SERVICE_GROUP_ID.ULTRASOUND: "ультразвуковое исследование",
            APPOINTMENT_SERVICE_GROUP_ID.ENDOSCOPY: "эндоспопичекое исследование",
            APPOINTMENT_SERVICE_GROUP_ID.MRI: "МРТ исследование", 
            APPOINTMENT_SERVICE_GROUP_ID.CT: "рентген исследование"
        }

        STATUS_EXCLUDE_FROM_VISIT_RESULT: list[int] = [63]

        ###

        TELEGRAM_BOT_URL: str = "https://t.me/pacifichospital_bot"

        REVIEW_ACTION_URL: str = "https://forms.gle/qriwujnAknYXga4eA"

        PERSON_VISIT_NOTIFICATION_TEXT_CANCEL_OR_REPLACE_RECEPTION: str = "\nДля отмены или переноса записи свяжитесь по номеру 2790790. С уважением, больница Пасифик Интернешнл Хоспитал."

        PERSON_VISIT_NOTIFICATION_HEADER: str = "_Здравствуйте, это *автоматическая* рассылка от Пасифик Интернешнл Хоспитал._\n\n"

        SEND_TELEGRAM_BOT_TEXT: str = "\n\nОтправляем ссылку на наш telegram-бот с *важной информацией* (подготовка к исследованиям, врачи, услуги, схема проезда и др.):\n" + TELEGRAM_BOT_URL

        ASK_TO_SEND_TELEGRAM_BOT_URL_TEXT: str = "\n\nОтправьте в ответ любое сообщение и мы пришлём Вам ссылку на наш telegram-бот с *важной информацией* (подготовка к исследованиям, врачи, услуги, схема проезда и др.)"

        PERSON_VISIT_NOTIFICATION_APPOINTMENT_INFORMATION: str = "*{name}*, Вы записаны в Пасифик Интернешнл Хоспитал на {appointment_information}. "

        PERSON_VISIT_GREETING_NOTIFICATION_TEXT_BASE: str = PERSON_VISIT_NOTIFICATION_HEADER + PERSON_VISIT_NOTIFICATION_APPOINTMENT_INFORMATION

        PERSON_VISIT_GREETING_NOTIFICATION_TEXT_WITHOUT_TEXT: str = PERSON_VISIT_GREETING_NOTIFICATION_TEXT_BASE + ASK_TO_SEND_TELEGRAM_BOT_URL_TEXT

        PERSON_VISIT_GREETING_NOTIFICATION_TEXT_FOR_CONFIRMED_NOTIFICATION: str = PERSON_VISIT_GREETING_NOTIFICATION_TEXT_BASE

        PERSON_VISIT_NOTIFICATION_WITH_TIME_TEXT: str = "\n\nВаш приём запланирован на {day_string} {month_string} в {hour_string}{minute_string}." + PERSON_VISIT_NOTIFICATION_TEXT_CANCEL_OR_REPLACE_RECEPTION

        ###

        PERSON_REVIEW_NOTIFICATION_TEXT_BASE: str = "Добрый день, *{name}*!\n\nМеня зовут Анна, я директор отдела качества *Pacific International Hospital* (ранее Falck).\n\nВы недавно обращались в нашу больницу. Будем очень признательны, если в целях улучшения качества обслуживания вы ответите на несколько вопросов"

        SEND_REVIEW_ACTION_URL_TEXT: str = ", перейдя по ссылке ниже:\n" + REVIEW_ACTION_URL

        PERSON_REVIEW_NOTIFICATION_TEXT_FOR_CONFIRMED_NOTIFICATION: str = PERSON_REVIEW_NOTIFICATION_TEXT_BASE + SEND_REVIEW_ACTION_URL_TEXT

        ASK_TO_SEND_REVIEW_ACTION_TEXT: str = ". Согласны ли Вы пройти опрос?"

        PERSON_REVIEW_NOTIFICATION_TEXT: str = PERSON_REVIEW_NOTIFICATION_TEXT_BASE + ASK_TO_SEND_REVIEW_ACTION_TEXT

        YES_ANSWER: list[str] = ["да", "согласен", "согласна", "ok", "ок", "yes", "хорошо", "ага"]

        NO_ANSWER: list[str] = ["нет", "не согласен", "не согласна", "no", "занят"]

        TAKE_TELEGRAM_BOT_URL_TEXT: str = "*{name}*, отправляем Вам ссылку:\n"

        PERSONLESS_TAKE_TELEGRAM_BOT_URL_TEXT: str = "Отправляем Вам ссылку:\n"

        TAKE_REVIEW_ACTION_URL_TEXT: str = "*{name}*, отправляем Вам ссылку для прохождения опроса:"


        DATE_FORMAT: str = "%d.%m.%Y"
        DATE_IS_NOT_SET_YEAR: int = 1899
        
        INSTANCE: str = "orcl.fmv.lan"
        USER: str = "POLIBASE"
        PASSWORD: str = "POLIBASE"
        
        class BARCODE:
            
            class PERSON:
                IMAGE_FORMAT: str =  FILE.EXTENSION.JPEG
            class PERSON_CARD_FOLDER:
                IMAGE_FORMAT: str = FILE.EXTENSION.PNG
            
            ACTUAL_FORMAT: str = BARCODE.CODE128
            OLD_FORMAT: str = BARCODE.I25

            SUPPORT_FORMATS: list[str] = [ACTUAL_FORMAT, OLD_FORMAT]

            NEW_PATTERN: str = "new_"

            @staticmethod
            def get_file_name(pin: int, with_extension: bool = False) -> str:
                extension: str = f".{CONST.POLIBASE.BARCODE.PERSON.IMAGE_FORMAT}" if with_extension else ""
                return f"{CONST.POLIBASE.BARCODE.NEW_PATTERN}{pin}{extension}"
            
        class DOCUMENT_DESCRIPTIONS(Enum):

            HOLTER_JOURNAL: PolibaseDocumentDescription = PolibaseDocumentDescription("Дневник суточного мониторинга ЭКГ", 70, 70, 80)
            PATIENT_CARD_AMBULATORY: PolibaseDocumentDescription = PolibaseDocumentDescription("Медицинская карта\nпациента, получившего медицинскую помощь\nв амбулаторных условиях", 70, 120, 120)
            PROCESSING_PRESONAL_DATA_CONSENT: PolibaseDocumentDescription = PolibaseDocumentDescription("согласие\nпациента на обработку персональных данных", 70, 70, 120, 1)
            INFORMED_VOLUNTARY_MEDICAL_INVENTION_CONSENT: PolibaseDocumentDescription = PolibaseDocumentDescription("информированное добровольное согласие\nна медицинское вмешательство", 70, 70, 120, 1)
            INFORMED_VOLUNTARY_MEDICAL_INVENTION_CONSENT_SPECIFIC: PolibaseDocumentDescription = PolibaseDocumentDescription("информированное добровольное согласие на виды медицинских\nвмешательств, включенные в перечень определенных видов\nмедицинских вмешательств, на которые граждане дают\nинформированное добровольное согласие при выборе врача и\nмедицинской организации для получения первичной медико-\nсанитарной помощи", 70, 70, 280, 2)

            @staticmethod
            def sorted() -> list:
                return sorted(CONST.POLIBASE.DOCUMENT_DESCRIPTIONS, key=lambda item: item.value.title_height, reverse=True)
    
    class VISUAL:

        NUMBER_SYMBOLS: list[str] = [
           "0️⃣",
           "1️⃣",
           "2️⃣",
           "3️⃣", 
           "4️⃣",
           "5️⃣",
           "6️⃣",
           "7️⃣",
           "8️⃣",
           "9️⃣",
           "🔟"
        ]

        ARROW: str = "➜"

        BULLET: str = "•" 

class RESOURCE:

    class DESCRIPTIONS:
    
        INTERNET: ResourceDescription = ResourceDescription(
            "77.88.55.242", "Интернет соединение")
        
        VPN_PACS_SPB: ResourceDescription = ResourceDescription(
            "192.168.5.3", "VPN соединение для PACS SPB", (2, 100, 5))
        PACS_SPB: ResourceDescription = ResourceDescription(
            "10.76.12.124:4242", "Соединение PACS SPB", (2, 100, 5))

        POLIBASE: ResourceDescription = ResourceDescription("polibase", "Polibase", inaccessibility_check_values=(2, 10000, 15))

        SITE_LIST: list[SiteResourceDescription] = [
            SiteResourceDescription(
                        CONST.SITE_ADDRESS, f"Сайт компании: {CONST.SITE_ADDRESS}", check_certificate_status=True, check_free_space_status=False),
            SiteResourceDescription(CONST.MAIL_ADDRESS,
                        f"Сайт корпоративной почты: {CONST.MAIL_ADDRESS}", check_certificate_status=True, check_free_space_status=True, driver_name="/dev/mapper/centos_tenant26--02-var"),
            SiteResourceDescription(CONST.API_SITE_ADDRESS,
                                    f"Api сайта {CONST.SITE_ADDRESS}: {CONST.API_SITE_ADDRESS}", check_certificate_status=True, check_free_space_status=False),
            SiteResourceDescription(CONST.BITRIX_SITE_URL, f"Сайт Битрикс ЦМРТ24: {CONST.BITRIX_SITE_URL}")
        ]
    
    class INACCESSABLE_REASON(Enum):

        SERTIFICATE_ERROR: str = "Ошибка проверки сертификата"

class MEDICAl_DOCUMENT:

    class DIRECTION_TYPES(Enum):
            
        MRI: MedicalDirectionDescription = MedicalDirectionDescription(("Магнитно-резонансная томография", ), "МРТ")
        CT: MedicalDirectionDescription = MedicalDirectionDescription(("Компьютерная томография", ), "КТ")
        ULTRASOUND: MedicalDirectionDescription = MedicalDirectionDescription(("ультразвуковая допплерография", ), "УЗИ")

class CheckableSections(Enum):

    RESOURCES: int = auto()
    WS: int = auto()
    PRINTER: int = auto()
    INDICATIONS: int = auto()
    BACKUPS: int = auto()

    @staticmethod
    def all() :
        return [item for item in CheckableSections]

class PATH_SHARE:

    NAME: str = "shares"
    PATH: str = os.path.join(AD.PATH_ROOT, NAME)

class PATH_SCAN:
    
    NAME: str = "scan"
    VALUE: str = os.path.join(AD.PATH_ROOT, NAME)

class PATH_SCAN_TEST:
    
    NAME: str = "test"
    VALUE: str = os.path.join(PATH_SCAN.VALUE, NAME)


class PATH_WS_816_SCAN:
    
    NAME: str = r"C$\Users\Nurse\Documents\Scanned Documents"
    VALUE: str = os.path.join(r"\\", HOSTS.WS816.NAME, NAME)

class PATH_OMS:
    
    NAME: str = "oms"
    VALUE: str = os.path.join(AD.PATH_ROOT, NAME)

class PATH_IT:

    NAME: str = "5. IT"
    NEW_EMPLOYEES_NAME: str = "New employees"
    ROOT: str = os.path.join(PATH_SHARE.PATH, NAME)

    @staticmethod
    def NEW_EMPLOYEE(name: str) -> str:
        return os.path.join(os.path.join(PATH_IT.ROOT, PATH_IT.NEW_EMPLOYEES_NAME), name)

class PATH_APP:

    NAME: str = "apps"
    FOLDER: str = os.path.join(CONST.FACADE.PATH, NAME)

class PATH_DOCS:
    
    NAME: str = f"Docs{CONST.FACADE.SERVICE_FOLDER_SUFFIX}"
    FOLDER: str = os.path.join(CONST.FACADE.PATH, NAME)

class PATH_FONTS:

    NAME: str = "fonts"
    FOLDER: str = os.path.join(PATH_DOCS.FOLDER, NAME)

    @staticmethod
    def get(name: str) -> str:
        from pih.tools import PathTool
        return os.path.join(PATH_FONTS.FOLDER, PathTool.add_extension(name, FILE.EXTENSION.TRUE_TYPE_FONT))

class PATH_APP_DATA:

    NAME: str = "data"
    FOLDER: str = os.path.join(PATH_APP.FOLDER, NAME)

    OCR_RESULT_NAME: str = "ocr result"
    OCR_RESULT_FOLDER: str =  os.path.join(FOLDER, OCR_RESULT_NAME)

class PATH_MOBILE_HELPER:

    NAME: str = "mobile helper"
    FOLDER: str = os.path.join(PATH_APP_DATA.FOLDER, NAME)

    QR_CODE_NAME: str = "qr code"
    QR_CODE_FOLDER: str =  os.path.join(FOLDER, QR_CODE_NAME)

    INCOME_IMAGES_NAME: str = "income images"
    INCOME_IMAGES_FOLDER: str =  os.path.join(FOLDER, INCOME_IMAGES_NAME)


class PATH_POLIBASE_APP_DATA:
    
    NAME: str = "polibase"
    FOLDER: str = os.path.join(PATH_APP_DATA.FOLDER, NAME)
    PERSON_CARD_FOLDER: str = os.path.join(FOLDER, "person card folder")

    SERVICE_FOLDER_PATH: str = os.path.join(CONST.FACADE.PATH, f"{NAME}{CONST.FACADE.SERVICE_FOLDER_SUFFIX}")
    
    class SETTINGS:
        MAIN: str = "polibase_main_settings.vbs"
        TEST: str = "polibase_test_settings.vbs"

class PATH_USER:

    NAME: str = "homes"
    HOME_FOLDER: str = os.path.join(AD.PATH_ROOT, NAME)
    HOME_FOLDER_FULL: str = os.path.join(AD.PATH_ROOT, NAME)

    @staticmethod
    def private_folder(login: str) -> str:
        return os.path.join(PATH_USER.HOME_FOLDER, login)

    @staticmethod
    def get_document_name(user_name: str, login: str = None) -> str:
        return PATH_IT.NEW_EMPLOYEE(user_name) + (f" ({login})" if login else "") + ".docx"

class PATH_POLIBASE:
    
    NAME: str = CONST.HOST.POLIBASE.NAME
    TEST_SUFFIX: str = "_test"
    PERSON_CARD_FOLDER: str = PATH_POLIBASE_APP_DATA.PERSON_CARD_FOLDER

    @staticmethod
    def get_person_folder(pin: int, test: bool = False) -> str:
        root: str = PATH_POLIBASE.NAME
        if test:
            if root.find(".") != -1:
                root_parts: list = root.split(".")
                root_parts[0] += PATH_POLIBASE.TEST_SUFFIX
                root = ".".join(root_parts)
            else:
                root += PATH_POLIBASE.TEST_SUFFIX
        return os.path.join(os.path.join(f"//{root}", "polibaseData", "PERSONS"), str(pin))

class PATH_WS:

    NAME: str = f"WS{CONST.FACADE.SERVICE_FOLDER_SUFFIX}"
    PATH: str = os.path.join(CONST.FACADE.PATH, NAME)


class PATH_BACKUP:

    class ROBOCOPY_CONFIG:

        NAME: str = "robocopy_config"
        ROOT: str = os.path.join(CONST.FACADE.PATH, f"Backup{CONST.FACADE.SERVICE_FOLDER_SUFFIX}", NAME)
    

class PATHS:

    SHARE: PATH_SHARE = PATH_SHARE()
    SCAN: PATH_SCAN = PATH_SCAN()
    SCAN_TEST = PATH_SCAN_TEST()
    WS_816_SCAN: PATH_WS_816_SCAN = PATH_WS_816_SCAN()
    OMS: PATH_OMS = PATH_OMS()
    IT: PATH_IT = PATH_IT()
    USER: PATH_USER = PATH_USER()
    POLIBASE: PATH_POLIBASE = PATH_POLIBASE()
    POLIBASE_APP_DATA: PATH_POLIBASE_APP_DATA = PATH_POLIBASE_APP_DATA()
    WS: PATH_WS = PATH_WS()
    BACKUP: PATH_BACKUP = PATH_BACKUP()
    DOCS: PATH_DOCS = PATH_DOCS()
    FONTS: PATH_FONTS = PATH_FONTS()
    MOBILE_HELPER: PATH_MOBILE_HELPER = PATH_MOBILE_HELPER()
    APP_DATA: PATH_APP_DATA = PATH_APP_DATA()

class MarkType(Enum):

    NORMAL: int = auto()
    FREE: int = auto()
    GUEST: int = auto()
    TEMPORARY: int = auto()

class FIELD_NAME_COLLECTION:

    FULL_NAME: str = "FullName"
    TYPE: str = "type"
    GROUP_NAME: str = "GroupName"
    GROUP_ID: str = "GroupID"
    COMMENT: str = "Comment"
    CARD_FOLDER: str = "ChartFolder"
    BIRTH: str = "Birth"
    TAB_NUMBER: str = "TabNumber"
    OWNER_TAB_NUMBER: str = "OwnerTabNumber"
    NAME: str = USER_PROPERTY.NAME
    MIDNAME: str = "MidName"
    PERSON_ID: str = "pID"
    MARK_ID: str = "mID"
    ID: str = "id"
    PIN: str = "pin"
    VISIT_ID: str = "visitID"
    MESSAGE_ID: str = "messageID"
    VALUE: str = "value"
    FILE: str = "file"
    DIVISION_NAME: str = "DivisionName"
    BARCODE: str = "barcode"
    PROPERTIES: str = "properties"
    MESSAGE: str = "message"
    STATUS: str = "status"
    FEEDBACK_CALL_STATUS: str = "feedbackCallStatus"
    REGISTRATION_DATE: str = "registrationDate"
    TYPE: str = "type"
    CABINET_ID: str = "cabinetID"
    DOCTOR_ID: str = "doctorID"
    DOCTOR_FULL_NAME: str = "doctorFullName"
    SERVICE_GROUP_ID: str = "serviceGroupID"
    PORT_NAME: str = "portName"
    TEMPERATURE: str = "temperature"
    HUMIDITY: str = "humidity"

    SEARCH_ATTRIBUTE_LOGIN: str = USER_PROPERTY.LOGIN
    SEARCH_ATTRIBUTE_NAME: str = USER_PROPERTY.NAME

    TELEPHONE_NUMBER: str = USER_PROPERTY.TELEPHONE_NUMBER
    EMAIL: str = USER_PROPERTY.EMAIL
    DN: str = USER_PROPERTY.DN
    LOGIN: str = USER_PROPERTY.LOGIN
    DESCRIPTION: str = USER_PROPERTY.DESCRIPTION
    PASSWORD: str = USER_PROPERTY.PASSWORD
    ACCESSABLE: str = "accessable"
    STEP: str = "step"
    STEP_CONFIRMED: str = "stepConfirmed"
    GRADE: str = "grade"
    INFORMATION_WAY: str = "informationWay"
    TIME: str = "time"

    TIMESTAMP: str = "timestamp"
    DATE: str = "date"
    BEGIN_DATE: str = "beginDate"
    COMPLETE_DATE: str = "completeDate"
    RECIPIENT: str = "recipient"
    SENDER: str = "sender"
    TYPE: str = "type"
    ANSWER: str = "answer"
    STATE: str = "state"

    INVENTORY_NUMBER: str = "inventory_number"
    QUANTITY: str = "quantity"
    ROW: str = "row"
    NAME_COLUMN: str = "name_column"
    INVENTORY_NUMBER_COLUMN: str = "inventory_number_column"
    QUANTITY_COLUMN: str = "quantity_column"

    TEMPLATE_USER_CONTAINER: str = "templated_user"
    CONTAINER: str = "container"

    REMOVE: str = "remove"
    AS_FREE: str = "as_free"
    CANCEL: str = "cancel"


class FIELD_ITEM_COLLECTION:

    TAB_NUMBER: FieldItem = FieldItem(
        FIELD_NAME_COLLECTION.TAB_NUMBER, "Табельный номер")
    OWNER_TAB_NUMBER: FieldItem = FieldItem(
        FIELD_NAME_COLLECTION.OWNER_TAB_NUMBER, "Табельный номер владельца")
    FULL_NAME: FieldItem = FieldItem(
        FIELD_NAME_COLLECTION.FULL_NAME, "Полное имя")
    

class FIELD_COLLECTION:

    INDEX: FieldItem = FieldItem("__Index__", "Индекс", True)
    POSITION: FieldItem = FieldItem("position", "Позиция", True, default_value="Нет")

    VALUE: FieldItem = FieldItem("", "Значение", True)
    VALUE_LIST: FieldItem = FieldItem("", "Список значений", True)

    class ORION:

        MARK_ACTION: FieldItemList = FieldItemList(
            FieldItem(FIELD_NAME_COLLECTION.REMOVE, "Удалить"),
            FieldItem(FIELD_NAME_COLLECTION.AS_FREE, "Сделать свободной"),
            FieldItem(FIELD_NAME_COLLECTION.CANCEL, "Оставить")
        )

        GROUP_BASE: FieldItemList = FieldItemList(
            FieldItem(FIELD_NAME_COLLECTION.GROUP_NAME, "Группа доступа"),
            FieldItem(FIELD_NAME_COLLECTION.COMMENT, "Описание", False)
        )

        TAB_NUMBER_BASE: FieldItemList = FieldItemList(
            FIELD_ITEM_COLLECTION.TAB_NUMBER)

        FREE_MARK: FieldItemList = FieldItemList(
            TAB_NUMBER_BASE, GROUP_BASE)

        TAB_NUMBER: FieldItemList = FieldItemList(
            TAB_NUMBER_BASE,
            FieldItem(FIELD_NAME_COLLECTION.DIVISION_NAME, "Подразделение", default_value="Без подразделения"),
            GROUP_BASE).position(FIELD_NAME_COLLECTION.DIVISION_NAME, 2)

        TEMPORARY_MARK: FieldItemList = FieldItemList(
            FIELD_ITEM_COLLECTION.TAB_NUMBER,
            FIELD_ITEM_COLLECTION.OWNER_TAB_NUMBER,
            FIELD_ITEM_COLLECTION.FULL_NAME,
            FieldItem(FIELD_NAME_COLLECTION.PERSON_ID, "Person ID", False),
            FieldItem(FIELD_NAME_COLLECTION.MARK_ID, "Mark ID", False)
        )

        PERSON: FieldItemList = FieldItemList(
            TAB_NUMBER,
            FieldItem(FIELD_NAME_COLLECTION.TELEPHONE_NUMBER,
                      "Телефон", True),
            FIELD_ITEM_COLLECTION.FULL_NAME
        ).position(FIELD_NAME_COLLECTION.FULL_NAME, 1).position(FIELD_NAME_COLLECTION.TELEPHONE_NUMBER, 2)

        PERSON_DIVISION: FieldItemList = FieldItemList(
            FieldItem(FIELD_NAME_COLLECTION.ID, "ID", False),
            FieldItem(FIELD_NAME_COLLECTION.NAME, "Название подразделения")
        )

        PERSON_EXTENDED: FieldItemList = FieldItemList(
            PERSON,
            FieldItem(FIELD_NAME_COLLECTION.PERSON_ID, "Person ID", False),
            FieldItem(FIELD_NAME_COLLECTION.MARK_ID, "Mark ID", False)
        )

        GROUP: FieldItemList = FieldItemList(
            GROUP_BASE,
            FieldItem(FIELD_NAME_COLLECTION.GROUP_ID, "Group id", False)
        ).visible(FIELD_NAME_COLLECTION.COMMENT, True)

        GROUP_STATISTICS: FieldItemList = FieldItemList(
            GROUP,
            FieldItem("Count", "Количество"),
        ).visible(FIELD_NAME_COLLECTION.COMMENT, False)

        TIME_TRACKING: FieldItemList = FieldItemList(FIELD_ITEM_COLLECTION.FULL_NAME,
                                                     FIELD_ITEM_COLLECTION.TAB_NUMBER,
                                                     FieldItem(
                                                         "TimeVal", "Время"),
                                                     FieldItem(
                                                         "Remark", "Remark"),
                                                     FieldItem(
                                                         "Mode", "Mode"))

        TIME_TRACKING_RESULT: FieldItemList = FieldItemList(
            FIELD_ITEM_COLLECTION.FULL_NAME,
            FIELD_ITEM_COLLECTION.TAB_NUMBER,
            FieldItem(
                "Date", "Дата"),
            FieldItem(
                "EnterTime", "Время прихода"),
            FieldItem(
                "ExitTime", "Время ухода"),
            FieldItem(
                "Duration", "Продолжительность"))

    class INRENTORY:

        ITEM: FieldItemList = FieldItemList(
            FieldItem(FIELD_NAME_COLLECTION.NAME,
                      "Название инвентарного объекта"),
            FieldItem(FIELD_NAME_COLLECTION.INVENTORY_NUMBER,
                      "Инвентарный номер"),
            FieldItem(FIELD_NAME_COLLECTION.QUANTITY, "Количество"),
            FieldItem(FIELD_NAME_COLLECTION.NAME_COLUMN, None, False),
            FieldItem(FIELD_NAME_COLLECTION.INVENTORY_NUMBER_COLUMN, None, False),
            FieldItem(FIELD_NAME_COLLECTION.QUANTITY_COLUMN, None, False)
        )

    class AD:

        WORKSTATION: FieldItemList = FieldItemList(
            FieldItem(FIELD_NAME_COLLECTION.NAME, "Имя компьютера"),
            FieldItem(FIELD_NAME_COLLECTION.DESCRIPTION, "Описание"),
            FieldItem(FIELD_NAME_COLLECTION.PROPERTIES, "Свойства", visible=False)
        )

        USER_ACTION: FieldItemList = FieldItemList(
            FieldItem(USER_PROPERTY.TELEPHONE_NUMBER, "Изменить номер телефона"),
            FieldItem(USER_PROPERTY.PASSWORD, "Изменить пароль"),
            FieldItem(USER_PROPERTY.USER_STATUS, "Активировать или деактивировать")
        )


        USER_WORKSTATION: FieldItemList = FieldItemList(
            WORKSTATION,
            FieldItem(FIELD_NAME_COLLECTION.ACCESSABLE, "Доступен"),
            FieldItem(FIELD_NAME_COLLECTION.LOGIN, "Имя залогированного пользователя")
        )

        SEARCH_ATTRIBUTE: FieldItemList = FieldItemList(
            FieldItem(FIELD_NAME_COLLECTION.SEARCH_ATTRIBUTE_LOGIN, "Логин"),
            FieldItem(FIELD_NAME_COLLECTION.SEARCH_ATTRIBUTE_NAME, "Имя")
        )

        CONTAINER: FieldItemList = FieldItemList(
            FieldItem(FIELD_NAME_COLLECTION.NAME, "Название"),
            FieldItem(FIELD_NAME_COLLECTION.DESCRIPTION, "Описание")
        )

        USER_NAME: FieldItemList = FieldItemList(
            FieldItem(FIELD_NAME_COLLECTION.NAME, "Полное имя пользователя")
        )

        TEMPLATED_USER: FieldItemList = FieldItemList(
            FieldItem(FIELD_NAME_COLLECTION.DESCRIPTION, "Описание"))

        USER: FieldItemList = FieldItemList(CONTAINER,
                                            FieldItem(FIELD_NAME_COLLECTION.LOGIN, "Логин"),
                                            FieldItem(FIELD_NAME_COLLECTION.TELEPHONE_NUMBER, "Телефон"),
                                            FieldItem(FIELD_NAME_COLLECTION.EMAIL, "Электронная почта"),
                                            FieldItem(FIELD_NAME_COLLECTION.DN, "Размещение"),
                                            FieldItem("userAccountControl", "Свойства аккаунта", False)).position(FIELD_NAME_COLLECTION.DESCRIPTION, 4).caption(FIELD_NAME_COLLECTION.NAME, USER_NAME.get_item_by_name(FIELD_NAME_COLLECTION.NAME).caption)

        CONTAINER_TYPE: FieldItemList = FieldItemList(
            FieldItem(FIELD_NAME_COLLECTION.TEMPLATE_USER_CONTAINER,
                      "Шаблонный пользователь"),
            FieldItem(FIELD_NAME_COLLECTION.CONTAINER, "Контейнер"))


    class POLIBASE:

        PERSON_BASE: FieldItemList = FieldItemList(FieldItem(FIELD_NAME_COLLECTION.PIN, "Номер пациента"),
                                              FieldItem(FIELD_NAME_COLLECTION.FULL_NAME, "ФИО пациента"),
                                              FieldItem(FIELD_NAME_COLLECTION.TELEPHONE_NUMBER, "Телефон"))

        PERSON_VISIT: FieldItemList = FieldItemList(PERSON_BASE,
                                              FieldItem(FIELD_NAME_COLLECTION.REGISTRATION_DATE, "Дата регистрации"),
                                              FieldItem(FIELD_NAME_COLLECTION.DOCTOR_FULL_NAME, "Имя доктора"))

        PERSON: FieldItemList = FieldItemList(PERSON_BASE,
                                              FieldItem(FIELD_NAME_COLLECTION.BIRTH, "День рождения", True, "datetime"),
                                              FieldItem(FIELD_NAME_COLLECTION.EMAIL, "Электронная почта"),
                                              FieldItem(FIELD_NAME_COLLECTION.CARD_FOLDER, "Папка карты пациента", default_value="Нет папки"),
                                              FieldItem(FIELD_NAME_COLLECTION.COMMENT, "Комментарий"))


    class POLICY:

        PASSWORD_TYPE: FieldItemList = FieldItemList(
            #FieldItem("EMAIL", "Для почты"),
            #FieldItem("SIMPLE", "Простой"),
            FieldItem("NORMAL", "Стандартный"),
            FieldItem("STRONG", "Сложный"))

    class PRINTER:

        MAIN: FieldItemList = FieldItemList(
            FieldItem(FIELD_NAME_COLLECTION.NAME, "Name"),
            FieldItem("serverName", "Server name"),
            FieldItem(FIELD_NAME_COLLECTION.PORT_NAME, "Host name"),
            FieldItem(FIELD_NAME_COLLECTION.DESCRIPTION, "Description"),
            FieldItem("adminDescription", "Admin description", False),
            FieldItem("driverName", "Driver name")
        )

    class INDICATIONS:

        CT: FieldItemList = FieldItemList(
            FieldItem(FIELD_NAME_COLLECTION.TEMPERATURE, "Температура", data_formatter="{data}°C"),
            FieldItem(FIELD_NAME_COLLECTION.HUMIDITY, "Влажность", data_formatter="{data}%")
        )

        CT_WITH_TIMESTAMP: FieldItemList = FieldItemList(CT,
                                              FieldItem(FIELD_NAME_COLLECTION.TIMESTAMP, "Время измерения", data_formatter=f"{DATA.FORMATTER.MY_DATETIME}"))


class FIELD_COLLECTION_ALIAS(Enum):
    TIME_TRACKING: FieldItem = FIELD_COLLECTION.ORION.TIME_TRACKING
    PERSON: FieldItem = FIELD_COLLECTION.ORION.PERSON
    TEMPORARY_MARK: FieldItem = FIELD_COLLECTION.ORION.TEMPORARY_MARK
    POLIBASE_PERSON: FieldItem = FIELD_COLLECTION.POLIBASE.PERSON
    POLIBASE_PERSON_VISIT: FieldItem = FIELD_COLLECTION.POLIBASE.PERSON_VISIT
    PERSON_DIVISION: FieldItem = FIELD_COLLECTION.ORION.PERSON_DIVISION
    PERSON_EXTENDED: FieldItem = FIELD_COLLECTION.ORION.PERSON_EXTENDED
    WORKSTATION: FieldItem = FIELD_COLLECTION.AD.WORKSTATION
    USER_WORKSTATION: FieldItem = FIELD_COLLECTION.AD.USER_WORKSTATION
    VALUE: FieldItem = FIELD_COLLECTION.VALUE
    VALUE_LIST: FieldItem = FIELD_COLLECTION.VALUE_LIST


class PolibasePersonInformationQuestStatus(Enum):
    UNKNOWN: int = -1
    GOOD: int = 0
    EMAIL_IS_EMPTY: int = 1
    EMAIL_IS_WRONG: int = 2
    EMAIL_IS_NOT_ACCESSABLE: int = 4


class PolibasePersonVisitNotificationType(Enum):
    GREETING: int = auto()
    REMINDER: int = auto()
    DEFAULT: int = auto()

class PolibasePersonReviewQuestStep(Enum):
    BEGIN: int = auto()
    #
    ASK_GRADE: int = auto()
    ASK_FEEDBACK_CALL: int = auto()
    ASK_INFORMATION_WAY: int = auto()
    #
    COMPLETE: int = auto()

LINK_EXT = "lnk"

class PrinterCommands(Enum):
    REPORT: str = "report"
    STATUS: str = "status"


class PASSWORD_GENERATION_ORDER:

    SPECIAL_CHARACTER: str = "s"
    LOWERCASE_ALPHABET: str = "a"
    UPPERCASE_ALPHABET: str = "A"
    DIGIT: str = "d"
    DEFAULT_ORDER_LIST: list[str] = [SPECIAL_CHARACTER,
                                     LOWERCASE_ALPHABET, UPPERCASE_ALPHABET, DIGIT]


class PASSWORD:

    class SETTINGS:

        SIMPLE: PasswordSettings = PasswordSettings(
            3, "", PASSWORD_GENERATION_ORDER.DEFAULT_ORDER_LIST, 0, 3, 0, 0, False)
        NORMAL: PasswordSettings = PasswordSettings(
            8, "!@#", PASSWORD_GENERATION_ORDER.DEFAULT_ORDER_LIST, 3, 3, 1, 1, False)
        STRONG: PasswordSettings = PasswordSettings(
            10, "#%+\-!=@()_",  PASSWORD_GENERATION_ORDER.DEFAULT_ORDER_LIST, 3, 3, 2, 2, True)
        DEFAULT: PasswordSettings = NORMAL
        PC: PasswordSettings = NORMAL
        EMAIL: PasswordSettings = NORMAL

    def get(name: str) -> SETTINGS:
        return PASSWORD.__getattribute__(PASSWORD.SETTINGS, name)


class LogTypes(Enum):
    MESSAGE: str = "message"
    COMMAND: str = "command"
    DEFAULT: str = MESSAGE


class LogChannels(Enum):
    BACKUP: int = auto()
    NOTIFICATION: int = auto()
    NOTIFICATION_BOT: int = auto()
    DEBUG: int = auto()
    DEBUG_BOT: int = auto()
    SERVICE: int = auto()
    SERVICE_BOT: int = auto()
    HR: int = auto()
    HR_BOT: int = auto()
    IT: int = auto()
    IT_BOT: int = auto()
    POLIBASE_PERSON_FEEDBACK_CALL: int = auto()
    POLIBASE_PERSON_REVIEW_QUEST_RESULT: int = auto()
    RESOURCES: int = auto()
    RESOURCES_BOT: int = auto() 
    PRINTER: int = auto()
    DEFAULT: int = NOTIFICATION


class LogLevels(Enum):
    NORMAL: int = 1
    ERROR: int = 2
    EVENT: int = 4
    DEBUG: str = 8
    TASK: int = 16
    NOTIFICATION: str = 32
    SILENCE: str = 4048
    DEFAULT: str = NORMAL


class ServiceCommands(Enum):
    ping: int = auto()
    subscribe: int = auto()
    unsubscribe: int = auto()
    unsubscribe_all: int = auto()
    stop: int = auto()
    #Log
    send_log_message: int = auto()
    send_log_command: int = auto()
    send_message_to_user_or_workstation: int = auto()
    add_message_to_queue: int = auto()
    send_delayed_message: int = auto()
    #Documents
    create_user_document: int = auto()
    save_time_tracking_report: int = auto()
    create_barcodes_for_inventory: int = auto()
    create_barcode_for_polibase_person: int = auto()
    create_qr_code: int = auto()
    check_inventory_report: int = auto()
    get_inventory_report: int = auto()
    save_inventory_report_item: int = auto()
    close_inventory_report: int = auto()
    #Polibase
    get_polibase_person_by_pin: int = auto()
    get_polibase_persons_by_pin: int = auto()
    get_polibase_persons_by_card_registry_folder_name: int = auto() 
    get_polibase_persons_by_full_name: int = auto()
    get_polibase_person_pin_list_with_old_format_barcode: int = auto()
    get_polibase_person_registrator_by_pin: int = auto()
    get_polibase_persons_pin_by_visit_date: int = auto()
    get_polibase_persons_by_telephone_number: int = auto()
    #
    get_polibase_person_visits_last_id: int = auto()
    search_polibase_person_visits: int = auto()
    #
    set_polibase_person_card_folder_name: int = auto()
    set_polibase_person_email: int = auto()
    set_polibase_person_barcode_by_pin: int = auto()
    check_polibase_person_card_registry_folder_name: int = auto()

    #ActiveDirectory
    check_user_exists_by_login: int = auto()
    get_user_by_full_name: int = auto()
    get_users_by_name: int = auto()
    #get_active_users_by_name: int = auto()
    get_user_by_login: int = auto()
    get_user_by_telephone_number: int = auto()
    get_template_users: int = auto()
    get_containers: int = auto()
    get_users_by_job_position: int = auto()
    get_users_by_group: int = auto()
    create_user_by_template: int = auto()
    create_user_in_container: int = auto()
    set_user_telephone: int = auto()
    authenticate: int = auto()
    set_user_password: int = auto()
    set_user_status: int = auto()
    get_printers: int = auto()
    remove_user: int = auto()
    get_all_workstation_description: int = auto()
    get_all_workstations: int = auto()
    get_workstation_by_user: int = auto()
    get_user_by_workstation: int = auto()
    #Printer
    printers_report: int = auto()
    printers_status: int = auto()
    #Orion
    get_free_marks: int = auto()
    get_temporary_marks: int = auto()
    get_person_divisions: int = auto()
    get_time_tracking: int = auto() 
    get_all_persons: int = auto()
    get_owner_mark_for_temporary_mark: int = auto()
    get_mark_by_tab_number: int = auto()
    get_mark_by_person_name: int = auto()
    get_free_marks_group_statistics: int = auto()
    get_free_marks_by_group_id: int = auto()
    set_full_name_by_tab_number: int = auto()
    set_telephone_by_tab_number: int = auto()
    check_mark_free: int = auto()
    create_mark: int = auto()
    remove_mark_by_tab_number: int = auto()
    make_mark_as_free_by_tab_number: int = auto()
    make_mark_as_temporary: int = auto()
    #PolibaseDatabaseBackup
    create_polibase_database_backup: int = auto()
    #DataStorage::Settings
    set_settings_value: int = auto()
    get_settings_value: int = auto()
    #HeatBeat
    heat_beat: int = auto()
    #Notifier
    register_polibase_person_information_quest: int = auto()
    search_polibase_person_information_quests: int = auto()
    update_polibase_person_information_quest: int = auto()
    #Visit Cached
    update_polibase_person_visit_to_data_stogare: int = auto()
    search_polibase_person_visits_in_data_storage: int = auto()
    #Visit notification
    register_polibase_person_visit_notification: int = auto()
    search_polibase_person_visit_notifications: int = auto()
    #Notification confirmation
    search_polibase_person_notification_confirmation: int = auto()
    update_polibase_person_notification_confirmation: int = auto()
    #
    check_email_accessibility: int = auto()
    #
    register_delayed_message: int = auto()
    search_delayed_messages: int = auto()
    update_delayed_message: int = auto()
    #WORKSTATION
    reboot: int = auto()
    shutdown: int = auto()
    log_out: int = auto()
    #Robocopy::Job
    robocopy_start_job: int = auto()
    robocopy_get_job_status_list: int = auto()
    #DataStorage::Storage value
    set_storage_value: int = auto()
    get_storage_value: int = auto()
    #Resource Manager
    get_resource_status_list: int = auto()
    send_mobile_helper_message: int = auto()

    register_ct_indications_value: int = auto()
    get_last_ct_indications_value_list: int = auto()
    #
    test: int = auto()
    #
    execute_ssh_command: int = auto()
    get_certificate_information: int = auto()
    get_unix_free_space_information_by_drive_name: int = auto()
    print_image: int = auto()
    #
    get_ogrn_value: int = auto()
    get_fms_unit_name: int = auto()
    #
    start_polibase_person_information_quest: int = auto()

    

class ServiceRoles(Enum):

    LOG: ServiceRoleDescription = ServiceRoleDescription(
                                            name="Log",
                                            description="Log service",
                                            host=CONST.HOST.BACKUP_WORKER.NAME, 
                                            port=CONST.RPC.PORT(),
                                            commands=[
                                                        ServiceCommands.send_log_message,
                                                        ServiceCommands.send_log_command
                                                     ],
                                            modules=["telegram-send"])

    HEART_BEAT: ServiceRoleDescription = ServiceRoleDescription(
        name="HeartBeat",
        description="Heart beat service",
        host=CONST.HOST.WS255.NAME,
        port=CONST.RPC.PORT(),
        commands=[
            ServiceCommands.heat_beat
        ],
        modules=["schedule"])

    INDICATIONS: ServiceRoleDescription = ServiceRoleDescription(
        name="Indications",
        description="Indications service",
        host=CONST.HOST.WS255.NAME,
        commands=[ServiceCommands.register_ct_indications_value,
                  ServiceCommands.get_last_ct_indications_value_list
                  ],
        port=CONST.RPC.PORT(5),
        modules=["fastapi", "uvicorn"]
    )

    DATA_STORAGE: ServiceRoleDescription = ServiceRoleDescription(
                                            name="DataStorage",
                                            description="DataStorage service", 
                                            host=CONST.HOST.BACKUP_WORKER.NAME, 
                                            port=CONST.RPC.PORT(1),
                                            commands=[
                                                        ServiceCommands.register_polibase_person_information_quest,
                                                        ServiceCommands.search_polibase_person_information_quests,
                                                        ServiceCommands.update_polibase_person_information_quest,
                                                        #
                                                        ServiceCommands.update_polibase_person_visit_to_data_stogare,
                                                        ServiceCommands.search_polibase_person_visits_in_data_storage,
                                                        #
                                                        ServiceCommands.register_polibase_person_visit_notification,
                                                        ServiceCommands.search_polibase_person_visit_notifications,
                                                        #
                                                        ServiceCommands.register_delayed_message,
                                                        ServiceCommands.search_delayed_messages,
                                                        ServiceCommands.update_delayed_message,
                                                        #
                                                        ServiceCommands.get_settings_value,
                                                        ServiceCommands.set_settings_value,
                                                        #
                                                        ServiceCommands.search_polibase_person_notification_confirmation,
                                                        ServiceCommands.update_polibase_person_notification_confirmation,
                                                        #
                                                        ServiceCommands.get_storage_value,
                                                        ServiceCommands.set_storage_value,
                                                        #
                                                        ServiceCommands.get_ogrn_value,
                                                        ServiceCommands.get_fms_unit_name
                                                    ],
                                            modules=["mysql-connector-python", "pysos", "lmdbm", "dadata"])

    FILE_WATCHDOG: ServiceRoleDescription = ServiceRoleDescription(
        name="FileWatchdog",
        description="FileWatchdog service",
        host=CONST.HOST.BACKUP_WORKER.NAME,
        port=CONST.RPC.PORT(2),
        modules=["watchdog"])

    MAIL: ServiceRoleDescription = ServiceRoleDescription(
        name="Mail",
        description="Mail service",
        host=CONST.HOST.BACKUP_WORKER.NAME,
        port=CONST.RPC.PORT(3),
        commands=
                [
                    ServiceCommands.check_email_accessibility
                ],
        modules=["py3-validate-email", "verify-email"])

    WS: ServiceRoleDescription = ServiceRoleDescription(
                                                name="WS",
                                                description="Workstation service",
                                                host=CONST.HOST.BACKUP_WORKER.NAME,
                                                port=CONST.RPC.PORT(4),
                                                commands=[
                                                    ServiceCommands.reboot,
                                                    ServiceCommands.shutdown,
                                                    ServiceCommands.send_message_to_user_or_workstation
                                                ])


    BACKUP: ServiceRoleDescription = ServiceRoleDescription(
                                                name="Backup",
                                                description="Backup service",
                                                host=CONST.HOST.BACKUP_WORKER.NAME,
                                                port=CONST.RPC.PORT(5),
                                                commands=[
                                                    ServiceCommands.robocopy_start_job,
                                                    ServiceCommands.robocopy_get_job_status_list
                                                ])

    AD: ServiceRoleDescription = ServiceRoleDescription(
                                                name="ActiveDirectory",
                                                description="Active directory service",
                                                host=CONST.HOST.DC2.NAME,
                                                port=CONST.RPC.PORT(),
                                                commands=
                                                        [
                                                            ServiceCommands.authenticate,
                                                            ServiceCommands.check_user_exists_by_login,
                                                            ServiceCommands.get_user_by_full_name,
                                                            ServiceCommands.get_users_by_name,
                                                            ServiceCommands.get_user_by_login,
                                                            ServiceCommands.get_user_by_telephone_number,
                                                            ServiceCommands.get_template_users,
                                                            ServiceCommands.get_containers,
                                                            ServiceCommands.get_users_by_job_position,
                                                            ServiceCommands.get_users_by_group, 
                                                            ServiceCommands.get_printers,
                                                            ServiceCommands.get_all_workstation_description,
                                                            ServiceCommands.get_all_workstations,
                                                            ServiceCommands.get_workstation_by_user,
                                                            ServiceCommands.get_user_by_workstation,
                                                            ServiceCommands.create_user_by_template,
                                                            ServiceCommands.create_user_in_container,
                                                            ServiceCommands.set_user_telephone,
                                                            ServiceCommands.set_user_password,
                                                            ServiceCommands.set_user_status,
                                                            ServiceCommands.remove_user
                                                        ],
                                                modules=["pyad", "pywin32", "wmi"]
                                            )

    DOCS: ServiceRoleDescription = ServiceRoleDescription(
                                                name="Docs", 
                                                description="Documents service",
                                                host=CONST.HOST.DC2.NAME,
                                                port=CONST.RPC.PORT(1),
                                                commands=
                                                        [
                                                            ServiceCommands.get_inventory_report,
                                                            ServiceCommands.create_user_document,
                                                            ServiceCommands.save_time_tracking_report,
                                                            ServiceCommands.create_barcodes_for_inventory,
                                                            ServiceCommands.create_barcode_for_polibase_person,
                                                            ServiceCommands.create_qr_code,
                                                            ServiceCommands.check_inventory_report,
                                                            ServiceCommands.save_inventory_report_item,
                                                            ServiceCommands.close_inventory_report,
                                                        ],
        modules=["xlsxwriter", "xlrd", "xlutils", "openpyxl",
                                                    "python-barcode", "Pillow", "transliterate", "qrcode"]
                                            )

    PRINTER: ServiceRoleDescription = ServiceRoleDescription(
                                                    name="Printer",
                                                    description="Printer service", 
                                                    host=CONST.HOST.DC2.NAME, 
                                                    port=CONST.RPC.PORT(2),
                                                    commands=
                                                            [
                                                                ServiceCommands.printers_report,
                                                                ServiceCommands.printers_status
                                                            ]
                                                           )

    MARK: ServiceRoleDescription = ServiceRoleDescription(
                                                name="Orion",
                                                description="Orion service",
                                                host=CONST.HOST.DC2.NAME,
                                                port=CONST.RPC.PORT(3),
                                                commands=
                                                        [
                                                            ServiceCommands.get_free_marks,
                                                            ServiceCommands.get_temporary_marks,
                                                            ServiceCommands.get_person_divisions,
                                                            ServiceCommands.get_time_tracking,
                                                            ServiceCommands.get_all_persons,
                                                            ServiceCommands.get_mark_by_tab_number,
                                                            ServiceCommands.get_mark_by_person_name,
                                                            ServiceCommands.get_free_marks_group_statistics,
                                                            ServiceCommands.get_free_marks_by_group_id,
                                                            ServiceCommands.get_owner_mark_for_temporary_mark,
                                                            ServiceCommands.set_full_name_by_tab_number, 
                                                            ServiceCommands.set_telephone_by_tab_number,
                                                            ServiceCommands.check_mark_free,
                                                            ServiceCommands.create_mark,
                                                            ServiceCommands.make_mark_as_free_by_tab_number,
                                                            ServiceCommands.make_mark_as_temporary,
                                                            ServiceCommands.remove_mark_by_tab_number,
                                                        ],
                                               modules=["pymssql"])

    POLIBASE: ServiceRoleDescription = ServiceRoleDescription(
                                                    name="Polibase",
                                                    description="Polibase service & FastApi server",
                                                    host=CONST.HOST.POLIBASE.NAME,
                                                    port=CONST.RPC.PORT(1),
                                                    commands=[
                                                                ServiceCommands.get_polibase_person_by_pin,
                                                                ServiceCommands.get_polibase_persons_by_pin,
                                                                ServiceCommands.get_polibase_persons_by_telephone_number,
                                                                ServiceCommands.get_polibase_persons_by_full_name,
                                                                ServiceCommands.get_polibase_persons_by_card_registry_folder_name,
                                                                ServiceCommands.get_polibase_person_registrator_by_pin,
                                                                ServiceCommands.get_polibase_person_pin_list_with_old_format_barcode,
                                                                #
                                                                ServiceCommands.get_polibase_persons_pin_by_visit_date,
                                                                #
                                                                ServiceCommands.search_polibase_person_visits,
                                                                ServiceCommands.get_polibase_person_visits_last_id,
                                                                #
                                                                ServiceCommands.set_polibase_person_card_folder_name,
                                                                ServiceCommands.set_polibase_person_email,
                                                                ServiceCommands.set_polibase_person_barcode_by_pin,
                                                                ServiceCommands.check_polibase_person_card_registry_folder_name
                                                            ], 
                                                    modules=["cx-Oracle", "fastapi", "uvicorn", "transliterate"])

    POLIBASE_DATABASE: ServiceRoleDescription = ServiceRoleDescription(
        name="PolibaseDB",
        description="Polibase database api",
        host=CONST.HOST.POLIBASE.NAME,
        port=CONST.RPC.PORT(2),
        commands=[
                    ServiceCommands.create_polibase_database_backup
                ],
        )

    POLIBASE_APP: ServiceRoleDescription = ServiceRoleDescription(
        name="PolibaseApp",
        description="Polibase Application service",
        host=CONST.HOST.POLIBASE.NAME,
        port=CONST.RPC.PORT(3)
        )

    MESSAGE_QUEUE: ServiceRoleDescription = ServiceRoleDescription(
        name="MessageQueue",
        description="Message queue service",
        host=CONST.HOST.BACKUP_WORKER.NAME,
        port=CONST.RPC.PORT(100),
        commands=[
            ServiceCommands.add_message_to_queue
        ]
        )

    POLIBASE_PERSON_NOTIFICATION: ServiceRoleDescription = ServiceRoleDescription(
        name="PolibasePersonNotification",
        description="Polibase Person Notification service",
        host=CONST.HOST.BACKUP_WORKER.NAME,
        port=CONST.RPC.PORT(7)
        )
    
    POLIBASE_PERSON_INFORMATION_QUEST: ServiceRoleDescription = ServiceRoleDescription(
        name="PolibasePersonInformationQuest",
        description="Polibase Person Information Quest service",
        host=CONST.HOST.BACKUP_WORKER.NAME,
        port=CONST.RPC.PORT(10),
         commands=[
            ServiceCommands.start_polibase_person_information_quest
        ]
        )
    
    POLIBASE_PERSON_REVIEW_NOTIFICATION: ServiceRoleDescription = ServiceRoleDescription(
        name="PolibasePersonReviewNotification",
        description="Polibase Person Review Notification service",
        host=CONST.HOST.BACKUP_WORKER.NAME,
        port=CONST.RPC.PORT(11)
        )
    
    MESSAGE_RECEIVER: ServiceRoleDescription = ServiceRoleDescription(
        name="MessageReceiver",
        description="Message service",
        host=CONST.HOST.BACKUP_WORKER.NAME,
        port=CONST.RPC.PORT(101),
        auto_restart=False,
        modules=["fastapi", "uvicorn"])

    SSH: ServiceRoleDescription = ServiceRoleDescription(
        name="SSH",
        description="Ssh service",
        host=CONST.HOST.BACKUP_WORKER.NAME,
        port=CONST.RPC.PORT(9),
        modules=["paramiko"],
        commands=[ServiceCommands.execute_ssh_command,
                  ServiceCommands.get_certificate_information,
                  ServiceCommands.get_unix_free_space_information_by_drive_name]
    )

    WS_735: ServiceRoleDescription = ServiceRoleDescription(
        name="ws_735",
        description="ws-735 service",
        host=CONST.HOST.WS735.NAME,
        port=CONST.RPC.PORT(),
        login="nak",
        password="Soad7623!",
        commands=[ServiceCommands.print_image],
        modules=["pywin32", "Pillow"]
    )

    RECOGNIZE: ServiceRoleDescription = ServiceRoleDescription(
        name="Recognize",
        description="Recognize service",
        host=CONST.HOST.WS255.NAME,
        port=CONST.RPC.PORT(-2)
    )

    RECOGNIZE_TEST: ServiceRoleDescription = ServiceRoleDescription(
        name="RecognizeTest",
        description="Recognize test service",
        host=CONST.HOST.WS255.NAME,
        port=CONST.RPC.PORT(-3),
        auto_start=False,
        auto_restart=False,
        visible_for_admin=False
    )

    CHECKER: ServiceRoleDescription = ServiceRoleDescription(
        name="Checker",
        description="Checker service",
        host=CONST.HOST.BACKUP_WORKER.NAME,
        commands=[ServiceCommands.get_resource_status_list],
        port=CONST.RPC.PORT(8)
    )

    AUTOMATION: ServiceRoleDescription = ServiceRoleDescription(
        name="Automation",
        description="Automation service",
        host=CONST.HOST.WS255.NAME,
        port=CONST.RPC.PORT(-1)
    )

    MOBILE_HELPER: ServiceRoleDescription = ServiceRoleDescription(
        name="MobileHelper",
        description="Mobile helper service",
        host=CONST.HOST.WS255.NAME,
        commands=[ServiceCommands.send_mobile_helper_message],
        port=CONST.RPC.PORT(4)
    )

    DEVELOPER: ServiceRoleDescription = ServiceRoleDescription(
        name="Developer",
        description="Developer service",
        host=CONST.HOST.DEVELOPER.NAME,
        port=CONST.RPC.PORT(1),
        visible_for_admin=False,
        auto_start=False,
        auto_restart=False,
        commands=[ServiceCommands.test]
    )

class SubscribtionTypes:
    BEFORE: int = 1
    AFTER: int = 2

class WorkstationMessageMethodTypes(Enum):

    REMOTE: int = auto()
    LOCAL_MSG: int = auto()
    LOCAL_PSTOOL_MSG: int = auto()

class MessageTypes(Enum):

    WHATSAPP: int = 1
    TELEGRAM: int = 2
    INTERNAL: int = 3


class MessageStatuses(Enum):

    REGISTERED: int = 0
    COMPLETE: int = 1
    AT_WORK: int = 2
    ERROR: int = 3
    ABORT: int = 4

class PolibasePersonVisitStatus:

    CONFIRMED: int = 107
    CANCELED: int = 102

"""
102 - отмена		
99 прошу перенести
101 - пришел			
102 - откзался	
103 - на приеме
104 - окончен
105 - не пришел	
106 - предварительно
107 - подверждено
108 - оказано
109 к оплате
"""

class SETTINGS(Enum):

    VALENTA_SYNCHRONIZATION_TEST: SettingsValue = SettingsValue(None, False)

    CT_TEMPERATURE_CORRECTION: SettingsValue = SettingsValue(None, 0.7)

    HOSPITAL_WORK_DAY_START_TIME: SettingsValue = SettingsValue(None, "8:00")
    HOSPITAL_WORK_DAY_END_TIME: SettingsValue = SettingsValue(None, "20:00")
    OFFICE_WORK_DAY_START_TIME: SettingsValue = SettingsValue(None, "8:30")
    OFFICE_WORK_DAY_END_TIME: SettingsValue = SettingsValue(None, "17:00")


    INDICATION_CT_NOTIFICATION_START_TIME: SettingsValue = SettingsValue(None, ["8:00", "17:00"])

    USER_USE_CACHE: SettingsValue = SettingsValue(None, 1)
    
    POLIBASE_PERSON_INFORMATION_QUEST_IS_ON: SettingsValue = SettingsValue(None, True)
    #
    POLIBASE_PERSON_REVIEW_NOTIFICATION_IS_ON: SettingsValue = SettingsValue(None, True)

    POLIBASE_PERSON_REVIEW_NOTIFICATION_DAY_DELTA: SettingsValue = SettingsValue(None, 1)

    POLIBASE_PERSON_REVIEW_NOTIFICATION_TEXT_FOR_CONFIRMED_NOTIFICATION: SettingsValue = SettingsValue(
        None, CONST.POLIBASE.PERSON_REVIEW_NOTIFICATION_TEXT_FOR_CONFIRMED_NOTIFICATION)

    POLIBASE_PERSON_REVIEW_NOTIFICATION_TEXT: SettingsValue = SettingsValue(
        None, CONST.POLIBASE.PERSON_REVIEW_NOTIFICATION_TEXT)

    POLIBASE_PERSON_REVIEW_NOTIFICATION_START_TIME: SettingsValue = SettingsValue(None, "13:53")
    #
    RESOURCE_MANAGER_CHECK_SITE_CERTIFICATE_START_TIME: SettingsValue = SettingsValue(None, "8:00")
    #
    POLIBASE_CREATION_DB_DUMP_START_TIME: SettingsValue = SettingsValue(None, "20:30")
    #
    RESOURCE_MANAGER_CHECK_SITE_FREE_SPACE_PERIOD_IN_MINUTES: SettingsValue = SettingsValue(None, 15)
    #
    POLIBASE_PERSON_VISIT_GREETING_NOTIFICATION_TEXT_WITHOUT_DATE_FOR_CONFIRMED_NOTIFICATION: SettingsValue = SettingsValue(
        None, CONST.POLIBASE.PERSON_VISIT_GREETING_NOTIFICATION_TEXT_FOR_CONFIRMED_NOTIFICATION + CONST.POLIBASE.SEND_TELEGRAM_BOT_TEXT)

    POLIBASE_PERSON_VISIT_GREETING_NOTIFICATION_TEXT_WITHOUT_DATE: SettingsValue = SettingsValue(
        None, CONST.POLIBASE.PERSON_VISIT_GREETING_NOTIFICATION_TEXT_WITHOUT_TEXT)

    POLIBASE_PERSON_VISIT_GREETING_NOTIFICATION_TEXT_FOR_CONFIRMED_NOTIFICATION: SettingsValue = SettingsValue(
        None,  CONST.POLIBASE.PERSON_VISIT_GREETING_NOTIFICATION_TEXT_FOR_CONFIRMED_NOTIFICATION + CONST.POLIBASE.PERSON_VISIT_NOTIFICATION_WITH_TIME_TEXT + CONST.POLIBASE.SEND_TELEGRAM_BOT_TEXT)
    
    POLIBASE_PERSON_VISIT_GREETING_NOTIFICATION_TEXT: SettingsValue = SettingsValue(
        None,  CONST.POLIBASE.PERSON_VISIT_GREETING_NOTIFICATION_TEXT_BASE + CONST.POLIBASE.PERSON_VISIT_NOTIFICATION_WITH_TIME_TEXT + CONST.POLIBASE.ASK_TO_SEND_TELEGRAM_BOT_URL_TEXT)

    POLIBASE_PERSON_VISIT_NOTIFICATION_TEXT: SettingsValue = SettingsValue(
        None, CONST.POLIBASE.PERSON_VISIT_NOTIFICATION_HEADER + CONST.POLIBASE.PERSON_VISIT_NOTIFICATION_APPOINTMENT_INFORMATION + CONST.POLIBASE.PERSON_VISIT_NOTIFICATION_WITH_TIME_TEXT)

    POLIBASE_PERSON_VISIT_REMINDER_TEXT: SettingsValue = SettingsValue(
        None, CONST.POLIBASE.PERSON_VISIT_NOTIFICATION_HEADER + "*{name}*, напоминаем Вам о записи сегодня {visit_time}. Вы записаны на {appointment_information}." + CONST.POLIBASE.PERSON_VISIT_NOTIFICATION_TEXT_CANCEL_OR_REPLACE_RECEPTION)

    POLIBASE_PERSON_TAKE_TELEGRAM_BOT_URL_TEXT: SettingsValue = SettingsValue(
        None, CONST.POLIBASE.TAKE_TELEGRAM_BOT_URL_TEXT)

    POLIBASE_PERSON_TAKE_REVIEW_ACTION_URL_TEXT: SettingsValue = SettingsValue(
         None, CONST.POLIBASE.TAKE_REVIEW_ACTION_URL_TEXT)

    POLIBASE_PERSON_YES_ANSWER_VARIANTS: SettingsValue = SettingsValue(
        None, CONST.POLIBASE.YES_ANSWER)

    POLIBASE_PERSON_NO_ANSWER_VARIANTS: SettingsValue = SettingsValue(
        None, CONST.POLIBASE.NO_ANSWER)

    POLIBASE_PERSON_NO_ANSWER_ON_NOTIFICATION_CONFIRMATION_TEXT: SettingsValue = SettingsValue(
        None, "Хорошего дня")

    POLIBASE_PERSON_REVIEW_QUEST_WAIT_TIME: SettingsValue = SettingsValue(
        None, 15)
    #
    POLIBASE_PERSON_VISIT_NEED_REGISTER_GREETING_NOTIFICATION: SettingsValue = SettingsValue(
        None, True)
    
    POLIBASE_PERSON_VISIT_NEED_REGISTER_REMINDER_NOTIFICATION: SettingsValue = SettingsValue(
        None, True)
    
    POLIBASE_PERSON_VISIT_TIME_BEFORE_REMINDER_NOTIFICATION_IN_MINUTES: SettingsValue = SettingsValue(
        None, 120)
    
    POLIBASE_PERSON_VISIT_NEED_CONFIRMATION_STATUS_TO_SEND_NOTIFICATION: SettingsValue = SettingsValue(
        None, True)
    
    POLIBASE_PERSON_VISIT_NOTIFICATION_TEST_TELEPHONE_NUMBER: SettingsValue = SettingsValue(
        None, "+79146717744")

    POLIBASE_PERSON_REVIEW_NOTIFICATION_TEST_TELEPHONE_NUMBER: SettingsValue = SettingsValue(
        None, None)
    
    WHATSAPP_SENDING_MESSAGES_VIA_WAPPI_IS_ON: SettingsValue = SettingsValue(
        None, True)
    
    WHATSAPP_BUFFERED_MESSAGE_MIN_DELAY_IN_MILLISECONDS: SettingsValue = SettingsValue(
        None, 6000)
    
    WHATSAPP_BUFFERED_MESSAGE_MAX_DELAY_IN_MILLISECONDS: SettingsValue = SettingsValue(
        None, 12000)
    
    WHATSAPP_MESSAGE_SENDER_USER_LOGIN: SettingsValue = SettingsValue(
        None, "Administrator")  # callCentreAdmin

    MOBILE_HELPER_USER_DATA_INPUT_TIMEOUT: SettingsValue = SettingsValue(
        None, CONST.MOBILE_HELPER.USER_DATA_INPUT_TIMEOUT)
    
    POLIBASE_WAS_EMERGENCY_CLOSED_NOTIFICATION_TEXT: SettingsValue = SettingsValue(
        None, "к сожалениию наш Полибейс поломался и был аварийно закрыт, ожидайте сообщение о просьбе переоткрыть его!")
    
    POLIBASE_WAS_RESTARTED_NOTIFICATION_TEXT: SettingsValue = SettingsValue(
        None, "Полибейс перезагружен, можете переоткрыть его.")
    
    WORKSTATION_SHUTDOWN_TIME: SettingsValue = SettingsValue(None, "21:00")

    WORKSTATION_REBOOT_TIME: SettingsValue = SettingsValue(None, "21:00")


class LogCommands(Enum):

    DEBUG: LogCommandDescription = LogCommandDescription(
        "It is a debug command", LogChannels.NOTIFICATION, LogLevels.DEBUG.value)
        
    PRINTER_REPORT: LogCommandDescription = LogCommandDescription("Принтер {printer_name} ({location}):\n {printer_report}", LogChannels.PRINTER, LogLevels.NORMAL.value, (ParamItem(
        "printer_name", "Name of printer"), ParamItem("location", "Location"), ParamItem("printer_report", "Printer report")))
    #
    LOG_IN: LogCommandDescription = LogCommandDescription(
        "Пользователь {full_name} ({login}) вошел с компьютера {computer_name}", LogChannels.IT, LogLevels.NORMAL.value, (ParamItem("full_name", "Name of user"), ParamItem("login", "Login of user"), ParamItem("computer_name", "Name of computer")))

    SESSION_STARTED: LogCommandDescription = LogCommandDescription(
        "Пользователь {full_name} ({login}) начал пользоваться программой {app_name}.\nВерсия: {version}.\nНазвание компьютера: {computer_name}", LogChannels.IT, LogLevels.NORMAL.value, (ParamItem("full_name", "Name of user"), ParamItem("login", "Login of user"), ParamItem("app_name", "Name of user"),  ParamItem("version", "Version"), ParamItem("computer_name", "Name of computer")))

    SERVICE_STARTS: LogCommandDescription = LogCommandDescription(
        "Сервис {service_name} ({service_description}) запускается!\nИмя хоста: {host_name}\nПорт: {port}\nИдентификатор процесса: {pid}\n", LogChannels.SERVICE, LogLevels.SILENCE.value, (ParamItem("service_name", "Name of service"), ParamItem("service_description", "Description of service"), ParamItem("host_name", "Name of host"), ParamItem("port", "Port"), ParamItem("pid", "PID")))
    
    SERVICE_STARTED: LogCommandDescription = LogCommandDescription(
        "Сервис {service_name} ({service_description}) запущен!\nИмя хоста: {host_name}\nПорт: {port}\nИдентификатор процесса: {pid}\n", LogChannels.SERVICE, LogLevels.NORMAL.value, (ParamItem("service_name", "Name of service"), ParamItem("service_description", "Description of service"), ParamItem("host_name", "Name of host"), ParamItem("port", "Port"), ParamItem("pid", "PID")))
    
    SERVICE_NOT_STARTED: LogCommandDescription = LogCommandDescription(
        "Сервис {service_name} ({service_description}) не запущен!\nИмя хоста: {host_name}\nПорт: {port}\nОшибка:{error}", LogChannels.SERVICE, LogLevels.ERROR.value, (ParamItem("service_name", "Name of service"), ParamItem("service_description", "Description of service"), ParamItem("host_name", "Name of host"), ParamItem("port", "Port"), ParamItem("error", "Error")))

    SERVICE_IS_INACCESIBLE_AND_WAITING_TO_BE_RESTARTED: LogCommandDescription = LogCommandDescription(
        "Сервис {service_name} ({service_description}) недоступен и будет перезапущен!\nИмя хоста: {host_name}\nПорт: {port}\nИдентификатор процесса: {pid}\n", LogChannels.SERVICE, LogLevels.ERROR.value, (ParamItem("service_name", "Name of service"), ParamItem("service_description", "Description of service"), ParamItem("host_name", "Name of host"), ParamItem("port", "Port"), ParamItem("pid", "PID")))
 
    WHATSAPP_MESSAGE_RECEIVED: LogCommandDescription = LogCommandDescription(
        "Получено сообщение", LogChannels.NOTIFICATION, LogLevels.SILENCE.value, (ParamItem("message", "Сообщение"),))
    
    NEW_FILE_DETECTED: LogCommandDescription = LogCommandDescription(
        "Новый файл", LogChannels.IT, LogLevels.SILENCE.value, (ParamItem("path", "Путь к файлу"),))
    
    NEW_POLIBASE_DOCUMENT_DETECTED: LogCommandDescription = LogCommandDescription(
        "Новый Polibase документ", LogChannels.IT, LogLevels.NORMAL.value, (ParamItem("path", "Путь к файлу"), ParamItem("person_pin", "Идентификационный номер пациента"), ParamItem("document_name", "Имя документа")))

    COMPUTER_WAS_STARTED: LogCommandDescription = LogCommandDescription(
        "Компьютер {name} загрузился", LogChannels.IT, LogLevels.NORMAL.value, (ParamItem("name", "Название компьютера"),))
    
    SERVER_WAS_STARTED: LogCommandDescription = LogCommandDescription(
        "Сервер {name} загрузился", LogChannels.IT, LogLevels.NORMAL.value, (ParamItem("name", "Название сервера"),))
    
    RESOURCE_INACCESSABLE: LogCommandDescription = LogCommandDescription(
        "Ресурс {resource_name} недоступен. {reason_string}", LogChannels.RESOURCES, LogLevels.ERROR.value, (ParamItem("resource_name", "Название ресурса"), ParamItem("resource", "Ресурс"), ParamItem("at_first_time", "Признак первого раза"), ParamItem("reason_string", "Строка причины"), ParamItem("reason", "Причины")))
    
    RESOURCE_ACCESSABLE: LogCommandDescription = LogCommandDescription(
        "Ресурс {resource_name} доступен", LogChannels.RESOURCES, LogLevels.NORMAL.value, (ParamItem("resource_name", "Название ресурса"), ParamItem("resource", "Ресурс"), ParamItem("at_first_time", "Признак первого раза")))

    #
    BACKUP_NOTIFY_ABOUT_ROBOCOPY_JOB_STARTED: LogCommandDescription = LogCommandDescription(
        "Robocopy: Начато выполнение задания: {status}", LogChannels.BACKUP, LogLevels.NOTIFICATION.value, (ParamItem("status", ""),))

    BACKUP_NOTIFY_ABOUT_ROBOCOPY_JOB_COMPLETED: LogCommandDescription = LogCommandDescription(
        "Robocopy: Завершено выполнение задания: {status}", LogChannels.BACKUP, LogLevels.NOTIFICATION.value, (ParamItem("status", ""),))
    #
    POLIBASE_CREATION_DB_DUMP_START: LogCommandDescription = LogCommandDescription(
        "Базы данных Polibase: Начато создание дампа",  LogChannels.BACKUP, LogLevels.NORMAL.value)
    
    POLIBASE_CREATION_DB_DUMP_COMPLETE: LogCommandDescription = LogCommandDescription(
        "Базы данных Polibase: Завершено создание дампа",  LogChannels.BACKUP, LogLevels.NORMAL.value)
    
    POLIBASE_CREATION_ARCHIVED_DB_DUMP_START: LogCommandDescription = LogCommandDescription(
        "Базы данных Polibase: Начато архивирование дампа",  LogChannels.BACKUP, LogLevels.NORMAL.value)

    POLIBASE_CREATION_ARCHIVED_DB_DUMP_COMPLETE: LogCommandDescription = LogCommandDescription(
        "Базы данных Polibase: Завершено архивирование дампа",  LogChannels.BACKUP, LogLevels.NORMAL.value)
    
    POLIBASE_COPING_ARCHIVED_DB_DUMP_START: LogCommandDescription = LogCommandDescription(
        "Базы данных Polibase: Начато копирование архивированного дампа на {destination}",  LogChannels.BACKUP, LogLevels.NORMAL.value, (ParamItem(
            "destination", ""),))

    POLIBASE_COPING_ARCHIVED_DB_DUMP_COMPLETE: LogCommandDescription = LogCommandDescription(
        "Базы данных Polibase: Завершено копирование архивированного дампа на {destination}",  LogChannels.BACKUP, LogLevels.NORMAL.value, (ParamItem(
            "destination", ""),))
    
    POLIBASE_COPING_DB_DUMP_START: LogCommandDescription = LogCommandDescription(
        "Базы данных Polibase: Начато копирование дампа на {destination}",  LogChannels.BACKUP, LogLevels.NORMAL.value, (ParamItem(
            "destination", ""),))

    POLIBASE_COPING_DB_DUMP_COMPLETE: LogCommandDescription = LogCommandDescription(
        "Базы данных Polibase: Завершено копирование дампа на {destination}",  LogChannels.BACKUP, LogLevels.NORMAL.value, (ParamItem(
            "destination", ""),))
    #
    HR_NOTIFY_ABOUT_NEW_EMPLOYEE: LogCommandDescription = LogCommandDescription("День добрый, {hr_given_name}.\nДокументы для нового сотрудника: {employee_full_name} готовы!\nЕго корпоративная почта: {employee_email}.", LogChannels.HR, LogLevels.NOTIFICATION.value, (ParamItem(
        "hr_given_name", "Имя руководителя отдела HR"), ParamItem("employee_full_name", "ФИО нового сотрудника"), ParamItem("employee_email", "Корпаротивная почта нового сотрудника")))
    #
    IT_NOTIFY_ABOUT_CREATE_USER: LogCommandDescription = LogCommandDescription("Добрый день, отдел Информационных технологий.\nДокументы для нового пользователя: {name} готовы!\nОписание: {description}\nЛогин: {login}\nПароль: {password}\nТелефон: {telephone_number}\nЭлектронная почта: {email}", LogChannels.IT, LogLevels.NOTIFICATION.value, (ParamItem(
        "name", ""), ParamItem("description", ""), ParamItem("login", ""), ParamItem("password", ""), ParamItem("telephone_number", ""),  ParamItem("email", "")))

    IT_NOTIFY_ABOUT_CREATE_NEW_MARK: LogCommandDescription = LogCommandDescription("Добрый день, отдел Информационных технологий.\nКарта доступа для новой персоны: {name} готова!\nТелефон: {telephone_number}\nНомер карты доступа: {tab_number}\nГруппа доступа: {group_name}", LogChannels.IT, LogLevels.NOTIFICATION.value, (ParamItem(
        "name", ""), ParamItem("telephone_number", ""), ParamItem("tab_number", ""), ParamItem("group_name", "")))

    IT_NOTIFY_ABOUT_CREATE_TEMPORARY_MARK: LogCommandDescription = LogCommandDescription("Добрый день, отдел Информационных технологий.\nВременная карта доступа для персоны: {name} готова!\nНомер карты: {tab_number}\nТелефон: {telephone_number}", LogChannels.IT, LogLevels.NOTIFICATION.value, (ParamItem(
        "name", ""), ParamItem("tab_number", ""), ParamItem("telephone_number", "")))

    IT_NOTIFY_ABOUT_TEMPORARY_MARK_RETURN: LogCommandDescription = LogCommandDescription("Добрый день, отдел Информационных технологий.\nВременная карта доступа для персоны: {name} возвращена!\nНомер карты: {tab_number}", LogChannels.IT, LogLevels.NOTIFICATION.value, (ParamItem(
        "name", ""), ParamItem("tab_number", "")))

    IT_NOTIFY_ABOUT_MARK_RETURN: LogCommandDescription = LogCommandDescription("Добрый день, отдел Информационных технологий.\nКарта доступа для персоны: {name} возвращена!\nНомер карты: {tab_number}", LogChannels.IT, LogLevels.NOTIFICATION.value, (ParamItem(
        "name", ""), ParamItem("tab_number", "")))

    IT_TASK_AFTER_CREATE_NEW_USER: LogCommandDescription = LogCommandDescription("Добрый день, {it_user_name}.\nНеобходимо создать почту для пользователя: {name}\nАдресс электронной почты: {mail}\nПароль: {password}", LogChannels.IT, LogLevels.TASK.value, (ParamItem(
        "it_user_name", ""), ParamItem("name", ""), ParamItem("mail", ""), ParamItem("password", "")))

    WATCHABLE_WORKSTATION_IS_NOT_ACCESSABLE: LogCommandDescription = LogCommandDescription(
        "Компьютер {workstation_name} вне сети", LogChannels.RESOURCES, LogLevels.ERROR.value, [ParamItem("workstation_name", "")])
    
    WATCHABLE_WORKSTATION_IS_ACCESSABLE: LogCommandDescription = LogCommandDescription(
        "Компьютер {workstation_name} в сети", LogChannels.RESOURCES, LogLevels.NORMAL.value, [ParamItem("workstation_name", "")])

    #POLIBASE

    POLIBASE_PERSON_VISIT_WAS_REGISTERED: LogCommandDescription = LogCommandDescription("Зарегистрировано новое посещение: {name} ({type_string})", LogChannels.NOTIFICATION, LogLevels.NOTIFICATION.value, (ParamItem(
        "name", ""), ParamItem("type_string", ""), ParamItem("visit", "")))

    POLIBASE_PERSON_VISIT_NOTIFICATION_WAS_REGISTERED: LogCommandDescription = LogCommandDescription("Зарегистрировано новое уведомление посещение: {name} ({type_string})", LogChannels.NOTIFICATION, LogLevels.SILENCE.value, (ParamItem(
        "name", ""), ParamItem("type_string", ""), ParamItem("notification", "")))

    POLIBASE_PERSONS_WITH_OLD_FORMAT_BARCODE_WAS_DETECTED: LogCommandDescription = LogCommandDescription(
        "Полибейс: обнаружены пациенты со старым форматом или отсутствующим штрих-кодом в количестве {persons_pin_length}", LogChannels.NOTIFICATION, LogLevels.SILENCE.value, (ParamItem("persons_pin_length", ""), ParamItem("persons_pin", "")))
    
    POLIBASE_ALL_PERSON_BARCODES_WITH_OLD_FORMAT_WAS_CREATED: LogCommandDescription = LogCommandDescription(
        "Полибейс: все новые штрих-коды созданы", LogChannels.NOTIFICATION, LogLevels.SILENCE.value, [ParamItem("persons_pin", "")])

    POLIBASE_PERSON_WANTS_FEEDBACK_CALL_AFTER_REVIEW_QUEST_COMPLETE: LogCommandDescription = LogCommandDescription("Клиент {name} ({pin}) запросил обратный звонок.\nОценка: {grade}\nПричина: {message}\nТелефон: {telephone_number}",  LogChannels.POLIBASE_PERSON_FEEDBACK_CALL, LogLevels.NOTIFICATION.value, (ParamItem(
        "name", ""), ParamItem("pin", ""), ParamItem("grade", ""), ParamItem("message", ""), ParamItem("telephone_number", "")))

    POLIBASE_PERSON_REVIEW_QUEST_RESULT_FOR_HIGH_GRADE: LogCommandDescription = LogCommandDescription("Клиент {name} ({pin}) завершил опрос.\nОценка: {grade}\nОткуда узнал о нас: {information_way}\nТелефон: {telephone_number}",  LogChannels.POLIBASE_PERSON_REVIEW_QUEST_RESULT, LogLevels.NOTIFICATION.value, (ParamItem(
        "name", ""), ParamItem("pin", ""), ParamItem("grade", ""), ParamItem("information_way", ""), ParamItem("telephone_number", "")))

    POLIBASE_PERSON_REVIEW_QUEST_RESULT_FOR_LOW_GRADE: LogCommandDescription = LogCommandDescription("Клиент {name} ({pin}) завершил опрос.\nОценка: {grade}\nПричина: {message}\nОткуда узнал о нас: {information_way}\nЗапросил обратный звонок: {feedback_call}\nТелефон: {telephone_number}",  LogChannels.POLIBASE_PERSON_REVIEW_QUEST_RESULT, LogLevels.NOTIFICATION.value, (ParamItem(
        "name", ""), ParamItem("pin", ""), ParamItem("grade", ""), ParamItem("message", ""), ParamItem("information_way", ""), ParamItem("feedback_call", ""), ParamItem("telephone_number", "")))