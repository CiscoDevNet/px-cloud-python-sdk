# pxcloud_api_client.CustomerDataApi

All URIs are relative to *https://api-cx.cisco.com/px/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_customers**](CustomerDataApi.md#get_customers) | **GET** /v1/customers | List customers
[**get_report_status**](CustomerDataApi.md#get_report_status) | **GET** /v1/customers/{customerId}/reports/{reportId} | Get report status and location
[**post_reports**](CustomerDataApi.md#post_reports) | **POST** /v1/customers/{customerId}/reports | Request customer data report


# **get_customers**
> CustomerResponse get_customers()

List customers

### Example

* OAuth Authentication (oAuth2):

```python
import time
import pxcloud_api_client
from pxcloud_api_client.api import customer_data_api
from pxcloud_api_client.model.error_response import ErrorResponse
from pxcloud_api_client.model.customer_response import CustomerResponse
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
    api_instance = customer_data_api.CustomerDataApi(api_client)
    max = 1 # int | Maximum number of items to return (optional)
    offset = 0 # int | Number of items to skip (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List customers
        api_response = api_instance.get_customers(max=max, offset=offset)
        pprint(api_response)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling CustomerDataApi->get_customers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **max** | **int**| Maximum number of items to return | [optional]
 **offset** | **int**| Number of items to skip | [optional]

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
**200** | OK |  * Link - URLs for previous (&#x60;rel&#x3D;\&quot;prev\&quot;&#x60;) and/or next (&#x60;rel&#x3D;\&quot;next\&quot;&#x60;) page of items <br>  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |
**503** | Service Unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report_status**
> ReportStatus get_report_status(customer_id, report_id)

Get report status and location

If report is in-progress (`200 OK`), body will include status description and suggested poll/retry interval.  If ready (`303 See Other`), `Location` header will contain the final report download URL.

### Example

* OAuth Authentication (oAuth2):

```python
import time
import pxcloud_api_client
from pxcloud_api_client.api import customer_data_api
from pxcloud_api_client.model.error_response import ErrorResponse
from pxcloud_api_client.model.report_status import ReportStatus
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
    api_instance = customer_data_api.CustomerDataApi(api_client)
    customer_id = "customerId_example" # str | 
    report_id = "reportId_example" # str | reportId returned by a report generation request.

    # example passing only required values which don't have defaults set
    try:
        # Get report status and location
        api_response = api_instance.get_report_status(customer_id, report_id)
        pprint(api_response)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling CustomerDataApi->get_report_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  |
 **report_id** | **str**| reportId returned by a report generation request. |

### Return type

[**ReportStatus**](ReportStatus.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**303** | See Other |  * Location - Final report download URL. <br>  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |
**503** | Service Unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_reports**
> post_reports(customer_id)

Request customer data report

Report generation is asynchronous. The response `Location` header will contain the report status URL.

### Example

* OAuth Authentication (oAuth2):

```python
import time
import pxcloud_api_client
from pxcloud_api_client.api import customer_data_api
from pxcloud_api_client.model.error_response import ErrorResponse
from pxcloud_api_client.model.report import Report
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
    api_instance = customer_data_api.CustomerDataApi(api_client)
    customer_id = "customerId_example" # str | 
    report = Report(
        report_name="Assets",
        success_track_id="success_track_id_example",
    ) # Report | Report request details. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Request customer data report
        api_instance.post_reports(customer_id)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling CustomerDataApi->post_reports: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Request customer data report
        api_instance.post_reports(customer_id, report=report)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling CustomerDataApi->post_reports: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  |
 **report** | [**Report**](Report.md)| Report request details. | [optional]

### Return type

void (empty response body)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  * Location - Final report download URL. <br>  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |
**503** | Service Unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

