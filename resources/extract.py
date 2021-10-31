from flask_restful import Resource
from flask import request

# OCR/Image Processing library
from PIL import Image
from pytesseract import pytesseract

# pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Module

# Extraction-OCR-Class

# Module
from AddressFormatter.addressFormatter import addressJSON


class Extract(Resource):
    # ----------
    # GET-METHOD
    def get(self):
        return {'OCR': 'REST-API'}
    # ----------
    # POST-METHOD

    def post(self):
        img = Image.open(request.files['img'])  # Load-Image
        text = pytesseract.image_to_string(img)  # Tesseract-Conversion
        # FormattedJSON =  (Format(text))
        return addressJSON(text)
