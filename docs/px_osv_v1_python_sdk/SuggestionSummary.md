# SuggestionSummary


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expected_software_group_risk** | **str** | Current risk score of the Cisco software release, which is the level of exposure the software release has to bugs, security advisories, and field notices. The risk score is used to make software suggestions intended to minimize risk for assets in the Software Group. | [optional] 
**expected_software_group_risk_category** | **str** | Risk level of the Cisco software release based on its risk score. The risk level can be High, Medium, or Low. | [optional] 
**suggestion_id** | **float** | Unique identifier of the suggestion | [optional] 
**name** | **str** | Value that indicates whether the Cisco software release is a current release or one of the suggested release options | [optional] 
**release_date** | **datetime** | Date the Cisco software image was released | [optional] 
**release** | **str** | Release of the Cisco software | [optional] 
**release_notes_url** | **str** | Public URL for the release notes of the Cisco software release | [optional] 
**bug_severity** | [**[SuggestionSummaryBugSeverityInner]**](SuggestionSummaryBugSeverityInner.md) | Number of bugs the Cisco software release is exposed to, and for suggested releases, the number of bugs the suggested release addresses | [optional] 
**advisories_severity** | [**[SuggestionSummaryAdvisoriesSeverityInner]**](SuggestionSummaryAdvisoriesSeverityInner.md) | Number of security advisories the current Cisco software releases are exposed to that are addressed by the suggested release | [optional] 
**field_notice_severity** | [**[SuggestionSummaryFieldNoticeSeverityInner]**](SuggestionSummaryFieldNoticeSeverityInner.md) | Number of field notices the current Cisco software releases are exposed to that are addressed by the suggested release | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


