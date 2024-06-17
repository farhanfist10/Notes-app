from flask import Blueprint,render_template,request,flash,redirect,url_for
from werkzeug.security import generate_password_hash,check_password_hash
from .models import User
from . import db
from flask_login import login_user,login_required,logout_user,current_user

auth=Blueprint('auth',__name__)

@auth.route("/login",methods=['GET','POST'])
def login():
    if request.method=='POST':
        email=request.form.get('email')
        password=request.form.get('password')
        
        user=User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password,password):
                flash('Logged in successfully!!!',category='success')
                login_user(user,remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect Password',category='error')
        else:
            flash('Email does not exist.',category='success')        
    return render_template("login.html",user=current_user)

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route("/sign-up",methods=['GET','POST'])
def sign_up():
    if request.method=='POST':
        email=request.form.get('email')
        firstName=request.form.get('firstName')
        password1=request.form.get('password1')
        password2=request.form.get('password2')
        
        user=User.query.filter_by(email=email).first()
        if user:
            flash('Email already exist',category='error')
        elif len(email)<4:
            flash('Email must be more than  4 Characters',category='error')
        elif len(firstName)<2:
            flash('First Name must be more than  2 Characters',category='error')
        elif password1!=password2:
            flash('Password Don\'t match',category='error')
        elif len(password1)<7:
            flash('Password must be more than  7 Characters',category='error')
        else:
            new_User = User(email=email, first_name=firstName, password=generate_password_hash(password1, method='pbkdf2:sha256'))
            db.session.add(new_User)
            db.session.commit()
            login_user(new_User,remember=True)
            flash('Account Created Successfully !!!',category='success')
            return redirect(url_for('views.home'))
    return render_template("sign_up.html",user=current_user)    