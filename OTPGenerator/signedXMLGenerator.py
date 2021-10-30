from lxml import etree
from signxml import XMLSigner

def signedXMLGenerator(data_to_sign, certificates):
    cert = open(certificates['cert']).read()
    key = open(certificates['key']).read()
    root = etree.fromstring(data_to_sign)
    signed_root = XMLSigner().sign(root, key=key, cert=cert)
    
    return etree.tostring(signed_root)