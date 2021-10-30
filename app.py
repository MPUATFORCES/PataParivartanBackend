from typing import Generator
from flask import Flask
from flask_restful import Api

# Modules
from resources.extract import Extract
from resources.validate import Validate
from resources.generateOTP import GenerateOTP
from resources.authenticate import Authenticate
from resources.moAuth import MoAuth

# initiate
app = Flask(__name__)
api = Api(app)

# Routes
api.add_resource(Extract, '/')
api.add_resource(Validate, '/gps')
api.add_resource(GenerateOTP, '/otp')
api.add_resource(Authenticate, '/auth')
api.add_resource(MoAuth, '/moauth')

# Run
if __name__ == '__main__':
    app.run(debug=True)
