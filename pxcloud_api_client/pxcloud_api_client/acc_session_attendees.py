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


class AccSessionAttendees(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            attendeeEmail = schemas.StrSchema
            attendeeName = schemas.StrSchema
            __annotations__ = {
                "attendeeEmail": attendeeEmail,
                "attendeeName": attendeeName,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["attendeeEmail"]) -> MetaOapg.properties.attendeeEmail: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["attendeeName"]) -> MetaOapg.properties.attendeeName: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["attendeeEmail", "attendeeName", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["attendeeEmail"]) -> typing.Union[MetaOapg.properties.attendeeEmail, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["attendeeName"]) -> typing.Union[MetaOapg.properties.attendeeName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["attendeeEmail", "attendeeName", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        attendeeEmail: typing.Union[MetaOapg.properties.attendeeEmail, str, schemas.Unset] = schemas.unset,
        attendeeName: typing.Union[MetaOapg.properties.attendeeName, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AccSessionAttendees':
        return super().__new__(
            cls,
            *_args,
            attendeeEmail=attendeeEmail,
            attendeeName=attendeeName,
            _configuration=_configuration,
            **kwargs,
        )