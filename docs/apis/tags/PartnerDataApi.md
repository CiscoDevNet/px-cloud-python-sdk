<a id="__pageTop"></a>
# pxcloud_api_client.apis.tags.partner_data_api.PartnerDataApi

All URIs are relative to *https://api-cx.cisco.com/sandbox/px*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_contract_details**](#get_contract_details) | **get** /v1/contract/details | Get customer contract details
[**get_contracts**](#get_contracts) | **get** /v1/contracts | List customer contracts
[**get_contracts_with_customers**](#get_contracts_with_customers) | **get** /v1/contractsWithCustomers | List contracts with customer details
[**get_partner_offers**](#get_partner_offers) | **get** /v1/partnerOffers | List partner offers
[**get_partner_offers_sessions**](#get_partner_offers_sessions) | **get** /v1/partnerOffersSessions | Get partner offers session details

# **get_contract_details**
<a id="get_contract_details"></a>
> ContractDetailsResponse get_contract_details(contract_numbersuccess_track_id)

Get customer contract details

### Example

* OAuth Authentication (oAuth2):
```python
import pxcloud_api_client
from pxcloud_api_client.apis.tags import partner_data_api
from pxcloud_api_client.pxcloud_api_client.contract_details_response import ContractDetailsResponse
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
    api_instance = partner_data_api.PartnerDataApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'contractNumber': 1,
        'successTrackId': "successTrackId_example",
    }
    try:
        # Get customer contract details
        api_response = api_instance.get_contract_details(
            query_params=query_params,
        )
        pprint(api_response)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling PartnerDataApi->get_contract_details: %s\n" % e)

    # example passing only optional values
    query_params = {
        'contractNumber': 1,
        'max': 10,
        'offset': 1,
        'componentType': "componentType_example",
        'contractLineItemType': "PARENT",
        'customerId': "customerId_example",
        'successTrackId': "successTrackId_example",
    }
    try:
        # Get customer contract details
        api_response = api_instance.get_contract_details(
            query_params=query_params,
        )
        pprint(api_response)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling PartnerDataApi->get_contract_details: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
contractNumber | ContractNumberSchema | | 
max | MaxSchema | | optional
offset | OffsetSchema | | optional
componentType | ComponentTypeSchema | | optional
contractLineItemType | ContractLineItemTypeSchema | | optional
customerId | CustomerIdSchema | | optional
successTrackId | SuccessTrackIdSchema | | 


# ContractNumberSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

# MaxSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 10value must be a 32 bit integer

# OffsetSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 1value must be a 32 bit integer

# ComponentTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ContractLineItemTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["PARENT", "CHILD", "STANDALONE", ] 

# CustomerIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SuccessTrackIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_contract_details.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_contract_details.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#get_contract_details.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#get_contract_details.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_contract_details.ApiResponseFor404) | Not found
500 | [ApiResponseFor500](#get_contract_details.ApiResponseFor500) | Internal server error
503 | [ApiResponseFor503](#get_contract_details.ApiResponseFor503) | Service Unavailable
504 | [ApiResponseFor504](#get_contract_details.ApiResponseFor504) | Gateway timeout

#### get_contract_details.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ContractDetailsResponse**](../../models/ContractDetailsResponse.md) |  | 

#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Link | LinkSchema | | optional

# LinkSchema

URLs for previous (`rel=\"prev\"`) and/or next (`rel=\"next\"`) page of items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | URLs for previous (&#x60;rel&#x3D;\&quot;prev\&quot;&#x60;) and/or next (&#x60;rel&#x3D;\&quot;next\&quot;&#x60;) page of items | 


#### get_contract_details.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_contract_details.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_contract_details.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_contract_details.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_contract_details.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_contract_details.ApiResponseFor503
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor503ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor503ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_contract_details.ApiResponseFor504
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

# **get_contracts**
<a id="get_contracts"></a>
> ContractResponse get_contracts()

List customer contracts

### Example

* OAuth Authentication (oAuth2):
```python
import pxcloud_api_client
from pxcloud_api_client.apis.tags import partner_data_api
from pxcloud_api_client.pxcloud_api_client.contract_response import ContractResponse
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
    api_instance = partner_data_api.PartnerDataApi(api_client)

    # example passing only optional values
    query_params = {
        'max': 10,
        'offset': 1,
    }
    try:
        # List customer contracts
        api_response = api_instance.get_contracts(
            query_params=query_params,
        )
        pprint(api_response)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling PartnerDataApi->get_contracts: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
max | MaxSchema | | optional
offset | OffsetSchema | | optional


# MaxSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 10value must be a 32 bit integer

# OffsetSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 1value must be a 32 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_contracts.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_contracts.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#get_contracts.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#get_contracts.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_contracts.ApiResponseFor404) | Not found
500 | [ApiResponseFor500](#get_contracts.ApiResponseFor500) | Internal server error
503 | [ApiResponseFor503](#get_contracts.ApiResponseFor503) | Service Unavailable
504 | [ApiResponseFor504](#get_contracts.ApiResponseFor504) | Gateway timeout

#### get_contracts.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ContractResponse**](../../models/ContractResponse.md) |  | 

#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Link | LinkSchema | | optional

# LinkSchema

URLs for previous (`rel=\"prev\"`) and/or next (`rel=\"next\"`) page of items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | URLs for previous (&#x60;rel&#x3D;\&quot;prev\&quot;&#x60;) and/or next (&#x60;rel&#x3D;\&quot;next\&quot;&#x60;) page of items | 


#### get_contracts.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_contracts.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_contracts.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_contracts.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_contracts.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_contracts.ApiResponseFor503
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor503ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor503ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_contracts.ApiResponseFor504
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

# **get_contracts_with_customers**
<a id="get_contracts_with_customers"></a>
> ContractsV2Response get_contracts_with_customers(success_track_id)

List contracts with customer details

### Example

* OAuth Authentication (oAuth2):
```python
import pxcloud_api_client
from pxcloud_api_client.apis.tags import partner_data_api
from pxcloud_api_client.pxcloud_api_client.contracts_v2_response import ContractsV2Response
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
    api_instance = partner_data_api.PartnerDataApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'successTrackId': "successTrackId_example",
    }
    try:
        # List contracts with customer details
        api_response = api_instance.get_contracts_with_customers(
            query_params=query_params,
        )
        pprint(api_response)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling PartnerDataApi->get_contracts_with_customers: %s\n" % e)

    # example passing only optional values
    query_params = {
        'max': 10,
        'offset': 1,
        'customerGUName': "customerGUName_example",
        'customerId': "customerId_example",
        'successTrackId': "successTrackId_example",
    }
    try:
        # List contracts with customer details
        api_response = api_instance.get_contracts_with_customers(
            query_params=query_params,
        )
        pprint(api_response)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling PartnerDataApi->get_contracts_with_customers: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
max | MaxSchema | | optional
offset | OffsetSchema | | optional
customerGUName | CustomerGUNameSchema | | optional
customerId | CustomerIdSchema | | optional
successTrackId | SuccessTrackIdSchema | | 


# MaxSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 10value must be a 32 bit integer

# OffsetSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 1value must be a 32 bit integer

# CustomerGUNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# CustomerIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SuccessTrackIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_contracts_with_customers.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_contracts_with_customers.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#get_contracts_with_customers.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#get_contracts_with_customers.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_contracts_with_customers.ApiResponseFor404) | Not found
500 | [ApiResponseFor500](#get_contracts_with_customers.ApiResponseFor500) | Internal server error
503 | [ApiResponseFor503](#get_contracts_with_customers.ApiResponseFor503) | Service Unavailable
504 | [ApiResponseFor504](#get_contracts_with_customers.ApiResponseFor504) | Gateway timeout

#### get_contracts_with_customers.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ContractsV2Response**](../../models/ContractsV2Response.md) |  | 

#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Link | LinkSchema | | optional

# LinkSchema

URLs for previous (`rel=\"prev\"`) and/or next (`rel=\"next\"`) page of items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | URLs for previous (&#x60;rel&#x3D;\&quot;prev\&quot;&#x60;) and/or next (&#x60;rel&#x3D;\&quot;next\&quot;&#x60;) page of items | 


#### get_contracts_with_customers.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_contracts_with_customers.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_contracts_with_customers.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_contracts_with_customers.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_contracts_with_customers.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_contracts_with_customers.ApiResponseFor503
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor503ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor503ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_contracts_with_customers.ApiResponseFor504
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

# **get_partner_offers**
<a id="get_partner_offers"></a>
> PartnerAssetResponse get_partner_offers(success_track_id)

List partner offers

### Example

* OAuth Authentication (oAuth2):
```python
import pxcloud_api_client
from pxcloud_api_client.apis.tags import partner_data_api
from pxcloud_api_client.pxcloud_api_client.partner_asset_response import PartnerAssetResponse
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
    api_instance = partner_data_api.PartnerDataApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'successTrackId': "successTrackId_example",
    }
    try:
        # List partner offers
        api_response = api_instance.get_partner_offers(
            query_params=query_params,
        )
        pprint(api_response)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling PartnerDataApi->get_partner_offers: %s\n" % e)

    # example passing only optional values
    query_params = {
        'max': 10,
        'offset': 1,
        'customerId': "customerId_example",
        'offerStatus': "Idle",
        'offerType': "Accelerator",
        'successTrackId': "successTrackId_example",
    }
    try:
        # List partner offers
        api_response = api_instance.get_partner_offers(
            query_params=query_params,
        )
        pprint(api_response)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling PartnerDataApi->get_partner_offers: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
max | MaxSchema | | optional
offset | OffsetSchema | | optional
customerId | CustomerIdSchema | | optional
offerStatus | OfferStatusSchema | | optional
offerType | OfferTypeSchema | | optional
successTrackId | SuccessTrackIdSchema | | 


# MaxSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 10value must be a 32 bit integer

# OffsetSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 1value must be a 32 bit integer

# CustomerIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# OfferStatusSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["Idle", "Published", "Unpublished", ] 

# OfferTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["Accelerator", "Ask the Experts", ] 

# SuccessTrackIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_partner_offers.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_partner_offers.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#get_partner_offers.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#get_partner_offers.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_partner_offers.ApiResponseFor404) | Not found
500 | [ApiResponseFor500](#get_partner_offers.ApiResponseFor500) | Internal server error
503 | [ApiResponseFor503](#get_partner_offers.ApiResponseFor503) | Service Unavailable
504 | [ApiResponseFor504](#get_partner_offers.ApiResponseFor504) | Gateway timeout

#### get_partner_offers.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PartnerAssetResponse**](../../models/PartnerAssetResponse.md) |  | 

#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Link | LinkSchema | | optional

# LinkSchema

URLs for previous (`rel=\"prev\"`) and/or next (`rel=\"next\"`) page of items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | URLs for previous (&#x60;rel&#x3D;\&quot;prev\&quot;&#x60;) and/or next (&#x60;rel&#x3D;\&quot;next\&quot;&#x60;) page of items | 


#### get_partner_offers.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_partner_offers.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_partner_offers.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_partner_offers.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_partner_offers.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_partner_offers.ApiResponseFor503
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor503ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor503ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_partner_offers.ApiResponseFor504
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

# **get_partner_offers_sessions**
<a id="get_partner_offers_sessions"></a>
> PartnerOfferWithSessions get_partner_offers_sessions(success_track_id)

Get partner offers session details

### Example

* OAuth Authentication (oAuth2):
```python
import pxcloud_api_client
from pxcloud_api_client.apis.tags import partner_data_api
from pxcloud_api_client.pxcloud_api_client.partner_offer_with_sessions import PartnerOfferWithSessions
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
    api_instance = partner_data_api.PartnerDataApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'successTrackId': "successTrackId_example",
    }
    try:
        # Get partner offers session details
        api_response = api_instance.get_partner_offers_sessions(
            query_params=query_params,
        )
        pprint(api_response)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling PartnerDataApi->get_partner_offers_sessions: %s\n" % e)

    # example passing only optional values
    query_params = {
        'max': 10,
        'offset': 1,
        'customerId': "customerId_example",
        'offerId': "offerId_example",
        'offerStatus': "Idle",
        'offerType': "Accelerator",
        'successTrackId': "successTrackId_example",
    }
    try:
        # Get partner offers session details
        api_response = api_instance.get_partner_offers_sessions(
            query_params=query_params,
        )
        pprint(api_response)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling PartnerDataApi->get_partner_offers_sessions: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
max | MaxSchema | | optional
offset | OffsetSchema | | optional
customerId | CustomerIdSchema | | optional
offerId | OfferIdSchema | | optional
offerStatus | OfferStatusSchema | | optional
offerType | OfferTypeSchema | | optional
successTrackId | SuccessTrackIdSchema | | 


# MaxSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 10value must be a 32 bit integer

# OffsetSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 1value must be a 32 bit integer

# CustomerIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# OfferIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# OfferStatusSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["Idle", "Published", "Unpublished", ] 

# OfferTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["Accelerator", "Ask the Experts", ] 

# SuccessTrackIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_partner_offers_sessions.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_partner_offers_sessions.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#get_partner_offers_sessions.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#get_partner_offers_sessions.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_partner_offers_sessions.ApiResponseFor404) | Not found
500 | [ApiResponseFor500](#get_partner_offers_sessions.ApiResponseFor500) | Internal server error
503 | [ApiResponseFor503](#get_partner_offers_sessions.ApiResponseFor503) | Service Unavailable
504 | [ApiResponseFor504](#get_partner_offers_sessions.ApiResponseFor504) | Gateway timeout

#### get_partner_offers_sessions.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PartnerOfferWithSessions**](../../models/PartnerOfferWithSessions.md) |  | 


#### get_partner_offers_sessions.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_partner_offers_sessions.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_partner_offers_sessions.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_partner_offers_sessions.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_partner_offers_sessions.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_partner_offers_sessions.ApiResponseFor503
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor503ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor503ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_partner_offers_sessions.ApiResponseFor504
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

