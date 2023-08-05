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


class SetupWebhooksRequest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "order_url",
            "refund_url",
            "payment_url",
        }
        
        class properties:
            payment_url = schemas.StrSchema
            refund_url = schemas.StrSchema
            order_url = schemas.StrSchema
            __annotations__ = {
                "payment_url": payment_url,
                "refund_url": refund_url,
                "order_url": order_url,
            }
    
    order_url: MetaOapg.properties.order_url
    refund_url: MetaOapg.properties.refund_url
    payment_url: MetaOapg.properties.payment_url
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payment_url"]) -> MetaOapg.properties.payment_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["refund_url"]) -> MetaOapg.properties.refund_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["order_url"]) -> MetaOapg.properties.order_url: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["payment_url", "refund_url", "order_url", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payment_url"]) -> MetaOapg.properties.payment_url: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["refund_url"]) -> MetaOapg.properties.refund_url: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["order_url"]) -> MetaOapg.properties.order_url: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["payment_url", "refund_url", "order_url", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        order_url: typing.Union[MetaOapg.properties.order_url, str, ],
        refund_url: typing.Union[MetaOapg.properties.refund_url, str, ],
        payment_url: typing.Union[MetaOapg.properties.payment_url, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SetupWebhooksRequest':
        return super().__new__(
            cls,
            *_args,
            order_url=order_url,
            refund_url=refund_url,
            payment_url=payment_url,
            _configuration=_configuration,
            **kwargs,
        )
