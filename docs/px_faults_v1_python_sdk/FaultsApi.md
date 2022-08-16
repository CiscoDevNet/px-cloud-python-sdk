# openapi_client.FaultsApi

All URIs are relative to *https://api.pxcloud-stg.cisco.com/torii*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_affected_assets_details_using_get**](FaultsApi.md#get_affected_assets_details_using_get) | **GET** /v1/customers/{customerId}/insights/faults/{faultId}/affectedAssets/{assetName}/faultHistory | Assets Fault History
[**get_affected_assets_using_get**](FaultsApi.md#get_affected_assets_using_get) | **GET** /v1/customers/{customerId}/insights/faults/{faultId}/affectedAssets | Affected Assets
[**get_faults_summary_using_get**](FaultsApi.md#get_faults_summary_using_get) | **GET** /v1/customers/{customerId}/insights/faults/{faultId}/summary | Fault summary
[**get_faults_using_get**](FaultsApi.md#get_faults_using_get) | **GET** /v1/customers/{customerId}/insights/faults | Faults details


# **get_affected_assets_details_using_get**
> AssetsFaultHistoryResponse get_affected_assets_details_using_get(success_track_id, customer_id, fault_id, asset_name)

Assets Fault History

Returns information about the occurrences of a fault on an asset based on the fault signatureId, asset name, and customerId provided

### Example


```python
import time
import openapi_client
from openapi_client.api import faults_api
from openapi_client.model.assets_fault_history_response import AssetsFaultHistoryResponse
from openapi_client.model.error_response import ErrorResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.pxcloud-stg.cisco.com/torii
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.pxcloud-stg.cisco.com/torii"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
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
        api_response = api_instance.get_affected_assets_details_using_get(success_track_id, customer_id, fault_id, asset_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling FaultsApi->get_affected_assets_details_using_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Assets Fault History
        api_response = api_instance.get_affected_assets_details_using_get(success_track_id, customer_id, fault_id, asset_name, days=days)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling FaultsApi->get_affected_assets_details_using_get: %s\n" % e)
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

No authorization required

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

# **get_affected_assets_using_get**
> AffectedAssetsResponse get_affected_assets_using_get(success_track_id, customer_id, fault_id)

Affected Assets

Returns information about the customer assets affected by the fault, based on the fault signatureId and customerId provided

### Example


```python
import time
import openapi_client
from openapi_client.api import faults_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.affected_assets_response import AffectedAssetsResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.pxcloud-stg.cisco.com/torii
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.pxcloud-stg.cisco.com/torii"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
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
        api_response = api_instance.get_affected_assets_using_get(success_track_id, customer_id, fault_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling FaultsApi->get_affected_assets_using_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Affected Assets
        api_response = api_instance.get_affected_assets_using_get(success_track_id, customer_id, fault_id, days=days, offset=offset, max=max)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling FaultsApi->get_affected_assets_using_get: %s\n" % e)
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

No authorization required

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

# **get_faults_summary_using_get**
> FaultsSummaryResponse get_faults_summary_using_get(success_track_id, customer_id, fault_id)

Fault summary

Returns detailed information for a fault based on the fault signatureId and customerId provided

### Example


```python
import time
import openapi_client
from openapi_client.api import faults_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.faults_summary_response import FaultsSummaryResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.pxcloud-stg.cisco.com/torii
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.pxcloud-stg.cisco.com/torii"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = faults_api.FaultsApi(api_client)
    success_track_id = "successTrackId_example" # str | 
    customer_id = "customerId_example" # str | Unique identifier of the customer
    fault_id = 1 # int | Unique identifier used in CX Cloud to identify the fault

    # example passing only required values which don't have defaults set
    try:
        # Fault summary
        api_response = api_instance.get_faults_summary_using_get(success_track_id, customer_id, fault_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling FaultsApi->get_faults_summary_using_get: %s\n" % e)
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

No authorization required

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

# **get_faults_using_get**
> FaultsResponse get_faults_using_get(success_track_id, customer_id)

Faults details

Returns fault information for the customerId provided.

### Example


```python
import time
import openapi_client
from openapi_client.api import faults_api
from openapi_client.model.faults_response import FaultsResponse
from openapi_client.model.error_response import ErrorResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.pxcloud-stg.cisco.com/torii
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.pxcloud-stg.cisco.com/torii"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
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
        api_response = api_instance.get_faults_using_get(success_track_id, customer_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling FaultsApi->get_faults_using_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Faults details
        api_response = api_instance.get_faults_using_get(success_track_id, customer_id, days=days, offset=offset, max=max)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling FaultsApi->get_faults_using_get: %s\n" % e)
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

No authorization required

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

