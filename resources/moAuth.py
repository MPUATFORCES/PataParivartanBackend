from flask import request
from flask_restful import Resource

class MoAuth(Resource):
    def get(self):
        return {'err': 'Wrong Request! Make POST request.'}

    def post(self):
        if request.json['username'] == 'testperson' and request.json['password'] == 'testpassword':
            return {'auth': True}
        else:
            return {'auth': False}