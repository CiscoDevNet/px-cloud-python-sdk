# openapi_client.ContractsDataApi

All URIs are relative to *https://api.pxcloud-stg.cisco.com/torii*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetch_contracts_summary_using_get**](ContractsDataApi.md#fetch_contracts_summary_using_get) | **GET** /v2/contracts | Get the list of contracts summary


# **fetch_contracts_summary_using_get**
> DataPaginationResponse fetch_contracts_summary_using_get(success_track_id, puid)

Get the list of contracts summary

### Example

* OAuth Authentication (oAuth2):

```python
import time
import openapi_client
from openapi_client.api import contracts_data_api
from openapi_client.model.contracts_error_response import ContractsErrorResponse
from openapi_client.model.data_pagination_response import DataPaginationResponse
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
    api_instance = contracts_data_api.ContractsDataApi(api_client)
    success_track_id = 1 # int | successTrackId
    puid = 1 # int | puid
    customer_id = "customerId_example" # str | customerId (optional)
    gu_name = "guName_example" # str | guName (optional)
    limit = 1 # int |  (optional)
    offset = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get the list of contracts summary
        api_response = api_instance.fetch_contracts_summary_using_get(success_track_id, puid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ContractsDataApi->fetch_contracts_summary_using_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the list of contracts summary
        api_response = api_instance.fetch_contracts_summary_using_get(success_track_id, puid, customer_id=customer_id, gu_name=gu_name, limit=limit, offset=offset)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ContractsDataApi->fetch_contracts_summary_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **success_track_id** | **int**| successTrackId |
 **puid** | **int**| puid |
 **customer_id** | **str**| customerId | [optional]
 **gu_name** | **str**| guName | [optional]
 **limit** | **int**|  | [optional]
 **offset** | **int**|  | [optional]

### Return type

[**DataPaginationResponse**](DataPaginationResponse.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully Fetched Contract Summary for Given Partner |  * Date -  <br>  |
**400** | Bad Input |  * Date -  <br>  |
**401** | Unauthorized |  * Date -  <br>  |
**403** | Forbidden |  * Date -  <br>  |
**404** | Entity Not Found |  * Date -  <br>  |
**500** | Error during fetch |  * Date -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

