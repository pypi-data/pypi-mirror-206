# coding: utf-8

"""
    Cashfree LRS

    CashFree LRS APIs (v2)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: nextgenapi@cashfree.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, constr, validator
from cashfree_lrs_client.models.purpose import Purpose

class CreateRemitterRequest(BaseModel):
    """
    CreateRemitterRequest
    """
    remitter_id: constr(strict=True, max_length=50, min_length=1) = Field(..., description="Unique remitter ID to identify the remitter. Alphanumeric characters, hyphens, and underscores are allowed. Maximum of 50 characters are allowed.")
    purpose: Purpose = ...
    account_number: constr(strict=True, max_length=25, min_length=9) = Field(..., description="Bank account number of the remitter.")
    ifsc: constr(strict=True, max_length=11, min_length=8) = Field(..., description="The IFSC information of the remitter bank account. It should be an alphanumeric value of 11 characters. The first 4 characters should be alphabets, the 5th character should be a 0, and the remaining 6 characters should be numerals.")
    pan: constr(strict=True, max_length=10, min_length=10) = Field(..., description="PAN of the remitter. Should include 10 characters. The first 5 characters are alphabets followed by 4 numbers and the 10th character is an alphabet.")
    name: constr(strict=True, max_length=50, min_length=3) = Field(..., description="Name of the remitter. Alphabets and spaces are allowed.")
    address: constr(strict=True, max_length=200, min_length=3) = Field(..., description="Address of the remitter. Alphanumeric charcaters, dot, and hyphens are allowed.")
    city: constr(strict=True, max_length=50, min_length=3) = Field(..., description="City of the remitter. Alphabets are only allowed.")
    state: constr(strict=True, max_length=50, min_length=3) = Field(..., description="State of the remitter. Alphabets are only allowed.")
    postal_code: constr(strict=True, max_length=6, min_length=6) = Field(..., description="Postal code of the remitter address. Numeric characters only allowed.")
    phone_number: Optional[constr(strict=True, max_length=10, min_length=10)] = Field(None, description="Phone number of the remitter. Only numbers and hyphens are allowed.")
    email: Optional[constr(strict=True, max_length=50, min_length=5)] = Field(None, description="Email address of the remitter. Example, abc@gmail.com")
    nationality: constr(strict=True, max_length=2, min_length=2) = Field(..., description="Nationality of the remitter. Only 2 alphabets are allowed. Example, IN for India.")
    bank_code: constr(strict=True, max_length=4) = Field(..., description="Remitter bank code. Required for net banking payments to perform bank account checks (TPV). Maximum of 4 characters allowed.")
    __properties = ["remitter_id", "purpose", "account_number", "ifsc", "pan", "name", "address", "city", "state", "postal_code", "phone_number", "email", "nationality", "bank_code"]

    @validator('nationality')
    def nationality_validate_enum(cls, v):
        if v not in ('IN', 'US'):
            raise ValueError("must be one of enum values ('IN', 'US')")
        return v

    class Config:
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> CreateRemitterRequest:
        """Create an instance of CreateRemitterRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CreateRemitterRequest:
        """Create an instance of CreateRemitterRequest from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return CreateRemitterRequest.parse_obj(obj)

        _obj = CreateRemitterRequest.parse_obj({
            "remitter_id": obj.get("remitter_id"),
            "purpose": obj.get("purpose"),
            "account_number": obj.get("account_number"),
            "ifsc": obj.get("ifsc"),
            "pan": obj.get("pan"),
            "name": obj.get("name"),
            "address": obj.get("address"),
            "city": obj.get("city"),
            "state": obj.get("state"),
            "postal_code": obj.get("postal_code"),
            "phone_number": obj.get("phone_number"),
            "email": obj.get("email"),
            "nationality": obj.get("nationality"),
            "bank_code": obj.get("bank_code")
        })
        return _obj

