"""
    Partner Experience Cloud API Python SDK

    Partner Experience Cloud API Python SDK - LA Release  # noqa: E501

    The version of the OpenAPI document: 0.9.0
    Contact: partner-support@cisco.com
    Generated by: https://openapi-generator.tech
"""

import unittest

import pxcloud_api_client
from pxcloud_api_client.api.insights_api import InsightsApi  # noqa: E501


class TestInsightsApi(unittest.TestCase):
    """InsightsApi unit test stubs"""

    def setUp(self):
        self.api = InsightsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_software_group_assets(self):
        """Test case for software_group_assets

        Asset information in the Software Group  # noqa: E501
        """
        pass

    def test_software_group_field_notices(self):
        """Test case for software_group_field_notices

        Software Group - Suggestions Field Notices  # noqa: E501
        """
        pass

    def test_software_group_security_advisories(self):
        """Test case for software_group_security_advisories

        Software Group - Suggestions Security Advisories  # noqa: E501
        """
        pass

    def test_software_group_suggestions(self):
        """Test case for software_group_suggestions

        Software Group Suggestions  # noqa: E501
        """
        pass

    def test_software_group_suggestions_bugs(self):
        """Test case for software_group_suggestions_bugs

        Software Group - Suggestions Bugs  # noqa: E501
        """
        pass

    def test_software_groups(self):
        """Test case for software_groups

        Software Group Information  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
