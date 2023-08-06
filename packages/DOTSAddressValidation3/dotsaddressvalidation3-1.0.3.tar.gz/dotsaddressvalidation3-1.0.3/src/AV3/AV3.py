'''
DOTS Address Validation 3 US (“AV3”) is a new version of our Address Validation and Address Validation 2 Web services. This service utilizes the latest .Net Framework, WCF, and can be used as a RESTful service or with SOAP. AV3 is designed to take an unstandardized address, validate it against the latest USPS data, and return standardized, deliverable addresses. The service provides corrected information such as the correct street location and zip plus four code, along with parsed address tokens, such as the PMB box number, pre- and post-directionals, county and state codes, and much more.
AV3 can provide instant address verification and correction to websites or enhancement to contact lists.  However, the output from AV3 must be considered carefully before the existence or non-existence of an address is decided.

Functions:
    GetBestMatches(String, String, String, String, String, String, String, String) -> dict
'''
import requests

def GetBestMatches(BusinessName: str, Address: str, Address2: str, City: str, State: str, PostalCode: str, LicenseKey: str, isLive: str) -> dict:
    '''
Returns parsed and validated address elements including Delivery Point Validation (DPV), Residential Delivery Indicator (RDI), and Suite data. GetBestMatches will attempt to validate the input address against a CASS approved engine, and make corrections where possible. Multiple address candidates may be returned if a definitive decision cannot be made by the service.

    Parameters:
        BusinessName (String): Name of business associated with this address. Used to append Suite data.
        Address (String): Address line of the address to validate. For example, “123 Main Street”.
        Address2 (String): This line is for address information that does not contribute to DPV coding an address. For example “C/O John Smith” does not help validate the address, but is still useful in delivery.
        City (String): The city of the address to validate. For example, “New York”.  The city isn’t required, but if one is not provided, the Zip code is required.
        State (String): The state of the address to validate.  For example, “NY”.  This does not need to be contracted, full state names will work as well.  The state isn’t required, but if one is not provided, the Zip code is required.
        PostalCode (String): The zip code of the address to validate.  A zip code isn’t required, but if one is not provided, the City and State are required.
        LicenseKey (String): Your license key to use the service.
        isLive (String): Option to use live service or trial service

    Returns:
        outputs (dict): This the container of the validation results
    '''
    #Set the primary and backup URLs as necessary
    primaryURL = 'https://ws.serviceobjects.com/AV3/api.svc/GetBestMatchesJson?'
    backupURL = 'https://wsbackup.serviceobjects.com/AV3/api.svc/GetBestMatchesJson?'
    trialURL = 'https://trial.serviceobjects.com/AV3/api.svc/GetBestMatchesJson?'


    #The Requests package allows the user to format the path parameters like so instead of having to manually insert them into the URL
    inputs = {'BusinessName': BusinessName, 'Address': Address, 'Address2': Address2, 'City': City, 'State': State, 'PostalCode': PostalCode, 'LicenseKey': LicenseKey}
    if(isLive):
        try:
            result = requests.get(primaryURL, params=inputs)
            #Outputs the results as json
            outputs = result.json()
            #checks the output for Errors and displays the info accordingly
            if 'Error' in outputs.keys():
                try:
                    result = requests.get(backupURL, params=inputs)
                    #Outputs the results as json
                    outputs = result.json()
                    #checks the output for Errors and displays the info accordingly
                    if 'Error' in outputs.keys():
                        raise
                    else:
                        return outputs
            #Displays an Error if the backup and primary URL failed
                except e:
                    raise
            else:
                return outputs

        #Uses the backup URL call the webservice if the primary URL failed
        except:
            try:
                result = requests.get(backupURL, params=inputs)
                #Outputs the results as json
                outputs = result.json()
                #checks the output for Errors and displays the info accordingly
                if 'Error' in outputs.keys():
                    raise
                else:
                    return outputs
            #Displays an Error if the backup and primary URL failed
            except e:
                raise
        return
    else:
        result = requests.get(trialURL, params=inputs)
        #Outputs the results as json
        outputs = result.json()
        #checks the output for Errors and displays the info accordingly
        if 'Error' in outputs.keys():
            raise
        else:
            return outputs


