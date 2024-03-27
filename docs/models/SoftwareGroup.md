# pxcloud_api_client.pxcloud_api_client.software_group.SoftwareGroup

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**assetCount** | decimal.Decimal, int,  | decimal.Decimal,  | Number of assets in the Software Group | [optional] value must be a 32 bit integer
**sourceId** | str,  | str,  | IP address of the Cisco network management system that manages the assets in the Software Group | [optional] 
**sourceSystemId** | str,  | str,  | Unique identifier of the Cisco network management system that manages the assets in the Software Group | [optional] 
**selectedRelease** | str,  | str,  | The suggested Cisco software release the customer selected to use for the next software update on the assets in the Software Group | [optional] 
**productFamily** | str,  | str,  | Cisco product family of the assets in the Software Group, for example Cisco Catalyst 9300 Series Switches | [optional] 
**softwareGroupName** | str,  | str,  | Software Group name based on the Cisco product ID of the assets in the Software Group | [optional] 
**softwareGroupId** | str,  | str,  | Unique identifier used in CX Cloud to identify the Software Group | [optional] 
**suggestionId** | str,  | str,  |  | [optional] 
**suggestions** | str,  | str,  | Indicates whether Cisco software release suggestions are available for the Software Group | [optional] 
**riskLevel** | str,  | str,  | Risk level of the Software Group based on the risk scores of the current Cisco software releases in the Software Group. The risk level can be High, Medium, or Low. | [optional] 
**softwareType** | str,  | str,  | Cisco software type running on the assets in the Software Group, for example IOS-XE | [optional] 
**currentReleases** | str,  | str,  | The Cisco software releases running on assets in the Software Group | [optional] 
**managedBy** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

