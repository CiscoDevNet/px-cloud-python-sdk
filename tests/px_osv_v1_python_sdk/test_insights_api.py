"""
    CX Partner Portal APIs

    PX Cloud APIs for the Partners  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: partner-support@cisco.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from px_osv_v1_python_sdk.api.insights_api import InsightsApi  # noqa: E501


class TestInsightsApi(unittest.TestCase):
    """InsightsApi unit test stubs"""

    def setUp(self):
        self.api = InsightsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_software_group_assets_using_get(self):
        """Test case for get_software_group_assets_using_get

        Asset information in the Software Group  # noqa: E501
        """
        pass

    def test_get_software_group_suggestions_using_get(self):
        """Test case for get_software_group_suggestions_using_get

        Software Group suggestions  # noqa: E501
        """
        pass

    def test_get_software_groups_using_get(self):
        """Test case for get_software_groups_using_get

        Software Group information  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()