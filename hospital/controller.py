from flask import request,json,make_response,jsonify
from flask_restful import Resource
from hospital.service import create_hospital
from util.util import Api

class Hospital(Resource):
    @Api.authenticate
    def post(self):
        try:
            create_hospital(request.json)
            data = {"Message":"resource created successfully"} # Your data in JSON-serializable type
            response = make_response(jsonify(data),201)
            return response
        except Exception:
            data = {"Message":"resource creation failed, Internal server error"} # Your data in JSON-serializable type
            response = make_response(jsonify(data),500)
            return response
        