from db import db
from passlib.apps import custom_app_context as pwd_context

from datetime import datetime
class User(db.Model):
    __tablename__ = 'users'
    __table_args__ = (
        db.UniqueConstraint('username'),
    )
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(32), index = True, nullable = False)
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String(128))
    contact_no = db.Column(db.String(10))
    first_name = db.Column(db.String(35),nullable = False)
    last_name = db.Column(db.String(35),nullable = False)
    sex = db.Column(db.String(1))
    created_date = db.Column(db.DateTime,default=datetime.utcnow)
    active = db.Column(db.String(1),default = 'Y')

    def __init__(self,userPayload):
        self.username = userPayload.get('userName')
        self.password_hash = pwd_context.encrypt(userPayload.get('password'))
        self.email = userPayload.get('email')
        self.contact_no = userPayload.get('contactNo')
        self.name = userPayload.get('name')
        self.sex = userPayload.get('sex').upper()[0]
        self.first_name = userPayload.get('firstName')
        self.last_name = userPayload.get('lastName')

class Hospital(db.Model):
    __tablename__ = 'Hospitals'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(),nullable = False)
    addrs = db.Column(db.String(),nullable = False)
    zip = db.Column(db.Integer,nullable = False)
    city = db.Column(db.String(30),nullable = False)
    state = db.Column(db.String(50),nullable = False)
    rating = db.Column(db.Integer)
    contact_no = db.Column(db.String(10))
    active_time = db.Column(db.String(10))
    active = db.Column(db.String(1),default='Y')
    doctors = db.relationship('Doctor',backref='belongs_to')

    def __init__(self,hospital_payload):

        self.name = hospital_payload.get('name')
        self.addrs = hospital_payload.get('address')
        self.zip = hospital_payload.get('zip')
        self.city = hospital_payload.get('city')
        self.state = hospital_payload.get('state')
        self.rating = hospital_payload.get('rating')
        self.contact_no = hospital_payload.get('contactNo')
        self.active_time = hospital_payload.get('activeTime')

class Doctor(db.Model):
    __tablename__ = 'Doctors'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(),nullable = False)
    specality = db.Column(db.String(),nullable = False)
    experience = db.Column(db.Integer,nullable = False)
    working_Hour = db.Column(db.Integer,nullable = False) 
    shift_timing = db.Column(db.String(17),nullable = False)
    rating = db.Column(db.Integer)
    active = db.Column(db.String(1),default='Y')
    hospital_id = db.Column(db.Integer,db.ForeignKey('Hospitals.id'))
    slots = db.relationship('Slot',backref='owner')

    def __init__(self,doctor_payload):
        self.name = doctor_payload.get('name')
        self.specality = doctor_payload.get('specality')
        self.experience = doctor_payload.get('experience')
        self.working_Hour = doctor_payload.get('workingHour')
        self.shift_timing = doctor_payload.get('shiftTiming')
        self.rating = doctor_payload.get('rating')

class Slot(db.Model):
    __tablename__ = 'Slot'
    id = db.Column(db.Integer,primary_key=True)
    slot_date = db.Column(db.String(25),nullable = False)
    slot_1 = db.Column(db.Integer)
    slot_2 = db.Column(db.Integer)
    slot_3 = db.Column(db.Integer)
    slot_4 = db.Column(db.Integer)
    slot_5 = db.Column(db.Integer)
    slot_6 = db.Column(db.Integer)
    slot_7 = db.Column(db.Integer)
    slot_8 = db.Column(db.Integer)
    doctor_id = db.Column(db.Integer,db.ForeignKey('Doctors.id'))

    def __init__(self,slot_payload):
        self.slot_date = slot_payload.get('slot_date')
        self.slot_1 = slot_payload.get('firstSlot')
        self.slot_2 = slot_payload.get('secondSlot')
        self.slot_3 = slot_payload.get('thirddSlot')
        self.slot_4 = slot_payload.get('fourthdSlot')
        self.slot_5 = slot_payload.get('fifthSlot')
        self.slot_6 = slot_payload.get('sixSlot')
        self.slot_7 = slot_payload.get('sevenSlot')
        self.slot_8 = slot_payload.get('eightSlot')