def GetSecondaryNumbers(Address: str, City: str, State: str, PostalCode: str, LicenseKey: str, isLive: str) -> dict:
    '''
Returns parsed and validated address elements along with a list of potential secondary numbers for a given input address. The operation can be leveraged in conjunction with the GetBestMatches operation to find secondary numbers for input data that has either missing or incorrect unit information. For an example workflow please see the Workflow section below.

    Parameters:
        Address (String): Address line of the address to validate. For example, “123 Main Street”.
        City (String): The city of the address to validate. For example, “New York”.  The city isn’t required, but if one is not provided, the Zip code is required.
        State (String): The state of the address to validate.  For example, “NY”.  This does not need to be contracted, full state names will work as well.  The state isn’t required, but if one is not provided, the Zip code is required.
        PostalCode (String): The zip code of the address to validate.  A zip code isn’t required, but if one is not provided, the City and State are required.
        LicenseKey (String): Your license key to use the service.
        isLive (String): Option to use live service or trial service

    Returns:
        outputs (dict): This the container of the validation results
    '''
    #Set the primary and backup URLs as necessary
    primaryURL = 'https://ws.serviceobjects.com/AV3/api.svc/GetSecondaryNumbersJson?'
    backupURL = 'https://wsbackup.serviceobjects.com/AV3/api.svc/GetSecondaryNumbersJson?'
    trialURL = 'https://trial.serviceobjects.com/AV3/api.svc/GetSecondaryNumbersJson?'


    #The Requests package allows the user to format the path parameters like so instead of having to manually insert them into the URL
    inputs = {'Address': Address, 'City': City, 'State': State, 'PostalCode': PostalCode, 'LicenseKey': LicenseKey}
    if(isLive):
        try:
            result = requests.get(primaryURL, params=inputs)
            #Outputs the results as json
            outputs = result.json()
            #checks the output for Errors and displays the info accordingly
            if 'Error' in outputs.keys():
                try:
                    result = requests.get(backupURL, params=inputs)
                    #Outputs the results as json
                    outputs = result.json()
                    #checks the output for Errors and displays the info accordingly
                    if 'Error' in outputs.keys():
                        raise
                    else:
                        return outputs
            #Displays an Error if the backup and primary URL failed
                except e:
                    raise
            else:
                return outputs

        #Uses the backup URL call the webservice if the primary URL failed
        except:
            try:
                result = requests.get(backupURL, params=inputs)
                #Outputs the results as json
                outputs = result.json()
                #checks the output for Errors and displays the info accordingly
                if 'Error' in outputs.keys():
                    raise
                else:
                    return outputs
            #Displays an Error if the backup and primary URL failed
            except e:
                raise
        return
    else:
        result = requests.get(trialURL, params=inputs)
        #Outputs the results as json
        outputs = result.json()
        #checks the output for Errors and displays the info accordingly
        if 'Error' in outputs.keys():
            raise
        else:
            return outputs

# def FindAddressLines(Address1: str, Address2: str, Address3: str, Address4: str, Address5: str, Address6: str, City: str, State: str, PostalCode: str, LicenseKey: str, isLive: str) -> dict:
#     '''
# This operation organizes really bad address data that is broken up into multiple arbitrary address fields.This function will sort up to six possible address lines and return what it thinks are the most probable candidates for the USPS Address1 and possibly Address2. For example, people’s names in the Address1 line mixed with actual street address lines

