from datetime import datetime, date

software_group_suggestions_model = {
    "suggestionUpdatedDate": date,
    "suggestionsInterval": str,
    "suggestionSelectedDate": str,
    "softwareGroupRiskTrend": [
        {
            "changeFromPrev": float,
            "riskCategory": str,
            "date": date,
            "riskScore": float
        }
    ],
    "suggestionSummaries": [
        {
            "expectedSoftwareGroupRisk": str,
            "expectedSoftwareGroupRiskCategory": str,
            "machineSuggestionId": str,
            "name": str,
            "releaseDate": datetime,
            "release": str,
            "releaseNotesUrl": str,
            "bugSeverity": {
                "Fixed": {
                    "High": int,
                    "Low": int,
                    "Medium": int
                },
                "New_Exposed": {
                    "High": int,
                    "Low": int,
                    "Medium": int
                },
                "Exposed": {
                    "High": int,
                    "Low": int,
                    "Medium": int
                }
            },
            "advisoriesSeverity": [
                {
                    "Fixed": {
                        "High": int,
                        "Low": int,
                        "Medium": int
                    },
                    "New_Exposed": {
                        "High": int,
                        "Low": int,
                        "Medium": int
                    },
                    "Exposed": {
                        "High": int,
                        "Low": int,
                        "Medium": int
                    }
                }
            ],
            "fieldNoticeSeverity": [
                {
                    "Fixed": {
                        "High": int,
                        "Low": int,
                        "Medium": int
                    },
                    "New_Exposed": {
                        "High": int,
                        "Low": int,
                        "Medium": int
                    },
                    "Exposed": {
                        "High": int,
                        "Low": int,
                        "Medium": int
                    }
                }
            ],
            "featuresCount": {
                "activeFeaturesCount": int,
                "affectedFeaturesCount": int,
                "fixedFeaturesCount": int
            }
        }
    ],
    "releaseSummary": [
        {
            "name": str,
            "releaseDate": (datetime, str),
            "release": str
        }
    ]
}
