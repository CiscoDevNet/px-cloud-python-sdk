# pxcloud_api_client.pxcloud_api_client.racetrack_usecase.RacetrackUsecase

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**adoptionPercentage** | decimal.Decimal, int,  | decimal.Decimal,  | Percentage completed checklist actions across all pitstops. | 
**name** | str,  | str,  | Usecase name | 
**description** | str,  | str,  | Usecase description | 
**[pitstops](#pitstops)** | list, tuple,  | tuple,  |  | 
**usecaseId** | str,  | str,  | Usecase description | 
**currentPitstop** | str,  | str,  | The current customer&#x27;s pitstop for this solution&#x27;s use case | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# pitstops

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**RacetrackBuidPitstop**](RacetrackBuidPitstop.md) | [**RacetrackBuidPitstop**](RacetrackBuidPitstop.md) | [**RacetrackBuidPitstop**](RacetrackBuidPitstop.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

