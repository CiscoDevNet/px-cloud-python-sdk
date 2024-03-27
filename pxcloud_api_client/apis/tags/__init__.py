# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from pxcloud_api_client.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    COMPLIANCE = "Compliance"
    CRASH_RISK = "Crash Risk"
    CUSTOMER_DATA = "Customer Data"
    CX_META_DATA = "CX Meta Data"
    FAULTS = "Faults"
    INSIGHTS = "Insights"
    PARTNER_DATA = "Partner Data"
