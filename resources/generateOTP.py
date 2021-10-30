from flask_restful import Resource
from flask import request

from OTPGenerator.otpRequest import requestOTP

#Location-Validation-Class
class GenerateOTP(Resource):
    #----------
    #GET-METHOD
    def get(self):
        return {'err': 'Invalid Request. Use POST request'}
    
    #----------
    #POST-METHOD 
    def post(self):
        parameters = {
            'uid': request.json['uid'],
            'version': 2.5,
            'ac': 'public',
            'sa': 'public',
            'asalk': 'MEY2cG1nhC02dzj6hnqyKN2A1u6U0LcLAYaPBaLI-3qE-FtthtweGuk',
            'lk': "MAElpSz56NccNf11_wSM_RrXwa7n8_CaoWRrjYYWouA1r8IoJjuaGYg"
        }
        response = requestOTP(parameters)

        return response

        
