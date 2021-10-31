import requests

def dataFromPincode(pincode):
    url = f'https://api.postalpincode.in/pincode/{pincode}'

    response = requests.request('GET', url)

    return response.json()

