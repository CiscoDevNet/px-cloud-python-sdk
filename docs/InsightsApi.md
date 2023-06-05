# pxcloud_api_client.InsightsApi

All URIs are relative to *https://api-cx.cisco.com/px/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_software_group_assets**](InsightsApi.md#get_software_group_assets) | **GET** /v1/customers/{customerId}/insights/software/softwareGroups/assets | List Asset information in the Software Group
[**get_software_group_field_notices**](InsightsApi.md#get_software_group_field_notices) | **GET** /v1/customers/{customerId}/insights/software/softwareGroups/suggestions/fieldNotices | List info on Software Group - Suggestions Field Notices
[**get_software_group_security_advisories**](InsightsApi.md#get_software_group_security_advisories) | **GET** /v1/customers/{customerId}/insights/software/softwareGroups/suggestions/securityAdvisories | List info on Software Group - Suggestions Security Advisories
[**get_software_group_suggestions**](InsightsApi.md#get_software_group_suggestions) | **GET** /v1/customers/{customerId}/insights/software/softwareGroups/suggestions | List Software Group Suggestions
[**get_software_group_suggestions_bugs**](InsightsApi.md#get_software_group_suggestions_bugs) | **GET** /v1/customers/{customerId}/insights/software/softwareGroups/suggestions/bugs | List info on Software Group - Suggestions Bugs
[**get_software_groups**](InsightsApi.md#get_software_groups) | **GET** /v1/customers/{customerId}/insights/software/softwareGroups | fetch Software Group Information


# **get_software_group_assets**
> AssetResponse get_software_group_assets(customer_id, success_track_id, software_group_id)

List Asset information in the Software Group

Returns information about assets in the Software Group based on the customerId and softwareGroupId provided

### Example

* OAuth Authentication (oAuth2):

```python
import time
import pxcloud_api_client
from pxcloud_api_client.api import insights_api
from pxcloud_api_client.model.error_response import ErrorResponse
from pxcloud_api_client.model.asset_response import AssetResponse
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
    api_instance = insights_api.InsightsApi(api_client)
    customer_id = "customerId_example" # str | Unique identifier of the customer
    success_track_id = "successTrackId_example" # str | 
    software_group_id = "softwareGroupId_example" # str | Unique identifier used in CX Cloud to identify the Software Group
    offset = 1 # int | The number of items to skip before starting to collect the result set. The default value is 1. (optional) if omitted the server will use the default value of 1
    max = 50 # int | The maximum number of items to return (optional) if omitted the server will use the default value of 50

    # example passing only required values which don't have defaults set
    try:
        # List Asset information in the Software Group
        api_response = api_instance.get_software_group_assets(customer_id, success_track_id, software_group_id)
        pprint(api_response)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling InsightsApi->get_software_group_assets: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Asset information in the Software Group
        api_response = api_instance.get_software_group_assets(customer_id, success_track_id, software_group_id, offset=offset, max=max)
        pprint(api_response)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling InsightsApi->get_software_group_assets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| Unique identifier of the customer |
 **success_track_id** | **str**|  |
 **software_group_id** | **str**| Unique identifier used in CX Cloud to identify the Software Group |
 **offset** | **int**| The number of items to skip before starting to collect the result set. The default value is 1. | [optional] if omitted the server will use the default value of 1
 **max** | **int**| The maximum number of items to return | [optional] if omitted the server will use the default value of 50

### Return type

[**AssetResponse**](AssetResponse.md)

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

# **get_software_group_field_notices**
> SoftwareGroupFieldNoticesResponse get_software_group_field_notices(customer_id, success_track_id, machine_suggestion_id)

List info on Software Group - Suggestions Field Notices

Returns field notice information, including ID number, title, and publish date.

### Example

* OAuth Authentication (oAuth2):

```python
import time
import pxcloud_api_client
from pxcloud_api_client.api import insights_api
from pxcloud_api_client.model.error_response import ErrorResponse
from pxcloud_api_client.model.software_group_field_notices_response import SoftwareGroupFieldNoticesResponse
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
    api_instance = insights_api.InsightsApi(api_client)
    customer_id = "customerId_example" # str | Unique identifier of the customer
    success_track_id = "successTrackId_example" # str | 
    machine_suggestion_id = "machineSuggestionId_example" # str | 
    offset = 1 # int | The number of items to skip before starting to collect the result set. The default value is 1. (optional) if omitted the server will use the default value of 1
    max = 50 # int | The maximum number of items to return (optional) if omitted the server will use the default value of 50

    # example passing only required values which don't have defaults set
    try:
        # List info on Software Group - Suggestions Field Notices
        api_response = api_instance.get_software_group_field_notices(customer_id, success_track_id, machine_suggestion_id)
        pprint(api_response)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling InsightsApi->get_software_group_field_notices: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List info on Software Group - Suggestions Field Notices
        api_response = api_instance.get_software_group_field_notices(customer_id, success_track_id, machine_suggestion_id, offset=offset, max=max)
        pprint(api_response)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling InsightsApi->get_software_group_field_notices: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| Unique identifier of the customer |
 **success_track_id** | **str**|  |
 **machine_suggestion_id** | **str**|  |
 **offset** | **int**| The number of items to skip before starting to collect the result set. The default value is 1. | [optional] if omitted the server will use the default value of 1
 **max** | **int**| The maximum number of items to return | [optional] if omitted the server will use the default value of 50

### Return type

[**SoftwareGroupFieldNoticesResponse**](SoftwareGroupFieldNoticesResponse.md)

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

# **get_software_group_security_advisories**
> SoftwareGroupFieldNoticesResponse get_software_group_security_advisories(customer_id, success_track_id, machine_suggestion_id)

List info on Software Group - Suggestions Security Advisories

Returns software advisory information, including ID number, version number, and severity level.

### Example

* OAuth Authentication (oAuth2):

```python
import time
import pxcloud_api_client
from pxcloud_api_client.api import insights_api
from pxcloud_api_client.model.software_group_field_notices_response import SoftwareGroupFieldNoticesResponse
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
    api_instance = insights_api.InsightsApi(api_client)
    customer_id = "customerId_example" # str | Unique identifier of the customer
    success_track_id = "successTrackId_example" # str | 
    machine_suggestion_id = "machineSuggestionId_example" # str | 
    offset = 1 # int | The number of items to skip before starting to collect the result set. The default value is 1. (optional) if omitted the server will use the default value of 1
    max = 50 # int | The maximum number of items to return (optional) if omitted the server will use the default value of 50

    # example passing only required values which don't have defaults set
    try:
        # List info on Software Group - Suggestions Security Advisories
        api_response = api_instance.get_software_group_security_advisories(customer_id, success_track_id, machine_suggestion_id)
        pprint(api_response)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling InsightsApi->get_software_group_security_advisories: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List info on Software Group - Suggestions Security Advisories
        api_response = api_instance.get_software_group_security_advisories(customer_id, success_track_id, machine_suggestion_id, offset=offset, max=max)
        pprint(api_response)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling InsightsApi->get_software_group_security_advisories: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| Unique identifier of the customer |
 **success_track_id** | **str**|  |
 **machine_suggestion_id** | **str**|  |
 **offset** | **int**| The number of items to skip before starting to collect the result set. The default value is 1. | [optional] if omitted the server will use the default value of 1
 **max** | **int**| The maximum number of items to return | [optional] if omitted the server will use the default value of 50

### Return type

[**SoftwareGroupFieldNoticesResponse**](SoftwareGroupFieldNoticesResponse.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_software_group_suggestions**
> SoftwareGroupSuggestions get_software_group_suggestions(success_track_id, customer_id, suggestion_id)

List Software Group Suggestions

Returns Software Group suggestions, including detailed information about Cisco software release recommendations and current Cisco software releases running on assets in the Software Group

### Example

* OAuth Authentication (oAuth2):

```python
import time
import pxcloud_api_client
from pxcloud_api_client.api import insights_api
from pxcloud_api_client.model.error_response import ErrorResponse
from pxcloud_api_client.model.software_group_suggestions import SoftwareGroupSuggestions
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
    api_instance = insights_api.InsightsApi(api_client)
    success_track_id = "successTrackId_example" # str | 
    customer_id = "customerId_example" # str | Unique identifier of the customer
    suggestion_id = "suggestionId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # List Software Group Suggestions
        api_response = api_instance.get_software_group_suggestions(success_track_id, customer_id, suggestion_id)
        pprint(api_response)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling InsightsApi->get_software_group_suggestions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **success_track_id** | **str**|  |
 **customer_id** | **str**| Unique identifier of the customer |
 **suggestion_id** | **str**|  |

### Return type

[**SoftwareGroupSuggestions**](SoftwareGroupSuggestions.md)

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

# **get_software_group_suggestions_bugs**
> SoftwareGroupBugsResponse get_software_group_suggestions_bugs(customer_id, success_track_id, machine_suggestion_id)

List info on Software Group - Suggestions Bugs

Returns information on bugs, including ID, description, and affected software releases.

### Example

* OAuth Authentication (oAuth2):

```python
import time
import pxcloud_api_client
from pxcloud_api_client.api import insights_api
from pxcloud_api_client.model.error_response import ErrorResponse
from pxcloud_api_client.model.software_group_bugs_response import SoftwareGroupBugsResponse
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
    api_instance = insights_api.InsightsApi(api_client)
    customer_id = "customerId_example" # str | Unique identifier of the customer
    success_track_id = "successTrackId_example" # str | 
    machine_suggestion_id = "machineSuggestionId_example" # str | 
    offset = 1 # int | The number of items to skip before starting to collect the result set. The default value is 1. (optional) if omitted the server will use the default value of 1
    max = 50 # int | The maximum number of items to return (optional) if omitted the server will use the default value of 50

    # example passing only required values which don't have defaults set
    try:
        # List info on Software Group - Suggestions Bugs
        api_response = api_instance.get_software_group_suggestions_bugs(customer_id, success_track_id, machine_suggestion_id)
        pprint(api_response)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling InsightsApi->get_software_group_suggestions_bugs: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List info on Software Group - Suggestions Bugs
        api_response = api_instance.get_software_group_suggestions_bugs(customer_id, success_track_id, machine_suggestion_id, offset=offset, max=max)
        pprint(api_response)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling InsightsApi->get_software_group_suggestions_bugs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| Unique identifier of the customer |
 **success_track_id** | **str**|  |
 **machine_suggestion_id** | **str**|  |
 **offset** | **int**| The number of items to skip before starting to collect the result set. The default value is 1. | [optional] if omitted the server will use the default value of 1
 **max** | **int**| The maximum number of items to return | [optional] if omitted the server will use the default value of 50

### Return type

[**SoftwareGroupBugsResponse**](SoftwareGroupBugsResponse.md)

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

# **get_software_groups**
> SoftwareGroupResponse get_software_groups(success_track_id, customer_id)

fetch Software Group Information

Returns Software Group information for the customerId provided

### Example

* OAuth Authentication (oAuth2):

```python
import time
import pxcloud_api_client
from pxcloud_api_client.api import insights_api
from pxcloud_api_client.model.error_response import ErrorResponse
from pxcloud_api_client.model.software_group_response import SoftwareGroupResponse
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
    api_instance = insights_api.InsightsApi(api_client)
    success_track_id = "successTrackId_example" # str | 
    customer_id = "customerId_example" # str | Unique identifier of the customer
    max = 50 # int | The maximum number of items to return (optional) if omitted the server will use the default value of 50
    offset = 1 # int | The number of items to skip before starting to collect the result set. The default value is 1. (optional) if omitted the server will use the default value of 1

    # example passing only required values which don't have defaults set
    try:
        # fetch Software Group Information
        api_response = api_instance.get_software_groups(success_track_id, customer_id)
        pprint(api_response)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling InsightsApi->get_software_groups: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # fetch Software Group Information
        api_response = api_instance.get_software_groups(success_track_id, customer_id, max=max, offset=offset)
        pprint(api_response)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling InsightsApi->get_software_groups: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **success_track_id** | **str**|  |
 **customer_id** | **str**| Unique identifier of the customer |
 **max** | **int**| The maximum number of items to return | [optional] if omitted the server will use the default value of 50
 **offset** | **int**| The number of items to skip before starting to collect the result set. The default value is 1. | [optional] if omitted the server will use the default value of 1

### Return type

[**SoftwareGroupResponse**](SoftwareGroupResponse.md)

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

