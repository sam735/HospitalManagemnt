from db import db
from db.model.models import Hospital

def create_hospital(hospital_payload):
    #import pdb; pdb.set_trace()
    hospital = Hospital(hospital_payload)
    db.session.add(hospital)
    db.session.commit()