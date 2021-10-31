from typing import Generator
from flask import Flask
from flask_restful import Api
# from logging.config import fileConfig

import logging
from flask_cors import CORS, cross_origin

# Modules
from resources.extract import Extract
from resources.validate import Validate
from resources.generateOTP import GenerateOTP
from resources.authenticate import Authenticate
from resources.moAuth import MoAuth

# initiate
app = Flask(__name__)
CORS(app)
api = Api(app)
app.config['CORS_HEADERS'] = 'Content-Type'

logging.basicConfig(filename='demo.log', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
# fileConfig('logging.cfg')

# Routes
api.add_resource(Extract, '/')
api.add_resource(Validate, '/gps')
api.add_resource(GenerateOTP, '/otp')
api.add_resource(Authenticate, '/auth')
api.add_resource(MoAuth, '/moauth')


@app.route('/')
@cross_origin()
def hello_world():
    app.logger.info('Processing default request')
    return 'Hello World!'


# Run
if __name__ == '__main__':
    app.run(debug=True)
