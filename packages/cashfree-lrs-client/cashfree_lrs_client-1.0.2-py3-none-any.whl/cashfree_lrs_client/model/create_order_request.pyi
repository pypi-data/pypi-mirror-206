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


class CreateOrderRequest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "beneficiary_id",
            "to_amount",
            "customer_relationship",
            "purpose",
            "remitter_id",
            "return_url",
            "order_id",
            "to_currency",
        }
        
        class properties:
            
            
            class order_id(
                schemas.StrSchema
            ):
                pass
        
            @staticmethod
            def to_currency() -> typing.Type['Currency']:
                return Currency
            
            
            class to_amount(
                schemas.Float64Schema
            ):
                pass
        
            @staticmethod
            def purpose() -> typing.Type['Purpose']:
                return Purpose
            
            
            class return_url(
                schemas.StrSchema
            ):
                pass
            
            
            class remitter_id(
                schemas.StrSchema
            ):
                pass
            
            
            class beneficiary_id(
                schemas.StrSchema
            ):
                pass
            
            
            class customer_relationship(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def SELF(cls):
                    return cls("SELF")
                
                @schemas.classproperty
                def SON(cls):
                    return cls("SON")
            
            
            class from_amount(
                schemas.Float64Schema
            ):
                pass
            customer_declaration = schemas.StrSchema
            doc_ids = schemas.StrSchema
            education_loan = schemas.BoolSchema
            remarks = schemas.StrSchema
            __annotations__ = {
                "order_id": order_id,
                "to_currency": to_currency,
                "to_amount": to_amount,
                "purpose": purpose,
                "return_url": return_url,
                "remitter_id": remitter_id,
                "beneficiary_id": beneficiary_id,
                "customer_relationship": customer_relationship,
                "from_amount": from_amount,
                "customer_declaration": customer_declaration,
                "doc_ids": doc_ids,
                "education_loan": education_loan,
                "remarks": remarks,
            }
    
    beneficiary_id: MetaOapg.properties.beneficiary_id
    to_amount: MetaOapg.properties.to_amount
    customer_relationship: MetaOapg.properties.customer_relationship
    purpose: 'Purpose'
    remitter_id: MetaOapg.properties.remitter_id
    return_url: MetaOapg.properties.return_url
    order_id: MetaOapg.properties.order_id
    to_currency: 'Currency'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["order_id"]) -> MetaOapg.properties.order_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["to_currency"]) -> 'Currency': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["to_amount"]) -> MetaOapg.properties.to_amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["purpose"]) -> 'Purpose': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["return_url"]) -> MetaOapg.properties.return_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["remitter_id"]) -> MetaOapg.properties.remitter_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["beneficiary_id"]) -> MetaOapg.properties.beneficiary_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customer_relationship"]) -> MetaOapg.properties.customer_relationship: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["from_amount"]) -> MetaOapg.properties.from_amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customer_declaration"]) -> MetaOapg.properties.customer_declaration: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["doc_ids"]) -> MetaOapg.properties.doc_ids: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["education_loan"]) -> MetaOapg.properties.education_loan: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["remarks"]) -> MetaOapg.properties.remarks: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["order_id", "to_currency", "to_amount", "purpose", "return_url", "remitter_id", "beneficiary_id", "customer_relationship", "from_amount", "customer_declaration", "doc_ids", "education_loan", "remarks", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["order_id"]) -> MetaOapg.properties.order_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["to_currency"]) -> 'Currency': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["to_amount"]) -> MetaOapg.properties.to_amount: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["purpose"]) -> 'Purpose': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["return_url"]) -> MetaOapg.properties.return_url: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["remitter_id"]) -> MetaOapg.properties.remitter_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["beneficiary_id"]) -> MetaOapg.properties.beneficiary_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customer_relationship"]) -> MetaOapg.properties.customer_relationship: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["from_amount"]) -> typing.Union[MetaOapg.properties.from_amount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customer_declaration"]) -> typing.Union[MetaOapg.properties.customer_declaration, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["doc_ids"]) -> typing.Union[MetaOapg.properties.doc_ids, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["education_loan"]) -> typing.Union[MetaOapg.properties.education_loan, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["remarks"]) -> typing.Union[MetaOapg.properties.remarks, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["order_id", "to_currency", "to_amount", "purpose", "return_url", "remitter_id", "beneficiary_id", "customer_relationship", "from_amount", "customer_declaration", "doc_ids", "education_loan", "remarks", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        beneficiary_id: typing.Union[MetaOapg.properties.beneficiary_id, str, ],
        to_amount: typing.Union[MetaOapg.properties.to_amount, decimal.Decimal, int, float, ],
        customer_relationship: typing.Union[MetaOapg.properties.customer_relationship, str, ],
        purpose: 'Purpose',
        remitter_id: typing.Union[MetaOapg.properties.remitter_id, str, ],
        return_url: typing.Union[MetaOapg.properties.return_url, str, ],
        order_id: typing.Union[MetaOapg.properties.order_id, str, ],
        to_currency: 'Currency',
        from_amount: typing.Union[MetaOapg.properties.from_amount, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        customer_declaration: typing.Union[MetaOapg.properties.customer_declaration, str, schemas.Unset] = schemas.unset,
        doc_ids: typing.Union[MetaOapg.properties.doc_ids, str, schemas.Unset] = schemas.unset,
        education_loan: typing.Union[MetaOapg.properties.education_loan, bool, schemas.Unset] = schemas.unset,
        remarks: typing.Union[MetaOapg.properties.remarks, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CreateOrderRequest':
        return super().__new__(
            cls,
            *_args,
            beneficiary_id=beneficiary_id,
            to_amount=to_amount,
            customer_relationship=customer_relationship,
            purpose=purpose,
            remitter_id=remitter_id,
            return_url=return_url,
            order_id=order_id,
            to_currency=to_currency,
            from_amount=from_amount,
            customer_declaration=customer_declaration,
            doc_ids=doc_ids,
            education_loan=education_loan,
            remarks=remarks,
            _configuration=_configuration,
            **kwargs,
        )

from cashfree_lrs_client.model.currency import Currency
from cashfree_lrs_client.model.purpose import Purpose
