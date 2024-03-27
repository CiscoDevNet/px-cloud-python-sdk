# pxcloud_api_client.pxcloud_api_client.faults.Faults

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**severity** | str,  | str,  | Severity value assigned by CX Cloud | [optional] 
**title** | str,  | str,  | Title of the fault | [optional] 
**lastOccurence** | str, datetime,  | str,  | Date the fault last occurred | [optional] value must conform to RFC-3339 date-time
**condition** | str,  | str,  | The facility, condition severity, and mnemonic portion of the fault message | [optional] 
**caseAutomation** | str,  | str,  | Indicates whether support case automation has been enabled for the fault | [optional] must be one of ["enabled", "disabled", ] 
**faultId** | decimal.Decimal, int,  | decimal.Decimal,  | Unique identifier used in CX Cloud to identify the fault | [optional] 
**category** | str,  | str,  | The category assigned to the fault by CX Cloud, for example System, CPU-Memory, Services, and Environment | [optional] 
**openCases** | decimal.Decimal, int,  | decimal.Decimal,  | Number of Cisco support cases automatically created for the fault | [optional] 
**affectedAssets** | decimal.Decimal, int,  | decimal.Decimal,  | Number of assets affected by the fault | [optional] 
**occurences** | decimal.Decimal, int,  | decimal.Decimal,  | Number of times the fault occurred | [optional] 
**ignoredAssets** | decimal.Decimal, int,  | decimal.Decimal,  | Number of assets the fault is ignored for | [optional] 
**mgmtSystemType** | str,  | str,  |  | [optional] 
**mgmtSystemAddr** | str,  | str,  |  | [optional] 
**mgmtSystemHostname** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

