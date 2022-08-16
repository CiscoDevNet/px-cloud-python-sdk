# openapi_client.ComplianceApi

All URIs are relative to *https://api.pxcloud-stg.cisco.com/torii*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_asset_violation_details_using_get**](ComplianceApi.md#get_asset_violation_details_using_get) | **GET** /v1/customers/{customerId}/insights/compliance/violations/assets | Get the violation details of impacted assets for the customer, and selected policy Group, Policy and Rule
[**get_asset_violations_using_get**](ComplianceApi.md#get_asset_violations_using_get) | **GET** /v1/customers/{customerId}/insights/compliance/assetViolations | Get the violations of the asset
[**get_asset_with_violations_using_get**](ComplianceApi.md#get_asset_with_violations_using_get) | **GET** /v1/customers/{customerId}/insights/compliance/assetsWithViolations | Get the asset summary
[**get_opt_in_using_get**](ComplianceApi.md#get_opt_in_using_get) | **GET** /v1/customers/{customerId}/insights/compliance/optIn | optIn status
[**get_policy_rule_details_using_get**](ComplianceApi.md#get_policy_rule_details_using_get) | **GET** /v1/customers/{customerId}/insights/compliance/policyRuleDetails | Returns information about the policy the rule belongs to
[**get_suggestions_using_get**](ComplianceApi.md#get_suggestions_using_get) | **GET** /v1/customers/{customerId}/insights/compliance/suggestions | Get the Suggestions filtered upon Severity (if given), for summary tab
[**get_violation_summary_using_get**](ComplianceApi.md#get_violation_summary_using_get) | **GET** /v1/customers/{customerId}/insights/compliance/violations | Get the violation summary of a customer


# **get_asset_violation_details_using_get**
> AssetsViolationsResponse get_asset_violation_details_using_get(success_track_id, customer_id, policy_category, policy_group_id, policy_id, rule_id, severity)

Get the violation details of impacted assets for the customer, and selected policy Group, Policy and Rule

Returns information about the customer assets in violation of the rule based on the customer, policy, and rule information provided. Default sorting is, assetName(asc)

### Example


```python
import time
import openapi_client
from openapi_client.api import compliance_api
from openapi_client.model.assets_violations_response import AssetsViolationsResponse
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
    api_instance = compliance_api.ComplianceApi(api_client)
    success_track_id = "successTrackId_example" # str | 
    customer_id = "customerId_example" # str | 
    policy_category = "policyCategory_example" # str | 
    policy_group_id = "policyGroupId_example" # str | 
    policy_id = "policyId_example" # str | 
    rule_id = "ruleId_example" # str | 
    severity = "severity_example" # str | 
    offset = 1 # int |  (optional) if omitted the server will use the default value of 1
    max = 10 # int |  (optional) if omitted the server will use the default value of 10

    # example passing only required values which don't have defaults set
    try:
        # Get the violation details of impacted assets for the customer, and selected policy Group, Policy and Rule
        api_response = api_instance.get_asset_violation_details_using_get(success_track_id, customer_id, policy_category, policy_group_id, policy_id, rule_id, severity)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ComplianceApi->get_asset_violation_details_using_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the violation details of impacted assets for the customer, and selected policy Group, Policy and Rule
        api_response = api_instance.get_asset_violation_details_using_get(success_track_id, customer_id, policy_category, policy_group_id, policy_id, rule_id, severity, offset=offset, max=max)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ComplianceApi->get_asset_violation_details_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **success_track_id** | **str**|  |
 **customer_id** | **str**|  |
 **policy_category** | **str**|  |
 **policy_group_id** | **str**|  |
 **policy_id** | **str**|  |
 **rule_id** | **str**|  |
 **severity** | **str**|  |
 **offset** | **int**|  | [optional] if omitted the server will use the default value of 1
 **max** | **int**|  | [optional] if omitted the server will use the default value of 10

### Return type

[**AssetsViolationsResponse**](AssetsViolationsResponse.md)

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

# **get_asset_violations_using_get**
> AssetViolationsResponse get_asset_violations_using_get(success_track_id, source_system_id, customer_id, asset_id)

Get the violations of the asset

Returns information about the rules violated by an asset based on the customer and asset information provided. Default is ruleSeverityId(desc)

### Example


```python
import time
import openapi_client
from openapi_client.api import compliance_api
from openapi_client.model.asset_violations_response import AssetViolationsResponse
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
    api_instance = compliance_api.ComplianceApi(api_client)
    success_track_id = "successTrackId_example" # str | 
    source_system_id = "sourceSystemId_example" # str | 
    customer_id = "customerId_example" # str | 
    asset_id = "assetId_example" # str | 
    offset = 1 # int |  (optional) if omitted the server will use the default value of 1
    max = 10 # int |  (optional) if omitted the server will use the default value of 10

    # example passing only required values which don't have defaults set
    try:
        # Get the violations of the asset
        api_response = api_instance.get_asset_violations_using_get(success_track_id, source_system_id, customer_id, asset_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ComplianceApi->get_asset_violations_using_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the violations of the asset
        api_response = api_instance.get_asset_violations_using_get(success_track_id, source_system_id, customer_id, asset_id, offset=offset, max=max)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ComplianceApi->get_asset_violations_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **success_track_id** | **str**|  |
 **source_system_id** | **str**|  |
 **customer_id** | **str**|  |
 **asset_id** | **str**|  |
 **offset** | **int**|  | [optional] if omitted the server will use the default value of 1
 **max** | **int**|  | [optional] if omitted the server will use the default value of 10

### Return type

[**AssetViolationsResponse**](AssetViolationsResponse.md)

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

# **get_asset_with_violations_using_get**
> AssetsWithViolationsResponse get_asset_with_violations_using_get(success_track_id, customer_id)

Get the asset summary

Returns information about assets that have at least one rule violation based on the customerId provided. Default is severityId(desc), violationCount(desc)

### Example


```python
import time
import openapi_client
from openapi_client.api import compliance_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.assets_with_violations_response import AssetsWithViolationsResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.pxcloud-stg.cisco.com/torii
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.pxcloud-stg.cisco.com/torii"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = compliance_api.ComplianceApi(api_client)
    success_track_id = "successTrackId_example" # str | 
    customer_id = "customerId_example" # str | 
    offset = 1 # int |  (optional) if omitted the server will use the default value of 1
    max = 10 # int |  (optional) if omitted the server will use the default value of 10

    # example passing only required values which don't have defaults set
    try:
        # Get the asset summary
        api_response = api_instance.get_asset_with_violations_using_get(success_track_id, customer_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ComplianceApi->get_asset_with_violations_using_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the asset summary
        api_response = api_instance.get_asset_with_violations_using_get(success_track_id, customer_id, offset=offset, max=max)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ComplianceApi->get_asset_with_violations_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **success_track_id** | **str**|  |
 **customer_id** | **str**|  |
 **offset** | **int**|  | [optional] if omitted the server will use the default value of 1
 **max** | **int**|  | [optional] if omitted the server will use the default value of 10

### Return type

[**AssetsWithViolationsResponse**](AssetsWithViolationsResponse.md)

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

# **get_opt_in_using_get**
> OptInResponse get_opt_in_using_get(success_track_id, customer_id)

optIn status

Returns information about whether the customer has successfully configured the regulatory compliance feature and has assets that are qualified to be checked.

### Example


```python
import time
import openapi_client
from openapi_client.api import compliance_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.opt_in_response import OptInResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.pxcloud-stg.cisco.com/torii
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.pxcloud-stg.cisco.com/torii"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = compliance_api.ComplianceApi(api_client)
    success_track_id = "successTrackId_example" # str | 
    customer_id = "customerId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # optIn status
        api_response = api_instance.get_opt_in_using_get(success_track_id, customer_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ComplianceApi->get_opt_in_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **success_track_id** | **str**|  |
 **customer_id** | **str**|  |

### Return type

[**OptInResponse**](OptInResponse.md)

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

# **get_policy_rule_details_using_get**
> PolicyRuleDetails get_policy_rule_details_using_get(success_track_id, customer_id, policy_category, policy_group_id, policy_id, rule_id, severity)

Returns information about the policy the rule belongs to

Returns information about the policy the rule belongs to.

### Example


```python
import time
import openapi_client
from openapi_client.api import compliance_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.policy_rule_details import PolicyRuleDetails
from pprint import pprint
# Defining the host is optional and defaults to https://api.pxcloud-stg.cisco.com/torii
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.pxcloud-stg.cisco.com/torii"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = compliance_api.ComplianceApi(api_client)
    success_track_id = "successTrackId_example" # str | 
    customer_id = "customerId_example" # str | Unique identifier of the customer
    policy_category = "policyCategory_example" # str | 
    policy_group_id = "policyGroupId_example" # str | 
    policy_id = "policyId_example" # str | 
    rule_id = "ruleId_example" # str | 
    severity = "severity_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Returns information about the policy the rule belongs to
        api_response = api_instance.get_policy_rule_details_using_get(success_track_id, customer_id, policy_category, policy_group_id, policy_id, rule_id, severity)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ComplianceApi->get_policy_rule_details_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **success_track_id** | **str**|  |
 **customer_id** | **str**| Unique identifier of the customer |
 **policy_category** | **str**|  |
 **policy_group_id** | **str**|  |
 **policy_id** | **str**|  |
 **rule_id** | **str**|  |
 **severity** | **str**|  |

### Return type

[**PolicyRuleDetails**](PolicyRuleDetails.md)

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

# **get_suggestions_using_get**
> SuggestionsResponse get_suggestions_using_get(policy_category, success_track_id, customer_id, policy_group_id, policy_id, rule_id)

Get the Suggestions filtered upon Severity (if given), for summary tab

Returns information about the violated rule conditions, including suggested remediation steps, based on the customer, policy, and rule information provided. Default sorting is severityId(desc)

### Example


```python
import time
import openapi_client
from openapi_client.api import compliance_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.suggestions_response import SuggestionsResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.pxcloud-stg.cisco.com/torii
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.pxcloud-stg.cisco.com/torii"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = compliance_api.ComplianceApi(api_client)
    policy_category = "policyCategory_example" # str | 
    success_track_id = "successTrackId_example" # str | 
    customer_id = "customerId_example" # str | 
    policy_group_id = "policyGroupId_example" # str | 
    policy_id = "policyId_example" # str | 
    rule_id = "ruleId_example" # str | 
    offset = 1 # int |  (optional) if omitted the server will use the default value of 1
    max = 10 # int |  (optional) if omitted the server will use the default value of 10

    # example passing only required values which don't have defaults set
    try:
        # Get the Suggestions filtered upon Severity (if given), for summary tab
        api_response = api_instance.get_suggestions_using_get(policy_category, success_track_id, customer_id, policy_group_id, policy_id, rule_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ComplianceApi->get_suggestions_using_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the Suggestions filtered upon Severity (if given), for summary tab
        api_response = api_instance.get_suggestions_using_get(policy_category, success_track_id, customer_id, policy_group_id, policy_id, rule_id, offset=offset, max=max)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ComplianceApi->get_suggestions_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_category** | **str**|  |
 **success_track_id** | **str**|  |
 **customer_id** | **str**|  |
 **policy_group_id** | **str**|  |
 **policy_id** | **str**|  |
 **rule_id** | **str**|  |
 **offset** | **int**|  | [optional] if omitted the server will use the default value of 1
 **max** | **int**|  | [optional] if omitted the server will use the default value of 10

### Return type

[**SuggestionsResponse**](SuggestionsResponse.md)

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

# **get_violation_summary_using_get**
> ViolationSummaryResponse get_violation_summary_using_get(success_track_id, customer_id)

Get the violation summary of a customer

Returns information about the rules violated for the customerId provided Default sorting is, severityId(asc), violationCount(desc)

### Example


```python
import time
import openapi_client
from openapi_client.api import compliance_api
from openapi_client.model.violation_summary_response import ViolationSummaryResponse
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
    api_instance = compliance_api.ComplianceApi(api_client)
    success_track_id = "successTrackId_example" # str | 
    customer_id = "customerId_example" # str | Unique identifier of the customer
    offset = 1 # int | The number of items to skip before starting to collect the result set. The default value is 1. (optional) if omitted the server will use the default value of 1
    max = 10 # int | The maximum number of items to return. The default value is 10. (optional) if omitted the server will use the default value of 10

    # example passing only required values which don't have defaults set
    try:
        # Get the violation summary of a customer
        api_response = api_instance.get_violation_summary_using_get(success_track_id, customer_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ComplianceApi->get_violation_summary_using_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the violation summary of a customer
        api_response = api_instance.get_violation_summary_using_get(success_track_id, customer_id, offset=offset, max=max)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ComplianceApi->get_violation_summary_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **success_track_id** | **str**|  |
 **customer_id** | **str**| Unique identifier of the customer |
 **offset** | **int**| The number of items to skip before starting to collect the result set. The default value is 1. | [optional] if omitted the server will use the default value of 1
 **max** | **int**| The maximum number of items to return. The default value is 10. | [optional] if omitted the server will use the default value of 10

### Return type

[**ViolationSummaryResponse**](ViolationSummaryResponse.md)

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

