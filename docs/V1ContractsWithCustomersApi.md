# pxcloud_api_client.V1ContractsWithCustomersApi

All URIs are relative to *https://api-cx.cisco.com/px*

Method | HTTP request | Description
------------- | ------------- | -------------
[**contracts_with_customers**](V1ContractsWithCustomersApi.md#contracts_with_customers) | **GET** /v1/contractsWithCustomers | Get the Outbound Contracts With Customers


# **contracts_with_customers**
> ContractsV2Response contracts_with_customers()

Get the Outbound Contracts With Customers

### Example

* OAuth Authentication (oAuth2):

```python
import time
import pxcloud_api_client
from pxcloud_api_client.api import v1_contracts_with_customers_api
from pxcloud_api_client.model.error_response import ErrorResponse
from pxcloud_api_client.model.contracts_v2_response import ContractsV2Response
from pprint import pprint
# Defining the host is optional and defaults to https://api-cx.cisco.com/px
# See configuration.py for a list of all supported configuration parameters.
configuration = pxcloud_api_client.Configuration(
    host = "https://api-cx.cisco.com/px"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oAuth2
configuration = pxcloud_api_client.Configuration(
    host = "https://api-cx.cisco.com/px"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pxcloud_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = v1_contracts_with_customers_api.V1ContractsWithCustomersApi(api_client)
    max = 1 # int |  (optional)
    offset = 1 # int |  (optional)
    customer_id = "customerId_example" # str | customerId (optional)
    customer_gu_name = "customerGUName_example" # str | customerGUName (optional)
    success_track_id = 1 # int | successTrackId (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the Outbound Contracts With Customers
        api_response = api_instance.contracts_with_customers(max=max, offset=offset, customer_id=customer_id, customer_gu_name=customer_gu_name, success_track_id=success_track_id)
        pprint(api_response)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling V1ContractsWithCustomersApi->contracts_with_customers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **max** | **int**|  | [optional]
 **offset** | **int**|  | [optional]
 **customer_id** | **str**| customerId | [optional]
 **customer_gu_name** | **str**| customerGUName | [optional]
 **success_track_id** | **int**| successTrackId | [optional]

### Return type

[**ContractsV2Response**](ContractsV2Response.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully Fetched Contract Details |  * Link - &lt;https://api-cx.cisco.com/px/v2/contracts?offset&#x3D;20&amp;max&#x3D;10&gt;; rel&#x3D;\&quot;next\&quot;, &lt;https://api-cx.cisco.com/px/v2/contracts?offset&#x3D;0&amp;max&#x3D;10&gt;; rel&#x3D;\&quot;prev\&quot; <br>  |
**400** | Bad Input |  * Date -  <br>  |
**401** | Unauthorized |  * Date -  <br>  |
**403** | Forbidden |  * Date -  <br>  |
**404** | Entity Not Found |  * Date -  <br>  |
**500** | Error during fetch |  * Date -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

