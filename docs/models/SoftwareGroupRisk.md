# pxcloud_api_client.pxcloud_api_client.software_group_risk.SoftwareGroupRisk

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**changeFromPrev** | decimal.Decimal, int, float,  | decimal.Decimal,  | The percentage the risk score has changed from the previous week | [optional] value must be a 64 bit float
**riskCategory** | str,  | str,  | Risk level of the Cisco software release based on its risk score. The risk level can be High, Medium, or Low. | [optional] 
**date** | str, date,  | str,  | Date the weekly risk score was calculated | [optional] value must conform to RFC-3339 full-date YYYY-MM-DD
**riskScore** | decimal.Decimal, int, float,  | decimal.Decimal,  | Risk score of the Cisco software release for the softwareGroupRiskTrend date | [optional] value must be a 64 bit float
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

