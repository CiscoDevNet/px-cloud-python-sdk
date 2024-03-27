# pxcloud_api_client.pxcloud_api_client.suggestion_summary.SuggestionSummary

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**expectedSoftwareGroupRisk** | str,  | str,  | Current risk score of the Cisco software release, which is the level of exposure the software release has to bugs, security advisories, and field notices. The risk score is used to make software suggestions intended to minimize risk for assets in the Software Group. | [optional] 
**expectedSoftwareGroupRiskCategory** | str,  | str,  | Risk level of the Cisco software release based on its risk score. The risk level can be High, Medium, or Low. | [optional] 
**machineSuggestionId** | str,  | str,  | Unique identifier of the suggestion | [optional] 
**name** | str,  | str,  | Value that indicates whether the Cisco software release is a current release or one of the suggested release options | [optional] 
**releaseDate** | str, datetime,  | str,  | Date the Cisco software image was released | [optional] value must conform to RFC-3339 date-time
**release** | str,  | str,  | Release of the Cisco software | [optional] 
**releaseNotesUrl** | str,  | str,  | Public URL for the release notes of the Cisco software release | [optional] 
**[bugSeverity](#bugSeverity)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Number of bugs the Cisco software release is exposed to, and for suggested releases, the number of bugs the suggested release addresses | [optional] 
**[advisoriesSeverity](#advisoriesSeverity)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Number of security advisories the current Cisco software releases are exposed to that are addressed by the suggested release | [optional] 
**[fieldNoticeSeverity](#fieldNoticeSeverity)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Number of field notices the current Cisco software releases are exposed to that are addressed by the suggested release | [optional] 
**[featuresCount](#featuresCount)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# bugSeverity

Number of bugs the Cisco software release is exposed to, and for suggested releases, the number of bugs the suggested release addresses

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Number of bugs the Cisco software release is exposed to, and for suggested releases, the number of bugs the suggested release addresses | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[Exposed](#Exposed)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Number of bugs the current Cisco software releases are exposed to that are addressed by the suggested release, grouped by severity. | [optional] 
**[New_Exposed](#New_Exposed)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Number of new bugs the suggested Cisco software release is exposed to compared to the current Cisco software releases, grouped by severity | [optional] 
**[Fixed](#Fixed)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Number of bugs the current Cisco software releases are exposed to, grouped by severity | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# Exposed

Number of bugs the current Cisco software releases are exposed to that are addressed by the suggested release, grouped by severity.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Number of bugs the current Cisco software releases are exposed to that are addressed by the suggested release, grouped by severity. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**High** | decimal.Decimal, int,  | decimal.Decimal,  | Number of High severity bugs addressed by the suggested Cisco software release | [optional] value must be a 64 bit integer
**Medium** | decimal.Decimal, int,  | decimal.Decimal,  | Number of Medium severity bugs addressed by the suggested Cisco software release | [optional] value must be a 64 bit integer
**Low** | decimal.Decimal, int,  | decimal.Decimal,  | Number of Low severity bugs addressed by the suggested Cisco software release | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# New_Exposed

Number of new bugs the suggested Cisco software release is exposed to compared to the current Cisco software releases, grouped by severity

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Number of new bugs the suggested Cisco software release is exposed to compared to the current Cisco software releases, grouped by severity | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**High** | decimal.Decimal, int,  | decimal.Decimal,  | Number of new High severity bugs the suggested Cisco software release is exposed to compared to the current Cisco software releases | [optional] value must be a 64 bit integer
**Low** | decimal.Decimal, int,  | decimal.Decimal,  | Number of new Low severity bugs the suggested Cisco software release is exposed to compared to the current Cisco software releases | [optional] value must be a 64 bit integer
**Medium** | decimal.Decimal, int,  | decimal.Decimal,  | Number of new Medium severity bugs the suggested Cisco software release is exposed to compared to the current Cisco software releases | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# Fixed

Number of bugs the current Cisco software releases are exposed to, grouped by severity

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Number of bugs the current Cisco software releases are exposed to, grouped by severity | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**High** | decimal.Decimal, int,  | decimal.Decimal,  | Number of High severity bugs the current Cisco software releases are exposed to | [optional] value must be a 64 bit integer
**Low** | decimal.Decimal, int,  | decimal.Decimal,  | Number of Low severity bugs the current Cisco software releases are exposed to | [optional] value must be a 64 bit integer
**Medium** | decimal.Decimal, int,  | decimal.Decimal,  | Number of Medium severity bugs the current Cisco software releases are exposed to | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# advisoriesSeverity

Number of security advisories the current Cisco software releases are exposed to that are addressed by the suggested release

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Number of security advisories the current Cisco software releases are exposed to that are addressed by the suggested release | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[Exposed](#Exposed)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Number of security advisories the current Cisco software releases are exposed to that are addressed by the suggested release, grouped by impact | [optional] 
**[New_Exposed](#New_Exposed)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Number of new security advisories the current Cisco software release are exposed to compared to the current Cisco software releases | [optional] 
**[Fixed](#Fixed)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Number of security advisories the current Cisco software release are exposed to | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# Exposed

Number of security advisories the current Cisco software releases are exposed to that are addressed by the suggested release, grouped by impact

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Number of security advisories the current Cisco software releases are exposed to that are addressed by the suggested release, grouped by impact | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**High** | decimal.Decimal, int,  | decimal.Decimal,  | Number of High impact security advisories addressed by the suggested Cisco software release | [optional] value must be a 64 bit integer
**Low** | decimal.Decimal, int,  | decimal.Decimal,  | Number of Low impact security advisories addressed by the suggested Cisco software release | [optional] value must be a 64 bit integer
**Medium** | decimal.Decimal, int,  | decimal.Decimal,  | Number of Medium impact security advisories addressed by the suggested Cisco software release | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# New_Exposed

Number of new security advisories the current Cisco software release are exposed to compared to the current Cisco software releases

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Number of new security advisories the current Cisco software release are exposed to compared to the current Cisco software releases | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**high** | decimal.Decimal, int,  | decimal.Decimal,  | Number of new High impact security advisories | [optional] value must be a 64 bit integer
**low** | decimal.Decimal, int,  | decimal.Decimal,  | Number of new Low impact security advisories | [optional] value must be a 64 bit integer
**medium** | decimal.Decimal, int,  | decimal.Decimal,  | Number of new Medium impact security advisories | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# Fixed

Number of security advisories the current Cisco software release are exposed to

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Number of security advisories the current Cisco software release are exposed to | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**high** | decimal.Decimal, int,  | decimal.Decimal,  | Number of High impact security advisories | [optional] value must be a 64 bit integer
**low** | decimal.Decimal, int,  | decimal.Decimal,  | Number of Low impact security advisories | [optional] value must be a 64 bit integer
**medium** | decimal.Decimal, int,  | decimal.Decimal,  | Number of Medium impact security advisories | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# fieldNoticeSeverity

Number of field notices the current Cisco software releases are exposed to that are addressed by the suggested release

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Number of field notices the current Cisco software releases are exposed to that are addressed by the suggested release | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[Exposed](#Exposed)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Number of field notices the current Cisco software releases are exposed to that are addressed by the suggested release | [optional] 
**[New_Exposed](#New_Exposed)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Number of new field notices the current Cisco software releases are exposed to compared to the current Cisco software releases | [optional] 
**[Fixed](#Fixed)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Number of field notices the current Cisco software releases are exposed to | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# Exposed

Number of field notices the current Cisco software releases are exposed to that are addressed by the suggested release

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Number of field notices the current Cisco software releases are exposed to that are addressed by the suggested release | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**High** | decimal.Decimal, int,  | decimal.Decimal,  | Number of High impact security advisories addressed by the suggested Cisco software release | [optional] value must be a 64 bit integer
**Low** | decimal.Decimal, int,  | decimal.Decimal,  | Number of Low impact security advisories addressed by the suggested Cisco software release | [optional] value must be a 64 bit integer
**Medium** | decimal.Decimal, int,  | decimal.Decimal,  | Number of Medium impact security advisories addressed by the suggested Cisco software release | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# New_Exposed

Number of new field notices the current Cisco software releases are exposed to compared to the current Cisco software releases

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Number of new field notices the current Cisco software releases are exposed to compared to the current Cisco software releases | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**High** | decimal.Decimal, int,  | decimal.Decimal,  | Number of High impact security advisories addressed by the suggested Cisco software release | [optional] value must be a 64 bit integer
**Low** | decimal.Decimal, int,  | decimal.Decimal,  | Number of Low impact security advisories addressed by the suggested Cisco software release | [optional] value must be a 64 bit integer
**Medium** | decimal.Decimal, int,  | decimal.Decimal,  | Number of Medium impact security advisories addressed by the suggested Cisco software release | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# Fixed

Number of field notices the current Cisco software releases are exposed to

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Number of field notices the current Cisco software releases are exposed to | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**High** | decimal.Decimal, int,  | decimal.Decimal,  | Number of High impact security advisories addressed by the suggested Cisco software release | [optional] value must be a 64 bit integer
**Low** | decimal.Decimal, int,  | decimal.Decimal,  | Number of Low impact security advisories addressed by the suggested Cisco software release | [optional] value must be a 64 bit integer
**Medium** | decimal.Decimal, int,  | decimal.Decimal,  | Number of Medium impact security advisories addressed by the suggested Cisco software release | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# featuresCount

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**activeFeaturesCount** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**affectedFeaturesCount** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**fixedFeaturesCount** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

