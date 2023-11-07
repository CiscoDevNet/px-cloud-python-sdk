# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from pxcloud_api_client.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    V1_CONTRACT_DETAILS = "/v1/contract/details"
    V1_CONTRACTS = "/v1/contracts"
    V1_CONTRACTS_WITH_CUSTOMERS = "/v1/contractsWithCustomers"
    V1_CUSTOMERS = "/v1/customers"
    V1_CUSTOMERS_CUSTOMER_ID_INSIGHTS_COMPLIANCE_ASSET_VIOLATIONS = "/v1/customers/{customerId}/insights/compliance/assetViolations"
    V1_CUSTOMERS_CUSTOMER_ID_INSIGHTS_COMPLIANCE_ASSETS_WITH_VIOLATIONS = "/v1/customers/{customerId}/insights/compliance/assetsWithViolations"
    V1_CUSTOMERS_CUSTOMER_ID_INSIGHTS_COMPLIANCE_OPT_IN = "/v1/customers/{customerId}/insights/compliance/optIn"
    V1_CUSTOMERS_CUSTOMER_ID_INSIGHTS_COMPLIANCE_POLICY_RULE_DETAILS = "/v1/customers/{customerId}/insights/compliance/policyRuleDetails"
    V1_CUSTOMERS_CUSTOMER_ID_INSIGHTS_COMPLIANCE_SUGGESTIONS = "/v1/customers/{customerId}/insights/compliance/suggestions"
    V1_CUSTOMERS_CUSTOMER_ID_INSIGHTS_COMPLIANCE_VIOLATIONS = "/v1/customers/{customerId}/insights/compliance/violations"
    V1_CUSTOMERS_CUSTOMER_ID_INSIGHTS_COMPLIANCE_VIOLATIONS_ASSETS = "/v1/customers/{customerId}/insights/compliance/violations/assets"
    V1_CUSTOMERS_CUSTOMER_ID_INSIGHTS_CRASH_RISK_ASSET_ASSET_UNIQUE_ID_CRASH_HISTORY = "/v1/customers/{customerId}/insights/crashRisk/asset/{assetUniqueId}/crashHistory"
    V1_CUSTOMERS_CUSTOMER_ID_INSIGHTS_CRASH_RISK_ASSETS = "/v1/customers/{customerId}/insights/crashRisk/assets"
    V1_CUSTOMERS_CUSTOMER_ID_INSIGHTS_CRASH_RISK_ASSETS_ASSET_UNIQUE_ID_RISK_FACTORS = "/v1/customers/{customerId}/insights/crashRisk/assets/{assetUniqueId}/riskFactors"
    V1_CUSTOMERS_CUSTOMER_ID_INSIGHTS_CRASH_RISK_ASSETS_ASSET_UNIQUE_ID_SIMILAR_ASSETS = "/v1/customers/{customerId}/insights/crashRisk/assets/{assetUniqueId}/similarAssets"
    V1_CUSTOMERS_CUSTOMER_ID_INSIGHTS_CRASH_RISK_ASSETS_CRASHED = "/v1/customers/{customerId}/insights/crashRisk/assetsCrashed"
    V1_CUSTOMERS_CUSTOMER_ID_INSIGHTS_FAULTS = "/v1/customers/{customerId}/insights/faults"
    V1_CUSTOMERS_CUSTOMER_ID_INSIGHTS_FAULTS_FAULT_ID_AFFECTED_ASSETS = "/v1/customers/{customerId}/insights/faults/{faultId}/affectedAssets"
    V1_CUSTOMERS_CUSTOMER_ID_INSIGHTS_FAULTS_FAULT_ID_AFFECTED_ASSETS_ASSET_NAME_FAULT_HISTORY = "/v1/customers/{customerId}/insights/faults/{faultId}/affectedAssets/{assetName}/faultHistory"
    V1_CUSTOMERS_CUSTOMER_ID_INSIGHTS_FAULTS_FAULT_ID_SUMMARY = "/v1/customers/{customerId}/insights/faults/{faultId}/summary"
    V1_CUSTOMERS_CUSTOMER_ID_INSIGHTS_SOFTWARE_SOFTWARE_GROUPS = "/v1/customers/{customerId}/insights/software/softwareGroups"
    V1_CUSTOMERS_CUSTOMER_ID_INSIGHTS_SOFTWARE_SOFTWARE_GROUPS_ASSETS = "/v1/customers/{customerId}/insights/software/softwareGroups/assets"
    V1_CUSTOMERS_CUSTOMER_ID_INSIGHTS_SOFTWARE_SOFTWARE_GROUPS_SUGGESTIONS = "/v1/customers/{customerId}/insights/software/softwareGroups/suggestions"
    V1_CUSTOMERS_CUSTOMER_ID_INSIGHTS_SOFTWARE_SOFTWARE_GROUPS_SUGGESTIONS_BUGS = "/v1/customers/{customerId}/insights/software/softwareGroups/suggestions/bugs"
    V1_CUSTOMERS_CUSTOMER_ID_INSIGHTS_SOFTWARE_SOFTWARE_GROUPS_SUGGESTIONS_FIELD_NOTICES = "/v1/customers/{customerId}/insights/software/softwareGroups/suggestions/fieldNotices"
    V1_CUSTOMERS_CUSTOMER_ID_INSIGHTS_SOFTWARE_SOFTWARE_GROUPS_SUGGESTIONS_SECURITY_ADVISORIES = "/v1/customers/{customerId}/insights/software/softwareGroups/suggestions/securityAdvisories"
    V1_CUSTOMERS_CUSTOMER_ID_REPORTS = "/v1/customers/{customerId}/reports"
    V1_CUSTOMERS_CUSTOMER_ID_REPORTS_REPORT_ID = "/v1/customers/{customerId}/reports/{reportId}"
    V1_PARTNER_OFFERS = "/v1/partnerOffers"
    V1_PARTNER_OFFERS_SESSIONS = "/v1/partnerOffersSessions"
    V1_SUCCESS_TRACKS = "/v1/successTracks"
