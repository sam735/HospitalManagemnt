from db.model.models import User
from db import db
def user_registration(user_payload):
    #import pdb; pdb.set_trace()
    user = User(user_payload)
    db.session.add(user)
    db.session.commit()