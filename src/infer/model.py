"""Module describe infer's model"""
from typing import Dict
from typing import Optional
from typing import Union

from fastapi.exceptions import HTTPException
from pydantic import BaseModel
from pydantic import Field
from pydantic import validator

from .enum import Education
from .exception import InvalidCategoryValueError


class InferResponse(BaseModel):
    """Infer response model"""

    response: str = Field(
        title="Response",
        description="Response",
        example="Ok!",
        default="Ok!",
    )


class InferRequest(BaseModel):
    """Infer request data model"""

    age: int = Field(
        title="Person's age",
        description="Usually between 17 and 90.",
        example="17",
        gt=0,
    )
    # capital_gain: int = Field(
    #     title="Capital gain",
    #     description="Capital gain",
    #     example="1077.64",
    #     gt=0,
    # )
    # capital_loss: int = Field(
    #     title="Capital loss",
    #     description="Capital loss",
    #     example="87.30",
    #     gt=0,
    # )
    education: Education = Field(
        title="Education level",
        description="Education level",
        example="5th-6th",
    )

    # @validator("education")
    # def _validate_salary(cls, education) -> Education:
    #     if education not in [v.value for v in Education]:
    #         raise InvalidCategoryValueError(education, Education)
    #     return {e.value: e for e in list(Education)}[education]

    # education_num: int = Field(
    #     title="Education number",
    #     description="Education number",
    #     example="10",
    #     gt=0,
    # )
    # fnlgt: int = Field(
    #     title="fnlgt",
    #     description="fnlgt",
    #     example="189778.40",
    #     gt=0,
    # )
    # hours_per_week: int = Field(
    #     title="Hours per week",
    #     description="Hours per week",
    #     example="40",
    #     gt=0,
    # )
    # marital_status: int = Field(
    #     title="Marital status",
    #     description="Marital status",
    #     example="Married-civ-spouse",
    # )
    # native_country: int = Field(
    #     title="Native country",
    #     description="Native country",
    #     example="Canada",
    # )
    # occupation: int = Field(
    #     title="Occupation",
    #     description="Occupation",
    #     example="Farming-fishing",
    # )
    # race: int = Field(
    #     title="Race",
    #     description="Race",
    #     example="Asian-Pac-Islander",
    # )
    # relationship: int = Field(
    #     title="Relationship",
    #     description="Relationship",
    #     example="Own-child",
    # )
    # salary: int = Field(
    #     title="Salary",
    #     description="Salary",
    #     example="<=50K",
    # )
    # sex: int = Field(
    #     title="Sex",
    #     description="Sex",
    #     example="Male",
    # )
    # workclass: int = Field(
    #     title="Workclass",
    #     description="Workclass",
    #     example="Self-emp-inc",
    # )

    # @validator("salary")
    # def _validate_salary(self, salary) -> Enum:
    #     if salary not in [v.value for v in Salary]:
    #         raise InvalidValueError(salary, Salary)


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
