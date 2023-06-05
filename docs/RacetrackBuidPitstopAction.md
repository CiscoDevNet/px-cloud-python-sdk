# RacetrackBuidPitstopAction


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A label identifying the action to be completed by the customer.  A set of actions identifies the exit criteria that must be met before proceeding to the next stage | 
**description** | **str** | A brief description of the action to be taken by the customer | 
**is_manual_check_allowed** | **bool** | When set to &#x60;true&#x60; it indicates that this action may be manually checked as completed/met. Otherwise completion must be automatically determined via analysis of collected data | 
**is_complete** | **bool** | When set to &#x60;true&#x60; it indicates that this action has been completed by the customer.  This is the reported status and it is set from one of &#x60;isActionCompleteAuto&#x60; (auto determined) or &#x60;isActionCompleteManual&#x60; (manually determined). Manual input takes precedence over the automated means and once set to manual it cannot be changed by automated means. It requires manual input | 
**update_method** | **str** | The method by which the the completion status was updated (&#x60;MANUAL&#x60; user input, &#x60;AUTO&#x60; Lifecycle Journey). This value must be set when &#x60;isActionComplete&#x60; is set to &#x60;true&#x60; and cleared if &#x60;isActionComplte&#x60; is set to &#x60;false&#x60; | 
**is_complete_auto** | **bool** | When set to &#x60;true&#x60; it indicates that this action was found to be completed/met through automated means.  An action manually set to completion takes precedence over the automated means.  An action set to completion via automated means may be manually overridden | 
**is_complete_manual** | **bool** | When set to &#x60;true&#x60; it indicates that action was manually set to completed / met | 
**is_manaual_override** | **bool** | When set to &#x60;true&#x60; it indicates that the automated result was overriden manually by a user | 
**tooltips** | [**[RacetrackTooltip]**](RacetrackTooltip.md) |  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


