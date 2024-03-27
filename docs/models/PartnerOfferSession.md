# pxcloud_api_client.pxcloud_api_client.partner_offer_session.PartnerOfferSession

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[attendeeList](#attendeeList)** | list, tuple,  | tuple,  |  | [optional] 
**businessOutcome** | str,  | str,  |  | [optional] 
**createdDate** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**modifiedDate** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**preferredSlot** | str,  | str,  |  | [optional] 
**reasonForInterest** | str,  | str,  |  | [optional] 
**sessionId** | str,  | str,  |  | [optional] 
**status** | str,  | str,  |  | [optional] 
**timezone** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# attendeeList

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**PartnerOfferAttendee**](PartnerOfferAttendee.md) | [**PartnerOfferAttendee**](PartnerOfferAttendee.md) | [**PartnerOfferAttendee**](PartnerOfferAttendee.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

