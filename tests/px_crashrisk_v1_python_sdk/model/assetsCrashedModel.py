from datetime import datetime

enums = {
    'mgmtSystemType': {'DNAC', 'NO_CONTROLLER'}
}

assets_crashed_model = {
    'items': [
        {
            'assetId': str,
            'assetName': str,
            'assetUniqueId': str,
            'productId': str,
            'productFamily': str,
            'softwareRelease': str,
            'softwareType': str,
            'serialNumber': str,
            'firstCrashDate': datetime,
            'lastCrashDate': datetime,
            'crashCount':  int,
            'ipAddress': str,
            'mgmtSystemType': str,
            'mgmtSystemHost': str,
            'mgmtSystemAddr': str,
            'hostAddress': (str, None)
        }
    ]
}
