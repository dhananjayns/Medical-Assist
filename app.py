from myproject import app,db,mongo
from flask import render_template, redirect, request, url_for, flash,abort
from flask_login import login_user,login_required,logout_user,current_user
from myproject.models import User,Disease,Doctors,reviews
from myproject.forms import LoginForm, RegistrationForm,SymptomForm,disease_form,DoctorForm,FindDoctor,AdminForm1,AdminForm2
from werkzeug.security import generate_password_hash, check_password_hash
import os,datetime
import re
from wtforms.validators import ValidationError
from gtts import gTTS
language = 'en'
result=None;health=None;status=None;flag=None;
Disease_type=[]
Disease_type.append('0')


@app.route('/')
def home():
    if current_user.is_authenticated:

        mongouser =list( mongo.db.user.find({'username':current_user.username}))
        return render_template('welcome_user.html',mongouser=mongouser)
    else:
        return render_template('home.html')

@app.route('/admin', methods=['GET', 'POST'])
@login_required
def admin():
    form=AdminForm1()
    form1=AdminForm2()
    if form.validate_on_submit():
        user = Doctors(doc_name=form.doc_name.data,
                doc_type=form.doc_type.data,
                doc_location=form.doc_location.data,
                doc_hospital=form.doc_hospital.data)
        db.session.add(user)
        db.session.commit()
        flash('Data entry successful and Session committed.')

        mytext = "Admin  !!"+'.Data entry successful and Session committed.!'
        myobj = gTTS(text=mytext, lang=language, slow=False)
        myobj.save("welcome.mp3")
        os.system("mpg123 welcome.mp3")
        return render_template('admin.html',form=form,form1=form1)
    elif form1.validate_on_submit():
        user = Disease(disease_name=form1.disease_name.data,
                prevention=form1.prevention.data,
                cause=form1.cause.data,
                cure=form1.cure.data,
                doc_type=form1.doc_type.data,
                age_group=form1.age_group.data)
        db.session.add(user)
        db.session.commit()
        flash('Data entry successful and Session committed.')

        mytext = "Admin  !!"+'.Data entry successful and Session committed.!'
        myobj = gTTS(text=mytext, lang=language, slow=False)
        myobj.save("welcome.mp3")
        os.system("mpg123 welcome.mp3")
        return render_template('admin.html',form1=form1,form=form)
    return render_template('admin.html',form=form,form1=form1)



@app.route('/diseases',methods=['GET', 'POST'])
@login_required
def diseases():
    result=None

    form = disease_form()

    if form.validate_on_submit():
        # print(form.age_group.data)
        result=Disease.query.filter_by(age_group=form.age_group.data)

        return render_template('diseases.html',form=form,result=result)

    return render_template('diseases.html',form=form,result=result)

@app.route('/finddoctor',methods=['GET', 'POST'])
@login_required
def finddoctor():
    result=None
    form = FindDoctor()
    if form.validate_on_submit():
        result=Doctors.query.filter_by(doc_type=form.doc_type.data,doc_location=current_user.location)
        return render_template('finddoctor.html',form=form,result=result)
    return render_template('finddoctor.html',form=form,result=result)

@app.route('/doctor_recommend',methods=['GET', 'POST'])
@login_required
def doctor_recommend():

    return render_template('doctor_recommend.html')

@app.route('/doctors',methods=['GET','POST'])
@login_required
def doctors():
    form=DoctorForm()
    result1=[]
    result=Doctors.query.filter_by(doc_type=Disease_type[0],doc_location=current_user.location).first()
    if result:

        mytext = 'Your nearest '+result.doc_type+"  is Dr."+result.doc_name+".  Here are his details:."
        myobj = gTTS(text=mytext, lang=language, slow=False)
        myobj.save("welcome.mp3")
        os.system("mpg123 welcome.mp3")

        result1=reviews.query.filter_by(doc_name=result.doc_name)
    if form.validate_on_submit():
        d=datetime.datetime.now()
        user = reviews(doc_name=result.doc_name,username=current_user.username,
                doc_review=form.doc_review.data,
                rating=form.rating.data,date=d)
        db.session.add(user)
        db.session.commit()
        flash('Review Submitted Successfully!')

        mytext = 'Well Done !!  Your Review has been Submitted Successfully!'
        myobj = gTTS(text=mytext, lang=language, slow=False)
        myobj.save("welcome.mp3")
        os.system("mpg123 welcome.mp3")

        if result:
            result1=reviews.query.filter_by(doc_name=result.doc_name)
        return render_template('doctor.html',form=form,result=result,result1=result1)
    return render_template('doctor.html',form=form,result=result,result1=result1)

