# coding: utf-8

"""
    Cashfree LRS

    CashFree LRS APIs (v2)  # noqa: E501

    The version of the OpenAPI document: 1.0.2
    Contact: nextgenapi@cashfree.com
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from cashfree_lrs_client import schemas  # noqa: F401


class Currency(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    ISO Currency code of currency in which remittance needs to be settled. Only 3 characters are allowed.
    """
    
    @schemas.classproperty
    def USD(cls):
        return cls("USD")
    
    @schemas.classproperty
    def INR(cls):
        return cls("INR")
