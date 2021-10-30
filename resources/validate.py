from flask_restful import Resource
from flask import request
import requests

#import keys
from common.config import POSITIONSTACK_APIKEY


# Extraction-OCR-Class with Validation


class Validate(Resource):
    
    def verify(fromgps,fromadd):
        if fromgps>=fromadd:
            diff=fromgps-fromadd
        else:
            diff=fromadd-fromgps
        if diff<=0.02:
            return True
        else:
            return False

    # ----------
    # GET-METHOD
    def get(self):
        return {'ExtractCoordinates': 'REST-API'}

    # ----------
    # POST-METHOD
    def post(self):
        data = request.args.get('limit')
        print('this is data:', data)
        # houseno = data.query.houseno
        # street = data.query.street
        # area = data.query.area
        # city = data.query.city
        # state = data.query.state
        # country = data.query.country

        # coordinates = requests.post(url='https://api.positionstack.com/v1/forward', params={
        #     'access_key': POSITIONSTACK_APIKEY,
        #     'query': f'{houseno} {street} {area} {city} {state} {country}',
        #     'limit': 1
        # })

        # latitude = coordinates.data[0].latitude
        # longitude = coordinates.data[0].longitude

        # print(latitude, longitude)
