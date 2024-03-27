# pxcloud_api_client.pxcloud_api_client.software_group_bugs.SoftwareGroupBugs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**bugId** | str,  | str,  | Unique identifier of the bug | [optional] 
**severity** | str,  | str,  | Severity level of the bug. Can be High, Medium, or Low. | [optional] 
**status** | str,  | str,  | Status of the bug. Can be Exposed or Not Exposed. | [optional] 
**title** | str,  | str,  | Title of the bug. For example, CiscoBug-2020-x8k2, or Cisco IOS XE Software Command Injection Vulnerability. | [optional] 
**affectedAssets** | str,  | str,  | Number of assets affected by the bug. | [optional] 
**features** | str,  | str,  | Number of features affected by the bug. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

