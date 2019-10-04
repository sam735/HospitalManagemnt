from flask import Flask
from flask_restful import reqparse, abort, Api
from db import db

from userRegistration.controller import UserRegistration
from userValidation.controller import ValidateUser
from hospital.controller import Hospital

app = Flask(__name__)
app.config.from_pyfile(filename='app.cfg')
db.init_app(app)
api = Api(app)
api.add_resource(UserRegistration,'/api/v1/userRegistration')
api.add_resource(ValidateUser,'/login')
api.add_resource(Hospital,'/api/v1/hospitals')

if __name__ == "__main__":
    app.run(debug=True)