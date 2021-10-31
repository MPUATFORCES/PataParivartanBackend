import json
from AddressFormatter.util import format
import re
from AddressFormatter.dataFromPincode import dataFromPincode

def addressJSON(extractedAddress):
    with open('data.json', 'r') as dataJSON:
        dict = json.load(dataJSON)

        dict['extractedAddress'] = extractedAddress.replace('\n', ' ').replace('\f', '')

    with open('data.json', 'w') as dataJSON:
        json.dump(dict, dataJSON)
    
    addJSON={}
    pincode = re.findall("\d{6}", extractedAddress)
    if pincode!=[]:
        data = dataFromPincode(pincode[0])[0]['PostOffice'][0]
        addJSON={
            "pin": pincode[0]
        }

        for i in data:
            if i=='District':
                addJSON['district']=data[i]
                addJSON['city']=data[i]
            elif i=='State':
                addJSON['state'] = data[i]
    
    formatAdd = format(extractedAddress, addJSON)
    return formatAdd
    
    
    


    