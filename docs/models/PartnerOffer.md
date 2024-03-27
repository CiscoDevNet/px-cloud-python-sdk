# pxcloud_api_client.pxcloud_api_client.partner_offer.PartnerOffer

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**accTimeRequiredHours** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] value must be a 32 bit float
**created** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**createdBy** | str,  | str,  |  | [optional] 
**[customerList](#customerList)** | list, tuple,  | tuple,  |  | [optional] 
**customerRating** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] value must be a 64 bit float
**description** | str,  | str,  |  | [optional] 
**duration** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**imageFileName** | str,  | str,  |  | [optional] 
**language** | str,  | str,  |  | [optional] 
**lastPublishedDate** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**logoFileName** | str,  | str,  |  | [optional] 
**[mapping](#mapping)** | list, tuple,  | tuple,  |  | [optional] 
**modified** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**modifiedBy** | str,  | str,  |  | [optional] 
**noOfAttendees** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**offerId** | str,  | str,  |  | [optional] 
**offerType** | str,  | str,  |  | [optional] 
**publishedToAllCustomers** | bool,  | BoolClass,  |  | [optional] 
**status** | str,  | str,  |  | [optional] 
**title** | str,  | str,  |  | [optional] 
**userEmailId** | str,  | str,  |  | [optional] 
**userFirstName** | str,  | str,  |  | [optional] 
**userLastName** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# customerList

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**CustomerInfo**](CustomerInfo.md) | [**CustomerInfo**](CustomerInfo.md) | [**CustomerInfo**](CustomerInfo.md) |  | 

# mapping

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**SuccessTrackMapping**](SuccessTrackMapping.md) | [**SuccessTrackMapping**](SuccessTrackMapping.md) | [**SuccessTrackMapping**](SuccessTrackMapping.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

