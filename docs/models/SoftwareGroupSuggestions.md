# pxcloud_api_client.pxcloud_api_client.software_group_suggestions.SoftwareGroupSuggestions

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**suggestionsInterval** | str,  | str,  | How often, in months, Cisco software release suggestions will be provided. The customer can configure this value in CX Cloud. | [optional] 
**suggestionUpdatedDate** | str, date,  | str,  | Date the machine learning suggestions were updated for the Software Group | [optional] value must conform to RFC-3339 full-date YYYY-MM-DD
**suggestionSelectedDate** | str, date,  | str,  | Date the customer selected a suggested Cisco software release in CX Cloud | [optional] value must conform to RFC-3339 full-date YYYY-MM-DD
**[releaseSummary](#releaseSummary)** | list, tuple,  | tuple,  | List of the following Cisco software releases for the Software Group - • Latest release available from Cisco Software Central • Suggested releases • Cisco DNA Center golden release • Cisco DNA Center Compatibility Matrix minimum release | [optional] 
**[suggestionSummaries](#suggestionSummaries)** | list, tuple,  | tuple,  | Information about the Cisco software releases running on, and suggested for, the assets in the Software Group | [optional] 
**[softwareGroupRiskTrend](#softwareGroupRiskTrend)** | list, tuple,  | tuple,  | List of weekly risk scores for the current Cisco software releases calculated over a period of time | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# releaseSummary

List of the following Cisco software releases for the Software Group - • Latest release available from Cisco Software Central • Suggested releases • Cisco DNA Center golden release • Cisco DNA Center Compatibility Matrix minimum release

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of the following Cisco software releases for the Software Group - • Latest release available from Cisco Software Central • Suggested releases • Cisco DNA Center golden release • Cisco DNA Center Compatibility Matrix minimum release | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ReleaseSummary**](ReleaseSummary.md) | [**ReleaseSummary**](ReleaseSummary.md) | [**ReleaseSummary**](ReleaseSummary.md) |  | 

# suggestionSummaries

Information about the Cisco software releases running on, and suggested for, the assets in the Software Group

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Information about the Cisco software releases running on, and suggested for, the assets in the Software Group | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**SuggestionSummary**](SuggestionSummary.md) | [**SuggestionSummary**](SuggestionSummary.md) | [**SuggestionSummary**](SuggestionSummary.md) |  | 

# softwareGroupRiskTrend

List of weekly risk scores for the current Cisco software releases calculated over a period of time

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of weekly risk scores for the current Cisco software releases calculated over a period of time | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**SoftwareGroupRisk**](SoftwareGroupRisk.md) | [**SoftwareGroupRisk**](SoftwareGroupRisk.md) | [**SoftwareGroupRisk**](SoftwareGroupRisk.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

