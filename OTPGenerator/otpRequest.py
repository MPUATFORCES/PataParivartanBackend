import requests
from OTPGenerator.signedXMLGenerator import signedXMLGenerator
from OTPGenerator.xmlStringGenerator import xmlStringGenerator
from OTPGenerator.xmlParse import xmlParse

def requestOTP(params):
    # Request parameters defined
    url = f"https://otp-stage.uidai.gov.in/uidotpserver/{params['version']}/{params['ac']}/{params['uid'][0]}/{params['uid'][1]}/{params['asalk']}"
    headers = {
        "Content-Type": "application/xml"
    }

    # Request XML created
    xmlString = xmlStringGenerator(params)
    certificates = {
        "cert": './OTPGenerator/certificates/PublicAUAforStagingServices.pem',
        'key': './OTPGenerator/certificates/PublicAUAforStagingServices.key'
    }
    signedXML = signedXMLGenerator(xmlString, certificates).decode('utf-8')
    parameter_xml = '<?xml version="1.0" encoding="UTF-8"?>'+signedXML

    # API request created and response captured
    response = requests.request("POST", url, headers=headers, data=parameter_xml)

    responseJSON = xmlParse(response.text)

    return responseJSON
