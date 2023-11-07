# pxcloud_api_client.pxcloud_api_client.affected_assets.AffectedAssets

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**assetName** | str,  | str,  | Unique asset name | [optional] 
**productId** | str,  | str,  | Cisco product number of the asset | [optional] 
**caseNumber** | str,  | str,  | If case automation is enabled, this is the Cisco support case number created | [optional] 
**caseAction** | str,  | str,  | If case automation is enabled, this is the status of the Cisco support case request submitted by CX Cloud for the asset | [optional] 
**occurrences** | decimal.Decimal, int,  | decimal.Decimal,  | Number of times the fault occurred on the asset | [optional] 
**firstOccurrence** | str, datetime,  | str,  | Date the fault first occurred on the asset | [optional] value must conform to RFC-3339 date-time
**lastOccurrence** | str, datetime,  | str,  | Date the fault last occurred on the asset | [optional] value must conform to RFC-3339 date-time
**faultId** | decimal.Decimal, int,  | decimal.Decimal,  | Unique identifier used in CX Cloud to identify the fault | [optional] 
**serialNumber** | str,  | str,  | Unique Cisco serial number of the asset | [optional] 
**mgmtSystemType** | str,  | str,  |  | [optional] 
**mgmtSystemAddr** | str,  | str,  |  | [optional] 
**mgmtSystemHostname** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