#     Parameters:
#         Address1 (String): Address line of the address to validate. For example, “123 Main Street”.
#         Address2 (String): This line is for address information that does not contribute to DPV coding an address. For example “C/O John Smith” does not help validate the address, but is still useful in delivery.
#         Address3 (String): Any address information that should belong in Address1 or Address2 lines.
#         Address4 (String): Any address information that should belong in Address1 or Address2 lines.Address line of the address to validate. For example, “123 Main Street”.
#         Address5 (String): Any address information that should belong in Address1 or Address2 lines.Address line of the address to validate. For example, “123 Main Street”.
#         Address6 (String): Any address information that should belong in Address1 or Address2 lines.Address line of the address to validate. For example, “123 Main Street”.
#         City (String): The city of the address to validate. For example, “New York”.  The city isn’t required, but if one is not provided, the Zip code is required.
#         State (String): The state of the address to validate.  For example, “NY”.  This does not need to be contracted, full state names will work as well.  The state isn’t required, but if one is not provided, the Zip code is required.
#         PostalCode (String): The zip code of the address to validate.  A zip code isn’t required, but if one is not provided, the City and State are required.
#         LicenseKey (String): Your license key to use the service.
#         isLive (String): Option to use live service or trial service

#     Returns:
#         outputs (dict): This the container of the validation results
#     '''
#     #Set the primary and backup URLs as necessary
#     primaryURL = 'https://ws.serviceobjects.com/AV3/api.svc/GetSecondaryNumbers?'
#     backupURL = 'https://wsbackup.serviceobjects.com/AV3/api.svc/GetSecondaryNumbers?'
#     trialURL = 'https://trial.serviceobjects.com/AV3/api.svc/GetSecondaryNumbers?'


#     #The Requests package allows the user to format the path parameters like so instead of having to manually insert them into the URL
#     inputs = {'Address1': Address1, 'Address2': Address2, 'Address3': Address3, 'Address4': Address4, 'Address5': Address5, 'Address6': Address6, 'City': City, 'State': State, 'PostalCode': PostalCode, 'LicenseKey': LicenseKey}
#     if(isLive):
#         try:
#             result = requests.get(primaryURL, params=inputs)
#             #Outputs the results as json
#             outputs = result.json()
#             #checks the output for Errors and displays the info accordingly
#             if 'Error' in outputs.keys():
#                 try:
#                     result = requests.get(backupURL, params=inputs)
#                     #Outputs the results as json
#                     outputs = result.json()
#                     #checks the output for Errors and displays the info accordingly
#                     if 'Error' in outputs.keys():
#                         raise
#                     else:
#                         return outputs
#             #Displays an Error if the backup and primary URL failed
#                 except e:
#                     raise
#             else:
#                 return outputs

#         #Uses the backup URL call the webservice if the primary URL failed
#         except:
#             try:
#                 result = requests.get(backupURL, params=inputs)
#                 #Outputs the results as json
#                 outputs = result.json()
#                 #checks the output for Errors and displays the info accordingly
#                 if 'Error' in outputs.keys():
#                     raise
#                 else:
#                     return outputs
#             #Displays an Error if the backup and primary URL failed
#             except e:
#                 raise
#         return
#     else:
#         result = requests.get(trialURL, params=inputs)
#         #Outputs the results as json
#         outputs = result.json()
#         #checks the output for Errors and displays the info accordingly
#         if 'Error' in outputs.keys():
#             raise
#         else:
#             return outputs


# def ValidateAddressWithDPV(Address: str, Address2: str, City: str, State: str, PostalCode: str, LicenseKey: str, isLive: str) -> dict:
#     '''
# Returns parsed and validated address elements including Delivery Point Validation.

#     Parameters:
#         Address (String): Address line of the address to validate. For example, “123 Main Street”.
#         Address2 (String): This line is for address information that does not contribute to DPV coding an address. For example “C/O John Smith” does not help validate the address, but is still useful in delivery.
#         City (String): The city of the address to validate. For example, “New York”.  The city isn’t required, but if one is not provided, the Zip code is required.
#         State (String): The state of the address to validate.  For example, “NY”.  This does not need to be contracted, full state names will work as well.  The state isn’t required, but if one is not provided, the Zip code is required.
#         PostalCode (String): The zip code of the address to validate.  A zip code isn’t required, but if one is not provided, the City and State are required.
#         LicenseKey (String): Your license key to use the service.
#         isLive (String): Option to use live service or trial service

