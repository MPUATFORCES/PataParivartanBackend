import requests

def authenticate(params):
    url = 'https://stage1.uidai.gov.in/onlineekyc/getAuth/'

    header = {
        "Content-Type": "application/json"
    }

    data = {
        "uid": params['uid'],
        "txnId": params['txnId'],
        "otp": params['otp']
    }

    response =  requests.request("POST", url, headers= header, json= data)

    return response.json()
