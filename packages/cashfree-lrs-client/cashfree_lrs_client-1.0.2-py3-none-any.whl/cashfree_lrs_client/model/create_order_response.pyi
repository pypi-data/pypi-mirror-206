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


class CreateOrderResponse(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            
            
            class tcs(
                schemas.Int32Schema
            ):
                pass
        
            @staticmethod
            def gst() -> typing.Type['Amount']:
                return Amount
        
            @staticmethod
            def fx_rate() -> typing.Type['Amount']:
                return Amount
        
            @staticmethod
            def amount_to_pay() -> typing.Type['Amount']:
                return Amount
            
            
            class handling_charges(
                schemas.Int32Schema
            ):
                pass
            order_expiry_time = schemas.DateTimeSchema
            payment_link = schemas.StrSchema
            order_token = schemas.StrSchema
            
            
            class missing_documents(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'missing_documents':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "tcs": tcs,
                "gst": gst,
                "fx_rate": fx_rate,
                "amount_to_pay": amount_to_pay,
                "handling_charges": handling_charges,
                "order_expiry_time": order_expiry_time,
                "payment_link": payment_link,
                "order_token": order_token,
                "missing_documents": missing_documents,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tcs"]) -> MetaOapg.properties.tcs: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gst"]) -> 'Amount': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fx_rate"]) -> 'Amount': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amount_to_pay"]) -> 'Amount': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["handling_charges"]) -> MetaOapg.properties.handling_charges: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["order_expiry_time"]) -> MetaOapg.properties.order_expiry_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payment_link"]) -> MetaOapg.properties.payment_link: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["order_token"]) -> MetaOapg.properties.order_token: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["missing_documents"]) -> MetaOapg.properties.missing_documents: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["tcs", "gst", "fx_rate", "amount_to_pay", "handling_charges", "order_expiry_time", "payment_link", "order_token", "missing_documents", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tcs"]) -> typing.Union[MetaOapg.properties.tcs, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gst"]) -> typing.Union['Amount', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fx_rate"]) -> typing.Union['Amount', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amount_to_pay"]) -> typing.Union['Amount', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["handling_charges"]) -> typing.Union[MetaOapg.properties.handling_charges, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["order_expiry_time"]) -> typing.Union[MetaOapg.properties.order_expiry_time, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payment_link"]) -> typing.Union[MetaOapg.properties.payment_link, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["order_token"]) -> typing.Union[MetaOapg.properties.order_token, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["missing_documents"]) -> typing.Union[MetaOapg.properties.missing_documents, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["tcs", "gst", "fx_rate", "amount_to_pay", "handling_charges", "order_expiry_time", "payment_link", "order_token", "missing_documents", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        tcs: typing.Union[MetaOapg.properties.tcs, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        gst: typing.Union['Amount', schemas.Unset] = schemas.unset,
        fx_rate: typing.Union['Amount', schemas.Unset] = schemas.unset,
        amount_to_pay: typing.Union['Amount', schemas.Unset] = schemas.unset,
        handling_charges: typing.Union[MetaOapg.properties.handling_charges, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        order_expiry_time: typing.Union[MetaOapg.properties.order_expiry_time, str, datetime, schemas.Unset] = schemas.unset,
        payment_link: typing.Union[MetaOapg.properties.payment_link, str, schemas.Unset] = schemas.unset,
        order_token: typing.Union[MetaOapg.properties.order_token, str, schemas.Unset] = schemas.unset,
        missing_documents: typing.Union[MetaOapg.properties.missing_documents, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CreateOrderResponse':
        return super().__new__(
            cls,
            *_args,
            tcs=tcs,
            gst=gst,
            fx_rate=fx_rate,
            amount_to_pay=amount_to_pay,
            handling_charges=handling_charges,
            order_expiry_time=order_expiry_time,
            payment_link=payment_link,
            order_token=order_token,
            missing_documents=missing_documents,
            _configuration=_configuration,
            **kwargs,
        )

from cashfree_lrs_client.model.amount import Amount
