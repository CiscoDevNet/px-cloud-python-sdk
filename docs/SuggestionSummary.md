# SuggestionSummary


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expected_software_group_risk** | **str** | Current risk score of the Cisco software release, which is the level of exposure the software release has to bugs, security advisories, and field notices. The risk score is used to make software suggestions intended to minimize risk for assets in the Software Group. | [optional] 
**expected_software_group_risk_category** | **str** | Risk level of the Cisco software release based on its risk score. The risk level can be High, Medium, or Low. | [optional] 
**machine_suggestion_id** | **str** | Unique identifier of the suggestion | [optional] 
**name** | **str** | Value that indicates whether the Cisco software release is a current release or one of the suggested release options | [optional] 
**release_date** | **datetime** | Date the Cisco software image was released | [optional] 
**release** | **str** | Release of the Cisco software | [optional] 
**release_notes_url** | **str** | Public URL for the release notes of the Cisco software release | [optional] 
**bug_severity** | [**SuggestionSummaryBugSeverity**](SuggestionSummaryBugSeverity.md) |  | [optional] 
**advisories_severity** | [**SuggestionSummaryAdvisoriesSeverity**](SuggestionSummaryAdvisoriesSeverity.md) |  | [optional] 
**field_notice_severity** | [**SuggestionSummaryFieldNoticeSeverity**](SuggestionSummaryFieldNoticeSeverity.md) |  | [optional] 
**features_count** | [**SuggestionSummaryFeaturesCount**](SuggestionSummaryFeaturesCount.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


