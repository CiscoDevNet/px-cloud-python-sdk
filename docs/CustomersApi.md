# pxcloud_api_client.CustomersApi

All URIs are relative to *https://api-cx.cisco.com/px*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customers**](CustomersApi.md#customers) | **GET** /v1/customers | Fetch list of customers paginated for a given partner Id


# **customers**
> CustomerResponse customers()

Fetch list of customers paginated for a given partner Id

### Example

* OAuth Authentication (oAuth2):

```python
import time
import pxcloud_api_client
from pxcloud_api_client.api import customers_api
from pxcloud_api_client.model.error_response import ErrorResponse
from pxcloud_api_client.model.customer_response import CustomerResponse
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
    api_instance = customers_api.CustomersApi(api_client)
    max = 1 # int |  (optional)
    offset = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch list of customers paginated for a given partner Id
        api_response = api_instance.customers(max=max, offset=offset)
        pprint(api_response)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling CustomersApi->customers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **max** | **int**|  | [optional]
 **offset** | **int**|  | [optional]

### Return type

[**CustomerResponse**](CustomerResponse.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully Fetched list of customers for a given partner Id |  * Link - &lt;https://api-cx.cisco.com/px/v2/contracts?offset&#x3D;20&amp;max&#x3D;10&gt;; rel&#x3D;\&quot;next\&quot;, &lt;https://api-cx.cisco.com/px/v2/contracts?offset&#x3D;0&amp;max&#x3D;10&gt;; rel&#x3D;\&quot;prev\&quot; <br>  |
**400** | Bad Request |  * Date -  <br>  |
**403** | Forbidden |  * Date -  <br>  |
**500** | Internal server error |  * Date -  <br>  |
**503** | Service Unavailable |  * Date -  <br>  |
**504** | Gateway timeout |  * Date -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

