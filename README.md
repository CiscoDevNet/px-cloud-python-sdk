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

Python >=3.6

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
from pxcloud_api_client.api import cx_meta_data_api
from pxcloud_api_client.model.error_response import ErrorResponse
from pxcloud_api_client.model.success_tracks_response import SuccessTracksResponse
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

 - [AccSessionAttendees](docs/AccSessionAttendees.md)
 - [AffectedAssets](docs/AffectedAssets.md)
 - [AffectedAssetsResponse](docs/AffectedAssetsResponse.md)
 - [Asset](docs/Asset.md)
 - [AssetError](docs/AssetError.md)
 - [AssetResponse](docs/AssetResponse.md)
 - [AssetSession](docs/AssetSession.md)
 - [AssetViolation](docs/AssetViolation.md)
 - [AssetViolationsResponse](docs/AssetViolationsResponse.md)
 - [AssetsFaultHistory](docs/AssetsFaultHistory.md)
 - [AssetsFaultHistoryResponse](docs/AssetsFaultHistoryResponse.md)
 - [AssetsViolations](docs/AssetsViolations.md)
 - [AssetsViolationsResponse](docs/AssetsViolationsResponse.md)
 - [AssetsWithViolations](docs/AssetsWithViolations.md)
 - [AssetsWithViolationsResponse](docs/AssetsWithViolationsResponse.md)
 - [Contract](docs/Contract.md)
 - [ContractDetails](docs/ContractDetails.md)
 - [ContractDetailsResponse](docs/ContractDetailsResponse.md)
 - [ContractDetailsV2Response](docs/ContractDetailsV2Response.md)
 - [ContractResponse](docs/ContractResponse.md)
 - [ContractV2](docs/ContractV2.md)
 - [ContractV2Details](docs/ContractV2Details.md)
 - [ContractsV2Response](docs/ContractsV2Response.md)
 - [Crash](docs/Crash.md)
 - [CrashRiskDevice](docs/CrashRiskDevice.md)
 - [CrashRiskDevices](docs/CrashRiskDevices.md)
 - [Customer](docs/Customer.md)
 - [CustomerDetails](docs/CustomerDetails.md)
 - [CustomerInfo](docs/CustomerInfo.md)
 - [CustomerResponse](docs/CustomerResponse.md)
 - [DeviceCrashDetail](docs/DeviceCrashDetail.md)
 - [DeviceDetail](docs/DeviceDetail.md)
 - [DeviceRiskFactors](docs/DeviceRiskFactors.md)
 - [DeviceRiskFactorsResponse](docs/DeviceRiskFactorsResponse.md)
 - [ErrorResponse](docs/ErrorResponse.md)
 - [Faults](docs/Faults.md)
 - [FaultsResponse](docs/FaultsResponse.md)
 - [FaultsSummary](docs/FaultsSummary.md)
 - [FaultsSummaryResponse](docs/FaultsSummaryResponse.md)
 - [InventoryCrashDetails](docs/InventoryCrashDetails.md)
 - [OptInResponse](docs/OptInResponse.md)
 - [Pagination](docs/Pagination.md)
 - [PartnerAsset](docs/PartnerAsset.md)
 - [PartnerAssetResponse](docs/PartnerAssetResponse.md)
 - [PartnerOffer](docs/PartnerOffer.md)
 - [PartnerOfferAttendee](docs/PartnerOfferAttendee.md)
 - [PartnerOfferSession](docs/PartnerOfferSession.md)
 - [PartnerOfferWithSessions](docs/PartnerOfferWithSessions.md)
 - [PartnerOffersInfo](docs/PartnerOffersInfo.md)
 - [PolicyRuleDetails](docs/PolicyRuleDetails.md)
 - [RacetrackBuid](docs/RacetrackBuid.md)
 - [RacetrackBuidPitstop](docs/RacetrackBuidPitstop.md)
 - [RacetrackBuidPitstopAction](docs/RacetrackBuidPitstopAction.md)
 - [RacetrackBuidSolution](docs/RacetrackBuidSolution.md)
 - [RacetrackTooltip](docs/RacetrackTooltip.md)
 - [RacetrackUsecase](docs/RacetrackUsecase.md)
 - [ReleaseSummary](docs/ReleaseSummary.md)
 - [Report](docs/Report.md)
 - [ReportStatus](docs/ReportStatus.md)
 - [SimilarDeviceData](docs/SimilarDeviceData.md)
 - [SimilarDevices](docs/SimilarDevices.md)
 - [SoftwareGroup](docs/SoftwareGroup.md)
 - [SoftwareGroupBugs](docs/SoftwareGroupBugs.md)
 - [SoftwareGroupBugsResponse](docs/SoftwareGroupBugsResponse.md)
 - [SoftwareGroupFieldNotices](docs/SoftwareGroupFieldNotices.md)
 - [SoftwareGroupFieldNoticesResponse](docs/SoftwareGroupFieldNoticesResponse.md)
 - [SoftwareGroupResponse](docs/SoftwareGroupResponse.md)
 - [SoftwareGroupRisk](docs/SoftwareGroupRisk.md)
 - [SoftwareGroupSecurityAdvisories](docs/SoftwareGroupSecurityAdvisories.md)
 - [SoftwareGroupSecurityAdvisoriesResponse](docs/SoftwareGroupSecurityAdvisoriesResponse.md)
 - [SoftwareGroupSuggestions](docs/SoftwareGroupSuggestions.md)
 - [SolutionMapping](docs/SolutionMapping.md)
 - [SuccessTrack](docs/SuccessTrack.md)
 - [SuccessTrackChecklistMapping](docs/SuccessTrackChecklistMapping.md)
 - [SuccessTrackMapping](docs/SuccessTrackMapping.md)
 - [SuccessTrackUsecasesInner](docs/SuccessTrackUsecasesInner.md)
 - [SuccessTracks](docs/SuccessTracks.md)
 - [SuccessTracksResponse](docs/SuccessTracksResponse.md)
 - [Suggestion](docs/Suggestion.md)
 - [SuggestionSummary](docs/SuggestionSummary.md)
 - [SuggestionSummaryAdvisoriesSeverity](docs/SuggestionSummaryAdvisoriesSeverity.md)
 - [SuggestionSummaryAdvisoriesSeverityExposed](docs/SuggestionSummaryAdvisoriesSeverityExposed.md)
 - [SuggestionSummaryAdvisoriesSeverityFixed](docs/SuggestionSummaryAdvisoriesSeverityFixed.md)
 - [SuggestionSummaryAdvisoriesSeverityNewExposed](docs/SuggestionSummaryAdvisoriesSeverityNewExposed.md)
 - [SuggestionSummaryBugSeverity](docs/SuggestionSummaryBugSeverity.md)
 - [SuggestionSummaryBugSeverityExposed](docs/SuggestionSummaryBugSeverityExposed.md)
 - [SuggestionSummaryBugSeverityFixed](docs/SuggestionSummaryBugSeverityFixed.md)
 - [SuggestionSummaryBugSeverityNewExposed](docs/SuggestionSummaryBugSeverityNewExposed.md)
 - [SuggestionSummaryFeaturesCount](docs/SuggestionSummaryFeaturesCount.md)
 - [SuggestionSummaryFieldNoticeSeverity](docs/SuggestionSummaryFieldNoticeSeverity.md)
 - [SuggestionSummaryFieldNoticeSeverityExposed](docs/SuggestionSummaryFieldNoticeSeverityExposed.md)
 - [SuggestionSummaryFieldNoticeSeverityFixed](docs/SuggestionSummaryFieldNoticeSeverityFixed.md)
 - [SuggestionSummaryFieldNoticeSeverityNewExposed](docs/SuggestionSummaryFieldNoticeSeverityNewExposed.md)
 - [SuggestionsResponse](docs/SuggestionsResponse.md)
 - [ViolationSummary](docs/ViolationSummary.md)
 - [ViolationSummaryResponse](docs/ViolationSummaryResponse.md)


## Documentation For Authorization

The access token authentication request is based on the OAuth client credentials grant flow, which is a single HTTP transaction, not requiring user interaction to complete.

More info: [Authentication for PX Cloud API](https://developer.cisco.com/docs/px-cloud/#!authentication/)

## FAQs and Troubleshooting

For FAQs and Troubleshooting please make use of the official forum [cisco communities](https://community.cisco.com/t5/px-cloud/ct-p/px-cloud)

## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in pxcloud_api_client.apis and pxcloud_api_client.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from pxcloud_api_client.api.default_api import DefaultApi`
- `from pxcloud_api_client.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import pxcloud_api_client
from pxcloud_api_client.apis import *
from pxcloud_api_client.models import *
```

