from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,StringField,TextAreaField,SelectField,BooleanField,IntegerField
from wtforms.validators import DataRequired,Email,EqualTo,Length
from wtforms import ValidationError
from myproject import app,db
from flask import flash,abort

from myproject.models import User,Disease,Doctors,reviews


import os,datetime
import re
from wtforms.validators import ValidationError
user=[]
user.append('0')
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()],render_kw={"placeholder":"E-mail Here"})
    password = PasswordField('Password', validators=[DataRequired()],render_kw={"placeholder":"Password"})
    submit = SubmitField('Log In')

    def validate_email(self, field):
        # Check if not None for that user email!
        user[0]=User.query.filter_by(email=field.data).first()

        if user[0]==None:
            flash('!Email not registered! Please Register to Login!!')
            # raise ValidationError('Your email is not registered!')

    def validate_password(self,field):
        if user[0]:
            if user[0].check_password(field.data)==False:
                raise ValidationError('Password Incorrect!!')





class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()],render_kw={"placeholder":"E-mail Here"})
    username = StringField('Username', validators=[DataRequired(),Length(min=4,max=32)],render_kw={"placeholder":"Username"})
    password = PasswordField('Password', validators=[DataRequired(),Length(min=4,max=32), EqualTo('pass_confirm', message='Passwords Must Match!')],render_kw={"placeholder":"Password"})
    pass_confirm = PasswordField('Confirm password', validators=[DataRequired(),Length(min=4,max=32)],render_kw={"placeholder":"Re-Enter Password"})
    location=SelectField('Choose Your Nearest Location',choices=[('Hebbal','Hebbal'),
                                        ('J P Nagar','J P Nagar'),
                                        ('Shivaji Nagar','Shivaji Nagar'),
                                        ('Kengeri','Kengeri'),
                                        ('Wilson Garden','Wilson Garden')])
    submit = SubmitField('Register!')

    def validate_email(self, field):
        # Check if not None for that user email!
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Your email has been registered already!')

    def validate_username(self, field):
        # Check if not None for that username!
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Sorry, that username is taken!')
    def validate_password(self,field):
        if not re.match(r"^(?=.*[\d])(?=.*[A-Z])(?=.*[a-z])(?=.*[@#$])[\w\d@#$]{6,12}$",field.data):
            raise ValidationError("Password must contain 1 Upper case letter,atleast 1 numerical digit and a special character")

class AdminForm1(FlaskForm):
    doc_name = StringField('Doctor Name', validators=[DataRequired(),Length(min=4,max=32)],render_kw={"placeholder":"Doctor Name"})
    doc_type=SelectField('Doctor Type',choices=[('Physician','Physician'),
                                        ('ENT','ENT'),
                                        ('Orthopedic','Orthopedic'),
                                        ('Psychiatrist','Psychiatrist'),
                                        ('Pediatrician','Pediatrician')])
    doc_location=SelectField('Choose Your Nearest Location',choices=[('Hebbal','Hebbal'),
                                        ('J P Nagar','J P Nagar'),
                                        ('Shivaji Nagar','Shivaji Nagar'),
                                        ('Kengeri','Kengeri'),
                                        ('Wilson Garden','Wilson Garden')])
    doc_hospital = StringField('Hospital Name', validators=[DataRequired(),Length(min=4,max=32)],render_kw={"placeholder":"Hospital"})
    submit=SubmitField('Submit')

class AdminForm2(FlaskForm):
    disease_name = StringField('Disease Name', validators=[DataRequired(),Length(min=4,max=32)],render_kw={"placeholder":"Disease Name"})
    prevention = StringField('Prevention', validators=[DataRequired(),Length(min=4,max=32)],render_kw={"placeholder":"Prevention"})
    cause = StringField('Causes', validators=[DataRequired(),Length(min=4,max=32)],render_kw={"placeholder":"Causes"})
    cure= StringField('Cures', validators=[DataRequired(),Length(min=4,max=32)],render_kw={"placeholder":"Cures"})
    doc_type=SelectField('Doctor Type',choices=[('Physician','Physician'),
                                        ('ENT','ENT'),
                                        ('Orthopedic','Orthopedic'),
                                        ('Psychiatrist','Psychiatrist'),
                                        ('Pediatrician','Pediatrician')])
    age_group= SelectField('Age Group',choices=[('Common','Common'),
                                            ('Children','Children'),
                                            ('20-50','20-50'),
                                            ('Above 50','Above 50')])


class SymptomForm(FlaskForm):
    read=BooleanField('Read out the result after submit')
    c1=BooleanField('Runny or stuffy nose')
    c2=BooleanField('Sore throat')
    c3=BooleanField('Congestion')
    c4=BooleanField('Sneezing')
    c5=BooleanField('A mild headache and Slight body aches')
    c6=BooleanField('Watery Eyes')
    f1=BooleanField('Skin flushing or hot skin')
    f2=BooleanField('Rapid heart rate and/or palpitations')
    f3=BooleanField('Excessive sweating and Aching muscles')
    f4=BooleanField('Shivering, shaking, and chills')
    f5=BooleanField('Temperature greater than 100.4 F')
    d1=BooleanField('Sudden, high fever and Severe abdominal pain')
    d2=BooleanField('Severe headaches,Bleeding from your gums or nose')
    d3=BooleanField('Skin rash, which appears two to five days after the onset of fever')
    d4=BooleanField('Nausea or Vomiting and Fatigue')
    d5=BooleanField('Pain behind the eyes')

    submit=SubmitField('Submit Symptoms')

class FindDoctor(FlaskForm):
    doc_type=SelectField('Doctor Type',choices=[('Physician','Physician'),
                                        ('ENT','ENT'),
                                        ('Orthopedic','Orthopedic'),
                                        ('Psychiatrist','Psychiatrist'),
                                        ('Pediatrician','Pediatrician')])
    submit = SubmitField('Search Doctors')

class DoctorForm(FlaskForm):
    # message='Follow Instructions and Enter the Rating!!'
    rating=IntegerField('Rating',validators=[DataRequired()],render_kw={"placeholder":"Rate between 1 to 5"})
    doc_review=TextAreaField('Something More?',render_kw={"placeholder":"Enter Text Here"})
    submit=SubmitField('Submit Feedback')
    def validate_rating(self, field):
        # Check if not None for that user email!
        if field.data>5 or  field.data<1:
            raise ValidationError('Please Rate between 1 to 5')

class disease_form(FlaskForm):
    age_group= SelectField('Age Group',choices=[('Common','Common'),
                                            ('Children','Children'),
                                            ('20-50','20-50'),
                                            ('Above 50','Above 50')])
    submit = SubmitField('Search Diseases')
