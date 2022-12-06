similar_assets_model = {
            'items' : [
                {
                    'assetId' : str,
                    'assetName' : str,
                    'assetUniqueId' : str,
                    'productId' : str,
                    'productFamily' : str,
                    'softwareRelease' : str,
                    'softwareType' : str,
                    'serialNumber' : str,
                    'risk' : str,
                    'similarityScore' : float,
                    'createdByUserName' : (str, None)
                }
            ],
            'totalCount' : int,
            'crashPredicted' : bool
        }