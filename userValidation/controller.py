from flask import request,json,make_response,jsonify
from flask_restful import Resource
from userValidation.service import userValidation

class ValidateUser(Resource):
    def get(self):
        user_detail = {'user_name':request.headers.get('userName'),'passward':request.headers.get('passward')}
        try:
            token =  userValidation(user_detail)
            if token is None:
               data={'Message':'User Is not register'}
               return make_response(jsonify(data),401)
            else:
                data ={'Token':token,'expireIn':'30'}
                return make_response(jsonify(data),200)
        except Exception:
            data = {'Message':'Internal server error'}
            return make_response(jsonify(data),500)

