# pxcloud_api_client.CrashRiskApi

All URIs are relative to *https://api-cx.cisco.com/px/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_crash_asset_crash_history**](CrashRiskApi.md#get_crash_asset_crash_history) | **GET** /v1/customers/{customerId}/insights/crashRisk/asset/{assetIdBase64}/crashHistory | List asset crash history incidents
[**get_crash_risk_asset_risk_factors**](CrashRiskApi.md#get_crash_risk_asset_risk_factors) | **GET** /v1/customers/{customerId}/insights/crashRisk/assets/{assetIdBase64}/riskFactors | List crash risk asset risk factors
[**get_crash_risk_asset_similar_assets**](CrashRiskApi.md#get_crash_risk_asset_similar_assets) | **GET** /v1/customers/{customerId}/insights/crashRisk/assets/{assetIdBase64}/similarAssets | List crash risk asset similar assets
[**get_crash_risk_assets**](CrashRiskApi.md#get_crash_risk_assets) | **GET** /v1/customers/{customerId}/insights/crashRisk/assets | List assets at risk of crashing
[**list_crash_risk_assets_crashed**](CrashRiskApi.md#list_crash_risk_assets_crashed) | **GET** /v1/customers/{customerId}/insights/crashRisk/assetsCrashed | List assets which have crashed


# **get_crash_asset_crash_history**
> DeviceCrashDetail get_crash_asset_crash_history(customer_id, asset_id_base64, success_track_id)

List asset crash history incidents

### Example

* OAuth Authentication (oAuth2):

```python
import time
import pxcloud_api_client
from pxcloud_api_client.api import crash_risk_api
from pxcloud_api_client.model.error_response import ErrorResponse
from pxcloud_api_client.model.device_crash_detail import DeviceCrashDetail
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
    api_instance = crash_risk_api.CrashRiskApi(api_client)
    customer_id = "customerId_example" # str | 
    asset_id_base64 = "assetIdBase64_example" # str | Base64 encoded value of the `assetId`.
    success_track_id = "successTrackId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # List asset crash history incidents
        api_response = api_instance.get_crash_asset_crash_history(customer_id, asset_id_base64, success_track_id)
        pprint(api_response)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling CrashRiskApi->get_crash_asset_crash_history: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  |
 **asset_id_base64** | **str**| Base64 encoded value of the &#x60;assetId&#x60;. |
 **success_track_id** | **str**|  |

### Return type

[**DeviceCrashDetail**](DeviceCrashDetail.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |
**503** | Service Unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_crash_risk_asset_risk_factors**
> DeviceRiskFactorsResponse get_crash_risk_asset_risk_factors(success_track_id, customer_id, asset_id_base64)

List crash risk asset risk factors

List factors that contribute to an asset's crash risk score.

### Example

* OAuth Authentication (oAuth2):

```python
import time
import pxcloud_api_client
from pxcloud_api_client.api import crash_risk_api
from pxcloud_api_client.model.device_risk_factors_response import DeviceRiskFactorsResponse
from pxcloud_api_client.model.error_response import ErrorResponse
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
    api_instance = crash_risk_api.CrashRiskApi(api_client)
    success_track_id = "successTrackId_example" # str | 
    customer_id = "customerId_example" # str | 
    asset_id_base64 = "assetIdBase64_example" # str | Base64 encoded value of the `assetId`.

    # example passing only required values which don't have defaults set
    try:
        # List crash risk asset risk factors
        api_response = api_instance.get_crash_risk_asset_risk_factors(success_track_id, customer_id, asset_id_base64)
        pprint(api_response)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling CrashRiskApi->get_crash_risk_asset_risk_factors: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **success_track_id** | **str**|  |
 **customer_id** | **str**|  |
 **asset_id_base64** | **str**| Base64 encoded value of the &#x60;assetId&#x60;. |

### Return type

[**DeviceRiskFactorsResponse**](DeviceRiskFactorsResponse.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |
**503** | Service Unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_crash_risk_asset_similar_assets**
> SimilarDevices get_crash_risk_asset_similar_assets(customer_id, asset_id_base64, success_track_id, similarity_criteria)

List crash risk asset similar assets

List other devices in the network that are similar to a device in terms of features , product family, and hardware.

### Example

* OAuth Authentication (oAuth2):

```python
import time
import pxcloud_api_client
from pxcloud_api_client.api import crash_risk_api
from pxcloud_api_client.model.similar_devices import SimilarDevices
from pxcloud_api_client.model.error_response import ErrorResponse
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
    api_instance = crash_risk_api.CrashRiskApi(api_client)
    customer_id = "customerId_example" # str | 
    asset_id_base64 = "assetIdBase64_example" # str | Base64 encoded value of the `assetId`.
    success_track_id = "successTrackId_example" # str | 
    similarity_criteria = "features" # str | Criteria used to determine whether an asset is similar to the specified asset.
    max = 1 # int | Maximum number of items to return (optional)
    offset = 0 # int | Number of items to skip (optional)

    # example passing only required values which don't have defaults set
    try:
        # List crash risk asset similar assets
        api_response = api_instance.get_crash_risk_asset_similar_assets(customer_id, asset_id_base64, success_track_id, similarity_criteria)
        pprint(api_response)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling CrashRiskApi->get_crash_risk_asset_similar_assets: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List crash risk asset similar assets
        api_response = api_instance.get_crash_risk_asset_similar_assets(customer_id, asset_id_base64, success_track_id, similarity_criteria, max=max, offset=offset)
        pprint(api_response)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling CrashRiskApi->get_crash_risk_asset_similar_assets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  |
 **asset_id_base64** | **str**| Base64 encoded value of the &#x60;assetId&#x60;. |
 **success_track_id** | **str**|  |
 **similarity_criteria** | **str**| Criteria used to determine whether an asset is similar to the specified asset. |
 **max** | **int**| Maximum number of items to return | [optional]
 **offset** | **int**| Number of items to skip | [optional]

### Return type

[**SimilarDevices**](SimilarDevices.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |
**503** | Service Unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_crash_risk_assets**
> CrashRiskDevices get_crash_risk_assets(customer_id, success_track_id)

List assets at risk of crashing

List devices that have a probability of crash, including risk score rating (`High`, `Medium`, `Low`).

### Example

* OAuth Authentication (oAuth2):

```python
import time
import pxcloud_api_client
from pxcloud_api_client.api import crash_risk_api
from pxcloud_api_client.model.crash_risk_devices import CrashRiskDevices
from pxcloud_api_client.model.error_response import ErrorResponse
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
    api_instance = crash_risk_api.CrashRiskApi(api_client)
    customer_id = "customerId_example" # str | 
    success_track_id = "successTrackId_example" # str | 
    max = 1 # int | Maximum number of items to return (optional)
    offset = 0 # int | Number of items to skip (optional)

    # example passing only required values which don't have defaults set
    try:
        # List assets at risk of crashing
        api_response = api_instance.get_crash_risk_assets(customer_id, success_track_id)
        pprint(api_response)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling CrashRiskApi->get_crash_risk_assets: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List assets at risk of crashing
        api_response = api_instance.get_crash_risk_assets(customer_id, success_track_id, max=max, offset=offset)
        pprint(api_response)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling CrashRiskApi->get_crash_risk_assets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  |
 **success_track_id** | **str**|  |
 **max** | **int**| Maximum number of items to return | [optional]
 **offset** | **int**| Number of items to skip | [optional]

### Return type

[**CrashRiskDevices**](CrashRiskDevices.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |
**503** | Service Unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_crash_risk_assets_crashed**
> InventoryCrashDetails list_crash_risk_assets_crashed(customer_id, success_track_id)

List assets which have crashed

### Example

* OAuth Authentication (oAuth2):

```python
import time
import pxcloud_api_client
from pxcloud_api_client.api import crash_risk_api
from pxcloud_api_client.model.error_response import ErrorResponse
from pxcloud_api_client.model.inventory_crash_details import InventoryCrashDetails
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
    api_instance = crash_risk_api.CrashRiskApi(api_client)
    customer_id = "customerId_example" # str | 
    success_track_id = "successTrackId_example" # str | 
    time_period = 1 # int | Filter results by X number of days in the past - valid range 1-99. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List assets which have crashed
        api_response = api_instance.list_crash_risk_assets_crashed(customer_id, success_track_id)
        pprint(api_response)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling CrashRiskApi->list_crash_risk_assets_crashed: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List assets which have crashed
        api_response = api_instance.list_crash_risk_assets_crashed(customer_id, success_track_id, time_period=time_period)
        pprint(api_response)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling CrashRiskApi->list_crash_risk_assets_crashed: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  |
 **success_track_id** | **str**|  |
 **time_period** | **int**| Filter results by X number of days in the past - valid range 1-99. | [optional]

### Return type

[**InventoryCrashDetails**](InventoryCrashDetails.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |
**503** | Service Unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

