# DOTS Address Validation US - 3

This package simplifies making API calls to Address Validation 3 US.  It allows for testing on our trial environments and running against our production environments as well while implementing best practices and failover.


## Examples:

import AV3

### Trial API 
GetBestMatchesTrial = GetBestMatches("", "27 E Cota St", "Suite 500","Santa Barbara", "CA", "93101", "ws72-soa1-dev1", False)
print(GetBestMatchesTrial) 

### Production API 
GetBestMatchesLive = GetBestMatches("", "27 E Cota St", "Suite 500","Santa Barbara", "CA", "93101", "ws72-soa1-dev1", True) 
print(GetBestMatchesLive)

### Trial API 
SecondaryNumbersResponseTrial = GetSecondaryNumbers("27 E Cota ST", "Santa Barbara", "CA", "93101", "ws72-soa1-dev1", False) 
print(SecondaryNumbersResponseTrial)

### Production API 
SecondaryNumbersResponseLive = GetSecondaryNumbers("27 E Cota ST", "Santa Barbara", "CA", "93101", "ws72-soa1-dev1", True) 
print(SecondaryNumbersResponseLive)

### Trial API 
CityStateZipResponseTrial = ValidateCityStateZip("Santa Barbara", "CA", "93101", "ws72-soa1-dev1", False) 
print(CityStateZipResponseTrial)

### Production API 
CityStateZipResponseLive = ValidateCityStateZip("Santa Barbara", "CA", "93101", "ws72-soa1-dev1", True) 
print(CityStateZipResponseLive)

### Trial API 
SingleLineMatchingResponseTrial = GetBestMatchesSingleLine("fooo", "27 E Cota ST STE 500, Santa Barbara, CA 93101", "ws72-soa1-dev1", False) 
print(SingleLineMatchingResponseTrial)

### Production API 
SingleLineMatchingResponseLive = GetBestMatchesSingleLine("fooo", "27 E Cota ST STE 500, Santa Barbara, CA 93101", "ws72-soa1-dev1", True) 
print(SingleLineMatchingResponseLive)

print()