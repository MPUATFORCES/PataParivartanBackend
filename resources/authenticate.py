from flask_restful import Resource
from flask import request

from Authenticator.authenticator import authenticate

class Authenticate(Resource):
    def get(self):
        return {'err': 'Invalid Request. Use POST request'}

    def post(self):
        response = authenticate(request.json)

        return response
