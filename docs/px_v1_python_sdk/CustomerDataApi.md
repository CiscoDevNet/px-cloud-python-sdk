# openapi_client.CustomerDataApi

All URIs are relative to *https://api.pxcloud-stg.cisco.com/torii*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetch_contracts_details_using_get**](CustomerDataApi.md#fetch_contracts_details_using_get) | **GET** /v1/contract/details | Get the list of contracts Details from flat table. It supports pagination , filtering and sorting
[**get_customer_report**](CustomerDataApi.md#get_customer_report) | **GET** /v1/customers/{customerId}/reports/{reportId} | Get the report
[**get_customers_life_cycle**](CustomerDataApi.md#get_customers_life_cycle) | **GET** /v1/customers/{customerId}/lifecycle | Get customer lifecycle
[**request_customer_report**](CustomerDataApi.md#request_customer_report) | **POST** /v1/customers/{customerId}/reports | Request customer data reports as bulk files


# **fetch_contracts_details_using_get**
> DataPaginationResponse fetch_contracts_details_using_get(contract_number, puid)

Get the list of contracts Details from flat table. It supports pagination , filtering and sorting

### Example

* OAuth Authentication (oAuth2):

```python
import time
import openapi_client
from openapi_client.api import customer_data_api
from openapi_client.model.contracts_error_response import ContractsErrorResponse
from openapi_client.model.data_pagination_response import DataPaginationResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.pxcloud-stg.cisco.com/torii
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.pxcloud-stg.cisco.com/torii"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oAuth2
configuration = openapi_client.Configuration(
    host = "https://api.pxcloud-stg.cisco.com/torii"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = customer_data_api.CustomerDataApi(api_client)
    contract_number = 1 # int | contractNumber
    puid = 1 # int | puid
    component_type = "componentType_example" # str | componentType (optional)
    customer_id = "customerId_example" # str | customerId (optional)
    limit = 1 # int |  (optional)
    offset = 1 # int |  (optional)
    success_track_id = 1 # int | successTrackId (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get the list of contracts Details from flat table. It supports pagination , filtering and sorting
        api_response = api_instance.fetch_contracts_details_using_get(contract_number, puid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CustomerDataApi->fetch_contracts_details_using_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the list of contracts Details from flat table. It supports pagination , filtering and sorting
        api_response = api_instance.fetch_contracts_details_using_get(contract_number, puid, component_type=component_type, customer_id=customer_id, limit=limit, offset=offset, success_track_id=success_track_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CustomerDataApi->fetch_contracts_details_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_number** | **int**| contractNumber |
 **puid** | **int**| puid |
 **component_type** | **str**| componentType | [optional]
 **customer_id** | **str**| customerId | [optional]
 **limit** | **int**|  | [optional]
 **offset** | **int**|  | [optional]
 **success_track_id** | **int**| successTrackId | [optional]

### Return type

[**DataPaginationResponse**](DataPaginationResponse.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully Fetched Contract Details for Given Partner |  * Date -  <br>  |
**400** | Bad Input |  * Date -  <br>  |
**401** | Unauthorized |  * Date -  <br>  |
**403** | Forbidden |  * Date -  <br>  |
**404** | Entity Not Found |  * Date -  <br>  |
**500** | Error during fetch |  * Date -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_report**
> [ReportStatus] get_customer_report(report_id, customer_id)

Get the report

Provides the status of resource. The status API provides additional info about the progress of the report. Partner application should poll periodically to get status of the report. When the report is complete the API responds with the 303 status pointing to final report in the Location header.

### Example

* OAuth Authentication (oAuth2):

```python
import time
import openapi_client
from openapi_client.api import customer_data_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.report_status import ReportStatus
from pprint import pprint
# Defining the host is optional and defaults to https://api.pxcloud-stg.cisco.com/torii
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.pxcloud-stg.cisco.com/torii"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oAuth2
configuration = openapi_client.Configuration(
    host = "https://api.pxcloud-stg.cisco.com/torii"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = customer_data_api.CustomerDataApi(api_client)
    report_id = "reportId_example" # str | Report id
    customer_id = "customerId_example" # str | Unique identifier for the Customer

    # example passing only required values which don't have defaults set
    try:
        # Get the report
        api_response = api_instance.get_customer_report(report_id, customer_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CustomerDataApi->get_customer_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_id** | **str**| Report id |
 **customer_id** | **str**| Unique identifier for the Customer |

### Return type

[**[ReportStatus]**](ReportStatus.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Provides the status of the report |  * Date -  <br>  |
**303** | Provides the final report resource to download the file |  * Date -  <br>  * Location - downloadable URL <br>  |
**400** | Bad Request |  * Date -  <br>  |
**403** | Forbidden |  * Date -  <br>  |
**404** | Not Found |  * Date -  <br>  |
**500** | Internal server error |  * Date -  <br>  |
**503** | Service Unavailable |  * Date -  <br>  |
**504** | Gateway timeout |  * Date -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customers_life_cycle**
> RacetrackBuid get_customers_life_cycle(success_track_id, customer_id)

Get customer lifecycle

Get customer lifecycle which will provide the CX solution, use case and pitstop information for the customer

### Example

* OAuth Authentication (oAuth2):

```python
import time
import openapi_client
from openapi_client.api import customer_data_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.racetrack_buid import RacetrackBuid
from pprint import pprint
# Defining the host is optional and defaults to https://api.pxcloud-stg.cisco.com/torii
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.pxcloud-stg.cisco.com/torii"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oAuth2
configuration = openapi_client.Configuration(
    host = "https://api.pxcloud-stg.cisco.com/torii"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = customer_data_api.CustomerDataApi(api_client)
    success_track_id = "successTrackId_example" # str | 
    customer_id = "customerId_example" # str | Unique identifier for the Customer

    # example passing only required values which don't have defaults set
    try:
        # Get customer lifecycle
        api_response = api_instance.get_customers_life_cycle(success_track_id, customer_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CustomerDataApi->get_customers_life_cycle: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **success_track_id** | **str**|  |
 **customer_id** | **str**| Unique identifier for the Customer |

### Return type

[**RacetrackBuid**](RacetrackBuid.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  * Date -  <br>  |
**400** | Bad Request |  * Date -  <br>  |
**403** | Forbidden |  * Date -  <br>  |
**404** | Not Found |  * Date -  <br>  |
**500** | Internal server error |  * Date -  <br>  |
**503** | Service Unavailable |  * Date -  <br>  |
**504** | Gateway timeout |  * Date -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_customer_report**
> request_customer_report(customer_id)

Request customer data reports as bulk files

Request customer data report. Creating a request for customer data sets like Assets, Hardware, Software and Advisories bulk json files

### Example

* OAuth Authentication (oAuth2):

```python
import time
import openapi_client
from openapi_client.api import customer_data_api
from openapi_client.model.report import Report
from openapi_client.model.error_response import ErrorResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.pxcloud-stg.cisco.com/torii
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.pxcloud-stg.cisco.com/torii"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oAuth2
configuration = openapi_client.Configuration(
    host = "https://api.pxcloud-stg.cisco.com/torii"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = customer_data_api.CustomerDataApi(api_client)
    customer_id = "customerId_example" # str | Unique identifier for the Customer
    report = Report(
        report_name="Assets",
    ) # Report | report infromation (optional)

    # example passing only required values which don't have defaults set
    try:
        # Request customer data reports as bulk files
        api_instance.request_customer_report(customer_id)
    except openapi_client.ApiException as e:
        print("Exception when calling CustomerDataApi->request_customer_report: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Request customer data reports as bulk files
        api_instance.request_customer_report(customer_id, report=report)
    except openapi_client.ApiException as e:
        print("Exception when calling CustomerDataApi->request_customer_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| Unique identifier for the Customer |
 **report** | [**Report**](Report.md)| report infromation | [optional]

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
**202** | Accepted |  * Location - downloadable URL <br>  * Date -  <br>  |
**400** | Bad Request |  * Location - downloadable URL <br>  * Date -  <br>  |
**403** | Forbidden |  * Location - downloadable URL <br>  * Date -  <br>  |
**404** | Not Found |  * Location - downloadable URL <br>  * Date -  <br>  |
**500** | Internal server error |  * Location - downloadable URL <br>  * Date -  <br>  |
**503** | Service Unavailable |  * Location - downloadable URL <br>  * Date -  <br>  |
**504** | Gateway timeout |  * Location - downloadable URL <br>  * Date -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

