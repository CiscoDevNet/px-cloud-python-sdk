import typing_extensions

from pxcloud_api_client.paths import PathValues
from pxcloud_api_client.apis.paths.v1_contract_details import V1ContractDetails
from pxcloud_api_client.apis.paths.v1_contracts import V1Contracts
from pxcloud_api_client.apis.paths.v1_contracts_with_customers import V1ContractsWithCustomers
from pxcloud_api_client.apis.paths.v1_customers import V1Customers
from pxcloud_api_client.apis.paths.v1_customers_customer_id_insights_compliance_asset_violations import V1CustomersCustomerIdInsightsComplianceAssetViolations
from pxcloud_api_client.apis.paths.v1_customers_customer_id_insights_compliance_assets_with_violations import V1CustomersCustomerIdInsightsComplianceAssetsWithViolations
from pxcloud_api_client.apis.paths.v1_customers_customer_id_insights_compliance_opt_in import V1CustomersCustomerIdInsightsComplianceOptIn
from pxcloud_api_client.apis.paths.v1_customers_customer_id_insights_compliance_policy_rule_details import V1CustomersCustomerIdInsightsCompliancePolicyRuleDetails
from pxcloud_api_client.apis.paths.v1_customers_customer_id_insights_compliance_suggestions import V1CustomersCustomerIdInsightsComplianceSuggestions
from pxcloud_api_client.apis.paths.v1_customers_customer_id_insights_compliance_violations import V1CustomersCustomerIdInsightsComplianceViolations
from pxcloud_api_client.apis.paths.v1_customers_customer_id_insights_compliance_violations_assets import V1CustomersCustomerIdInsightsComplianceViolationsAssets
from pxcloud_api_client.apis.paths.v1_customers_customer_id_insights_crash_risk_asset_asset_unique_id_crash_history import V1CustomersCustomerIdInsightsCrashRiskAssetAssetUniqueIdCrashHistory
from pxcloud_api_client.apis.paths.v1_customers_customer_id_insights_crash_risk_assets import V1CustomersCustomerIdInsightsCrashRiskAssets
from pxcloud_api_client.apis.paths.v1_customers_customer_id_insights_crash_risk_assets_asset_unique_id_risk_factors import V1CustomersCustomerIdInsightsCrashRiskAssetsAssetUniqueIdRiskFactors
from pxcloud_api_client.apis.paths.v1_customers_customer_id_insights_crash_risk_assets_asset_unique_id_similar_assets import V1CustomersCustomerIdInsightsCrashRiskAssetsAssetUniqueIdSimilarAssets
from pxcloud_api_client.apis.paths.v1_customers_customer_id_insights_crash_risk_assets_crashed import V1CustomersCustomerIdInsightsCrashRiskAssetsCrashed
from pxcloud_api_client.apis.paths.v1_customers_customer_id_insights_faults import V1CustomersCustomerIdInsightsFaults
from pxcloud_api_client.apis.paths.v1_customers_customer_id_insights_faults_fault_id_affected_assets import V1CustomersCustomerIdInsightsFaultsFaultIdAffectedAssets
from pxcloud_api_client.apis.paths.v1_customers_customer_id_insights_faults_fault_id_affected_assets_asset_name_fault_history import V1CustomersCustomerIdInsightsFaultsFaultIdAffectedAssetsAssetNameFaultHistory
from pxcloud_api_client.apis.paths.v1_customers_customer_id_insights_faults_fault_id_summary import V1CustomersCustomerIdInsightsFaultsFaultIdSummary
from pxcloud_api_client.apis.paths.v1_customers_customer_id_insights_software_software_groups import V1CustomersCustomerIdInsightsSoftwareSoftwareGroups
from pxcloud_api_client.apis.paths.v1_customers_customer_id_insights_software_software_groups_assets import V1CustomersCustomerIdInsightsSoftwareSoftwareGroupsAssets
from pxcloud_api_client.apis.paths.v1_customers_customer_id_insights_software_software_groups_suggestions import V1CustomersCustomerIdInsightsSoftwareSoftwareGroupsSuggestions
from pxcloud_api_client.apis.paths.v1_customers_customer_id_insights_software_software_groups_suggestions_bugs import V1CustomersCustomerIdInsightsSoftwareSoftwareGroupsSuggestionsBugs
from pxcloud_api_client.apis.paths.v1_customers_customer_id_insights_software_software_groups_suggestions_field_notices import V1CustomersCustomerIdInsightsSoftwareSoftwareGroupsSuggestionsFieldNotices
from pxcloud_api_client.apis.paths.v1_customers_customer_id_insights_software_software_groups_suggestions_security_advisories import V1CustomersCustomerIdInsightsSoftwareSoftwareGroupsSuggestionsSecurityAdvisories
from pxcloud_api_client.apis.paths.v1_customers_customer_id_reports import V1CustomersCustomerIdReports
from pxcloud_api_client.apis.paths.v1_customers_customer_id_reports_report_id import V1CustomersCustomerIdReportsReportId
from pxcloud_api_client.apis.paths.v1_partner_offers import V1PartnerOffers
from pxcloud_api_client.apis.paths.v1_partner_offers_sessions import V1PartnerOffersSessions
from pxcloud_api_client.apis.paths.v1_success_tracks import V1SuccessTracks

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.V1_CONTRACT_DETAILS: V1ContractDetails,
        PathValues.V1_CONTRACTS: V1Contracts,
        PathValues.V1_CONTRACTS_WITH_CUSTOMERS: V1ContractsWithCustomers,
        PathValues.V1_CUSTOMERS: V1Customers,
        PathValues.V1_CUSTOMERS_CUSTOMER_ID_INSIGHTS_COMPLIANCE_ASSET_VIOLATIONS: V1CustomersCustomerIdInsightsComplianceAssetViolations,
        PathValues.V1_CUSTOMERS_CUSTOMER_ID_INSIGHTS_COMPLIANCE_ASSETS_WITH_VIOLATIONS: V1CustomersCustomerIdInsightsComplianceAssetsWithViolations,
        PathValues.V1_CUSTOMERS_CUSTOMER_ID_INSIGHTS_COMPLIANCE_OPT_IN: V1CustomersCustomerIdInsightsComplianceOptIn,
        PathValues.V1_CUSTOMERS_CUSTOMER_ID_INSIGHTS_COMPLIANCE_POLICY_RULE_DETAILS: V1CustomersCustomerIdInsightsCompliancePolicyRuleDetails,
        PathValues.V1_CUSTOMERS_CUSTOMER_ID_INSIGHTS_COMPLIANCE_SUGGESTIONS: V1CustomersCustomerIdInsightsComplianceSuggestions,
        PathValues.V1_CUSTOMERS_CUSTOMER_ID_INSIGHTS_COMPLIANCE_VIOLATIONS: V1CustomersCustomerIdInsightsComplianceViolations,
        PathValues.V1_CUSTOMERS_CUSTOMER_ID_INSIGHTS_COMPLIANCE_VIOLATIONS_ASSETS: V1CustomersCustomerIdInsightsComplianceViolationsAssets,
        PathValues.V1_CUSTOMERS_CUSTOMER_ID_INSIGHTS_CRASH_RISK_ASSET_ASSET_UNIQUE_ID_CRASH_HISTORY: V1CustomersCustomerIdInsightsCrashRiskAssetAssetUniqueIdCrashHistory,
        PathValues.V1_CUSTOMERS_CUSTOMER_ID_INSIGHTS_CRASH_RISK_ASSETS: V1CustomersCustomerIdInsightsCrashRiskAssets,
        PathValues.V1_CUSTOMERS_CUSTOMER_ID_INSIGHTS_CRASH_RISK_ASSETS_ASSET_UNIQUE_ID_RISK_FACTORS: V1CustomersCustomerIdInsightsCrashRiskAssetsAssetUniqueIdRiskFactors,
        PathValues.V1_CUSTOMERS_CUSTOMER_ID_INSIGHTS_CRASH_RISK_ASSETS_ASSET_UNIQUE_ID_SIMILAR_ASSETS: V1CustomersCustomerIdInsightsCrashRiskAssetsAssetUniqueIdSimilarAssets,
        PathValues.V1_CUSTOMERS_CUSTOMER_ID_INSIGHTS_CRASH_RISK_ASSETS_CRASHED: V1CustomersCustomerIdInsightsCrashRiskAssetsCrashed,
        PathValues.V1_CUSTOMERS_CUSTOMER_ID_INSIGHTS_FAULTS: V1CustomersCustomerIdInsightsFaults,
        PathValues.V1_CUSTOMERS_CUSTOMER_ID_INSIGHTS_FAULTS_FAULT_ID_AFFECTED_ASSETS: V1CustomersCustomerIdInsightsFaultsFaultIdAffectedAssets,
        PathValues.V1_CUSTOMERS_CUSTOMER_ID_INSIGHTS_FAULTS_FAULT_ID_AFFECTED_ASSETS_ASSET_NAME_FAULT_HISTORY: V1CustomersCustomerIdInsightsFaultsFaultIdAffectedAssetsAssetNameFaultHistory,
        PathValues.V1_CUSTOMERS_CUSTOMER_ID_INSIGHTS_FAULTS_FAULT_ID_SUMMARY: V1CustomersCustomerIdInsightsFaultsFaultIdSummary,
        PathValues.V1_CUSTOMERS_CUSTOMER_ID_INSIGHTS_SOFTWARE_SOFTWARE_GROUPS: V1CustomersCustomerIdInsightsSoftwareSoftwareGroups,
        PathValues.V1_CUSTOMERS_CUSTOMER_ID_INSIGHTS_SOFTWARE_SOFTWARE_GROUPS_ASSETS: V1CustomersCustomerIdInsightsSoftwareSoftwareGroupsAssets,
        PathValues.V1_CUSTOMERS_CUSTOMER_ID_INSIGHTS_SOFTWARE_SOFTWARE_GROUPS_SUGGESTIONS: V1CustomersCustomerIdInsightsSoftwareSoftwareGroupsSuggestions,
        PathValues.V1_CUSTOMERS_CUSTOMER_ID_INSIGHTS_SOFTWARE_SOFTWARE_GROUPS_SUGGESTIONS_BUGS: V1CustomersCustomerIdInsightsSoftwareSoftwareGroupsSuggestionsBugs,
        PathValues.V1_CUSTOMERS_CUSTOMER_ID_INSIGHTS_SOFTWARE_SOFTWARE_GROUPS_SUGGESTIONS_FIELD_NOTICES: V1CustomersCustomerIdInsightsSoftwareSoftwareGroupsSuggestionsFieldNotices,
        PathValues.V1_CUSTOMERS_CUSTOMER_ID_INSIGHTS_SOFTWARE_SOFTWARE_GROUPS_SUGGESTIONS_SECURITY_ADVISORIES: V1CustomersCustomerIdInsightsSoftwareSoftwareGroupsSuggestionsSecurityAdvisories,
        PathValues.V1_CUSTOMERS_CUSTOMER_ID_REPORTS: V1CustomersCustomerIdReports,
        PathValues.V1_CUSTOMERS_CUSTOMER_ID_REPORTS_REPORT_ID: V1CustomersCustomerIdReportsReportId,
        PathValues.V1_PARTNER_OFFERS: V1PartnerOffers,
        PathValues.V1_PARTNER_OFFERS_SESSIONS: V1PartnerOffersSessions,
        PathValues.V1_SUCCESS_TRACKS: V1SuccessTracks,
    }
)

