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


class Crash(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            resetReason = schemas.StrSchema
            timeStamp = schemas.DateTimeSchema
            __annotations__ = {
                "resetReason": resetReason,
                "timeStamp": timeStamp,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["resetReason"]) -> MetaOapg.properties.resetReason: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timeStamp"]) -> MetaOapg.properties.timeStamp: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["resetReason", "timeStamp", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["resetReason"]) -> typing.Union[MetaOapg.properties.resetReason, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timeStamp"]) -> typing.Union[MetaOapg.properties.timeStamp, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["resetReason", "timeStamp", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        resetReason: typing.Union[MetaOapg.properties.resetReason, str, schemas.Unset] = schemas.unset,
        timeStamp: typing.Union[MetaOapg.properties.timeStamp, str, datetime, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Crash':
        return super().__new__(
            cls,
            *_args,
            resetReason=resetReason,
            timeStamp=timeStamp,
            _configuration=_configuration,
            **kwargs,
        )