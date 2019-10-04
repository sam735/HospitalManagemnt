from flask import request,json,make_response,jsonify
from flask_restful import Resource
from userRegistration.service import user_registration

class UserRegistration(Resource):
    def post(self):
        try:
            user_registration(request.json)
            data = {"Message":"User registration got successfull"} # Your data in JSON-serializable type
            response = make_response(jsonify(data),201)
            return response
        except Exception:
            data = {"Message":"User registration failed, Internal server error"} # Your data in JSON-serializable type
            response = make_response(jsonify(data),500)
            return response