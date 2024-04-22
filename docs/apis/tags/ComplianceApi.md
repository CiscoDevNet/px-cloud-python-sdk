<a id="__pageTop"></a>
# pxcloud_api_client.apis.tags.compliance_api.ComplianceApi

All URIs are relative to *https://api-cx.cisco.com/sandbox/px*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_asset_violations**](#get_asset_violations) | **get** /v1/customers/{customerId}/insights/compliance/assetViolations | List the violations of the asset
[**get_assets_with_violations**](#get_assets_with_violations) | **get** /v1/customers/{customerId}/insights/compliance/assetsWithViolations | Fetch the asset summary
[**get_opt_in**](#get_opt_in) | **get** /v1/customers/{customerId}/insights/compliance/optIn | Fetch optIn status
[**get_policy_rule_details**](#get_policy_rule_details) | **get** /v1/customers/{customerId}/insights/compliance/policyRuleDetails | Fetch information about the policy the rule belongs to
[**get_suggestions**](#get_suggestions) | **get** /v1/customers/{customerId}/insights/compliance/suggestions | Get the Suggestions filtered upon Severity (if given), for summary tab
[**get_violations**](#get_violations) | **get** /v1/customers/{customerId}/insights/compliance/violations | Fetch the violation summary of a customer
[**get_violations_assets**](#get_violations_assets) | **get** /v1/customers/{customerId}/insights/compliance/violations/assets | Fetch the violation details of impacted assets for the customer, and selected policy Group, Policy and Rule

# **get_asset_violations**
<a id="get_asset_violations"></a>
> AssetViolationsResponse get_asset_violations(success_track_idsource_system_idcustomer_idasset_id)

List the violations of the asset

Returns information about the rules violated by an asset based on the customer and asset information provided. Default is ruleSeverityId(desc)

### Example

* OAuth Authentication (oAuth2):
```python
import pxcloud_api_client
from pxcloud_api_client.apis.tags import compliance_api
from pxcloud_api_client.pxcloud_api_client.asset_violations_response import AssetViolationsResponse
from pxcloud_api_client.pxcloud_api_client.error_response import ErrorResponse
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
    host = "https://api-cx.cisco.com/sandbox/px",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with pxcloud_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = compliance_api.ComplianceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'customerId': "customerId_example",
    }
    query_params = {
        'successTrackId': "successTrackId_example",
        'sourceSystemId': "sourceSystemId_example",
        'assetId': "assetId_example",
    }
    try:
        # List the violations of the asset
        api_response = api_instance.get_asset_violations(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling ComplianceApi->get_asset_violations: %s\n" % e)

    # example passing only optional values
    path_params = {
        'customerId': "customerId_example",
    }
    query_params = {
        'successTrackId': "successTrackId_example",
        'sourceSystemId': "sourceSystemId_example",
        'assetId': "assetId_example",
        'offset': 1,
        'max': 10,
    }
    try:
        # List the violations of the asset
        api_response = api_instance.get_asset_violations(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling ComplianceApi->get_asset_violations: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
successTrackId | SuccessTrackIdSchema | | 
sourceSystemId | SourceSystemIdSchema | | 
assetId | AssetIdSchema | | 
offset | OffsetSchema | | optional
max | MaxSchema | | optional


# SuccessTrackIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SourceSystemIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AssetIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# OffsetSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 1value must be a 32 bit integer

# MaxSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 10value must be a 32 bit integer

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
customerId | CustomerIdSchema | | 

# CustomerIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_asset_violations.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_asset_violations.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#get_asset_violations.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#get_asset_violations.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_asset_violations.ApiResponseFor404) | Not found
500 | [ApiResponseFor500](#get_asset_violations.ApiResponseFor500) | Internal server error
503 | [ApiResponseFor503](#get_asset_violations.ApiResponseFor503) | Service Unavailable
504 | [ApiResponseFor504](#get_asset_violations.ApiResponseFor504) | Gateway timeout

#### get_asset_violations.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AssetViolationsResponse**](../../models/AssetViolationsResponse.md) |  | 


#### get_asset_violations.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_asset_violations.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_asset_violations.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_asset_violations.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_asset_violations.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_asset_violations.ApiResponseFor503
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor503ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor503ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_asset_violations.ApiResponseFor504
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor504ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor504ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


### Authorization

[oAuth2](../../../README.md#oAuth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_assets_with_violations**
<a id="get_assets_with_violations"></a>
> AssetsWithViolationsResponse get_assets_with_violations(success_track_idcustomer_id)

Fetch the asset summary

Returns information about assets that have at least one rule violation based on the customerId provided. Default is severityId(desc), violationCount(desc)

### Example

* OAuth Authentication (oAuth2):
```python
import pxcloud_api_client
from pxcloud_api_client.apis.tags import compliance_api
from pxcloud_api_client.pxcloud_api_client.assets_with_violations_response import AssetsWithViolationsResponse
from pxcloud_api_client.pxcloud_api_client.error_response import ErrorResponse
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
    host = "https://api-cx.cisco.com/sandbox/px",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with pxcloud_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = compliance_api.ComplianceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'customerId': "customerId_example",
    }
    query_params = {
        'successTrackId': "successTrackId_example",
    }
    try:
        # Fetch the asset summary
        api_response = api_instance.get_assets_with_violations(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling ComplianceApi->get_assets_with_violations: %s\n" % e)

    # example passing only optional values
    path_params = {
        'customerId': "customerId_example",
    }
    query_params = {
        'successTrackId': "successTrackId_example",
        'offset': 1,
        'max': 10,
    }
    try:
        # Fetch the asset summary
        api_response = api_instance.get_assets_with_violations(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling ComplianceApi->get_assets_with_violations: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
successTrackId | SuccessTrackIdSchema | | 
offset | OffsetSchema | | optional
max | MaxSchema | | optional


# SuccessTrackIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# OffsetSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 1value must be a 32 bit integer

# MaxSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 10value must be a 32 bit integer

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
customerId | CustomerIdSchema | | 

# CustomerIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_assets_with_violations.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_assets_with_violations.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#get_assets_with_violations.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#get_assets_with_violations.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_assets_with_violations.ApiResponseFor404) | Not found
500 | [ApiResponseFor500](#get_assets_with_violations.ApiResponseFor500) | Internal server error
503 | [ApiResponseFor503](#get_assets_with_violations.ApiResponseFor503) | Service Unavailable
504 | [ApiResponseFor504](#get_assets_with_violations.ApiResponseFor504) | Gateway timeout

#### get_assets_with_violations.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AssetsWithViolationsResponse**](../../models/AssetsWithViolationsResponse.md) |  | 


#### get_assets_with_violations.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_assets_with_violations.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_assets_with_violations.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_assets_with_violations.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_assets_with_violations.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_assets_with_violations.ApiResponseFor503
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor503ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor503ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_assets_with_violations.ApiResponseFor504
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor504ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor504ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


### Authorization

[oAuth2](../../../README.md#oAuth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_opt_in**
<a id="get_opt_in"></a>
> OptInResponse get_opt_in(success_track_idcustomer_id)

Fetch optIn status

Returns information about whether the customer has successfully configured the regulatory compliance feature and has assets that are qualified to be checked.

### Example

* OAuth Authentication (oAuth2):
```python
import pxcloud_api_client
from pxcloud_api_client.apis.tags import compliance_api
from pxcloud_api_client.pxcloud_api_client.opt_in_response import OptInResponse
from pxcloud_api_client.pxcloud_api_client.error_response import ErrorResponse
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
    host = "https://api-cx.cisco.com/sandbox/px",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with pxcloud_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = compliance_api.ComplianceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'customerId': "customerId_example",
    }
    query_params = {
        'successTrackId': "successTrackId_example",
    }
    try:
        # Fetch optIn status
        api_response = api_instance.get_opt_in(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling ComplianceApi->get_opt_in: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
successTrackId | SuccessTrackIdSchema | | 


# SuccessTrackIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
customerId | CustomerIdSchema | | 

# CustomerIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_opt_in.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_opt_in.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#get_opt_in.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#get_opt_in.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_opt_in.ApiResponseFor404) | Not found
500 | [ApiResponseFor500](#get_opt_in.ApiResponseFor500) | Internal server error
503 | [ApiResponseFor503](#get_opt_in.ApiResponseFor503) | Service Unavailable
504 | [ApiResponseFor504](#get_opt_in.ApiResponseFor504) | Gateway timeout

#### get_opt_in.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**OptInResponse**](../../models/OptInResponse.md) |  | 


#### get_opt_in.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_opt_in.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_opt_in.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_opt_in.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_opt_in.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_opt_in.ApiResponseFor503
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor503ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor503ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_opt_in.ApiResponseFor504
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor504ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor504ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


### Authorization

[oAuth2](../../../README.md#oAuth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_policy_rule_details**
<a id="get_policy_rule_details"></a>
> PolicyRuleDetails get_policy_rule_details(success_track_idcustomer_idpolicy_categorypolicy_group_idpolicy_idrule_idseverity)

Fetch information about the policy the rule belongs to

Returns information about the policy the rule belongs to.

### Example

* OAuth Authentication (oAuth2):
```python
import pxcloud_api_client
from pxcloud_api_client.apis.tags import compliance_api
from pxcloud_api_client.pxcloud_api_client.error_response import ErrorResponse
from pxcloud_api_client.pxcloud_api_client.policy_rule_details import PolicyRuleDetails
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
    host = "https://api-cx.cisco.com/sandbox/px",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with pxcloud_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = compliance_api.ComplianceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'customerId': "customerId_example",
    }
    query_params = {
        'successTrackId': "successTrackId_example",
        'policyCategory': "policyCategory_example",
        'policyGroupId': "policyGroupId_example",
        'policyId': "policyId_example",
        'ruleId': "ruleId_example",
        'severity': "severity_example",
    }
    try:
        # Fetch information about the policy the rule belongs to
        api_response = api_instance.get_policy_rule_details(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling ComplianceApi->get_policy_rule_details: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
successTrackId | SuccessTrackIdSchema | | 
policyCategory | PolicyCategorySchema | | 
policyGroupId | PolicyGroupIdSchema | | 
policyId | PolicyIdSchema | | 
ruleId | RuleIdSchema | | 
severity | SeveritySchema | | 


# SuccessTrackIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PolicyCategorySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PolicyGroupIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PolicyIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# RuleIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SeveritySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
customerId | CustomerIdSchema | | 

# CustomerIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_policy_rule_details.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_policy_rule_details.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#get_policy_rule_details.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#get_policy_rule_details.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_policy_rule_details.ApiResponseFor404) | Not found
500 | [ApiResponseFor500](#get_policy_rule_details.ApiResponseFor500) | Internal server error
503 | [ApiResponseFor503](#get_policy_rule_details.ApiResponseFor503) | Service Unavailable
504 | [ApiResponseFor504](#get_policy_rule_details.ApiResponseFor504) | Gateway timeout

#### get_policy_rule_details.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PolicyRuleDetails**](../../models/PolicyRuleDetails.md) |  | 


#### get_policy_rule_details.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_policy_rule_details.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_policy_rule_details.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_policy_rule_details.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_policy_rule_details.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_policy_rule_details.ApiResponseFor503
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor503ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor503ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_policy_rule_details.ApiResponseFor504
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor504ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor504ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


### Authorization

[oAuth2](../../../README.md#oAuth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_suggestions**
<a id="get_suggestions"></a>
> SuggestionsResponse get_suggestions(policy_categorysuccess_track_idcustomer_idpolicy_group_idpolicy_idrule_id)

Get the Suggestions filtered upon Severity (if given), for summary tab

Returns information about the violated rule conditions, including suggested remediation steps, based on the customer, policy, and rule information provided. Default sorting is severityId(desc)

### Example

* OAuth Authentication (oAuth2):
```python
import pxcloud_api_client
from pxcloud_api_client.apis.tags import compliance_api
from pxcloud_api_client.pxcloud_api_client.error_response import ErrorResponse
from pxcloud_api_client.pxcloud_api_client.suggestions_response import SuggestionsResponse
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
    host = "https://api-cx.cisco.com/sandbox/px",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with pxcloud_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = compliance_api.ComplianceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'customerId': "customerId_example",
    }
    query_params = {
        'policyCategory': "policyCategory_example",
        'successTrackId': "successTrackId_example",
        'policyGroupId': "policyGroupId_example",
        'policyId': "policyId_example",
        'ruleId': "ruleId_example",
    }
    try:
        # Get the Suggestions filtered upon Severity (if given), for summary tab
        api_response = api_instance.get_suggestions(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling ComplianceApi->get_suggestions: %s\n" % e)

    # example passing only optional values
    path_params = {
        'customerId': "customerId_example",
    }
    query_params = {
        'policyCategory': "policyCategory_example",
        'successTrackId': "successTrackId_example",
        'policyGroupId': "policyGroupId_example",
        'policyId': "policyId_example",
        'ruleId': "ruleId_example",
        'offset': 1,
        'max': 10,
    }
    try:
        # Get the Suggestions filtered upon Severity (if given), for summary tab
        api_response = api_instance.get_suggestions(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling ComplianceApi->get_suggestions: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
policyCategory | PolicyCategorySchema | | 
successTrackId | SuccessTrackIdSchema | | 
policyGroupId | PolicyGroupIdSchema | | 
policyId | PolicyIdSchema | | 
ruleId | RuleIdSchema | | 
offset | OffsetSchema | | optional
max | MaxSchema | | optional


# PolicyCategorySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SuccessTrackIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PolicyGroupIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PolicyIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# RuleIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# OffsetSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 1value must be a 32 bit integer

# MaxSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 10value must be a 32 bit integer

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
customerId | CustomerIdSchema | | 

# CustomerIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_suggestions.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_suggestions.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#get_suggestions.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#get_suggestions.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_suggestions.ApiResponseFor404) | Not found
500 | [ApiResponseFor500](#get_suggestions.ApiResponseFor500) | Internal server error
503 | [ApiResponseFor503](#get_suggestions.ApiResponseFor503) | Service Unavailable
504 | [ApiResponseFor504](#get_suggestions.ApiResponseFor504) | Gateway timeout

#### get_suggestions.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SuggestionsResponse**](../../models/SuggestionsResponse.md) |  | 


#### get_suggestions.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_suggestions.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_suggestions.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_suggestions.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_suggestions.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_suggestions.ApiResponseFor503
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor503ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor503ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_suggestions.ApiResponseFor504
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor504ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor504ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


### Authorization

[oAuth2](../../../README.md#oAuth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_violations**
<a id="get_violations"></a>
> ViolationSummaryResponse get_violations(success_track_idcustomer_id)

Fetch the violation summary of a customer

Returns information about the rules violated for the customerId provided Default sorting is, severityId(asc), violationCount(desc)

### Example

* OAuth Authentication (oAuth2):
```python
import pxcloud_api_client
from pxcloud_api_client.apis.tags import compliance_api
from pxcloud_api_client.pxcloud_api_client.violation_summary_response import ViolationSummaryResponse
from pxcloud_api_client.pxcloud_api_client.error_response import ErrorResponse
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
    host = "https://api-cx.cisco.com/sandbox/px",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with pxcloud_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = compliance_api.ComplianceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'customerId': "customerId_example",
    }
    query_params = {
        'successTrackId': "successTrackId_example",
    }
    try:
        # Fetch the violation summary of a customer
        api_response = api_instance.get_violations(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling ComplianceApi->get_violations: %s\n" % e)

    # example passing only optional values
    path_params = {
        'customerId': "customerId_example",
    }
    query_params = {
        'successTrackId': "successTrackId_example",
        'offset': 1,
        'max': 10,
    }
    try:
        # Fetch the violation summary of a customer
        api_response = api_instance.get_violations(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling ComplianceApi->get_violations: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
successTrackId | SuccessTrackIdSchema | | 
offset | OffsetSchema | | optional
max | MaxSchema | | optional


# SuccessTrackIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# OffsetSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 1value must be a 32 bit integer

# MaxSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 10value must be a 32 bit integer

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
customerId | CustomerIdSchema | | 

# CustomerIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_violations.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_violations.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#get_violations.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#get_violations.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_violations.ApiResponseFor404) | Not found
500 | [ApiResponseFor500](#get_violations.ApiResponseFor500) | Internal server error
503 | [ApiResponseFor503](#get_violations.ApiResponseFor503) | Service Unavailable
504 | [ApiResponseFor504](#get_violations.ApiResponseFor504) | Gateway timeout

#### get_violations.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ViolationSummaryResponse**](../../models/ViolationSummaryResponse.md) |  | 


#### get_violations.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_violations.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_violations.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_violations.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_violations.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_violations.ApiResponseFor503
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor503ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor503ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_violations.ApiResponseFor504
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor504ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor504ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


### Authorization

[oAuth2](../../../README.md#oAuth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_violations_assets**
<a id="get_violations_assets"></a>
> AssetsViolationsResponse get_violations_assets(success_track_idcustomer_idpolicy_categorypolicy_group_idpolicy_idrule_idseverity)

Fetch the violation details of impacted assets for the customer, and selected policy Group, Policy and Rule

Returns information about the customer assets in violation of the rule based on the customer, policy, and rule information provided. Default sorting is, assetName(asc)

### Example

* OAuth Authentication (oAuth2):
```python
import pxcloud_api_client
from pxcloud_api_client.apis.tags import compliance_api
from pxcloud_api_client.pxcloud_api_client.error_response import ErrorResponse
from pxcloud_api_client.pxcloud_api_client.assets_violations_response import AssetsViolationsResponse
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
    host = "https://api-cx.cisco.com/sandbox/px",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with pxcloud_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = compliance_api.ComplianceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'customerId': "customerId_example",
    }
    query_params = {
        'successTrackId': "successTrackId_example",
        'policyCategory': "policyCategory_example",
        'policyGroupId': "policyGroupId_example",
        'policyId': "policyId_example",
        'ruleId': "ruleId_example",
        'severity': "severity_example",
    }
    try:
        # Fetch the violation details of impacted assets for the customer, and selected policy Group, Policy and Rule
        api_response = api_instance.get_violations_assets(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling ComplianceApi->get_violations_assets: %s\n" % e)

    # example passing only optional values
    path_params = {
        'customerId': "customerId_example",
    }
    query_params = {
        'successTrackId': "successTrackId_example",
        'policyCategory': "policyCategory_example",
        'policyGroupId': "policyGroupId_example",
        'policyId': "policyId_example",
        'ruleId': "ruleId_example",
        'severity': "severity_example",
        'offset': 1,
        'max': 10,
    }
    try:
        # Fetch the violation details of impacted assets for the customer, and selected policy Group, Policy and Rule
        api_response = api_instance.get_violations_assets(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling ComplianceApi->get_violations_assets: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
successTrackId | SuccessTrackIdSchema | | 
policyCategory | PolicyCategorySchema | | 
policyGroupId | PolicyGroupIdSchema | | 
policyId | PolicyIdSchema | | 
ruleId | RuleIdSchema | | 
severity | SeveritySchema | | 
offset | OffsetSchema | | optional
max | MaxSchema | | optional


# SuccessTrackIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PolicyCategorySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PolicyGroupIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PolicyIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# RuleIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SeveritySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# OffsetSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 1value must be a 32 bit integer

# MaxSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 10value must be a 32 bit integer

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
customerId | CustomerIdSchema | | 

# CustomerIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_violations_assets.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_violations_assets.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#get_violations_assets.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#get_violations_assets.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_violations_assets.ApiResponseFor404) | Not found
500 | [ApiResponseFor500](#get_violations_assets.ApiResponseFor500) | Internal server error
503 | [ApiResponseFor503](#get_violations_assets.ApiResponseFor503) | Service Unavailable
504 | [ApiResponseFor504](#get_violations_assets.ApiResponseFor504) | Gateway timeout

#### get_violations_assets.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AssetsViolationsResponse**](../../models/AssetsViolationsResponse.md) |  | 


#### get_violations_assets.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_violations_assets.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_violations_assets.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_violations_assets.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_violations_assets.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_violations_assets.ApiResponseFor503
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor503ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor503ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_violations_assets.ApiResponseFor504
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor504ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor504ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


### Authorization

[oAuth2](../../../README.md#oAuth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

