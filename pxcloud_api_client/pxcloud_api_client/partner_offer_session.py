# coding: utf-8

"""
    PX Cloud for Success Tracks API

    PX Cloud for Success Tracks API  # noqa: E501

    The version of the OpenAPI document: 0.9.11
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

from pxcloud_api_client import schemas  # noqa: F401


class PartnerOfferSession(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            
            
            class attendeeList(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['PartnerOfferAttendee']:
                        return PartnerOfferAttendee
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['PartnerOfferAttendee'], typing.List['PartnerOfferAttendee']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'attendeeList':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'PartnerOfferAttendee':
                    return super().__getitem__(i)
            businessOutcome = schemas.StrSchema
            createdDate = schemas.DateTimeSchema
            modifiedDate = schemas.DateTimeSchema
            preferredSlot = schemas.StrSchema
            reasonForInterest = schemas.StrSchema
            sessionId = schemas.StrSchema
            status = schemas.StrSchema
            timezone = schemas.StrSchema
            __annotations__ = {
                "attendeeList": attendeeList,
                "businessOutcome": businessOutcome,
                "createdDate": createdDate,
                "modifiedDate": modifiedDate,
                "preferredSlot": preferredSlot,
                "reasonForInterest": reasonForInterest,
                "sessionId": sessionId,
                "status": status,
                "timezone": timezone,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["attendeeList"]) -> MetaOapg.properties.attendeeList: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["businessOutcome"]) -> MetaOapg.properties.businessOutcome: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["createdDate"]) -> MetaOapg.properties.createdDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["modifiedDate"]) -> MetaOapg.properties.modifiedDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["preferredSlot"]) -> MetaOapg.properties.preferredSlot: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reasonForInterest"]) -> MetaOapg.properties.reasonForInterest: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sessionId"]) -> MetaOapg.properties.sessionId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timezone"]) -> MetaOapg.properties.timezone: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["attendeeList", "businessOutcome", "createdDate", "modifiedDate", "preferredSlot", "reasonForInterest", "sessionId", "status", "timezone", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["attendeeList"]) -> typing.Union[MetaOapg.properties.attendeeList, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["businessOutcome"]) -> typing.Union[MetaOapg.properties.businessOutcome, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["createdDate"]) -> typing.Union[MetaOapg.properties.createdDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["modifiedDate"]) -> typing.Union[MetaOapg.properties.modifiedDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["preferredSlot"]) -> typing.Union[MetaOapg.properties.preferredSlot, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reasonForInterest"]) -> typing.Union[MetaOapg.properties.reasonForInterest, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sessionId"]) -> typing.Union[MetaOapg.properties.sessionId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timezone"]) -> typing.Union[MetaOapg.properties.timezone, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["attendeeList", "businessOutcome", "createdDate", "modifiedDate", "preferredSlot", "reasonForInterest", "sessionId", "status", "timezone", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        attendeeList: typing.Union[MetaOapg.properties.attendeeList, list, tuple, schemas.Unset] = schemas.unset,
        businessOutcome: typing.Union[MetaOapg.properties.businessOutcome, str, schemas.Unset] = schemas.unset,
        createdDate: typing.Union[MetaOapg.properties.createdDate, str, datetime, schemas.Unset] = schemas.unset,
        modifiedDate: typing.Union[MetaOapg.properties.modifiedDate, str, datetime, schemas.Unset] = schemas.unset,
        preferredSlot: typing.Union[MetaOapg.properties.preferredSlot, str, schemas.Unset] = schemas.unset,
        reasonForInterest: typing.Union[MetaOapg.properties.reasonForInterest, str, schemas.Unset] = schemas.unset,
        sessionId: typing.Union[MetaOapg.properties.sessionId, str, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        timezone: typing.Union[MetaOapg.properties.timezone, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PartnerOfferSession':
        return super().__new__(
            cls,
            *_args,
            attendeeList=attendeeList,
            businessOutcome=businessOutcome,
            createdDate=createdDate,
            modifiedDate=modifiedDate,
            preferredSlot=preferredSlot,
            reasonForInterest=reasonForInterest,
            sessionId=sessionId,
            status=status,
            timezone=timezone,
            _configuration=_configuration,
            **kwargs,
        )

from pxcloud_api_client.pxcloud_api_client.partner_offer_attendee import PartnerOfferAttendee
