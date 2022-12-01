"""Module describe infer's model"""
from enum import Enum
from enum import unique
from typing import Dict
from typing import Optional
from typing import Union

from fastapi import Field
from fastapi.exceptions import HTTPException
from pydantic import BaseModel
from pydantic import Field
from pydantic import validator


class InferRequest(BaseModel):
    """Infer Data"""

    age: int = Field(
        title="Person's age",
        description="Usually between 17 and 90.",
        example="17",
        gt=0,
    )
    capital_gain: int = Field(
        title="Capital gain",
        description="Capital gain",
        example="1077.64",
        gt=0,
    )
    capital_loss: int = Field(
        title="Capital loss",
        description="Capital loss",
        example="87.30",
        gt=0,
    )
    education: int = Field(
        title="Education level",
        description="Education level",
        example="5th-6th",
    )
    education_num: int = Field(
        title="Education number",
        description="Education number",
        example="10",
        gt=0,
    )
    fnlgt: int = Field(
        title="fnlgt",
        description="fnlgt",
        example="189778.40",
        gt=0,
    )
    hours_per_week: int = Field(
        title="Hours per week",
        description="Hours per week",
        example="40",
        gt=0,
    )
    marital_status: int = Field(
        title="Marital status",
        description="Marital status",
        example="Married-civ-spouse",
    )
    native_country: int = Field(
        title="Native country",
        description="Native country",
        example="Canada",
    )
    occupation: int = Field(
        title="Occupation",
        description="Occupation",
        example="Farming-fishing",
    )
    race: int = Field(
        title="Race",
        description="Race",
        example="Asian-Pac-Islander",
    )
    relationship: int = Field(
        title="Relationship",
        description="Relationship",
        example="Own-child",
    )
    salary: int = Field(
        title="Salary",
        description="Salary",
        example="<=50K",
    )
    sex: int = Field(
        title="Sex",
        description="Sex",
        example="Male",
    )
    workclass: int = Field(
        title="Workclass",
        description="Workclass",
        example="Self-emp-inc",
    )

    @validator("salary")
    def _validate_salary(self, salary) -> Enum:
        if salary not in [v.value for v in Salary]:
            raise InvalidValueError(salary, Salary)


# @validator("education")
# def _validate_education(self, education) -> Enum:
# Education
# MaritalStatus
# NativeCountry
# Occupation
# Race
# Relationship
# Salary
# Sex
# Workclass


class InvalidValueError(Exception):
    """Exception raised when invalid value in request"""

    def __init__(self, value, enumerator, message=None):
        """Set message depending on value and enumerator"""
        self._value = value
        self._enumerator = enumerator
        self._set_message(message)
        super().__init__(self.message)

    def _set_message(self, message):
        if message is not None:
            self.message = message
        else:
            self.message = (
                "Received a categorical value not within trained set. "
                f"{self._value} not in {[v.value for v in self._enumerator]}."
            )


@unique
class Salary(Enum):
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
