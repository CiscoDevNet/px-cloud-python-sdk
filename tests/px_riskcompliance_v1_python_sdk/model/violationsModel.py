violations_model = {
    'items' : [
        {
            'severity' : str,
            'severityId' : str,
            'policyGroupId' : str,
            'policyGroupName' : str,
            'policyId' : str,
            'policyName' : str,
            'ruleId' : str,
            'ruleTitle' : str,
            'violationCount' : int,
            'affectedAssetsCount' : int,
            'policyCategory' : str,
            'waiverTooltipInfo' : (None, object),
            'swType' : str,
        }
    ],
    'totalCount' : int
}