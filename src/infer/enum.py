"""Module describing enumerations for categorical values"""
from enum import Enum
from enum import unique


@unique
class Education(Enum):
    LEQ_50K = "<=50K"
    GT_50K = ">50K"


@unique
class Workclass(Enum):
    FEDERAL_GOV = "Federal-gov"
    LOCAL_GOV = "Local-gov"
    NEVER_WORKED = "Never-worked"
    OTHER = "?"
    PRIVATE = "Private"
    SELF_EMP_INC = "Self-emp-inc"
    SELF_EMP_NOT_INC = "Self-emp-not-inc"
    STATE_GOV = "State-gov"
    WITHOUT_PAY = "Without-pay"


@unique
class Education(Enum):
    ASSOC_ACDm = "Assoc-acdm"
    ASSOC_VOC = "Assoc-voc"
    BACHELORS = "Bachelors"
    DOCTORATE = "Doctorate"
    HS_GRAD = "HS-grad"
    MHASTERS = "Masters"
    N10TH = "10th"
    N11TH = "11th"
    N12TH = "12th"
    N1ST_4TH = "1st-4th"
    N5TH_6TH = "5th-6th"
    N7TH_8TH = "7th-8th"
    N9TH = "9TH"
    PRESCHOOL = "Preschool"
    PROF_SCHOol = "Prof-school"
    SOME_COLLege = "Some-college"


@unique
class MaritalStatus(Enum):
    DIVORCED = "Divorced"
    MARRIED_AF_SPOUSE = "Married-AF-spouse"
    MARRIED_CIV_SPOUSE = "Married-civ-spouse"
    MARRIED_SPOUSE_ABSENT = "Married-spouse-absent"
    NEVER_MARRIED = "Never-married"
    SEPARATED = "Separated"
    WIDOWED = "Widowed"


@unique
class Occupation(Enum):
    ADM_CLERICAL = "Adm-clerical"
    ARMED_FORCES = "Armed-Forces"
    CRAFT_REPAIR = "Craft-repair"
    EXEC_MANAGERIAL = "Exec-managerial"
    FARMING_FISHING = "Farming-fishing"
    HANDLERS_CLEANERS = "Handlers-cleaners"
    MACHINE_OP_INSPCT = "Machine-op-inspct"
    OTHER = "?"
    OTHER_SERVICE = "Other-service"
    PRIV_HOUSE_SERV = "Priv-house-serv"
    PROF_SPECIALTY = "Prof-specialty"
    PROTECTIVE_SERV = "Protective-serv"
    SALES = "Sales"
    TECH_SUPPORT = "Tech-support"
    TRANSPORT_MOVING = "Transport-moving"


@unique
class Relationship(Enum):
    NOT_IN_FAMILY = "Not-in-family"
    HUSBAND = "Husband"
    WIFE = "Wife"
    OWN_CHILD = "Own-child"
    UNMARRIED = "Unmarried"
    OTHER_RELATIVE = "Other-relative"


@unique
class Race(Enum):
    WHITE = "White"
    BLACK = "Black"
    ASIAN_PAC_ISLANDER = "Asian-Pac-Islander"
    AMER_INDIAN_ESKIMO = "Amer-Indian-Eskimo"
    OTHER = "Other"


@unique
class Sex(Enum):
    MALE = "Male"
    FEMALE = "Female"


@unique
class NativeCountry(Enum):
    CAMBODIA = "Cambodia"
    CANADA = "Canada"
    CHINA = "China"
    COLUMBIA = "Columbia"
    CUBA = "Cuba"
    DOMINICAN_REPUBLIC = "Dominican-Republic"
    ECUADOR = "Ecuador"
    EL_SALVADOR = "El-Salvador"
    ENGLAND = "England"
    FRANCE = "France"
    GERMANY = "Germany"
    GREECE = "Greece"
    GUATEMALA = "Guatemala"
    HAITI = "Haiti"
    HOLAND_NETHERLANDS = "Holand-Netherlands"
    HONDURAS = "Honduras"
    HONG = "Hong"
    HUNGARY = "Hungary"
    INDIA = "India"
    IRAN = "Iran"
    IRELAND = "Ireland"
    ITALY = "Italy"
    JAMAICA = "Jamaica"
    JAPAN = "Japan"
    LAOS = "Laos"
    MEXICO = "Mexico"
    NICARAGUA = "Nicaragua"
    OTHER = "?"
    OUTLYING_US = "Outlying-US(Guam-USVI-etc)"
    PERU = "Peru"
    PHILIPPINES = "Philippines"
    POLAND = "Poland"
    PORTUGAL = "Portugal"
    PUERTO_RICO = "Puerto-Rico"
    SCOTLAND = "Scotland"
    SOUTH = "South"
    TAIWAN = "Taiwan"
    THAILAND = "Thailand"
    TRINADAD_TOBAGO = "Trinadad&Tobago"
    UNITED_STATES = "United-States"
    VIETNAM = "Vietnam"
    YUGOSLAVIA = "Yugoslavia"
