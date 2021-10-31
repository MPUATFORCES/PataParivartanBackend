from flask import request
from flask_restful import Resource


class MoAuth(Resource):
    def get(self):
        return {'err': 'Wrong Request! Make POST request.'}

    def post(self):
        print(request.get_data())
        username = request.json['username']
        password = request.json['password']
        if username == 'testperson' and password == 'testpassword':
            return {'user': username, 'auth': True, 'token': 'sampletoken'}
        else:
            return {'auth': False}
