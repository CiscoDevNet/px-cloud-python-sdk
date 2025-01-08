# pxcloud_api_client.pxcloud_api_client.assets_with_violations.AssetsWithViolations

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**sourceSystemId** | str,  | str,  |  | [optional] 
**assetId** | str,  | str,  |  | [optional] 
**assetName** | str,  | str,  |  | [optional] 
**ipAddress** | str,  | str,  |  | [optional] 
**softwareType** | str,  | str,  |  | [optional] 
**serialNumber** | str,  | str,  |  | [optional] 
**softwareRelease** | str,  | str,  |  | [optional] 
**severity** | str,  | str,  |  | [optional] 
**lastChecked** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**violationCount** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**scanStatus** | bool,  | BoolClass,  |  | [optional] 
**severityId** | str,  | str,  |  | [optional] 
**role** | str,  | str,  |  | [optional] 
**[assetGroups](#assetGroups)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# assetGroups

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

