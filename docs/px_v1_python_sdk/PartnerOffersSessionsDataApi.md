# openapi_client.PartnerOffersSessionsDataApi

All URIs are relative to *https://api.pxcloud-stg.cisco.com/torii*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_partner_offers_sessions**](PartnerOffersSessionsDataApi.md#get_partner_offers_sessions) | **GET** /v1/partnerOffersSessions | Get Info about Partner Offers Sessions


# **get_partner_offers_sessions**
> PartnerOfferWithSessions get_partner_offers_sessions()

Get Info about Partner Offers Sessions

Information about Partner offers sessions - Ask the Experts and Accelerator

### Example

* OAuth Authentication (oAuth2):

```python
import time
import openapi_client
from openapi_client.api import partner_offers_sessions_data_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.partner_offer_with_sessions import PartnerOfferWithSessions
from pprint import pprint
# Defining the host is optional and defaults to https://api.pxcloud-stg.cisco.com/torii
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.pxcloud-stg.cisco.com/torii"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oAuth2
configuration = openapi_client.Configuration(
    host = "https://api.pxcloud-stg.cisco.com/torii"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = partner_offers_sessions_data_api.PartnerOffersSessionsDataApi(api_client)
    customer_id = [
        "customerId_example",
    ] # [str] | Customer Id's for filtering the results (optional)
    offer_id = "offerId_example" # str | published Asset Id from Path Params (optional)
    offer_status = [
        "offerStatus_example",
    ] # [str] | Status for filtering the results (optional)
    offer_type = [
        "offerType_example",
    ] # [str] | Asset Type for filtering the results (optional)
    page = 1 # int | Page number. Default value is 1 (optional) if omitted the server will use the default value of 1
    pagination_required = True # bool | Pagination data required flag (optional) if omitted the server will use the default value of True
    partner_id = [
        1,
    ] # [int] | Partner ID for filtering the results (optional)
    rows = 10 # int | No of rows in a page. Default value is 10 and the maximum rows allowed per page is 100 (optional) if omitted the server will use the default value of 10
    success_track_id = [
        "successTrackId_example",
    ] # [str] | Solution Id field for filtering the results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Info about Partner Offers Sessions
        api_response = api_instance.get_partner_offers_sessions(customer_id=customer_id, offer_id=offer_id, offer_status=offer_status, offer_type=offer_type, page=page, pagination_required=pagination_required, partner_id=partner_id, rows=rows, success_track_id=success_track_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PartnerOffersSessionsDataApi->get_partner_offers_sessions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **[str]**| Customer Id&#39;s for filtering the results | [optional]
 **offer_id** | **str**| published Asset Id from Path Params | [optional]
 **offer_status** | **[str]**| Status for filtering the results | [optional]
 **offer_type** | **[str]**| Asset Type for filtering the results | [optional]
 **page** | **int**| Page number. Default value is 1 | [optional] if omitted the server will use the default value of 1
 **pagination_required** | **bool**| Pagination data required flag | [optional] if omitted the server will use the default value of True
 **partner_id** | **[int]**| Partner ID for filtering the results | [optional]
 **rows** | **int**| No of rows in a page. Default value is 10 and the maximum rows allowed per page is 100 | [optional] if omitted the server will use the default value of 10
 **success_track_id** | **[str]**| Solution Id field for filtering the results | [optional]

### Return type

[**PartnerOfferWithSessions**](PartnerOfferWithSessions.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response |  * Date -  <br>  |
**400** | Bad Request |  * Date -  <br>  |
**403** | Forbidden |  * Date -  <br>  |
**500** | Internal server error |  * Date -  <br>  |
**503** | Service Unavailable |  * Date -  <br>  |
**504** | Gateway timeout |  * Date -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

