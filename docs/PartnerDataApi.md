# pxcloud_api_client.PartnerDataApi

All URIs are relative to *https://api-cx.cisco.com/sandbox/px*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_contract_details**](PartnerDataApi.md#get_contract_details) | **GET** /v1/contract/details | Get customer contract details
[**get_contracts**](PartnerDataApi.md#get_contracts) | **GET** /v1/contracts | List customer contracts
[**get_contracts_with_customers**](PartnerDataApi.md#get_contracts_with_customers) | **GET** /v1/contractsWithCustomers | List contracts with customer details
[**get_partner_offers**](PartnerDataApi.md#get_partner_offers) | **GET** /v1/partnerOffers | List partner offers
[**get_partner_offers_sessions**](PartnerDataApi.md#get_partner_offers_sessions) | **GET** /v1/partnerOffersSessions | Get partner offers session details


# **get_contract_details**
> ContractDetailsResponse get_contract_details(contract_number, success_track_id)

Get customer contract details

### Example

* OAuth Authentication (oAuth2):

```python
import time
import pxcloud_api_client
from pxcloud_api_client.api import partner_data_api
from pxcloud_api_client.model.error_response import ErrorResponse
from pxcloud_api_client.model.contract_details_response import ContractDetailsResponse
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
    api_instance = partner_data_api.PartnerDataApi(api_client)
    contract_number = 1 # int | 
    success_track_id = "successTrackId_example" # str | 
    max = 10 # int | The maximum number of items to return. The default value is 10. (optional) if omitted the server will use the default value of 10
    offset = 1 # int | The number of items to skip before starting to collect the result set. The default value is 1. (optional) if omitted the server will use the default value of 1
    component_type = "componentType_example" # str | Deprecated, use `contractLineItemType`. (optional)
    contract_line_item_type = "PARENT" # str |  (optional)
    customer_id = "customerId_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get customer contract details
        api_response = api_instance.get_contract_details(contract_number, success_track_id)
        pprint(api_response)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling PartnerDataApi->get_contract_details: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get customer contract details
        api_response = api_instance.get_contract_details(contract_number, success_track_id, max=max, offset=offset, component_type=component_type, contract_line_item_type=contract_line_item_type, customer_id=customer_id)
        pprint(api_response)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling PartnerDataApi->get_contract_details: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_number** | **int**|  |
 **success_track_id** | **str**|  |
 **max** | **int**| The maximum number of items to return. The default value is 10. | [optional] if omitted the server will use the default value of 10
 **offset** | **int**| The number of items to skip before starting to collect the result set. The default value is 1. | [optional] if omitted the server will use the default value of 1
 **component_type** | **str**| Deprecated, use &#x60;contractLineItemType&#x60;. | [optional]
 **contract_line_item_type** | **str**|  | [optional]
 **customer_id** | **str**|  | [optional]

### Return type

[**ContractDetailsResponse**](ContractDetailsResponse.md)

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

# **get_contracts**
> ContractResponse get_contracts()

List customer contracts

### Example

* OAuth Authentication (oAuth2):

```python
import time
import pxcloud_api_client
from pxcloud_api_client.api import partner_data_api
from pxcloud_api_client.model.error_response import ErrorResponse
from pxcloud_api_client.model.contract_response import ContractResponse
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
    api_instance = partner_data_api.PartnerDataApi(api_client)
    max = 10 # int | The maximum number of items to return. The default value is 10. (optional) if omitted the server will use the default value of 10
    offset = 1 # int | The number of items to skip before starting to collect the result set. The default value is 1. (optional) if omitted the server will use the default value of 1

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List customer contracts
        api_response = api_instance.get_contracts(max=max, offset=offset)
        pprint(api_response)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling PartnerDataApi->get_contracts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **max** | **int**| The maximum number of items to return. The default value is 10. | [optional] if omitted the server will use the default value of 10
 **offset** | **int**| The number of items to skip before starting to collect the result set. The default value is 1. | [optional] if omitted the server will use the default value of 1

### Return type

[**ContractResponse**](ContractResponse.md)

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

# **get_contracts_with_customers**
> ContractsV2Response get_contracts_with_customers(success_track_id)

List contracts with customer details

### Example

* OAuth Authentication (oAuth2):

```python
import time
import pxcloud_api_client
from pxcloud_api_client.api import partner_data_api
from pxcloud_api_client.model.error_response import ErrorResponse
from pxcloud_api_client.model.contracts_v2_response import ContractsV2Response
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
    api_instance = partner_data_api.PartnerDataApi(api_client)
    success_track_id = "successTrackId_example" # str | 
    max = 10 # int | The maximum number of items to return. The default value is 10. (optional) if omitted the server will use the default value of 10
    offset = 1 # int | The number of items to skip before starting to collect the result set. The default value is 1. (optional) if omitted the server will use the default value of 1
    customer_gu_name = "customerGUName_example" # str | customerGUName (optional)
    customer_id = "customerId_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # List contracts with customer details
        api_response = api_instance.get_contracts_with_customers(success_track_id)
        pprint(api_response)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling PartnerDataApi->get_contracts_with_customers: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List contracts with customer details
        api_response = api_instance.get_contracts_with_customers(success_track_id, max=max, offset=offset, customer_gu_name=customer_gu_name, customer_id=customer_id)
        pprint(api_response)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling PartnerDataApi->get_contracts_with_customers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **success_track_id** | **str**|  |
 **max** | **int**| The maximum number of items to return. The default value is 10. | [optional] if omitted the server will use the default value of 10
 **offset** | **int**| The number of items to skip before starting to collect the result set. The default value is 1. | [optional] if omitted the server will use the default value of 1
 **customer_gu_name** | **str**| customerGUName | [optional]
 **customer_id** | **str**|  | [optional]

### Return type

[**ContractsV2Response**](ContractsV2Response.md)

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

# **get_partner_offers**
> PartnerAssetResponse get_partner_offers(success_track_id)

List partner offers

### Example

* OAuth Authentication (oAuth2):

```python
import time
import pxcloud_api_client
from pxcloud_api_client.api import partner_data_api
from pxcloud_api_client.model.error_response import ErrorResponse
from pxcloud_api_client.model.partner_asset_response import PartnerAssetResponse
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
    api_instance = partner_data_api.PartnerDataApi(api_client)
    success_track_id = "successTrackId_example" # str | 
    max = 10 # int | The maximum number of items to return. The default value is 10. (optional) if omitted the server will use the default value of 10
    offset = 1 # int | The number of items to skip before starting to collect the result set. The default value is 1. (optional) if omitted the server will use the default value of 1
    customer_id = "customerId_example" # str |  (optional)
    offer_status = "Idle" # str |  (optional)
    offer_type = "Accelerator" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # List partner offers
        api_response = api_instance.get_partner_offers(success_track_id)
        pprint(api_response)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling PartnerDataApi->get_partner_offers: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List partner offers
        api_response = api_instance.get_partner_offers(success_track_id, max=max, offset=offset, customer_id=customer_id, offer_status=offer_status, offer_type=offer_type)
        pprint(api_response)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling PartnerDataApi->get_partner_offers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **success_track_id** | **str**|  |
 **max** | **int**| The maximum number of items to return. The default value is 10. | [optional] if omitted the server will use the default value of 10
 **offset** | **int**| The number of items to skip before starting to collect the result set. The default value is 1. | [optional] if omitted the server will use the default value of 1
 **customer_id** | **str**|  | [optional]
 **offer_status** | **str**|  | [optional]
 **offer_type** | **str**|  | [optional]

### Return type

[**PartnerAssetResponse**](PartnerAssetResponse.md)

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

# **get_partner_offers_sessions**
> PartnerOfferWithSessions get_partner_offers_sessions(success_track_id)

Get partner offers session details

### Example

* OAuth Authentication (oAuth2):

```python
import time
import pxcloud_api_client
from pxcloud_api_client.api import partner_data_api
from pxcloud_api_client.model.error_response import ErrorResponse
from pxcloud_api_client.model.partner_offer_with_sessions import PartnerOfferWithSessions
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
    api_instance = partner_data_api.PartnerDataApi(api_client)
    success_track_id = "successTrackId_example" # str | 
    max = 10 # int | The maximum number of items to return. The default value is 10. (optional) if omitted the server will use the default value of 10
    offset = 1 # int | The number of items to skip before starting to collect the result set. The default value is 1. (optional) if omitted the server will use the default value of 1
    customer_id = "customerId_example" # str |  (optional)
    offer_id = "offerId_example" # str |  (optional)
    offer_status = "Idle" # str |  (optional)
    offer_type = "Accelerator" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get partner offers session details
        api_response = api_instance.get_partner_offers_sessions(success_track_id)
        pprint(api_response)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling PartnerDataApi->get_partner_offers_sessions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get partner offers session details
        api_response = api_instance.get_partner_offers_sessions(success_track_id, max=max, offset=offset, customer_id=customer_id, offer_id=offer_id, offer_status=offer_status, offer_type=offer_type)
        pprint(api_response)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling PartnerDataApi->get_partner_offers_sessions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **success_track_id** | **str**|  |
 **max** | **int**| The maximum number of items to return. The default value is 10. | [optional] if omitted the server will use the default value of 10
 **offset** | **int**| The number of items to skip before starting to collect the result set. The default value is 1. | [optional] if omitted the server will use the default value of 1
 **customer_id** | **str**|  | [optional]
 **offer_id** | **str**|  | [optional]
 **offer_status** | **str**|  | [optional]
 **offer_type** | **str**|  | [optional]

### Return type

[**PartnerOfferWithSessions**](PartnerOfferWithSessions.md)

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

