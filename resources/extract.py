from flask_restful import Resource
from flask import request

#OCR/Image Processing library
from PIL import Image
from pytesseract import pytesseract

#Module
from common.util import Format

#Extraction-OCR-Class
class Extract(Resource):
    #----------
    #GET-METHOD
    def get(self):
        return {'OCR':'REST-API'}
    #----------
    #POST-METHOD    
    def post(self):
        img=Image.open(request.files['img'])   #Load-Image
        text=pytesseract.image_to_string(img)  #Tesseract-Conversion
        return Format(text)
