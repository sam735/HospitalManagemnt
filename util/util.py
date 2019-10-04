import jwt
import datetime
from seckretKey import value_dict
from passlib.apps import custom_app_context as pwd_context
from functools import wraps
from flask import request,jsonify,make_response
def generate_token(user_id):
    token = jwt.encode({'user_id':user_id,'exp':datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},
                        value_dict['SECRET_KEY'],
                        )
    return token.decode('UTF-8')

def verify_password(password,password_hash):
    return pwd_context.verify(password, password_hash)

class Api():
    @classmethod
    def authenticate(cls,f):
        @wraps(f)
        def decorate(*args, **kwrgs):
            if request.headers.get('token') is None:
                return make_response(jsonify({'Message':'Token is missing'}),403)
            try:
                data = jwt.decode(request.headers.get('token'),value_dict['SECRET_KEY'])
            except jwt.DecodeError:
                return make_response(jsonify({'Message':'Token is invalid'}),403)
            except jwt.ExpiredSignatureError:
                return make_response(jsonify({'Message':'Token expired'}),403)
            return f(*args, **kwrgs)
        return decorate