@app.route('/symptoms',methods=['GET', 'POST'])
@login_required
def symptoms():
    form=SymptomForm()
    count=[]

    if form.validate_on_submit():
        i=0
        while i<3:
            count.append(0);
            i+=1

        if form.c1.data:
            count[2]+=1
        if form.c2.data:
            count[2]+=1
        if form.c3.data:
            count[2]+=1
        if form.c4.data:
            count[2]+=1
        if form.c5.data:
            count[2]+=1
        if form.c6.data:
            count[2]+=1

        if form.f1.data:
            count[1]+=2
        if form.f2.data:
            count[1]+=2
        if form.f3.data:
            count[1]+=2
        if form.f4.data:
            count[1]+=2
        if form.f5.data:
            count[1]+=2

        if form.d1.data:
            count[0]+=4
        if form.d2.data:
            count[0]+=4
        if form.d3.data:
            count[0]+=4
        if form.d4.data:
            count[0]+=4
        if form.d5.data:
            count[0]+=4

        max_count=max(count)
        total_count=0
        for i in range(0,3):
            total_count+=count[i]
        if total_count==0:
            flash('Please select some Symptoms')

            mytext = 'Please select some Symptoms'
            myobj = gTTS(text=mytext, lang=language, slow=False)
            myobj.save("welcome.mp3")
            os.system("mpg123 welcome.mp3")

            redirect(url_for('symptoms'))

        else:

            m_index=count.index(max_count)

            if m_index==2:
                result=Disease.query.filter_by(disease_name='Cold').first()
            elif m_index==1:
                result=Disease.query.filter_by(disease_name='Fever').first()
            elif m_index==0:
                result=Disease.query.filter_by(disease_name='Dengue').first()
            doc=mongo.db.user.insert_one({'username':current_user.username,'disease_name':result.disease_name,'intensity':total_count,'date':datetime.datetime.now()})
            # print(doc)
            status=None
            health=abs(total_count*100//36)
            # print(health)
            if health in range(1,11):
                status="Be Alert"
            elif health in range(11,25):
                status="Not Satisfactory"
            elif health in range(25,39):
                status="Average"
            elif health in range(39,53):
                status="Bad"
            elif health in range(53,67):
                status="Very Bad"
            elif health in range(67,81):
                status="Alarming"
            elif health in range(81,101):
                status="Extremely Dangerous"
            Disease_type[0]=result.doc_type
            # print(count[0],count[1],count[2],m_index,result)
            # print(Disease_type[0],current_user.location)

            flag=form.read.data
            if form.read.data:

                mytext = "hello  "+current_user.username+",  your health status is  "+status+"   .   Health Deterioration level is  "+str(health)+\
                "%.   Identified disease is,"+result.disease_name+"   .     Here are few ways of prevention  "+result.prevention+".  Causes are,  "+\
                result.cause+"   .   Here are some home remedies available,  "+result.cure+"."

                if max_count>=3 or total_count>=5:
                    mytext+=".   Med Assist Highly recommends you to visit a doctor.   Preferably a  "+\
                    result.doc_type+".   Do you want to locate "+result.doc_type+"  near your location?.   Click the 'Locate doctors nearby' button below."
                # mytext="hello i am working fine"
                myobj = gTTS(text=mytext, lang=language, slow=False)
                myobj.save("welcome.mp3")
                os.system("mpg123 welcome.mp3")
            return render_template('doctor_recommend.html',result=result,max_count=max_count,total_count=total_count,health=health,status=status)

    return render_template('symptoms.html',form=form)


@app.route('/welcome', methods=['GET', 'POST'])
@login_required
def welcome_user():

    if True:
        mongouser =list( mongo.db.user.find({'username':current_user.username}))
        # print(mongouser)
        return render_template('welcome_user.html',mongouser=mongouser)

    return render_template('welcome_user.html',mongouser=mongouser)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You logged out!')

    mytext = '  You logged out!'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("welcome.mp3")
    os.system("mpg123 welcome.mp3")

    return redirect(url_for('home'))


@app.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()
    if form.validate_on_submit():
        # Grab the user from our User Models table
        user = User.query.filter_by(email=form.email.data).first()

        # Check that the user was supplied and the password is right
        # The verify_password method comes from the User object
        # https://stackoverflow.com/questions/2209755/python-operation-vs-is-not

        if user is not None and user.check_password(form.password.data):
            #Log in the user

            login_user(user)
            flash('Logged in successfully.')

            mytext = "Welcome to Med Assist "+current_user.username+'.       Logged in successfully.'
            myobj = gTTS(text=mytext, lang=language, slow=False)
            myobj.save("welcome.mp3")
            os.system("mpg123 welcome.mp3")

            # If a user was trying to visit a page that requires a login
            # flask saves that URL as 'next'.
            next = request.args.get('next')

            # So let's now check if that next exists, otherwise we'll go to
            # the welcome page.
            if next == None or not next[0]=='/':

                mongouser =list( mongo.db.user.find({'username':current_user.username}))
                return render_template('welcome_user.html',mongouser=mongouser)

            return redirect(next)


    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()


    if form.validate_on_submit():

        # # Check if not None for that user email!
        # if User.query.filter_by(email=form.email.data).first():
        #     raise ValidationError('Your email has been registered already!')
        #     #return redirect(url_for('register'))
        #     flag=False
        #
        #
        # # Check if not None for that username!
        # if User.query.filter_by(username=form.username.data).first():
        #     raise ValidationError('Sorry, that username is taken!')
        #     #return redirect(url_for('register'))
        #     flag=False
        #
        # if flag:
        user = User(email=form.email.data,
                username=form.username.data,
                password=form.password.data,
                location=form.location.data)
        db.session.add(user)
        db.session.commit()
        flash('Thanks for registering! Now you can login!')

        mytext = "Welcome to Med Assist!"+'.Thanks for registering! Now you can login!'
        myobj = gTTS(text=mytext, lang=language, slow=False)
        myobj.save("welcome.mp3")
        os.system("mpg123 welcome.mp3")

        return redirect(url_for('login'))


    return render_template('register.html', form=form)

if __name__ == '__main__':
    # ,debug=True,port=5001,host="192.168.1.101"
    app.run(debug=True,host="127.0.0.1",port=5000)
