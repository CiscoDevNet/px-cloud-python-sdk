# pxcloud_api_client.CrashRiskApi

All URIs are relative to *https://api.pxcloud.cisco.com/torii*

Method | HTTP request | Description
------------- | ------------- | -------------
[**asset_risk_factors**](CrashRiskApi.md#asset_risk_factors) | **GET** /v1/customers/{customerId}/insights/crashRisk/assets/{assetIdBase64}/riskFactors | Get risk factors of a device
[**assets**](CrashRiskApi.md#assets) | **GET** /v1/customers/{customerId}/insights/crashRisk/assets | Get devices which are at risk of crash owned by a customer, sorted by risk score in descending order by default
[**assets_crashed**](CrashRiskApi.md#assets_crashed) | **GET** /v1/customers/{customerId}/insights/crashRisk/assetsCrashed | Get the list of crashed devices for last given time period
[**crash_history**](CrashRiskApi.md#crash_history) | **GET** /v1/customers/{customerId}/insights/crashRisk/asset/{assetIdBase64}/crashHistory | Get the device crash-detail - Asset 360(time stamp, reset reason)
[**similar_assets**](CrashRiskApi.md#similar_assets) | **GET** /v1/customers/{customerId}/insights/crashRisk/assets/{assetIdBase64}/similarAssets | Get similar assets based on the similarity score


# **asset_risk_factors**
> DeviceRiskFactorsResponse asset_risk_factors(success_track_id, customer_id, asset_id_base64)

Get risk factors of a device

This API provides list of risk factors that contribute to the high risk score. Default sorting is factorWeight

### Example

* OAuth Authentication (oAuth2):

```python
import time
import pxcloud_api_client
from pxcloud_api_client.api import crash_risk_api
from pxcloud_api_client.model.device_risk_factors_response import DeviceRiskFactorsResponse
from pxcloud_api_client.model.error_response import ErrorResponse
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
    api_instance = crash_risk_api.CrashRiskApi(api_client)
    success_track_id = "successTrackId_example" # str | 
    customer_id = "customerId_example" # str | 
    asset_id_base64 = "assetIdBase64_example" # str | base64 encoded value of the assetId

    # example passing only required values which don't have defaults set
    try:
        # Get risk factors of a device
        api_response = api_instance.asset_risk_factors(success_track_id, customer_id, asset_id_base64)
        pprint(api_response)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling CrashRiskApi->asset_risk_factors: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **success_track_id** | **str**|  |
 **customer_id** | **str**|  |
 **asset_id_base64** | **str**| base64 encoded value of the assetId |

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
**200** | Ok |  * Date -  <br>  |
**400** | Bad Request |  * Date -  <br>  |
**401** | Unauthorized |  * Date -  <br>  |
**403** | Forbidden error |  * Date -  <br>  |
**404** | Not Found |  * Date -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets**
> CrashRiskDevices assets(success_track_id, customer_id)

Get devices which are at risk of crash owned by a customer, sorted by risk score in descending order by default

This API provides details of the devices that have a probability of crash with crash score rating as High, Medium and Low. Default sorting is End date

### Example

* OAuth Authentication (oAuth2):

```python
import time
import pxcloud_api_client
from pxcloud_api_client.api import crash_risk_api
from pxcloud_api_client.model.crash_risk_devices import CrashRiskDevices
from pxcloud_api_client.model.error_response import ErrorResponse
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
    api_instance = crash_risk_api.CrashRiskApi(api_client)
    success_track_id = "successTrackId_example" # str | 
    customer_id = "customerId_example" # str | 
    offset = 1 # int |  (optional) if omitted the server will use the default value of 1
    max = 10 # int |  (optional) if omitted the server will use the default value of 10

    # example passing only required values which don't have defaults set
    try:
        # Get devices which are at risk of crash owned by a customer, sorted by risk score in descending order by default
        api_response = api_instance.assets(success_track_id, customer_id)
        pprint(api_response)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling CrashRiskApi->assets: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get devices which are at risk of crash owned by a customer, sorted by risk score in descending order by default
        api_response = api_instance.assets(success_track_id, customer_id, offset=offset, max=max)
        pprint(api_response)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling CrashRiskApi->assets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **success_track_id** | **str**|  |
 **customer_id** | **str**|  |
 **offset** | **int**|  | [optional] if omitted the server will use the default value of 1
 **max** | **int**|  | [optional] if omitted the server will use the default value of 10

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
**200** | Ok |  * Date -  <br>  |
**400** | Bad Request |  * Date -  <br>  |
**401** | Unauthorized |  * Date -  <br>  |
**403** | Forbidden error |  * Date -  <br>  |
**404** | Not Found |  * Date -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_crashed**
> InventoryCrashDetails assets_crashed(success_track_id, customer_id)

Get the list of crashed devices for last given time period

This API provides the list of devices with details (i.e. Asset, Product Id, Product Family, Software Version, Crash Count, First Occurrence and Last Occurrence) by customer Id that have crashed in the last 1d,7d,15d,90d based on the filter input. Default sort is by lastCrashDate

### Example

* OAuth Authentication (oAuth2):

```python
import time
import pxcloud_api_client
from pxcloud_api_client.api import crash_risk_api
from pxcloud_api_client.model.error_response import ErrorResponse
from pxcloud_api_client.model.inventory_crash_details import InventoryCrashDetails
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
    api_instance = crash_risk_api.CrashRiskApi(api_client)
    success_track_id = "successTrackId_example" # str | 
    customer_id = "customerId_example" # str | customerId
    time_period = "1" # str | timePeriod (optional) if omitted the server will use the default value of "1"

    # example passing only required values which don't have defaults set
    try:
        # Get the list of crashed devices for last given time period
        api_response = api_instance.assets_crashed(success_track_id, customer_id)
        pprint(api_response)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling CrashRiskApi->assets_crashed: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the list of crashed devices for last given time period
        api_response = api_instance.assets_crashed(success_track_id, customer_id, time_period=time_period)
        pprint(api_response)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling CrashRiskApi->assets_crashed: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **success_track_id** | **str**|  |
 **customer_id** | **str**| customerId |
 **time_period** | **str**| timePeriod | [optional] if omitted the server will use the default value of "1"

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
**200** | OK |  * Date -  <br>  |
**401** | Unauthorized |  * Date -  <br>  |
**403** | Forbidden |  * Date -  <br>  |
**404** | Not Found |  * Date -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crash_history**
> DeviceCrashDetail crash_history(success_track_id, customer_id, asset_id_base64)

Get the device crash-detail - Asset 360(time stamp, reset reason)

Details of the number of times the device crashed in the last 365 days with reset reason. Default sort is by timeStamp

### Example

* OAuth Authentication (oAuth2):

```python
import time
import pxcloud_api_client
from pxcloud_api_client.api import crash_risk_api
from pxcloud_api_client.model.error_response import ErrorResponse
from pxcloud_api_client.model.device_crash_detail import DeviceCrashDetail
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
    api_instance = crash_risk_api.CrashRiskApi(api_client)
    success_track_id = "successTrackId_example" # str | 
    customer_id = "customerId_example" # str | customerId
    asset_id_base64 = "assetIdBase64_example" # str | base64 encoded value of the assetId

    # example passing only required values which don't have defaults set
    try:
        # Get the device crash-detail - Asset 360(time stamp, reset reason)
        api_response = api_instance.crash_history(success_track_id, customer_id, asset_id_base64)
        pprint(api_response)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling CrashRiskApi->crash_history: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **success_track_id** | **str**|  |
 **customer_id** | **str**| customerId |
 **asset_id_base64** | **str**| base64 encoded value of the assetId |

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
**200** | OK |  * Date -  <br>  |
**401** | Unauthorized |  * Date -  <br>  |
**403** | Forbidden |  * Date -  <br>  |
**404** | Not Found |  * Date -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **similar_assets**
> SimilarDevices similar_assets(success_track_id, customer_id, asset_id_base64, similarity_criteria)

Get similar assets based on the similarity score

This API provides details of other devices in the network that are similar to the current device pre in terms of features , prodict familiy and hardware. Default sort is similarityScore

### Example

* OAuth Authentication (oAuth2):

```python
import time
import pxcloud_api_client
from pxcloud_api_client.api import crash_risk_api
from pxcloud_api_client.model.similar_devices import SimilarDevices
from pxcloud_api_client.model.error_response import ErrorResponse
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
    api_instance = crash_risk_api.CrashRiskApi(api_client)
    success_track_id = "successTrackId_example" # str | 
    customer_id = "customerId_example" # str | 
    asset_id_base64 = "assetIdBase64_example" # str | base64 encoded value of the assetId
    similarity_criteria = "similarityCriteria_example" # str | should be one of the following values features,fingerprint,softwares_features
    offset = 1 # int |  (optional) if omitted the server will use the default value of 1
    max = 10 # int |  (optional) if omitted the server will use the default value of 10

    # example passing only required values which don't have defaults set
    try:
        # Get similar assets based on the similarity score
        api_response = api_instance.similar_assets(success_track_id, customer_id, asset_id_base64, similarity_criteria)
        pprint(api_response)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling CrashRiskApi->similar_assets: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get similar assets based on the similarity score
        api_response = api_instance.similar_assets(success_track_id, customer_id, asset_id_base64, similarity_criteria, offset=offset, max=max)
        pprint(api_response)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling CrashRiskApi->similar_assets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **success_track_id** | **str**|  |
 **customer_id** | **str**|  |
 **asset_id_base64** | **str**| base64 encoded value of the assetId |
 **similarity_criteria** | **str**| should be one of the following values features,fingerprint,softwares_features |
 **offset** | **int**|  | [optional] if omitted the server will use the default value of 1
 **max** | **int**|  | [optional] if omitted the server will use the default value of 10

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
**200** | Ok |  * Date -  <br>  |
**400** | Bad Request |  * Date -  <br>  |
**401** | Unauthorized |  * Date -  <br>  |
**403** | Forbidden error |  * Date -  <br>  |
**404** | Not Found |  * Date -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

