"""
    CX Partner Portal APIs

    PX Cloud APIs for the Partners  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: partner-support@cisco.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from px_faults_v1_python_sdk.api.faults_api import FaultsApi  # noqa: E501


class TestFaultsApi(unittest.TestCase):
    """FaultsApi unit test stubs"""

    def setUp(self):
        self.api = FaultsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_affected_assets_details_using_get(self):
        """Test case for get_affected_assets_details_using_get

        Assets Fault History  # noqa: E501
        """
        pass

    def test_get_affected_assets_using_get(self):
        """Test case for get_affected_assets_using_get

        Affected Assets  # noqa: E501
        """
        pass

    def test_get_faults_summary_using_get(self):
        """Test case for get_faults_summary_using_get

        Fault summary  # noqa: E501
        """
        pass

    def test_get_faults_using_get(self):
        """Test case for get_faults_using_get

        Faults details  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