path_to_api = PathToApi(
    {
        PathValues.V1_CONTRACT_DETAILS: V1ContractDetails,
        PathValues.V1_CONTRACTS: V1Contracts,
        PathValues.V1_CONTRACTS_WITH_CUSTOMERS: V1ContractsWithCustomers,
        PathValues.V1_CUSTOMERS: V1Customers,
        PathValues.V1_CUSTOMERS_CUSTOMER_ID_INSIGHTS_COMPLIANCE_ASSET_VIOLATIONS: V1CustomersCustomerIdInsightsComplianceAssetViolations,
        PathValues.V1_CUSTOMERS_CUSTOMER_ID_INSIGHTS_COMPLIANCE_ASSETS_WITH_VIOLATIONS: V1CustomersCustomerIdInsightsComplianceAssetsWithViolations,
        PathValues.V1_CUSTOMERS_CUSTOMER_ID_INSIGHTS_COMPLIANCE_OPT_IN: V1CustomersCustomerIdInsightsComplianceOptIn,
        PathValues.V1_CUSTOMERS_CUSTOMER_ID_INSIGHTS_COMPLIANCE_POLICY_RULE_DETAILS: V1CustomersCustomerIdInsightsCompliancePolicyRuleDetails,
        PathValues.V1_CUSTOMERS_CUSTOMER_ID_INSIGHTS_COMPLIANCE_SUGGESTIONS: V1CustomersCustomerIdInsightsComplianceSuggestions,
        PathValues.V1_CUSTOMERS_CUSTOMER_ID_INSIGHTS_COMPLIANCE_VIOLATIONS: V1CustomersCustomerIdInsightsComplianceViolations,
        PathValues.V1_CUSTOMERS_CUSTOMER_ID_INSIGHTS_COMPLIANCE_VIOLATIONS_ASSETS: V1CustomersCustomerIdInsightsComplianceViolationsAssets,
        PathValues.V1_CUSTOMERS_CUSTOMER_ID_INSIGHTS_CRASH_RISK_ASSET_ASSET_UNIQUE_ID_CRASH_HISTORY: V1CustomersCustomerIdInsightsCrashRiskAssetAssetUniqueIdCrashHistory,
        PathValues.V1_CUSTOMERS_CUSTOMER_ID_INSIGHTS_CRASH_RISK_ASSETS: V1CustomersCustomerIdInsightsCrashRiskAssets,
        PathValues.V1_CUSTOMERS_CUSTOMER_ID_INSIGHTS_CRASH_RISK_ASSETS_ASSET_UNIQUE_ID_RISK_FACTORS: V1CustomersCustomerIdInsightsCrashRiskAssetsAssetUniqueIdRiskFactors,
        PathValues.V1_CUSTOMERS_CUSTOMER_ID_INSIGHTS_CRASH_RISK_ASSETS_ASSET_UNIQUE_ID_SIMILAR_ASSETS: V1CustomersCustomerIdInsightsCrashRiskAssetsAssetUniqueIdSimilarAssets,
        PathValues.V1_CUSTOMERS_CUSTOMER_ID_INSIGHTS_CRASH_RISK_ASSETS_CRASHED: V1CustomersCustomerIdInsightsCrashRiskAssetsCrashed,
        PathValues.V1_CUSTOMERS_CUSTOMER_ID_INSIGHTS_FAULTS: V1CustomersCustomerIdInsightsFaults,
        PathValues.V1_CUSTOMERS_CUSTOMER_ID_INSIGHTS_FAULTS_FAULT_ID_AFFECTED_ASSETS: V1CustomersCustomerIdInsightsFaultsFaultIdAffectedAssets,
        PathValues.V1_CUSTOMERS_CUSTOMER_ID_INSIGHTS_FAULTS_FAULT_ID_AFFECTED_ASSETS_ASSET_NAME_FAULT_HISTORY: V1CustomersCustomerIdInsightsFaultsFaultIdAffectedAssetsAssetNameFaultHistory,
        PathValues.V1_CUSTOMERS_CUSTOMER_ID_INSIGHTS_FAULTS_FAULT_ID_SUMMARY: V1CustomersCustomerIdInsightsFaultsFaultIdSummary,
        PathValues.V1_CUSTOMERS_CUSTOMER_ID_INSIGHTS_SOFTWARE_SOFTWARE_GROUPS: V1CustomersCustomerIdInsightsSoftwareSoftwareGroups,
        PathValues.V1_CUSTOMERS_CUSTOMER_ID_INSIGHTS_SOFTWARE_SOFTWARE_GROUPS_ASSETS: V1CustomersCustomerIdInsightsSoftwareSoftwareGroupsAssets,
        PathValues.V1_CUSTOMERS_CUSTOMER_ID_INSIGHTS_SOFTWARE_SOFTWARE_GROUPS_SUGGESTIONS: V1CustomersCustomerIdInsightsSoftwareSoftwareGroupsSuggestions,
        PathValues.V1_CUSTOMERS_CUSTOMER_ID_INSIGHTS_SOFTWARE_SOFTWARE_GROUPS_SUGGESTIONS_BUGS: V1CustomersCustomerIdInsightsSoftwareSoftwareGroupsSuggestionsBugs,
        PathValues.V1_CUSTOMERS_CUSTOMER_ID_INSIGHTS_SOFTWARE_SOFTWARE_GROUPS_SUGGESTIONS_FIELD_NOTICES: V1CustomersCustomerIdInsightsSoftwareSoftwareGroupsSuggestionsFieldNotices,
        PathValues.V1_CUSTOMERS_CUSTOMER_ID_INSIGHTS_SOFTWARE_SOFTWARE_GROUPS_SUGGESTIONS_SECURITY_ADVISORIES: V1CustomersCustomerIdInsightsSoftwareSoftwareGroupsSuggestionsSecurityAdvisories,
        PathValues.V1_CUSTOMERS_CUSTOMER_ID_REPORTS: V1CustomersCustomerIdReports,
        PathValues.V1_CUSTOMERS_CUSTOMER_ID_REPORTS_REPORT_ID: V1CustomersCustomerIdReportsReportId,
        PathValues.V1_PARTNER_OFFERS: V1PartnerOffers,
        PathValues.V1_PARTNER_OFFERS_SESSIONS: V1PartnerOffersSessions,
        PathValues.V1_SUCCESS_TRACKS: V1SuccessTracks,
    }
)
