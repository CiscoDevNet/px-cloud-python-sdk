# pxcloud_api_client.pxcloud_api_client.asset.Asset

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**deploymentStatus** | str,  | str,  | Value that indicates whether a suggested Cisco software release has been selected by the customer in CX Cloud to use for the next software update on the asset - • None- A suggested release has not been selected • Upgrade- A suggested release has been selected • Production- A suggested release is already running on the asset | [optional] 
**assetName** | str,  | str,  | Unique asset name | [optional] 
**ipAddress** | str,  | str,  | IP address assigned to the asset | [optional] 
**selectedRelease** | str,  | str,  | The suggested Cisco software release the customer selected to use for the next software update on the asset | [optional] 
**softwareType** | str,  | str,  | Cisco software type running on the asset, for example IOS-XE | [optional] 
**currentRelease** | str,  | str,  | Cisco software release running on the asset | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

