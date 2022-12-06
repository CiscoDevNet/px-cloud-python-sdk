from datetime import datetime

asset_with_violations_model = {
    "totalCount": int,
    "items": [
        {
            "sourceSystemId": str,
            "assetId": str,
            "assetName": str,
            "softwareType": str,
            "serialNumber": str,
            "softwareRelease": str,
            "ipAddress": str,
            "severity": str,
            "lastChecked": datetime,
            "violationCount": int,
            "scanStatus": bool,
            "severityId": str,
            "role": str,
            "assetGroups": list
        }
    ]
}
