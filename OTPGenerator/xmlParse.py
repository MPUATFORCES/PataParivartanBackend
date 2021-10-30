import xml.etree.ElementTree as ET

def xmlParse(xmlString):
    root = ET.fromstring(xmlString)

    parsedValues = {
        'ret': root.attrib['ret'],
        'txnId': root.attrib['txn']
    }
    
    return parsedValues