#     Returns:
#         outputs (dict): This the container of the validation results
#     '''
#     if Address == '':
#         Address = ' '
#     if Address2 == '':
#         Address2 = ' '
#     if City == '':
#         City = ' '
#     if State == '':
#         State = ' '
#     if PostalCode == '':
#         PostalCode = ' '
#     if LicenseKey == '':
#         LicenseKey = ' '
#     #Set the primary and backup URLs as necessary
#     primaryURL = f'https://ws.serviceobjects.com/AV3/api.svc/DPVAddressInfo/{Address}/{Address2}/{City}/{State}/{PostalCode}/{LicenseKey}?format=json'
#     backupURL = f'https://wsbackup.serviceobjects.com/AV3/api.svc/DPVAddressInfo/{Address}/{Address2}/{City}/{State}/{PostalCode}/{LicenseKey}?format=json'
#     trialURL = f'https://trial.serviceobjects.com/AV3/api.svc/DPVAddressInfo/{Address}/{Address2}/{City}/{State}/{PostalCode}/{LicenseKey}?format=json'


#     #The Requests package allows the user to format the path parameters like so instead of having to manually insert them into the URL
#     if(isLive):
#         try:
#             result = requests.get(primaryURL)
#             #Outputs the results as json
#             outputs = result.json()
#             #checks the output for Errors and displays the info accordingly
#             if 'Error' in outputs.keys():
#                 try:
#                     result = requests.get(backupURL)
#                     #Outputs the results as json
#                     outputs = result.json()
#                     #checks the output for Errors and displays the info accordingly
#                     if 'Error' in outputs.keys():
#                         raise
#                     else:
#                         return outputs
#             #Displays an Error if the backup and primary URL failed
#                 except e:
#                     raise
#             else:
#                 return outputs

#         #Uses the backup URL call the webservice if the primary URL failed
#         except:
#             try:
#                 result = requests.get(backupURL)
#                 #Outputs the results as json
#                 outputs = result.json()
#                 #checks the output for Errors and displays the info accordingly
#                 if 'Error' in outputs.keys():
#                     raise
#                 else:
#                     return outputs
#             #Displays an Error if the backup and primary URL failed
#             except e:
#                 raise
#         return
#     else:
#         result = requests.get(trialURL)
#         #Outputs the results as json
#         outputs = result.json()
#         #checks the output for Errors and displays the info accordingly
#         if 'Error' in outputs.keys():
#             raise
#         else:
#             return outputs

# def ValidateAddressWithRDI(Address: str, Address2: str, City: str, State: str, PostalCode: str, LicenseKey: str, isLive: str) -> dict:
#     '''
# Identical to the ValidateAddressWithDPV operation but also returns RDI (Residential Delivery Indicator) data in the form of the “IsResidential” output node. Returns parsed and validated address elements including Delivery Point Validation.

# This operation is only available to DOTS Address Validation – US subscribers through a special agreement. Please contact Service Objects at (805) 963-1700 or by emailing the sales department at sales@serviceobjects.com for more information about Residential Delivery Indicator.

#     Parameters:
#         Address (String): Address line of the address to validate. For example, “123 Main Street”.
#         Address2 (String): This line is for address information that does not contribute to DPV coding an address. For example “C/O John Smith” does not help validate the address, but is still useful in delivery.
#         City (String): The city of the address to validate. For example, “New York”.  The city isn’t required, but if one is not provided, the Zip code is required.
#         State (String): The state of the address to validate.  For example, “NY”.  This does not need to be contracted, full state names will work as well.  The state isn’t required, but if one is not provided, the Zip code is required.
#         PostalCode (String): The zip code of the address to validate.  A zip code isn’t required, but if one is not provided, the City and State are required.
#         LicenseKey (String): Your license key to use the service.
#         isLive (String): Option to use live service or trial service

