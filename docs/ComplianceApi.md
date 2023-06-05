# pxcloud_api_client.ComplianceApi

All URIs are relative to *https://api-cx.cisco.com/sandbox/px*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_asset_violations**](ComplianceApi.md#get_asset_violations) | **GET** /v1/customers/{customerId}/insights/compliance/assetViolations | List the violations of the asset
[**get_assets_with_violations**](ComplianceApi.md#get_assets_with_violations) | **GET** /v1/customers/{customerId}/insights/compliance/assetsWithViolations | Fetch the asset summary
[**get_opt_in**](ComplianceApi.md#get_opt_in) | **GET** /v1/customers/{customerId}/insights/compliance/optIn | Fetch optIn status
[**get_policy_rule_details**](ComplianceApi.md#get_policy_rule_details) | **GET** /v1/customers/{customerId}/insights/compliance/policyRuleDetails | Fetch information about the policy the rule belongs to
[**get_suggestions**](ComplianceApi.md#get_suggestions) | **GET** /v1/customers/{customerId}/insights/compliance/suggestions | Get the Suggestions filtered upon Severity (if given), for summary tab
[**get_violations**](ComplianceApi.md#get_violations) | **GET** /v1/customers/{customerId}/insights/compliance/violations | Fetch the violation summary of a customer
[**get_violations_assets**](ComplianceApi.md#get_violations_assets) | **GET** /v1/customers/{customerId}/insights/compliance/violations/assets | Fetch the violation details of impacted assets for the customer, and selected policy Group, Policy and Rule


# **get_asset_violations**
> AssetViolationsResponse get_asset_violations(success_track_id, source_system_id, customer_id, asset_id)

List the violations of the asset

Returns information about the rules violated by an asset based on the customer and asset information provided. Default is ruleSeverityId(desc)

### Example

* OAuth Authentication (oAuth2):

```python
import time
import pxcloud_api_client
from pxcloud_api_client.api import compliance_api
from pxcloud_api_client.model.error_response import ErrorResponse
from pxcloud_api_client.model.asset_violations_response import AssetViolationsResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-cx.cisco.com/sandbox/px
# See configuration.py for a list of all supported configuration parameters.
configuration = pxcloud_api_client.Configuration(
    host = "https://api-cx.cisco.com/sandbox/px"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oAuth2
configuration = pxcloud_api_client.Configuration(
    host = "https://api-cx.cisco.com/sandbox/px"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pxcloud_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = compliance_api.ComplianceApi(api_client)
    success_track_id = "successTrackId_example" # str | 
    source_system_id = "sourceSystemId_example" # str | 
    customer_id = "customerId_example" # str | Unique identifier of the customer
    asset_id = "assetId_example" # str | 
    offset = 1 # int | The number of items to skip before starting to collect the result set. The default value is 1. (optional) if omitted the server will use the default value of 1
    max = 10 # int | The maximum number of items to return. The default value is 10. (optional) if omitted the server will use the default value of 10

    # example passing only required values which don't have defaults set
    try:
        # List the violations of the asset
        api_response = api_instance.get_asset_violations(success_track_id, source_system_id, customer_id, asset_id)
        pprint(api_response)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling ComplianceApi->get_asset_violations: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List the violations of the asset
        api_response = api_instance.get_asset_violations(success_track_id, source_system_id, customer_id, asset_id, offset=offset, max=max)
        pprint(api_response)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling ComplianceApi->get_asset_violations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **success_track_id** | **str**|  |
 **source_system_id** | **str**|  |
 **customer_id** | **str**| Unique identifier of the customer |
 **asset_id** | **str**|  |
 **offset** | **int**| The number of items to skip before starting to collect the result set. The default value is 1. | [optional] if omitted the server will use the default value of 1
 **max** | **int**| The maximum number of items to return. The default value is 10. | [optional] if omitted the server will use the default value of 10

### Return type

[**AssetViolationsResponse**](AssetViolationsResponse.md)

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

# **get_assets_with_violations**
> AssetsWithViolationsResponse get_assets_with_violations(success_track_id, customer_id)

Fetch the asset summary

Returns information about assets that have at least one rule violation based on the customerId provided. Default is severityId(desc), violationCount(desc)

### Example

* OAuth Authentication (oAuth2):

```python
import time
import pxcloud_api_client
from pxcloud_api_client.api import compliance_api
from pxcloud_api_client.model.error_response import ErrorResponse
from pxcloud_api_client.model.assets_with_violations_response import AssetsWithViolationsResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-cx.cisco.com/sandbox/px
# See configuration.py for a list of all supported configuration parameters.
configuration = pxcloud_api_client.Configuration(
    host = "https://api-cx.cisco.com/sandbox/px"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oAuth2
configuration = pxcloud_api_client.Configuration(
    host = "https://api-cx.cisco.com/sandbox/px"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pxcloud_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = compliance_api.ComplianceApi(api_client)
    success_track_id = "successTrackId_example" # str | 
    customer_id = "customerId_example" # str | Unique identifier of the customer
    offset = 1 # int | The number of items to skip before starting to collect the result set. The default value is 1. (optional) if omitted the server will use the default value of 1
    max = 10 # int | The maximum number of items to return. The default value is 10. (optional) if omitted the server will use the default value of 10

    # example passing only required values which don't have defaults set
    try:
        # Fetch the asset summary
        api_response = api_instance.get_assets_with_violations(success_track_id, customer_id)
        pprint(api_response)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling ComplianceApi->get_assets_with_violations: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch the asset summary
        api_response = api_instance.get_assets_with_violations(success_track_id, customer_id, offset=offset, max=max)
        pprint(api_response)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling ComplianceApi->get_assets_with_violations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **success_track_id** | **str**|  |
 **customer_id** | **str**| Unique identifier of the customer |
 **offset** | **int**| The number of items to skip before starting to collect the result set. The default value is 1. | [optional] if omitted the server will use the default value of 1
 **max** | **int**| The maximum number of items to return. The default value is 10. | [optional] if omitted the server will use the default value of 10

### Return type

[**AssetsWithViolationsResponse**](AssetsWithViolationsResponse.md)

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

# **get_opt_in**
> OptInResponse get_opt_in(success_track_id, customer_id)

Fetch optIn status

Returns information about whether the customer has successfully configured the regulatory compliance feature and has assets that are qualified to be checked.

### Example

* OAuth Authentication (oAuth2):

```python
import time
import pxcloud_api_client
from pxcloud_api_client.api import compliance_api
from pxcloud_api_client.model.error_response import ErrorResponse
from pxcloud_api_client.model.opt_in_response import OptInResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-cx.cisco.com/sandbox/px
# See configuration.py for a list of all supported configuration parameters.
configuration = pxcloud_api_client.Configuration(
    host = "https://api-cx.cisco.com/sandbox/px"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oAuth2
configuration = pxcloud_api_client.Configuration(
    host = "https://api-cx.cisco.com/sandbox/px"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pxcloud_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = compliance_api.ComplianceApi(api_client)
    success_track_id = "successTrackId_example" # str | 
    customer_id = "customerId_example" # str | Unique identifier of the customer

    # example passing only required values which don't have defaults set
    try:
        # Fetch optIn status
        api_response = api_instance.get_opt_in(success_track_id, customer_id)
        pprint(api_response)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling ComplianceApi->get_opt_in: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **success_track_id** | **str**|  |
 **customer_id** | **str**| Unique identifier of the customer |

### Return type

[**OptInResponse**](OptInResponse.md)

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

# **get_policy_rule_details**
> PolicyRuleDetails get_policy_rule_details(success_track_id, customer_id, policy_category, policy_group_id, policy_id, rule_id, severity)

Fetch information about the policy the rule belongs to

Returns information about the policy the rule belongs to.

### Example

* OAuth Authentication (oAuth2):

```python
import time
import pxcloud_api_client
from pxcloud_api_client.api import compliance_api
from pxcloud_api_client.model.policy_rule_details import PolicyRuleDetails
from pxcloud_api_client.model.error_response import ErrorResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-cx.cisco.com/sandbox/px
# See configuration.py for a list of all supported configuration parameters.
configuration = pxcloud_api_client.Configuration(
    host = "https://api-cx.cisco.com/sandbox/px"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oAuth2
configuration = pxcloud_api_client.Configuration(
    host = "https://api-cx.cisco.com/sandbox/px"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pxcloud_api_client.ApiClient(configuration) as api_client:
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
        # Fetch information about the policy the rule belongs to
        api_response = api_instance.get_policy_rule_details(success_track_id, customer_id, policy_category, policy_group_id, policy_id, rule_id, severity)
        pprint(api_response)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling ComplianceApi->get_policy_rule_details: %s\n" % e)
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

# **get_suggestions**
> SuggestionsResponse get_suggestions(policy_category, success_track_id, customer_id, policy_group_id, policy_id, rule_id)

Get the Suggestions filtered upon Severity (if given), for summary tab

Returns information about the violated rule conditions, including suggested remediation steps, based on the customer, policy, and rule information provided. Default sorting is severityId(desc)

### Example

* OAuth Authentication (oAuth2):

```python
import time
import pxcloud_api_client
from pxcloud_api_client.api import compliance_api
from pxcloud_api_client.model.error_response import ErrorResponse
from pxcloud_api_client.model.suggestions_response import SuggestionsResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-cx.cisco.com/sandbox/px
# See configuration.py for a list of all supported configuration parameters.
configuration = pxcloud_api_client.Configuration(
    host = "https://api-cx.cisco.com/sandbox/px"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oAuth2
configuration = pxcloud_api_client.Configuration(
    host = "https://api-cx.cisco.com/sandbox/px"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pxcloud_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = compliance_api.ComplianceApi(api_client)
    policy_category = "policyCategory_example" # str | 
    success_track_id = "successTrackId_example" # str | 
    customer_id = "customerId_example" # str | Unique identifier of the customer
    policy_group_id = "policyGroupId_example" # str | 
    policy_id = "policyId_example" # str | 
    rule_id = "ruleId_example" # str | 
    offset = 1 # int | The number of items to skip before starting to collect the result set. The default value is 1. (optional) if omitted the server will use the default value of 1
    max = 10 # int | The maximum number of items to return. The default value is 10. (optional) if omitted the server will use the default value of 10

    # example passing only required values which don't have defaults set
    try:
        # Get the Suggestions filtered upon Severity (if given), for summary tab
        api_response = api_instance.get_suggestions(policy_category, success_track_id, customer_id, policy_group_id, policy_id, rule_id)
        pprint(api_response)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling ComplianceApi->get_suggestions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the Suggestions filtered upon Severity (if given), for summary tab
        api_response = api_instance.get_suggestions(policy_category, success_track_id, customer_id, policy_group_id, policy_id, rule_id, offset=offset, max=max)
        pprint(api_response)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling ComplianceApi->get_suggestions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_category** | **str**|  |
 **success_track_id** | **str**|  |
 **customer_id** | **str**| Unique identifier of the customer |
 **policy_group_id** | **str**|  |
 **policy_id** | **str**|  |
 **rule_id** | **str**|  |
 **offset** | **int**| The number of items to skip before starting to collect the result set. The default value is 1. | [optional] if omitted the server will use the default value of 1
 **max** | **int**| The maximum number of items to return. The default value is 10. | [optional] if omitted the server will use the default value of 10

### Return type

[**SuggestionsResponse**](SuggestionsResponse.md)

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

# **get_violations**
> ViolationSummaryResponse get_violations(success_track_id, customer_id)

Fetch the violation summary of a customer

Returns information about the rules violated for the customerId provided Default sorting is, severityId(asc), violationCount(desc)

### Example

* OAuth Authentication (oAuth2):

```python
import time
import pxcloud_api_client
from pxcloud_api_client.api import compliance_api
from pxcloud_api_client.model.violation_summary_response import ViolationSummaryResponse
from pxcloud_api_client.model.error_response import ErrorResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-cx.cisco.com/sandbox/px
# See configuration.py for a list of all supported configuration parameters.
configuration = pxcloud_api_client.Configuration(
    host = "https://api-cx.cisco.com/sandbox/px"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oAuth2
configuration = pxcloud_api_client.Configuration(
    host = "https://api-cx.cisco.com/sandbox/px"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pxcloud_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = compliance_api.ComplianceApi(api_client)
    success_track_id = "successTrackId_example" # str | 
    customer_id = "customerId_example" # str | Unique identifier of the customer
    offset = 1 # int | The number of items to skip before starting to collect the result set. The default value is 1. (optional) if omitted the server will use the default value of 1
    max = 10 # int | The maximum number of items to return. The default value is 10. (optional) if omitted the server will use the default value of 10

    # example passing only required values which don't have defaults set
    try:
        # Fetch the violation summary of a customer
        api_response = api_instance.get_violations(success_track_id, customer_id)
        pprint(api_response)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling ComplianceApi->get_violations: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch the violation summary of a customer
        api_response = api_instance.get_violations(success_track_id, customer_id, offset=offset, max=max)
        pprint(api_response)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling ComplianceApi->get_violations: %s\n" % e)
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

# **get_violations_assets**
> AssetsViolationsResponse get_violations_assets(success_track_id, customer_id, policy_category, policy_group_id, policy_id, rule_id, severity)

Fetch the violation details of impacted assets for the customer, and selected policy Group, Policy and Rule

Returns information about the customer assets in violation of the rule based on the customer, policy, and rule information provided. Default sorting is, assetName(asc)

### Example

* OAuth Authentication (oAuth2):

```python
import time
import pxcloud_api_client
from pxcloud_api_client.api import compliance_api
from pxcloud_api_client.model.error_response import ErrorResponse
from pxcloud_api_client.model.assets_violations_response import AssetsViolationsResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-cx.cisco.com/sandbox/px
# See configuration.py for a list of all supported configuration parameters.
configuration = pxcloud_api_client.Configuration(
    host = "https://api-cx.cisco.com/sandbox/px"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oAuth2
configuration = pxcloud_api_client.Configuration(
    host = "https://api-cx.cisco.com/sandbox/px"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pxcloud_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = compliance_api.ComplianceApi(api_client)
    success_track_id = "successTrackId_example" # str | 
    customer_id = "customerId_example" # str | Unique identifier of the customer
    policy_category = "policyCategory_example" # str | 
    policy_group_id = "policyGroupId_example" # str | 
    policy_id = "policyId_example" # str | 
    rule_id = "ruleId_example" # str | 
    severity = "severity_example" # str | 
    offset = 1 # int | The number of items to skip before starting to collect the result set. The default value is 1. (optional) if omitted the server will use the default value of 1
    max = 10 # int | The maximum number of items to return. The default value is 10. (optional) if omitted the server will use the default value of 10

    # example passing only required values which don't have defaults set
    try:
        # Fetch the violation details of impacted assets for the customer, and selected policy Group, Policy and Rule
        api_response = api_instance.get_violations_assets(success_track_id, customer_id, policy_category, policy_group_id, policy_id, rule_id, severity)
        pprint(api_response)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling ComplianceApi->get_violations_assets: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch the violation details of impacted assets for the customer, and selected policy Group, Policy and Rule
        api_response = api_instance.get_violations_assets(success_track_id, customer_id, policy_category, policy_group_id, policy_id, rule_id, severity, offset=offset, max=max)
        pprint(api_response)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling ComplianceApi->get_violations_assets: %s\n" % e)
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
 **offset** | **int**| The number of items to skip before starting to collect the result set. The default value is 1. | [optional] if omitted the server will use the default value of 1
 **max** | **int**| The maximum number of items to return. The default value is 10. | [optional] if omitted the server will use the default value of 10

### Return type

[**AssetsViolationsResponse**](AssetsViolationsResponse.md)

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

