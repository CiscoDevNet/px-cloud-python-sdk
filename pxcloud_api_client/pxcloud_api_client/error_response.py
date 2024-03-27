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


class ErrorResponse(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Error Message.
    """


    class MetaOapg:
        
        class properties:
            statusCode = schemas.Int64Schema
            statusMessage = schemas.StrSchema
            errorCode = schemas.StrSchema
            path = schemas.StrSchema
            code = schemas.Int64Schema
            message = schemas.StrSchema
            description = schemas.StrSchema
            __annotations__ = {
                "statusCode": statusCode,
                "statusMessage": statusMessage,
                "errorCode": errorCode,
                "path": path,
                "code": code,
                "message": message,
                "description": description,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["statusCode"]) -> MetaOapg.properties.statusCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["statusMessage"]) -> MetaOapg.properties.statusMessage: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["errorCode"]) -> MetaOapg.properties.errorCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["path"]) -> MetaOapg.properties.path: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["code"]) -> MetaOapg.properties.code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["message"]) -> MetaOapg.properties.message: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["statusCode", "statusMessage", "errorCode", "path", "code", "message", "description", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["statusCode"]) -> typing.Union[MetaOapg.properties.statusCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["statusMessage"]) -> typing.Union[MetaOapg.properties.statusMessage, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["errorCode"]) -> typing.Union[MetaOapg.properties.errorCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["path"]) -> typing.Union[MetaOapg.properties.path, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["code"]) -> typing.Union[MetaOapg.properties.code, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["message"]) -> typing.Union[MetaOapg.properties.message, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["statusCode", "statusMessage", "errorCode", "path", "code", "message", "description", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        statusCode: typing.Union[MetaOapg.properties.statusCode, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        statusMessage: typing.Union[MetaOapg.properties.statusMessage, str, schemas.Unset] = schemas.unset,
        errorCode: typing.Union[MetaOapg.properties.errorCode, str, schemas.Unset] = schemas.unset,
        path: typing.Union[MetaOapg.properties.path, str, schemas.Unset] = schemas.unset,
        code: typing.Union[MetaOapg.properties.code, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        message: typing.Union[MetaOapg.properties.message, str, schemas.Unset] = schemas.unset,
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ErrorResponse':
        return super().__new__(
            cls,
            *_args,
            statusCode=statusCode,
            statusMessage=statusMessage,
            errorCode=errorCode,
            path=path,
            code=code,
            message=message,
            description=description,
            _configuration=_configuration,
            **kwargs,
        )