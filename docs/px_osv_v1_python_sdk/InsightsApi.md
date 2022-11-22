# openapi_client.InsightsApi

All URIs are relative to *https://api.pxcloud-stg.cisco.com/torii*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_software_group_assets_using_get**](InsightsApi.md#get_software_group_assets_using_get) | **GET** /v1/customers/{customerId}/insights/software/softwareGroups/assets | Asset information in the Software Group
[**get_software_group_suggestions_using_get**](InsightsApi.md#get_software_group_suggestions_using_get) | **GET** /v1/customers/{customerId}/insights/software/softwareGroups/suggestions | Software Group suggestions
[**get_software_groups_using_get**](InsightsApi.md#get_software_groups_using_get) | **GET** /v1/customers/{customerId}/insights/software/softwareGroups | Software Group information


# **get_software_group_assets_using_get**
> AssetResponse get_software_group_assets_using_get(success_track_id, customer_id, software_group_id)

Asset information in the Software Group

Returns information about assets in the Software Group based on the customerId and softwareGroupId provided

### Example


```python
import time
import openapi_client
from openapi_client.api import insights_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.asset_response import AssetResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.pxcloud-stg.cisco.com/torii
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.pxcloud-stg.cisco.com/torii"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = insights_api.InsightsApi(api_client)
    success_track_id = "successTrackId_example" # str | 
    customer_id = "customerId_example" # str | Unique identifier of the customer
    software_group_id = "softwareGroupId_example" # str | Unique identifier used in CX Cloud to identify the Software Group
    offset = 1 # int | The number of items to skip before starting to collect the result set. The default value is 1. (optional)
    max = 50 # int | The maximum number of items to return (optional) if omitted the server will use the default value of 50

    # example passing only required values which don't have defaults set
    try:
        # Asset information in the Software Group
        api_response = api_instance.get_software_group_assets_using_get(success_track_id, customer_id, software_group_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling InsightsApi->get_software_group_assets_using_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Asset information in the Software Group
        api_response = api_instance.get_software_group_assets_using_get(success_track_id, customer_id, software_group_id, offset=offset, max=max)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling InsightsApi->get_software_group_assets_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **success_track_id** | **str**|  |
 **customer_id** | **str**| Unique identifier of the customer |
 **software_group_id** | **str**| Unique identifier used in CX Cloud to identify the Software Group |
 **offset** | **int**| The number of items to skip before starting to collect the result set. The default value is 1. | [optional]
 **max** | **int**| The maximum number of items to return | [optional] if omitted the server will use the default value of 50

### Return type

[**AssetResponse**](AssetResponse.md)

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

# **get_software_group_suggestions_using_get**
> SoftwareGroupSuggestions get_software_group_suggestions_using_get(success_track_id, customer_id, software_group_name, source_system_id, software_type)

Software Group suggestions

Returns Software Group suggestions, including detailed information about Cisco software release recommendations and current Cisco software releases running on assets in the Software Group

### Example


```python
import time
import openapi_client
from openapi_client.api import insights_api
from openapi_client.model.software_group_suggestions import SoftwareGroupSuggestions
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
    api_instance = insights_api.InsightsApi(api_client)
    success_track_id = "successTrackId_example" # str | 
    customer_id = "customerId_example" # str | Unique identifier of the customer
    software_group_name = "softwareGroupName_example" # str | Name of the Software Group, which is based on the Cisco product ID of the assets in the Software Group
    source_system_id = "sourceSystemId_example" # str | UUID of the Cisco network management system that manages the assets in the Software Group
    software_type = "softwareType_example" # str | Cisco software type running on the assets in the Software Group

    # example passing only required values which don't have defaults set
    try:
        # Software Group suggestions
        api_response = api_instance.get_software_group_suggestions_using_get(success_track_id, customer_id, software_group_name, source_system_id, software_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling InsightsApi->get_software_group_suggestions_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **success_track_id** | **str**|  |
 **customer_id** | **str**| Unique identifier of the customer |
 **software_group_name** | **str**| Name of the Software Group, which is based on the Cisco product ID of the assets in the Software Group |
 **source_system_id** | **str**| UUID of the Cisco network management system that manages the assets in the Software Group |
 **software_type** | **str**| Cisco software type running on the assets in the Software Group |

### Return type

[**SoftwareGroupSuggestions**](SoftwareGroupSuggestions.md)

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

# **get_software_groups_using_get**
> SoftwareGroupResponse get_software_groups_using_get(success_track_id, customer_id)

Software Group information

Returns Software Group information for the customerId provided

### Example


```python
import time
import openapi_client
from openapi_client.api import insights_api
from openapi_client.model.software_group_response import SoftwareGroupResponse
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
    api_instance = insights_api.InsightsApi(api_client)
    success_track_id = "successTrackId_example" # str | 
    customer_id = "customerId_example" # str | Unique identifier of the customer
    offset = 1 # int | The number of items to skip before starting to collect the result set. The default value is 1. (optional)
    max = 50 # int | The maximum number of items to return (optional) if omitted the server will use the default value of 50

    # example passing only required values which don't have defaults set
    try:
        # Software Group information
        api_response = api_instance.get_software_groups_using_get(success_track_id, customer_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling InsightsApi->get_software_groups_using_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Software Group information
        api_response = api_instance.get_software_groups_using_get(success_track_id, customer_id, offset=offset, max=max)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling InsightsApi->get_software_groups_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **success_track_id** | **str**|  |
 **customer_id** | **str**| Unique identifier of the customer |
 **offset** | **int**| The number of items to skip before starting to collect the result set. The default value is 1. | [optional]
 **max** | **int**| The maximum number of items to return | [optional] if omitted the server will use the default value of 50

### Return type

[**SoftwareGroupResponse**](SoftwareGroupResponse.md)

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

