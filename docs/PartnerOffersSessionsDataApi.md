# pxcloud_api_client.PartnerOffersSessionsDataApi

All URIs are relative to *https://api.pxcloud.cisco.com/sandbox*

Method | HTTP request | Description
------------- | ------------- | -------------
[**partner_offers_sessions**](PartnerOffersSessionsDataApi.md#partner_offers_sessions) | **GET** /v1/partnerOffersSessions | Get Partner Offers Session data


# **partner_offers_sessions**
> PartnerOfferWithSessions partner_offers_sessions()

Get Partner Offers Session data

Get one or more partner offers data along with all the session details of the partner offer.

### Example

* OAuth Authentication (oAuth2):

```python
import time
import pxcloud_api_client
from pxcloud_api_client.api import partner_offers_sessions_data_api
from pxcloud_api_client.model.error_response import ErrorResponse
from pxcloud_api_client.model.partner_offer_with_sessions import PartnerOfferWithSessions
from pprint import pprint
# Defining the host is optional and defaults to https://api.pxcloud.cisco.com/sandbox
# See configuration.py for a list of all supported configuration parameters.
configuration = pxcloud_api_client.Configuration(
    host = "https://api.pxcloud.cisco.com/sandbox"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oAuth2
configuration = pxcloud_api_client.Configuration(
    host = "https://api.pxcloud.cisco.com/sandbox"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pxcloud_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = partner_offers_sessions_data_api.PartnerOffersSessionsDataApi(api_client)
    customer_id = "customerId_example" # str | Customer Id's for filtering the results (optional)
    max = 10 # int | No of max rows in a page. Default value is 10 (optional) if omitted the server will use the default value of 10
    offer_id = "offerId_example" # str | published Asset Id from Path Params (optional)
    offer_status = "offerStatus_example" # str | Status for filtering the results (optional)
    offer_type = "offerType_example" # str | Asset Type for filtering the results (optional)
    offset = 0 # int | Offset to consider the starting record. Default value is 0 (optional) if omitted the server will use the default value of 0
    partner_id = 1 # int | Partner ID for filtering the results (optional)
    success_track_id = "successTrackId_example" # str | Solution Id field for filtering the results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Partner Offers Session data
        api_response = api_instance.partner_offers_sessions(customer_id=customer_id, max=max, offer_id=offer_id, offer_status=offer_status, offer_type=offer_type, offset=offset, partner_id=partner_id, success_track_id=success_track_id)
        pprint(api_response)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling PartnerOffersSessionsDataApi->partner_offers_sessions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| Customer Id&#39;s for filtering the results | [optional]
 **max** | **int**| No of max rows in a page. Default value is 10 | [optional] if omitted the server will use the default value of 10
 **offer_id** | **str**| published Asset Id from Path Params | [optional]
 **offer_status** | **str**| Status for filtering the results | [optional]
 **offer_type** | **str**| Asset Type for filtering the results | [optional]
 **offset** | **int**| Offset to consider the starting record. Default value is 0 | [optional] if omitted the server will use the default value of 0
 **partner_id** | **int**| Partner ID for filtering the results | [optional]
 **success_track_id** | **str**| Solution Id field for filtering the results | [optional]

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
**200** | Successfully retrieved results |  -  |
**401** | Unauthorized |  -  |
**403** | Operation forbidden due to business policies |  -  |
**404** | Not Found |  -  |
**500** | Error during retrieving Published Parner Assets |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

