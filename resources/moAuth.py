from flask import request
from flask_restful import Resource

import json


class MoAuth(Resource):
    def get(self):
        return {'err': 'Wrong Request! Make POST request.'}

    def post(self):
        if request.json['username'] == 'testperson' and request.json['password'] == 'testpassword':
            # Writing to JSON file
            dict = {
                'username': request.json['username']
            }
            with open('data.json', 'w') as dataJSON:
                json.dump(dict, dataJSON, indent=4)

            return {'auth': True}
        else:
            return {'auth': False}
