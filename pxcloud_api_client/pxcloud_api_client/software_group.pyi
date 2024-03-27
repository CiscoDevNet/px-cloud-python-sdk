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


class SoftwareGroup(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            assetCount = schemas.Int32Schema
            sourceId = schemas.StrSchema
            sourceSystemId = schemas.StrSchema
            selectedRelease = schemas.StrSchema
            productFamily = schemas.StrSchema
            softwareGroupName = schemas.StrSchema
            softwareGroupId = schemas.StrSchema
            suggestionId = schemas.StrSchema
            suggestions = schemas.StrSchema
            riskLevel = schemas.StrSchema
            softwareType = schemas.StrSchema
            currentReleases = schemas.StrSchema
            managedBy = schemas.StrSchema
            __annotations__ = {
                "assetCount": assetCount,
                "sourceId": sourceId,
                "sourceSystemId": sourceSystemId,
                "selectedRelease": selectedRelease,
                "productFamily": productFamily,
                "softwareGroupName": softwareGroupName,
                "softwareGroupId": softwareGroupId,
                "suggestionId": suggestionId,
                "suggestions": suggestions,
                "riskLevel": riskLevel,
                "softwareType": softwareType,
                "currentReleases": currentReleases,
                "managedBy": managedBy,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["assetCount"]) -> MetaOapg.properties.assetCount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sourceId"]) -> MetaOapg.properties.sourceId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sourceSystemId"]) -> MetaOapg.properties.sourceSystemId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["selectedRelease"]) -> MetaOapg.properties.selectedRelease: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["productFamily"]) -> MetaOapg.properties.productFamily: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["softwareGroupName"]) -> MetaOapg.properties.softwareGroupName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["softwareGroupId"]) -> MetaOapg.properties.softwareGroupId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["suggestionId"]) -> MetaOapg.properties.suggestionId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["suggestions"]) -> MetaOapg.properties.suggestions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["riskLevel"]) -> MetaOapg.properties.riskLevel: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["softwareType"]) -> MetaOapg.properties.softwareType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currentReleases"]) -> MetaOapg.properties.currentReleases: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["managedBy"]) -> MetaOapg.properties.managedBy: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["assetCount", "sourceId", "sourceSystemId", "selectedRelease", "productFamily", "softwareGroupName", "softwareGroupId", "suggestionId", "suggestions", "riskLevel", "softwareType", "currentReleases", "managedBy", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["assetCount"]) -> typing.Union[MetaOapg.properties.assetCount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sourceId"]) -> typing.Union[MetaOapg.properties.sourceId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sourceSystemId"]) -> typing.Union[MetaOapg.properties.sourceSystemId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["selectedRelease"]) -> typing.Union[MetaOapg.properties.selectedRelease, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["productFamily"]) -> typing.Union[MetaOapg.properties.productFamily, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["softwareGroupName"]) -> typing.Union[MetaOapg.properties.softwareGroupName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["softwareGroupId"]) -> typing.Union[MetaOapg.properties.softwareGroupId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["suggestionId"]) -> typing.Union[MetaOapg.properties.suggestionId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["suggestions"]) -> typing.Union[MetaOapg.properties.suggestions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["riskLevel"]) -> typing.Union[MetaOapg.properties.riskLevel, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["softwareType"]) -> typing.Union[MetaOapg.properties.softwareType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currentReleases"]) -> typing.Union[MetaOapg.properties.currentReleases, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["managedBy"]) -> typing.Union[MetaOapg.properties.managedBy, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["assetCount", "sourceId", "sourceSystemId", "selectedRelease", "productFamily", "softwareGroupName", "softwareGroupId", "suggestionId", "suggestions", "riskLevel", "softwareType", "currentReleases", "managedBy", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        assetCount: typing.Union[MetaOapg.properties.assetCount, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        sourceId: typing.Union[MetaOapg.properties.sourceId, str, schemas.Unset] = schemas.unset,
        sourceSystemId: typing.Union[MetaOapg.properties.sourceSystemId, str, schemas.Unset] = schemas.unset,
        selectedRelease: typing.Union[MetaOapg.properties.selectedRelease, str, schemas.Unset] = schemas.unset,
        productFamily: typing.Union[MetaOapg.properties.productFamily, str, schemas.Unset] = schemas.unset,
        softwareGroupName: typing.Union[MetaOapg.properties.softwareGroupName, str, schemas.Unset] = schemas.unset,
        softwareGroupId: typing.Union[MetaOapg.properties.softwareGroupId, str, schemas.Unset] = schemas.unset,
        suggestionId: typing.Union[MetaOapg.properties.suggestionId, str, schemas.Unset] = schemas.unset,
        suggestions: typing.Union[MetaOapg.properties.suggestions, str, schemas.Unset] = schemas.unset,
        riskLevel: typing.Union[MetaOapg.properties.riskLevel, str, schemas.Unset] = schemas.unset,
        softwareType: typing.Union[MetaOapg.properties.softwareType, str, schemas.Unset] = schemas.unset,
        currentReleases: typing.Union[MetaOapg.properties.currentReleases, str, schemas.Unset] = schemas.unset,
        managedBy: typing.Union[MetaOapg.properties.managedBy, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SoftwareGroup':
        return super().__new__(
            cls,
            *_args,
            assetCount=assetCount,
            sourceId=sourceId,
            sourceSystemId=sourceSystemId,
            selectedRelease=selectedRelease,
            productFamily=productFamily,
            softwareGroupName=softwareGroupName,
            softwareGroupId=softwareGroupId,
            suggestionId=suggestionId,
            suggestions=suggestions,
            riskLevel=riskLevel,
            softwareType=softwareType,
            currentReleases=currentReleases,
            managedBy=managedBy,
            _configuration=_configuration,
            **kwargs,
        )