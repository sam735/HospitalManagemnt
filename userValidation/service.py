from db import db
from db.model.models import User
from util.util import generate_token,verify_password

def userValidation(user_dtls):
    #import pdb; pdb.set_trace()
    usr = User.query.filter_by(username=user_dtls.get('user_name')).all()
    if usr != []:
        is_user = verify_password(user_dtls.get('passward'),usr[0].password_hash)
        if is_user:
            token =  generate_token(usr[0].id)
            return token
    return None
    

    