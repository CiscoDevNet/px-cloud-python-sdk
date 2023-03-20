# pxcloud_api_client.FaultsApi

All URIs are relative to *https://api.pxcloud.cisco.com/torii*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fault_affected_assets**](FaultsApi.md#fault_affected_assets) | **GET** /v1/customers/{customerId}/insights/faults/{faultId}/affectedAssets | Affected Assets
[**fault_history**](FaultsApi.md#fault_history) | **GET** /v1/customers/{customerId}/insights/faults/{faultId}/affectedAssets/{assetName}/faultHistory | Assets Fault History
[**fault_summary**](FaultsApi.md#fault_summary) | **GET** /v1/customers/{customerId}/insights/faults/{faultId}/summary | Fault summary
[**faults**](FaultsApi.md#faults) | **GET** /v1/customers/{customerId}/insights/faults | Faults details


# **fault_affected_assets**
> AffectedAssetsResponse fault_affected_assets(success_track_id, customer_id, fault_id)

Affected Assets

Returns information about the customer assets affected by the fault, based on the fault signatureId and customerId provided

### Example

* OAuth Authentication (oAuth2):

```python
import time
import pxcloud_api_client
from pxcloud_api_client.api import faults_api
from pxcloud_api_client.model.error_response import ErrorResponse
from pxcloud_api_client.model.affected_assets_response import AffectedAssetsResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.pxcloud.cisco.com/torii
# See configuration.py for a list of all supported configuration parameters.
configuration = pxcloud_api_client.Configuration(
    host = "https://api.pxcloud.cisco.com/torii"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oAuth2
configuration = pxcloud_api_client.Configuration(
    host = "https://api.pxcloud.cisco.com/torii"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pxcloud_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = faults_api.FaultsApi(api_client)
    success_track_id = "successTrackId_example" # str | 
    customer_id = "customerId_example" # str | Unique identifier of the customer
    fault_id = 1 # int | Unique identifier used in CX Cloud to identify the fault
    days = 1 # int | The number of days to retrieve fault data for. This value can be 1, 7, 15, 30. The default is 1. (optional) if omitted the server will use the default value of 1
    offset = 1 # int | The number of items to skip before starting to collect the result set. The default value is 1. (optional) if omitted the server will use the default value of 1
    max = 10 # int | The maximum number of items to return. (optional) if omitted the server will use the default value of 10

    # example passing only required values which don't have defaults set
    try:
        # Affected Assets
        api_response = api_instance.fault_affected_assets(success_track_id, customer_id, fault_id)
        pprint(api_response)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling FaultsApi->fault_affected_assets: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Affected Assets
        api_response = api_instance.fault_affected_assets(success_track_id, customer_id, fault_id, days=days, offset=offset, max=max)
        pprint(api_response)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling FaultsApi->fault_affected_assets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **success_track_id** | **str**|  |
 **customer_id** | **str**| Unique identifier of the customer |
 **fault_id** | **int**| Unique identifier used in CX Cloud to identify the fault |
 **days** | **int**| The number of days to retrieve fault data for. This value can be 1, 7, 15, 30. The default is 1. | [optional] if omitted the server will use the default value of 1
 **offset** | **int**| The number of items to skip before starting to collect the result set. The default value is 1. | [optional] if omitted the server will use the default value of 1
 **max** | **int**| The maximum number of items to return. | [optional] if omitted the server will use the default value of 10

### Return type

[**AffectedAssetsResponse**](AffectedAssetsResponse.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Date -  <br>  |
**401** | Unauthorized |  * Date -  <br>  |
**403** | Forbidden |  * Date -  <br>  |
**404** | Not Found |  * Date -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fault_history**
> AssetsFaultHistoryResponse fault_history(success_track_id, customer_id, fault_id, asset_name)

Assets Fault History

Returns information about the occurrences of a fault on an asset based on the fault signatureId, asset name, and customerId provided

### Example

* OAuth Authentication (oAuth2):

```python
import time
import pxcloud_api_client
from pxcloud_api_client.api import faults_api
from pxcloud_api_client.model.error_response import ErrorResponse
from pxcloud_api_client.model.assets_fault_history_response import AssetsFaultHistoryResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.pxcloud.cisco.com/torii
# See configuration.py for a list of all supported configuration parameters.
configuration = pxcloud_api_client.Configuration(
    host = "https://api.pxcloud.cisco.com/torii"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oAuth2
configuration = pxcloud_api_client.Configuration(
    host = "https://api.pxcloud.cisco.com/torii"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pxcloud_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = faults_api.FaultsApi(api_client)
    success_track_id = "successTrackId_example" # str | 
    customer_id = "customerId_example" # str | Unique identifier of the customer
    fault_id = 1 # int | Unique identifier used in CX Cloud to identify the fault
    asset_name = "assetName_example" # str | Unique asset name
    days = 1 # int | The number of days to retrieve fault data for. This value can be 1, 7, 15, 30. The default is 1. (optional) if omitted the server will use the default value of 1

    # example passing only required values which don't have defaults set
    try:
        # Assets Fault History
        api_response = api_instance.fault_history(success_track_id, customer_id, fault_id, asset_name)
        pprint(api_response)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling FaultsApi->fault_history: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Assets Fault History
        api_response = api_instance.fault_history(success_track_id, customer_id, fault_id, asset_name, days=days)
        pprint(api_response)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling FaultsApi->fault_history: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **success_track_id** | **str**|  |
 **customer_id** | **str**| Unique identifier of the customer |
 **fault_id** | **int**| Unique identifier used in CX Cloud to identify the fault |
 **asset_name** | **str**| Unique asset name |
 **days** | **int**| The number of days to retrieve fault data for. This value can be 1, 7, 15, 30. The default is 1. | [optional] if omitted the server will use the default value of 1

### Return type

[**AssetsFaultHistoryResponse**](AssetsFaultHistoryResponse.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Date -  <br>  |
**401** | Unauthorized |  * Date -  <br>  |
**403** | Forbidden |  * Date -  <br>  |
**404** | Not Found |  * Date -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fault_summary**
> FaultsSummaryResponse fault_summary(success_track_id, customer_id, fault_id)

Fault summary

Returns detailed information for a fault based on the fault signatureId and customerId provided

### Example

* OAuth Authentication (oAuth2):

```python
import time
import pxcloud_api_client
from pxcloud_api_client.api import faults_api
from pxcloud_api_client.model.error_response import ErrorResponse
from pxcloud_api_client.model.faults_summary_response import FaultsSummaryResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.pxcloud.cisco.com/torii
# See configuration.py for a list of all supported configuration parameters.
configuration = pxcloud_api_client.Configuration(
    host = "https://api.pxcloud.cisco.com/torii"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oAuth2
configuration = pxcloud_api_client.Configuration(
    host = "https://api.pxcloud.cisco.com/torii"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pxcloud_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = faults_api.FaultsApi(api_client)
    success_track_id = "successTrackId_example" # str | 
    customer_id = "customerId_example" # str | Unique identifier of the customer
    fault_id = 1 # int | Unique identifier used in CX Cloud to identify the fault

    # example passing only required values which don't have defaults set
    try:
        # Fault summary
        api_response = api_instance.fault_summary(success_track_id, customer_id, fault_id)
        pprint(api_response)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling FaultsApi->fault_summary: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **success_track_id** | **str**|  |
 **customer_id** | **str**| Unique identifier of the customer |
 **fault_id** | **int**| Unique identifier used in CX Cloud to identify the fault |

### Return type

[**FaultsSummaryResponse**](FaultsSummaryResponse.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Date -  <br>  |
**401** | Unauthorized |  * Date -  <br>  |
**403** | Forbidden |  * Date -  <br>  |
**404** | Not Found |  * Date -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **faults**
> FaultsResponse faults(success_track_id, customer_id)

Faults details

Returns fault information for the customerId provided.

### Example

* OAuth Authentication (oAuth2):

```python
import time
import pxcloud_api_client
from pxcloud_api_client.api import faults_api
from pxcloud_api_client.model.error_response import ErrorResponse
from pxcloud_api_client.model.faults_response import FaultsResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.pxcloud.cisco.com/torii
# See configuration.py for a list of all supported configuration parameters.
configuration = pxcloud_api_client.Configuration(
    host = "https://api.pxcloud.cisco.com/torii"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oAuth2
configuration = pxcloud_api_client.Configuration(
    host = "https://api.pxcloud.cisco.com/torii"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pxcloud_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = faults_api.FaultsApi(api_client)
    success_track_id = "successTrackId_example" # str | 
    customer_id = "customerId_example" # str | Unique identifier of the customer
    days = 1 # int | The number of days to retrieve fault data for. This value can be 1, 7, 15, 30. The default is 1. (optional) if omitted the server will use the default value of 1
    offset = 1 # int | The number of items to skip before starting to collect the result set. The default value is 1. (optional) if omitted the server will use the default value of 1
    max = 10 # int | The maximum number of items to return (optional) if omitted the server will use the default value of 10

    # example passing only required values which don't have defaults set
    try:
        # Faults details
        api_response = api_instance.faults(success_track_id, customer_id)
        pprint(api_response)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling FaultsApi->faults: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Faults details
        api_response = api_instance.faults(success_track_id, customer_id, days=days, offset=offset, max=max)
        pprint(api_response)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling FaultsApi->faults: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **success_track_id** | **str**|  |
 **customer_id** | **str**| Unique identifier of the customer |
 **days** | **int**| The number of days to retrieve fault data for. This value can be 1, 7, 15, 30. The default is 1. | [optional] if omitted the server will use the default value of 1
 **offset** | **int**| The number of items to skip before starting to collect the result set. The default value is 1. | [optional] if omitted the server will use the default value of 1
 **max** | **int**| The maximum number of items to return | [optional] if omitted the server will use the default value of 10

### Return type

[**FaultsResponse**](FaultsResponse.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Date -  <br>  |
**401** | Unauthorized |  * Date -  <br>  |
**403** | Forbidden |  * Date -  <br>  |
**404** | Not Found |  * Date -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

