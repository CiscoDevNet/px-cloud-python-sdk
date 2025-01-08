# pxcloud_api_client.pxcloud_api_client.faults_summary.FaultsSummary

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**title** | str,  | str,  | Title of the fault | [optional] 
**suggestion** | str,  | str,  | Suggestion provided by CX Cloud to help address the fault | [optional] 
**description** | str,  | str,  | Detailed description of the fault | [optional] 
**condition** | str,  | str,  | The facility, condition severity, and mnemonic portion of the fault message | [optional] 
**category** | str,  | str,  | The category assigned to the fault by CX Cloud, such as System, CPU-Memory, Services, and Environment | [optional] 
**supportedProductSeries** | str,  | str,  | Cisco product families the fault applies to | [optional] 
**impact** | str,  | str,  | The possible effect the fault has on the assets and network | [optional] 
**severity** | str,  | str,  | Severity value assigned by CX Cloud | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