#     Returns:
#         outputs (dict): This the container of the validation results
#     '''
#     if Address == '':
#         Address = ' '
#     if Address2 == '':
#         Address2 = ' '
#     if City == '':
#         City = ' '
#     if State == '':
#         State = ' '
#     if PostalCode == '':
#         PostalCode = ' '
#     if LicenseKey == '':
#         LicenseKey = ' '
#     #Set the primary and backup URLs as necessary
#     primaryURL = f'https://ws.serviceobjects.com/AV3/api.svc/RDIAddressInfo/{Address}/{Address2}/{City}/{State}/{PostalCode}/{LicenseKey}?format=json'
#     backupURL = f'https://wsbackup.serviceobjects.com/AV3/api.svc/RDIAddressInfo/{Address}/{Address2}/{City}/{State}/{PostalCode}/{LicenseKey}?format=json'
#     trialURL = f'https://trial.serviceobjects.com/AV3/api.svc/RDIAddressInfo/{Address}/{Address2}/{City}/{State}/{PostalCode}/{LicenseKey}?format=json'


#     #The Requests package allows the user to format the path parameters like so instead of having to manually insert them into the URL
#     if(isLive):
#         try:
#             result = requests.get(primaryURL)
#             #Outputs the results as json
#             outputs = result.json()
#             #checks the output for Errors and displays the info accordingly
#             if 'Error' in outputs.keys():
#                 try:
#                     result = requests.get(backupURL)
#                     #Outputs the results as json
#                     outputs = result.json()
#                     #checks the output for Errors and displays the info accordingly
#                     if 'Error' in outputs.keys():
#                         raise
#                     else:
#                         return outputs
#             #Displays an Error if the backup and primary URL failed
#                 except e:
#                     raise
#             else:
#                 return outputs

#         #Uses the backup URL call the webservice if the primary URL failed
#         except:
#             try:
#                 result = requests.get(backupURL)
#                 #Outputs the results as json
#                 outputs = result.json()
#                 #checks the output for Errors and displays the info accordingly
#                 if 'Error' in outputs.keys():
#                     raise
#                 else:
#                     return outputs
#             #Displays an Error if the backup and primary URL failed
#             except e:
#                 raise
#         return
#     else:
#         result = requests.get(trialURL)
#         #Outputs the results as json
#         outputs = result.json()
#         #checks the output for Errors and displays the info accordingly
#         if 'Error' in outputs.keys():
#             raise
#         else:
#             return outputs


# def ValidateAddressWithSLK(BusinessName: str,Address: str, Address2: str, City: str, State: str, PostalCode: str, LicenseKey: str, isLive: str) -> dict:
#     '''
# Identical to the ValidateAddressWithDPV operation but also accepts a business name in order to attempt to append Suite data. Also returns parsed and validated address elements including Delivery Point Validation.

#     Parameters:
#         BusinessName (String): Name of business associated with this address. Used to append Suite data.
#         Address (String): Address line of the address to validate. For example, “123 Main Street”.
#         Address2 (String): This line is for address information that does not contribute to DPV coding an address. For example “C/O John Smith” does not help validate the address, but is still useful in delivery.
#         City (String): The city of the address to validate. For example, “New York”.  The city isn’t required, but if one is not provided, the Zip code is required.
#         State (String): The state of the address to validate.  For example, “NY”.  This does not need to be contracted, full state names will work as well.  The state isn’t required, but if one is not provided, the Zip code is required.
#         PostalCode (String): The zip code of the address to validate.  A zip code isn’t required, but if one is not provided, the City and State are required.
#         LicenseKey (String): Your license key to use the service.
#         isLive (String): Option to use live service or trial service

