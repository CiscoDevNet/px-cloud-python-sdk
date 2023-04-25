# Faults


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**severity** | **str** | Severity value assigned by CX Cloud | [optional] 
**title** | **str** | Title of the fault | [optional] 
**last_occurence** | **datetime** | Date the fault last occurred | [optional] 
**condition** | **str** | The facility, condition severity, and mnemonic portion of the fault message | [optional] 
**case_automation** | **str** | Indicates whether support case automation has been enabled for the fault | [optional] 
**fault_id** | **int** | Unique identifier used in CX Cloud to identify the fault | [optional] 
**category** | **str** | The category assigned to the fault by CX Cloud, for example System, CPU-Memory, Services, and Environment | [optional] 
**open_cases** | **int** | Number of Cisco support cases automatically created for the fault | [optional] 
**affected_assets** | **int** | Number of assets affected by the fault | [optional] 
**occurences** | **int** | Number of times the fault occurred | [optional] 
**ignored_assets** | **int** | Number of assets the fault is ignored for | [optional] 
**mgmt_system_type** | **str** |  | [optional] 
**mgmt_system_addr** | **str** |  | [optional] 
**mgmt_system_hostname** | **str** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


