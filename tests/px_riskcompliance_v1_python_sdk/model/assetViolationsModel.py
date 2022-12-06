asset_violations_model = {
    'totalCount' : int,
    'items' : [
        {
            "severity": str,
            "regulatoryType": str,
            "violationMessage": str,
            "violationAge": int,
            "suggestion": str,
            "policyDescription": str,
            "ruleTitle": str,
            "ruleDescription": str
        }
    ]
}