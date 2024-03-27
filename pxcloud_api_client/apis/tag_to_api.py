import typing_extensions

from pxcloud_api_client.apis.tags import TagValues
from pxcloud_api_client.apis.tags.compliance_api import ComplianceApi
from pxcloud_api_client.apis.tags.crash_risk_api import CrashRiskApi
from pxcloud_api_client.apis.tags.customer_data_api import CustomerDataApi
from pxcloud_api_client.apis.tags.cx_meta_data_api import CXMetaDataApi
from pxcloud_api_client.apis.tags.faults_api import FaultsApi
from pxcloud_api_client.apis.tags.insights_api import InsightsApi
from pxcloud_api_client.apis.tags.partner_data_api import PartnerDataApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.COMPLIANCE: ComplianceApi,
        TagValues.CRASH_RISK: CrashRiskApi,
        TagValues.CUSTOMER_DATA: CustomerDataApi,
        TagValues.CX_META_DATA: CXMetaDataApi,
        TagValues.FAULTS: FaultsApi,
        TagValues.INSIGHTS: InsightsApi,
        TagValues.PARTNER_DATA: PartnerDataApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.COMPLIANCE: ComplianceApi,
        TagValues.CRASH_RISK: CrashRiskApi,
        TagValues.CUSTOMER_DATA: CustomerDataApi,
        TagValues.CX_META_DATA: CXMetaDataApi,
        TagValues.FAULTS: FaultsApi,
        TagValues.INSIGHTS: InsightsApi,
        TagValues.PARTNER_DATA: PartnerDataApi,
    }
)