#     Returns:
#         outputs (dict): This the container of the validation results
#     '''
#     if BusinessName == '':
#         BusinessName = ' '
#     if Address == '':
#         Address = ' '
#     if Address2 == '':
#         Address2 = ' '
#     if City == '':
#         City = ' '
#     if State == '':
#         State = ' '
#     if PostalCode == '':
#         PostalCode = ' '
#     if LicenseKey == '':
#         LicenseKey = ' '
#     #Set the primary and backup URLs as necessary
#     primaryURL = f'https://ws.serviceobjects.com/AV3/api.svc/SuiteLinkInfo/{BusinessName}/{Address}/{Address2}/{City}/{State}/{PostalCode}/{LicenseKey}?format=json'
#     backupURL = f'https://wsbackup.serviceobjects.com/AV3/api.svc/SuiteLinkInfo/{BusinessName}/{Address}/{Address2}/{City}/{State}/{PostalCode}/{LicenseKey}?format=json'
#     trialURL = f'https://trial.serviceobjects.com/AV3/api.svc/SuiteLinkInfo/{BusinessName}/{Address}/{Address2}/{City}/{State}/{PostalCode}/{LicenseKey}?format=json'


#     #The Requests package allows the user to format the path parameters like so instead of having to manually insert them into the URL
#     if(isLive):
#         try:
#             result = requests.get(primaryURL)
#             #Outputs the results as json
#             outputs = result.json()
#             #checks the output for Errors and displays the info accordingly
#             if 'Error' in outputs.keys():
#                 try:
#                     result = requests.get(backupURL)
#                     #Outputs the results as json
#                     outputs = result.json()
#                     #checks the output for Errors and displays the info accordingly
#                     if 'Error' in outputs.keys():
#                         raise
#                     else:
#                         return outputs
#             #Displays an Error if the backup and primary URL failed
#                 except e:
#                     raise
#             else:
#                 return outputs

#         #Uses the backup URL call the webservice if the primary URL failed
#         except:
#             try:
#                 result = requests.get(backupURL)
#                 #Outputs the results as json
#                 outputs = result.json()
#                 #checks the output for Errors and displays the info accordingly
#                 if 'Error' in outputs.keys():
#                     raise
#                 else:
#                     return outputs
#             #Displays an Error if the backup and primary URL failed
#             except e:
#                 raise
#         return
#     else:
#         result = requests.get(trialURL)
#         #Outputs the results as json
#         outputs = result.json()
#         #checks the output for Errors and displays the info accordingly
#         if 'Error' in outputs.keys():
#             raise
#         else:
#             return outputs


# def ParseAddress(Address: str, Address2: str, City: str, State: str, PostalCode: str, LicenseKey: str, isLive: str) -> dict:
#     '''
# Parses an address into its individual address elements. This is purely a parsing method and it does not validate, correct or verify an address. The operation is useful for parsing street names, suites and other address fragments out of an otherwise undeliverable address. This method can also be used to parse single line addresses.

#     Parameters:
#         Address (String): Address line of the address to validate. For example, “123 Main Street”.
#         Address2 (String): This line is for address information that does not contribute to DPV coding an address. For example “C/O John Smith” does not help validate the address, but is still useful in delivery.
#         City (String): The city of the address to validate. For example, “New York”.  The city isn’t required, but if one is not provided, the Zip code is required.
#         State (String): The state of the address to validate.  For example, “NY”.  This does not need to be contracted, full state names will work as well.  The state isn’t required, but if one is not provided, the Zip code is required.
#         PostalCode (String): The zip code of the address to validate.  A zip code isn’t required, but if one is not provided, the City and State are required.
#         LicenseKey (String): Your license key to use the service.
#         isLive (String): Option to use live service or trial service

