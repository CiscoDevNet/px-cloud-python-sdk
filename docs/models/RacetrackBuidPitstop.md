# pxcloud_api_client.pxcloud_api_client.racetrack_buid_pitstop.RacetrackBuidPitstop

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[pitstopActions](#pitstopActions)** | list, tuple,  | tuple,  |  | 
**name** | str,  | str,  |  | must be one of ["onboard", "implement", "use", "engage", "adopt", "optimize", ] 
**description** | str,  | str,  | Brief description of the pitstop | 
**isComplete** | bool,  | BoolClass,  | When set to &#x60;true&#x60; it indicates that the pre-requisites for advancing to the next pitstop have been met by the customer. This determination may be done through manual input (customer) or automated (LifecycleJourney). | 
**completionPercentage** | decimal.Decimal, int,  | decimal.Decimal,  | Percentage completed checklist actions. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# pitstopActions

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**RacetrackBuidPitstopAction**](RacetrackBuidPitstopAction.md) | [**RacetrackBuidPitstopAction**](RacetrackBuidPitstopAction.md) | [**RacetrackBuidPitstopAction**](RacetrackBuidPitstopAction.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

