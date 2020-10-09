from myproject import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin,current_user
import os,datetime
import re
# By inheriting the UserMixin we get access to a lot of built-in attributes
# which we will be able to call in our views!
# is_authenticated()
# is_active()
# is_anonymous()
# get_id()


# The user_loader decorator allows flask-login to load the current user
# and grab their id.
@login_manager.user_loader
def load_user(user_id):

    return User.query.get(user_id)

class User(UserMixin,db.Model):

    # Create a table in the db
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(64), unique=True, nullable=False)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    location=db.Column(db.String(64))

    def __init__(self, email, username, password,location):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)
        # self.password_hash = password
        self.location = location

    def check_password(self,password):
        # https://stackoverflow.com/questions/23432478/flask-generate-password-hash-not-constant-output
        # if password==self.password_hash:
        #     return True
        # else:
        #     return False
        return check_password_hash(self.password_hash,password)
class Disease(UserMixin,db.Model):


    __tablename__ = 'Disease'

    id = db.Column(db.Integer, primary_key = True)
    disease_name = db.Column(db.String(64), unique=True,nullable=False)
    prevention = db.Column(db.String, nullable=False)
    cause = db.Column(db.String)
    cure =db.Column(db.String)
    doc_type=db.Column(db.String,nullable=False)
    age_group=db.Column(db.Integer,nullable=False)

    def __init__(self, disease_name, prevention, cause,cure,doc_type,age_group):
        self.disease_name = disease_name
        self.prevention = prevention
        self.cause = cause
        self.cure = cure
        self.doc_type=doc_type
        self.age_group=age_group

class Doctors(db.Model):
    __tablename__ = 'Doctors'
    id = db.Column(db.Integer,primary_key=True)
    doc_name=db.Column(db.String,nullable=False)
    doc_type=db.Column(db.String,nullable=False)
    doc_location=db.Column(db.String,nullable=False)
    doc_hospital=db.Column(db.String)

    def __init__(self, doc_name, doc_type, doc_location,doc_hospital):
        self.doc_name = doc_name
        self.doc_type = doc_type
        self.doc_location = doc_location
        self.doc_hospital = doc_hospital

class Symptoms(db.Model):
    __tablename__ = 'symptoms'
    disease_id = db.Column(db.Integer,primary_key=True)
    symptom_name=db.Column(db.String,primary_key=True)


    def __init__(self, disease_id,symptom_name):
        self.disease_id = disease_id
        self.symptom_name = symptom_name


class reviews(db.Model):
    __tablename__='reviews'
    id=db.Column(db.Integer,primary_key=True)
    doc_name=db.Column(db.String)
    username=db.Column(db.String)
    rating=db.Column(db.Integer)
    doc_review=db.Column(db.String)
    date=db.Column(db.DateTime,default=datetime.datetime.now())

    def __init__(self,doc_name,username,rating,doc_review,date):
        self.doc_name=doc_name
        self.username=username
        self.rating = rating
        self.doc_review = doc_review
        self.date=date
