from OTPGenerator.transactionIDGenerator import transactionIDGenerator
import datetime

def xmlStringGenerator(attributes):
    xmlString = f'''<Otp uid='{attributes['uid']}' ac='{attributes['ac']}' sa='{attributes['sa']}' ver="{attributes['version']}" txn="{transactionIDGenerator()}" ts="{datetime.datetime.now().isoformat()}" lk='{attributes['lk']}' type="A"><Opts ch="00"/></Otp>'''

    return xmlString