#     Returns:
#         outputs (dict): This the container of the validation results
#     '''
#     if Address == '':
#         Address = ' '
#     if Address2 == '':
#         Address2 = ' '
#     if City == '':
#         City = ' '
#     if State == '':
#         State = ' '
#     if PostalCode == '':
#         PostalCode = ' '
#     if LicenseKey == '':
#         LicenseKey = ' '
#     #Set the primary and backup URLs as necessary
#     primaryURL = f'https://ws.serviceobjects.com/AV3/api.svc/ParseAddress/{Address}/{Address2}/{City}/{State}/{PostalCode}/{LicenseKey}?format=json'
#     backupURL = f'https://wsbackup.serviceobjects.com/AV3/api.svc/ParseAddress/{Address}/{Address2}/{City}/{State}/{PostalCode}/{LicenseKey}?format=json'
#     trialURL = f'https://trial.serviceobjects.com/AV3/api.svc/ParseAddress/{Address}/{Address2}/{City}/{State}/{PostalCode}/{LicenseKey}?format=json'


#     #The Requests package allows the user to format the path parameters like so instead of having to manually insert them into the URL
#     if(isLive):
#         try:
#             result = requests.get(primaryURL)
#             #Outputs the results as json
#             outputs = result.json()
#             #checks the output for Errors and displays the info accordingly
#             if 'Error' in outputs.keys():
#                 try:
#                     result = requests.get(backupURL)
#                     #Outputs the results as json
#                     outputs = result.json()
#                     #checks the output for Errors and displays the info accordingly
#                     if 'Error' in outputs.keys():
#                         raise
#                     else:
#                         return outputs
#             #Displays an Error if the backup and primary URL failed
#                 except e:
#                     raise
#             else:
#                 return outputs

#         #Uses the backup URL call the webservice if the primary URL failed
#         except:
#             try:
#                 result = requests.get(backupURL)
#                 #Outputs the results as json
#                 outputs = result.json()
#                 #checks the output for Errors and displays the info accordingly
#                 if 'Error' in outputs.keys():
#                     raise
#                 else:
#                     return outputs
#             #Displays an Error if the backup and primary URL failed
#             except e:
#                 raise
#         return
#     else:
#         result = requests.get(trialURL)
#         #Outputs the results as json
#         outputs = result.json()
#         #checks the output for Errors and displays the info accordingly
#         if 'Error' in outputs.keys():
#             raise
#         else:
#             return outputs

def ValidateCityStateZip(City: str, State: str, PostalCode: str, LicenseKey: str, isLive: str) -> dict:
    '''
This operation will validate that a given city-state-zip validate together properly.  The inputs can be marginally incorrect, and this operation will correct them.  For instance, a combination with a valid city, slightly misspelled state, and totally incorrect zip code will be corrected to a valid city – state – zip code combination.
 
    Parameters:
        City (String): The city of the address to validate. For example, “New York”.  The city isn’t required, but if one is not provided, the Zip code is required.
        State (String): The state of the address to validate.  For example, “NY”.  This does not need to be contracted, full state names will work as well.  The state isn’t required, but if one is not provided, the Zip code is required.
        PostalCode (String): The zip code of the address to validate.  A zip code isn’t required, but if one is not provided, the City and State are required.
        LicenseKey (String): Your license key to use the service.
        isLive (String): Option to use live service or trial service

    Returns:
        outputs (dict): This the container of the validation results
    '''

    if City == '':
        City = ' '
    if State == '':
        State = ' '
    if PostalCode == '':
        PostalCode = ' '
    if LicenseKey == '':
        LicenseKey = ' '
    #Set the primary and backup URLs as necessary
    primaryURL = f'https://ws.serviceobjects.com/AV3/api.svc/CityStateZipInfo/{City}/{State}/{PostalCode}/{LicenseKey}?format=json'
    backupURL = f'https://wsbackup.serviceobjects.com/AV3/api.svc/CityStateZipInfo/{City}/{State}/{PostalCode}/{LicenseKey}?format=json'
    trialURL = f'https://trial.serviceobjects.com/AV3/api.svc/CityStateZipInfo/{City}/{State}/{PostalCode}/{LicenseKey}?format=json'


    #The Requests package allows the user to format the path parameters like so instead of having to manually insert them into the URL
    if(isLive):
        try:
            result = requests.get(primaryURL)
            #Outputs the results as json
            outputs = result.json()
            #checks the output for Errors and displays the info accordingly
            if 'Error' in outputs.keys():
                try:
                    result = requests.get(backupURL)
                    #Outputs the results as json
                    outputs = result.json()
                    #checks the output for Errors and displays the info accordingly
                    if 'Error' in outputs.keys():
                        raise
                    else:
                        return outputs
            #Displays an Error if the backup and primary URL failed
                except e:
                    raise
            else:
                return outputs

        #Uses the backup URL call the webservice if the primary URL failed
        except:
            try:
                result = requests.get(backupURL)
                #Outputs the results as json
                outputs = result.json()
                #checks the output for Errors and displays the info accordingly
                if 'Error' in outputs.keys():
                    raise
                else:
                    return outputs
            #Displays an Error if the backup and primary URL failed
            except e:
                raise
        return
    else:
        result = requests.get(trialURL)
        #Outputs the results as json
        outputs = result.json()
        #checks the output for Errors and displays the info accordingly
        if 'Error' in outputs.keys():
            raise
        else:
            return outputs

