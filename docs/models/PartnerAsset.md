# pxcloud_api_client.pxcloud_api_client.partner_asset.PartnerAsset

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**additionalInfo** | str,  | str,  |  | [optional] 
**assetId** | str,  | str,  |  | [optional] 
**assetType** | str,  | str,  |  | [optional] 
**complies** | bool,  | BoolClass,  |  | [optional] 
**createdBy** | str,  | str,  |  | [optional] 
**[customer](#customer)** | list, tuple,  | tuple,  |  | [optional] 
**customerRating** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] value must be a 64 bit float
**description** | str,  | str,  |  | [optional] 
**duration** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**imageFileName** | str,  | str,  |  | [optional] 
**imageUrl** | str,  | str,  |  | [optional] 
**lastUpdated** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**[mapping](#mapping)** | list, tuple,  | tuple,  |  | [optional] 
**partnerId** | str,  | str,  |  | [optional] 
**partnerName** | str,  | str,  |  | [optional] 
**partnerUserEmailId** | str,  | str,  |  | [optional] 
**partnerUserFirstName** | str,  | str,  |  | [optional] 
**partnerUserLastName** | str,  | str,  |  | [optional] 
**pitstops** | str,  | str,  |  | [optional] 
**recordingUrl** | str,  | str,  |  | [optional] 
**[sessions](#sessions)** | list, tuple,  | tuple,  |  | [optional] 
**solutions** | str,  | str,  |  | [optional] 
**status** | str,  | str,  |  | [optional] 
**technologyArea** | str,  | str,  |  | [optional] 
**title** | str,  | str,  |  | [optional] 
**usecases** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# customer

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# mapping

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**SolutionMapping**](SolutionMapping.md) | [**SolutionMapping**](SolutionMapping.md) | [**SolutionMapping**](SolutionMapping.md) |  | 

# sessions

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**AssetSession**](AssetSession.md) | [**AssetSession**](AssetSession.md) | [**AssetSession**](AssetSession.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

