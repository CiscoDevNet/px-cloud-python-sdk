violations_assets_model = {
    'totalCount' : int,
    'items' : [
        {
            'assetId' : str,
            'assetName' : str,
            'softwareType' : str,
            'softwareRelease' : str,
            'productFamily' : str,
            'productId' : str,
            'severity' : str,
            'ipAddress' : str,
            'lastChecked' : str,
            'scanStatus' : bool,
            'violationCount' : int,
            'mgmtSystemHostname' : str,
            'role' : str,
            'mgmtSystemType' : str
        }
    ]
}