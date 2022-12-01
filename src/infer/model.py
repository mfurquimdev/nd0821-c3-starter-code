"""Module describe infer's model"""
from typing import Dict
from typing import Optional
from typing import Union

from fastapi.exceptions import HTTPException
from pydantic import BaseModel
from pydantic import Field
from pydantic import validator

from .enum import Education
from .enum import MaritalStatus
from .enum import NativeCountry
from .enum import Occupation
from .enum import Race
from .enum import Relationship
from .enum import Salary
from .enum import Sex
from .enum import Workclass
from .exception import InvalidCategoryValueError


class InferResponse(BaseModel):
    """Infer response model"""

    salary: Salary = Field(
        title="Salary",
        description="Salary",
        example="<=50K",
    )


class InferRequest(BaseModel):
    """Infer request data model"""

    age: int = Field(
        title="Person's age",
        description="Usually between 17 and 90.",
        example="17",
        gt=0,
        lt=150,
    )

    capital_gain: float = Field(
        title="Capital gain",
        description="Capital gain",
        example="1077.64",
        gt=0,
    )

    capital_loss: float = Field(
        title="Capital loss",
        description="Capital loss",
        example="87.30",
        gt=0,
    )

    education: Education = Field(
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

    fnlgt: float = Field(
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

    marital_status: MaritalStatus = Field(
        title="Marital status",
        description="Marital status",
        example="Married-civ-spouse",
    )

    native_country: NativeCountry = Field(
        title="Native country",
        description="Native country",
        example="Canada",
    )

    occupation: Occupation = Field(
        title="Occupation",
        description="Occupation",
        example="Farming-fishing",
    )

    race: Race = Field(
        title="Race",
        description="Race",
        example="Asian-Pac-Islander",
    )

    relationship: Relationship = Field(
        title="Relationship",
        description="Relationship",
        example="Own-child",
    )

    sex: Sex = Field(
        title="Sex",
        description="Sex",
        example="Male",
    )

    workclass: Workclass = Field(
        title="Workclass",
        description="Workclass",
        example="Self-emp-inc",
    )
