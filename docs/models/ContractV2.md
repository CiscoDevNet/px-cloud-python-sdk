# pxcloud_api_client.pxcloud_api_client.contract_v2.ContractV2

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**contractNumber** | str,  | str,  |  | [optional] 
**contractStatus** | str,  | str,  |  | [optional] 
**contractValue** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**coverageStartDate** | str,  | str,  |  | [optional] 
**coverageEndDate** | str,  | str,  |  | [optional] 
**[customerDetails](#customerDetails)** | list, tuple,  | tuple,  |  | [optional] 
**serviceLevel** | str,  | str,  |  | [optional] 
**[successTrackIds](#successTrackIds)** | list, tuple,  | tuple,  |  | [optional] 
**onboardedStatus** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# customerDetails

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**CustomerDetails**](CustomerDetails.md) | [**CustomerDetails**](CustomerDetails.md) | [**CustomerDetails**](CustomerDetails.md) |  | 

# successTrackIds

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

