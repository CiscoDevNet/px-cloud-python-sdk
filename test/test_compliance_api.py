"""
    Partner Experience Cloud API Python SDK

    Partner Experience Cloud API Python SDK - LA Release  # noqa: E501

    The version of the OpenAPI document: 0.9.0
    Contact: partner-support@cisco.com
    Generated by: https://openapi-generator.tech
"""

import unittest

import pxcloud_api_client
from pxcloud_api_client.api.compliance_api import ComplianceApi  # noqa: E501


class TestComplianceApi(unittest.TestCase):
    """ComplianceApi unit test stubs"""

    def setUp(self):
        self.api = ComplianceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_asset_violations(self):
        """Test case for asset_violations

        Get the violations of the asset  # noqa: E501
        """
        pass

    def test_assets_with_violations(self):
        """Test case for assets_with_violations

        Get the asset summary  # noqa: E501
        """
        pass

    def test_opt_in(self):
        """Test case for opt_in

        optIn status  # noqa: E501
        """
        pass

    def test_policy_rule_details(self):
        """Test case for policy_rule_details

        Returns information about the policy the rule belongs to  # noqa: E501
        """
        pass

    def test_suggestions(self):
        """Test case for suggestions

        Get the Suggestions filtered upon Severity (if given), for summary tab  # noqa: E501
        """
        pass

    def test_violations(self):
        """Test case for violations

        Get the violation summary of a customer  # noqa: E501
        """
        pass

    def test_violations_assets(self):
        """Test case for violations_assets

        Get the violation details of impacted assets for the customer, and selected policy Group, Policy and Rule  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
