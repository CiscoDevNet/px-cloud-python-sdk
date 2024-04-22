# Partner Experience Cloud API - Python SDK

A Python package enabling simple access to the PX Cloud REST API.


## About PX Cloud

Partner Experience (PX) Cloud for Success Tracks is the Cisco partner's digital experience where they can connect with Cisco and their customers. It aims to transform customer-partner relationships by providing business and technology insights, such as customer lifecycle journeys, access to customer CX Cloud dashboards, partner offers, and more.

More info: [PX Cloud](https://www.cisco.com/c/m/en_us/successhub/px-cloud.html)

## About the PX Cloud REST API

The PX Cloud REST API enables partner applications to integrate PX Cloud portal data and functionality via an easy-to-use REST interface. With this API, partners can access customer life-cycle data and develop innovative, customized services, adding unique value to their customers' business networks.

Available customer data include: organization details, contract information, Success Track analytics, and hardware asset reports.

More info: [PX Cloud API](https://developer.cisco.com/docs/px-cloud)

## Requirements.

Python &gt;&#x3D;3.7

## Migration from other generators like python and python-legacy

### Changes
1. This generator uses spec case for all (object) property names and parameter names.
    - So if the spec has a property name like camelCase, it will use camelCase rather than camel_case
    - So you will need to update how you input and read properties to use spec case
2. Endpoint parameters are stored in dictionaries to prevent collisions (explanation below)
    - So you will need to update how you pass data in to endpoints
3. Endpoint responses now include the original response, the deserialized response body, and (todo)the deserialized headers
    - So you will need to update your code to use response.body to access deserialized data
4. All validated data is instantiated in an instance that subclasses all validated Schema classes and Decimal/str/list/tuple/frozendict/NoneClass/BoolClass/bytes/io.FileIO
    - This means that you can use isinstance to check if a payload validated against a schema class
    - This means that no data will be of type None/True/False
        - ingested None will subclass NoneClass
        - ingested True will subclass BoolClass
        - ingested False will subclass BoolClass
        - So if you need to check is True/False/None, instead use instance.is_true_oapg()/.is_false_oapg()/.is_none_oapg()
5. All validated class instances are immutable except for ones based on io.File
    - This is because if properties were changed after validation, that validation would no longer apply
    - So no changing values or property values after a class has been instantiated
6. String + Number types with formats
    - String type data is stored as a string and if you need to access types based on its format like date,
    date-time, uuid, number etc then you will need to use accessor functions on the instance
    - type string + format: See .as_date_oapg, .as_datetime_oapg, .as_decimal_oapg, .as_uuid_oapg
    - type number + format: See .as_float_oapg, .as_int_oapg
    - this was done because openapi/json-schema defines constraints. string data may be type string with no format
    keyword in one schema, and include a format constraint in another schema
    - So if you need to access a string format based type, use as_date_oapg/as_datetime_oapg/as_decimal_oapg/as_uuid_oapg
    - So if you need to access a number format based type, use as_int_oapg/as_float_oapg
7. Property access on AnyType(type unset) or object(dict) schemas
    - Only required keys with valid python names are properties like .someProp and have type hints
    - All optional keys may not exist, so properties are not defined for them
    - One can access optional values with dict_instance['optionalProp'] and KeyError will be raised if it does not exist
    - Use get_item_oapg if you need a way to always get a value whether or not the key exists
        - If the key does not exist, schemas.unset is returned from calling dict_instance.get_item_oapg('optionalProp')
        - All required and optional keys have type hints for this method, and @typing.overload is used
        - A type hint is also generated for additionalProperties accessed using this method
    - So you will need to update you code to use some_instance['optionalProp'] to access optional property
    and additionalProperty values
8. The location of the api classes has changed
    - Api classes are located in your_package.apis.tags.some_api
    - This change was made to eliminate redundant code generation
    - Legacy generators generated the same endpoint twice if it had > 1 tag on it
    - This generator defines an endpoint in one class, then inherits that class to generate
      apis by tags and by paths
    - This change reduces code and allows quicker run time if you use the path apis
        - path apis are at your_package.apis.paths.some_path
    - Those apis will only load their needed models, which is less to load than all of the resources needed in a tag api
    - So you will need to update your import paths to the api classes

### Why are Oapg and _oapg used in class and method names?
Classes can have arbitrarily named properties set on them
Endpoints can have arbitrary operationId method names set
For those reasons, I use the prefix Oapg and _oapg to greatly reduce the likelihood of collisions
on protected + public classes/methods.
oapg stands for OpenApi Python Generator.

### Object property spec case
This was done because when payloads are ingested, they can be validated against N number of schemas.
If the input signature used a different property name then that has mutated the payload.
So SchemaA and SchemaB must both see the camelCase spec named variable.
Also it is possible to send in two properties, named camelCase and camel_case in the same payload.
That use case should be support so spec case is used.

### Parameter spec case
Parameters can be included in different locations including:
- query
- path
- header
- cookie

Any of those parameters could use the same parameter names, so if every parameter
was included as an endpoint parameter in a function signature, they would collide.
For that reason, each of those inputs have been separated out into separate typed dictionaries:
- query_params
- path_params
- header_params
- cookie_params

So when updating your code, you will need to pass endpoint parameters in using those
dictionaries.

### Endpoint responses
Endpoint responses have been enriched to now include more information.
Any response reom an endpoint will now include the following properties:
response: urllib3.HTTPResponse
body: typing.Union[Unset, Schema]
headers: typing.Union[Unset, TODO]
Note: response header deserialization has not yet been added


## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/CiscoDevNet/px-cloud-python-sdk.git
```

(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/CiscoDevNet/px-cloud-python-sdk.git`)

Then import the package you need:
```python
import pxcloud_api_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import pxcloud_api_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import pxcloud_api_client
from pprint import pprint
from pxcloud_api_client.apis.tags import cx_meta_data_api
from pxcloud_api_client.pxcloud_api_client.error_response import ErrorResponse
from pxcloud_api_client.pxcloud_api_client.success_tracks_response import SuccessTracksResponse
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
    api_instance = cx_meta_data_api.CXMetaDataApi(api_client)
    
    try:
        # List success tracks
        api_response = api_instance.get_success_tracks()
        pprint(api_response)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling CXMetaDataApi->get_success_tracks: %s\n" % e)
```

## Auto Authentication

The [auth.py](./examples/auth.py) generates the authorization tokens to access the PXCloud.

For more info see [example.py](./examples/example.py) which shows the usage of the [auth.py](./examples/auth.py).

## Documentation for API Endpoints

All URIs are relative to *https://api-cx.cisco.com/px/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ComplianceApi* | [**asset_violations**](docs/ComplianceApi.md#asset_violations) | **GET** /v1/customers/{customerId}/insights/compliance/assetViolations | Get the violations of the asset
*ComplianceApi* | [**assets_with_violations**](docs/ComplianceApi.md#assets_with_violations) | **GET** /v1/customers/{customerId}/insights/compliance/assetsWithViolations | Get the asset summary
*ComplianceApi* | [**opt_in**](docs/ComplianceApi.md#opt_in) | **GET** /v1/customers/{customerId}/insights/compliance/optIn | optIn status
*ComplianceApi* | [**policy_rule_details**](docs/ComplianceApi.md#policy_rule_details) | **GET** /v1/customers/{customerId}/insights/compliance/policyRuleDetails | Returns information about the policy the rule belongs to
*ComplianceApi* | [**suggestions**](docs/ComplianceApi.md#suggestions) | **GET** /v1/customers/{customerId}/insights/compliance/suggestions | Get the Suggestions filtered upon Severity (if given), for summary tab
*ComplianceApi* | [**violations**](docs/ComplianceApi.md#violations) | **GET** /v1/customers/{customerId}/insights/compliance/violations | Get the violation summary of a customer
*ComplianceApi* | [**violations_assets**](docs/ComplianceApi.md#violations_assets) | **GET** /v1/customers/{customerId}/insights/compliance/violations/assets | Get the violation details of impacted assets for the customer, and selected policy Group, Policy and Rule
*ContractsApi* | [**contract_details**](docs/ContractsApi.md#contract_details) | **GET** /v1/contract/details | Get the list of contracts Details from flat table. It supports pagination , filtering and sorting
*ContractsApi* | [**contracts**](docs/ContractsApi.md#contracts) | **GET** /v1/contracts | Get the list of customer contracts for a particular partner. It supports pagination with offset and limit parameters , filtering and sorting
*CrashRiskApi* | [**asset_risk_factors**](docs/CrashRiskApi.md#asset_risk_factors) | **GET** /v1/customers/{customerId}/insights/crashRisk/assets/{assetIdBase64}/riskFactors | Get risk factors of a device
*CrashRiskApi* | [**assets**](docs/CrashRiskApi.md#assets) | **GET** /v1/customers/{customerId}/insights/crashRisk/assets | Get devices which are at risk of crash owned by a customer, sorted by risk score in descending order by default
*CrashRiskApi* | [**assets_crashed**](docs/CrashRiskApi.md#assets_crashed) | **GET** /v1/customers/{customerId}/insights/crashRisk/assetsCrashed | Get the list of crashed devices for last given time period
*CrashRiskApi* | [**crash_history**](docs/CrashRiskApi.md#crash_history) | **GET** /v1/customers/{customerId}/insights/crashRisk/asset/{assetIdBase64}/crashHistory | Get the device crash-detail - Asset 360(time stamp, reset reason)
*CrashRiskApi* | [**similar_assets**](docs/CrashRiskApi.md#similar_assets) | **GET** /v1/customers/{customerId}/insights/crashRisk/assets/{assetIdBase64}/similarAssets | Get similar assets based on the similarity score
*CustomerDataApi* | [**lifecycle**](docs/CustomerDataApi.md#lifecycle) | **GET** /v1/customers/{customerId}/lifecycle | Get customer lifecycle
*CustomerDataApi* | [**report_summary**](docs/CustomerDataApi.md#report_summary) | **GET** /v1/customers/{customerId}/reports/{reportId} | Get the report
*CustomerDataApi* | [**reports**](docs/CustomerDataApi.md#reports) | **POST** /v1/customers/{customerId}/reports | Request customer data reports as bulk files
*CustomersApi* | [**customers**](docs/CustomersApi.md#customers) | **GET** /v1/customers | Fetch list of customers paginated for a given partner Id
*FaultsApi* | [**fault_affected_assets**](docs/FaultsApi.md#fault_affected_assets) | **GET** /v1/customers/{customerId}/insights/faults/{faultId}/affectedAssets | Affected Assets
*FaultsApi* | [**fault_history**](docs/FaultsApi.md#fault_history) | **GET** /v1/customers/{customerId}/insights/faults/{faultId}/affectedAssets/{assetName}/faultHistory | Assets Fault History
*FaultsApi* | [**fault_summary**](docs/FaultsApi.md#fault_summary) | **GET** /v1/customers/{customerId}/insights/faults/{faultId}/summary | Fault summary
*FaultsApi* | [**faults**](docs/FaultsApi.md#faults) | **GET** /v1/customers/{customerId}/insights/faults | Faults details
*InsightsApi* | [**software_group_assets**](docs/InsightsApi.md#software_group_assets) | **GET** /v1/customers/{customerId}/insights/software/softwareGroups/assets | Asset information in the Software Group
*InsightsApi* | [**software_group_field_notices**](docs/InsightsApi.md#software_group_field_notices) | **GET** /v1/customers/{customerId}/insights/software/softwareGroups/suggestions/fieldNotices | Software Group - Suggestions Field Notices
*InsightsApi* | [**software_group_security_advisories**](docs/InsightsApi.md#software_group_security_advisories) | **GET** /v1/customers/{customerId}/insights/software/softwareGroups/suggestions/securityAdvisories | Software Group - Suggestions Security Advisories
*InsightsApi* | [**software_group_suggestions**](docs/InsightsApi.md#software_group_suggestions) | **GET** /v1/customers/{customerId}/insights/software/softwareGroups/suggestions | Software Group Suggestions
*InsightsApi* | [**software_group_suggestions_bugs**](docs/InsightsApi.md#software_group_suggestions_bugs) | **GET** /v1/customers/{customerId}/insights/software/softwareGroups/suggestions/bugs | Software Group - Suggestions Bugs
*InsightsApi* | [**software_groups**](docs/InsightsApi.md#software_groups) | **GET** /v1/customers/{customerId}/insights/software/softwareGroups | Software Group Information
*PartnerDataApi* | [**success_tracks**](docs/PartnerDataApi.md#success_tracks) | **GET** /v1/successTracks | Success Tracks
*PartnerOffersDataApi* | [**partner_offers**](docs/PartnerOffersDataApi.md#partner_offers) | **GET** /v1/partnerOffers | Get Partner Offers
*PartnerOffersSessionsDataApi* | [**partner_offers_sessions**](docs/PartnerOffersSessionsDataApi.md#partner_offers_sessions) | **GET** /v1/partnerOffersSessions | Get Partner Offers Session data
*V1ContractsWithCustomersApi* | [**contracts_with_customers**](docs/V1ContractsWithCustomersApi.md#contracts_with_customers) | **GET** /v1/contractsWithCustomers | Get the Outbound Contracts With Customers


## Documentation For Models

 - [AccSessionAttendees](docs/models/AccSessionAttendees.md)
 - [AffectedAssets](docs/models/AffectedAssets.md)
 - [AffectedAssetsResponse](docs/models/AffectedAssetsResponse.md)
 - [Asset](docs/models/Asset.md)
 - [AssetError](docs/models/AssetError.md)
 - [AssetResponse](docs/models/AssetResponse.md)
 - [AssetSession](docs/models/AssetSession.md)
 - [AssetViolation](docs/models/AssetViolation.md)
 - [AssetViolationsResponse](docs/models/AssetViolationsResponse.md)
 - [AssetsFaultHistory](docs/models/AssetsFaultHistory.md)
 - [AssetsFaultHistoryResponse](docs/models/AssetsFaultHistoryResponse.md)
 - [AssetsViolations](docs/models/AssetsViolations.md)
 - [AssetsViolationsResponse](docs/models/AssetsViolationsResponse.md)
 - [AssetsWithViolations](docs/models/AssetsWithViolations.md)
 - [AssetsWithViolationsResponse](docs/models/AssetsWithViolationsResponse.md)
 - [Contract](docs/models/Contract.md)
 - [ContractDetails](docs/models/ContractDetails.md)
 - [ContractDetailsResponse](docs/models/ContractDetailsResponse.md)
 - [ContractDetailsV2Response](docs/models/ContractDetailsV2Response.md)
 - [ContractResponse](docs/models/ContractResponse.md)
 - [ContractV2](docs/models/ContractV2.md)
 - [ContractV2Details](docs/models/ContractV2Details.md)
 - [ContractsV2Response](docs/models/ContractsV2Response.md)
 - [Crash](docs/models/Crash.md)
 - [CrashRiskDevice](docs/models/CrashRiskDevice.md)
 - [CrashRiskDevices](docs/models/CrashRiskDevices.md)
 - [Customer](docs/models/Customer.md)
 - [CustomerDetails](docs/models/CustomerDetails.md)
 - [CustomerInfo](docs/models/CustomerInfo.md)
 - [CustomerResponse](docs/models/CustomerResponse.md)
 - [DeviceCrashDetail](docs/models/DeviceCrashDetail.md)
 - [DeviceDetail](docs/models/DeviceDetail.md)
 - [DeviceRiskFactors](docs/models/DeviceRiskFactors.md)
 - [DeviceRiskFactorsResponse](docs/models/DeviceRiskFactorsResponse.md)
 - [ErrorResponse](docs/models/ErrorResponse.md)
 - [Faults](docs/models/Faults.md)
 - [FaultsResponse](docs/models/FaultsResponse.md)
 - [FaultsSummary](docs/models/FaultsSummary.md)
 - [FaultsSummaryResponse](docs/models/FaultsSummaryResponse.md)
 - [InventoryCrashDetails](docs/models/InventoryCrashDetails.md)
 - [OptInResponse](docs/models/OptInResponse.md)
 - [Pagination](docs/models/Pagination.md)
 - [PartnerAsset](docs/models/PartnerAsset.md)
 - [PartnerAssetResponse](docs/models/PartnerAssetResponse.md)
 - [PartnerOffer](docs/models/PartnerOffer.md)
 - [PartnerOfferAttendee](docs/models/PartnerOfferAttendee.md)
 - [PartnerOfferSession](docs/models/PartnerOfferSession.md)
 - [PartnerOfferWithSessions](docs/models/PartnerOfferWithSessions.md)
 - [PartnerOffersInfo](docs/models/PartnerOffersInfo.md)
 - [PolicyRuleDetails](docs/models/PolicyRuleDetails.md)
 - [RacetrackBuid](docs/models/RacetrackBuid.md)
 - [RacetrackBuidPitstop](docs/models/RacetrackBuidPitstop.md)
 - [RacetrackBuidPitstopAction](docs/models/RacetrackBuidPitstopAction.md)
 - [RacetrackBuidSolution](docs/models/RacetrackBuidSolution.md)
 - [RacetrackTooltip](docs/models/RacetrackTooltip.md)
 - [RacetrackUsecase](docs/models/RacetrackUsecase.md)
 - [ReleaseSummary](docs/models/ReleaseSummary.md)
 - [Report](docs/models/Report.md)
 - [ReportStatus](docs/models/ReportStatus.md)
 - [SimilarDeviceData](docs/models/SimilarDeviceData.md)
 - [SimilarDevices](docs/models/SimilarDevices.md)
 - [SoftwareGroup](docs/models/SoftwareGroup.md)
 - [SoftwareGroupBugs](docs/models/SoftwareGroupBugs.md)
 - [SoftwareGroupBugsResponse](docs/models/SoftwareGroupBugsResponse.md)
 - [SoftwareGroupFieldNotices](docs/models/SoftwareGroupFieldNotices.md)
 - [SoftwareGroupFieldNoticesResponse](docs/models/SoftwareGroupFieldNoticesResponse.md)
 - [SoftwareGroupResponse](docs/models/SoftwareGroupResponse.md)
 - [SoftwareGroupRisk](docs/models/SoftwareGroupRisk.md)
 - [SoftwareGroupSecurityAdvisories](docs/models/SoftwareGroupSecurityAdvisories.md)
 - [SoftwareGroupSecurityAdvisoriesResponse](docs/models/SoftwareGroupSecurityAdvisoriesResponse.md)
 - [SoftwareGroupSuggestions](docs/models/SoftwareGroupSuggestions.md)
 - [SolutionMapping](docs/models/SolutionMapping.md)
 - [SuccessTrack](docs/models/SuccessTrack.md)
 - [SuccessTrackChecklistMapping](docs/models/SuccessTrackChecklistMapping.md)
 - [SuccessTrackMapping](docs/models/SuccessTrackMapping.md)
 - [SuccessTracks](docs/models/SuccessTracks.md)
 - [SuccessTracksResponse](docs/models/SuccessTracksResponse.md)
 - [Suggestion](docs/models/Suggestion.md)
 - [SuggestionSummary](docs/models/SuggestionSummary.md)
 - [SuggestionsResponse](docs/models/SuggestionsResponse.md)
 - [ViolationSummary](docs/models/ViolationSummary.md)
 - [ViolationSummaryResponse](docs/models/ViolationSummaryResponse.md)

## Documentation For Authorization

### oAuth2

- **Type**: OAuth
- **Flow**: application
- **Authorization URL**: 
- **Scopes**: 
 - **api.authz.iam.manage**: Production
 - **api.customer.assets.manage**: Sandbox


## FAQs and Troubleshooting

For FAQs and Troubleshooting please make use of the official forum [cisco communities](https://community.cisco.com/t5/px-cloud/ct-p/px-cloud)

## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in pxcloud_api_client.apis and pxcloud_api_client.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from pxcloud_api_client.apis.default_api import DefaultApi`
- `from pxcloud_api_client.pxcloud_api_client.pet import Pet`

Solution 1:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import pxcloud_api_client
from pxcloud_api_client.apis import *
from pxcloud_api_client.models import *
```
