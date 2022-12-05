
enums = {
    'mgmtSystemType' : {'DNAC', 'NO_CONTROLLER'}
}

crash_risk_assets_model = {
    'items' : [
        {
            'assetId' : str,
            'assetName' : str,
            'assetUniqueId' : str,
            'productId' : str,
            'productFamily' : str,
            'ipAddress' : str,
            'softwareRelease' : str,
            'softwareType' : str,
            'serialNumber' : str,
            'risk' : str,
            'endDate' : str,
            'mgmtSystemType' : enums['mgmtSystemType'],
            'mgmtSystemHostname' : str,
            'mgmtSystemAddr' : str
        }
    ],
    'totalCount' : int,
    'crashPredicted': bool
}