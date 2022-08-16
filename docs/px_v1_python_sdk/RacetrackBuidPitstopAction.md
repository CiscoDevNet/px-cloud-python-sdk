# RacetrackBuidPitstopAction


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A label identifying the action to be completed by the customer.  A set of actions identifies the exit criteria that must be met before proceeding to the next stage | 
**description** | **str** | A brief description of the action to be taken by the customer | 
**is_manual_check_allowed** | **bool** | When set to true it indicates that this action may be manually checked as completed/met. Otherwise completion must be automatically determined via analysis of collected data | 
**is_complete** | **bool** | When set to true it indicates that this action has been completed by the customer.  This is the reported status and it is set from one of isActionCompleteAuto (Auto determined), isActionCompleteManual (Manually determined). Manual input takes precedence over the automated means and once set to manual it cannot be changed by automated means. It requires manual input | 
**update_method** | **str** | The method by which the the completion status was updated (MANUAL user input, AUTO Lifecycle Journey). This value must be set when isActionComplete is set to true and cleared if isActionComplte is set to false | 
**is_complete_auto** | **bool** | When set to true it indicates that this action was found to be completed/met through automated means.  An action manually set to completion takes precedence over the automated means.  An action set to completion via automated means may be manually overridden | 
**is_complete_manual** | **bool** | When set to true it indicates that action was manually set to completed / met | 
**is_manaual_override** | **bool** | When set to true it indicates that the automated result was overriden manually by a user | 
**tooltips** | [**[RacetrackTooltip]**](RacetrackTooltip.md) |  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


