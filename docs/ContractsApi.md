# pxcloud_api_client.ContractsApi

All URIs are relative to *https://api-cx.cisco.com/px/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**contract_details**](ContractsApi.md#contract_details) | **GET** /v1/contract/details | Get the list of contracts Details from flat table. It supports pagination , filtering and sorting
[**contracts**](ContractsApi.md#contracts) | **GET** /v1/contracts | Get the list of customer contracts for a particular partner. It supports pagination with offset and limit parameters , filtering and sorting


# **contract_details**
> ContractDetailsResponse contract_details(contract_number)

Get the list of contracts Details from flat table. It supports pagination , filtering and sorting

### Example

* OAuth Authentication (oAuth2):

```python
import time
import pxcloud_api_client
from pxcloud_api_client.api import contracts_api
from pxcloud_api_client.model.error_response import ErrorResponse
from pxcloud_api_client.model.contract_details_response import ContractDetailsResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-cx.cisco.com/px/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = pxcloud_api_client.Configuration(
    host = "https://api-cx.cisco.com/px/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oAuth2
configuration = pxcloud_api_client.Configuration(
    host = "https://api-cx.cisco.com/px/v1"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pxcloud_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = contracts_api.ContractsApi(api_client)
    contract_number = 1 # int | contractNumber
    max = 1 # int |  (optional)
    offset = 1 # int |  (optional)
    customer_id = "customerId_example" # str | customerId (optional)
    component_type = "componentType_example" # str | componentType (optional)
    contract_line_item_type = "contractLineItemType_example" # str | contractLineItemType (optional)
    success_track_id = "successTrackId_example" # str | successTrackId (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get the list of contracts Details from flat table. It supports pagination , filtering and sorting
        api_response = api_instance.contract_details(contract_number)
        pprint(api_response)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling ContractsApi->contract_details: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the list of contracts Details from flat table. It supports pagination , filtering and sorting
        api_response = api_instance.contract_details(contract_number, max=max, offset=offset, customer_id=customer_id, component_type=component_type, contract_line_item_type=contract_line_item_type, success_track_id=success_track_id)
        pprint(api_response)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling ContractsApi->contract_details: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_number** | **int**| contractNumber |
 **max** | **int**|  | [optional]
 **offset** | **int**|  | [optional]
 **customer_id** | **str**| customerId | [optional]
 **component_type** | **str**| componentType | [optional]
 **contract_line_item_type** | **str**| contractLineItemType | [optional]
 **success_track_id** | **str**| successTrackId | [optional]

### Return type

[**ContractDetailsResponse**](ContractDetailsResponse.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully Fetched Contract Details for Given Partner |  * Link - &lt;https://api-cx.cisco.com/px/v2/contracts?offset&#x3D;20&amp;max&#x3D;10&gt;; rel&#x3D;\&quot;next\&quot;, &lt;https://api-cx.cisco.com/px/v2/contracts?offset&#x3D;0&amp;max&#x3D;10&gt;; rel&#x3D;\&quot;prev\&quot; <br>  |
**400** | Bad Input |  * Date -  <br>  |
**401** | Unauthorized |  * Date -  <br>  |
**403** | Forbidden |  * Date -  <br>  |
**404** | Entity Not Found |  * Date -  <br>  |
**500** | Error during fetch |  * Date -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contracts**
> ContractResponse contracts()

Get the list of customer contracts for a particular partner. It supports pagination with offset and limit parameters , filtering and sorting

### Example

* OAuth Authentication (oAuth2):

```python
import time
import pxcloud_api_client
from pxcloud_api_client.api import contracts_api
from pxcloud_api_client.model.error_response import ErrorResponse
from pxcloud_api_client.model.contract_response import ContractResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-cx.cisco.com/px/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = pxcloud_api_client.Configuration(
    host = "https://api-cx.cisco.com/px/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oAuth2
configuration = pxcloud_api_client.Configuration(
    host = "https://api-cx.cisco.com/px/v1"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pxcloud_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = contracts_api.ContractsApi(api_client)
    max = 1 # int |  (optional)
    offset = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the list of customer contracts for a particular partner. It supports pagination with offset and limit parameters , filtering and sorting
        api_response = api_instance.contracts(max=max, offset=offset)
        pprint(api_response)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling ContractsApi->contracts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **max** | **int**|  | [optional]
 **offset** | **int**|  | [optional]

### Return type

[**ContractResponse**](ContractResponse.md)

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