def GetBestMatchesSingleLine(BusinessName: str, Address: str, LicenseKey: str, isLive: str) -> dict:
    '''
Takes a single line of address information as the input and returns the best candidate with parsed and corrected address information. This operation may return multiple address candidates if a single best match cannot be determined.

    Parameters:
        BusinessName (String): Name of business associated with this address. Used to append Suite data
        Address (String): Entire address to Validate. For example (123 Main Street, Anytown CA 99999″)
        LicenseKey (String): Your license key to use the service.
        isLive (String): Option to use live service or trial service

    Returns:
        outputs (dict): This the container of the validation results
    '''

    #Set the primary and backup URLs as necessary
    primaryURL = 'https://ws.serviceobjects.com/AV3/api.svc/GetBestMatchesSingleLineJson?'
    backupURL = 'https://wsbackup.serviceobjects.com/AV3/api.svc/GetBestMatchesSingleLineJson?'
    trialURL = 'https://trial.serviceobjects.com/AV3/api.svc/GetBestMatchesSingleLineJson?'

    inputs = {'BusinessName': BusinessName, 'Address': Address, 'LicenseKey': LicenseKey}

    #The Requests package allows the user to format the path parameters like so instead of having to manually insert them into the URL
    if(isLive):
        try:
            result = requests.get(primaryURL, params=inputs)
            #Outputs the results as json
            outputs = result.json()
            #checks the output for Errors and displays the info accordingly
            if 'Error' in outputs.keys():
                try:
                    result = requests.get(backupURL, params=inputs)
                    #Outputs the results as json
                    outputs = result.json()
                    #checks the output for Errors and displays the info accordingly
                    if 'Error' in outputs.keys():
                        raise
                    else:
                        return outputs
            #Displays an Error if the backup and primary URL failed
                except e:
                    raise
            else:
                return outputs

        #Uses the backup URL call the webservice if the primary URL failed
        except:
            try:
                result = requests.get(backupURL, params=inputs)
                #Outputs the results as json
                outputs = result.json()
                #checks the output for Errors and displays the info accordingly
                if 'Error' in outputs.keys():
                    raise
                else:
                    return outputs
            #Displays an Error if the backup and primary URL failed
            except e:
                raise
        return
    else:
        result = requests.get(trialURL, params=inputs)
        #Outputs the results as json
        outputs = result.json()
        #checks the output for Errors and displays the info accordingly
        if 'Error' in outputs.keys():
            raise
        else:
            return outputs