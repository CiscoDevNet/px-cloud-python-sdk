# SoftwareGroupSuggestions


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**suggestions_interval** | **str** | How often, in months, Cisco software release suggestions will be provided. The customer can configure this value in CX Cloud. | [optional] 
**suggestion_updated_date** | **date** | Date the machine learning suggestions were updated for the Software Group | [optional] 
**suggestion_selected_date** | **date** | Date the customer selected a suggested Cisco software release in CX Cloud | [optional] 
**release_summary** | [**[ReleaseSummary]**](ReleaseSummary.md) | List of the following Cisco software releases for the Software Group - • Latest release available from Cisco Software Central • Suggested releases • Cisco DNA Center golden release • Cisco DNA Center Compatibility Matrix minimum release | [optional] 
**suggestion_summaries** | [**[SuggestionSummary]**](SuggestionSummary.md) | Information about the Cisco software releases running on, and suggested for, the assets in the Software Group | [optional] 
**software_group_risk_trend** | [**[SoftwareGroupRisk]**](SoftwareGroupRisk.md) | List of weekly risk scores for the current Cisco software releases calculated over a period of time | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


