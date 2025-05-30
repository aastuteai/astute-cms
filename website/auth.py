from flask import Blueprint, render_template, request, flash,redirect,url_for
from .models import User
from . import db
from flask_login import login_user, login_required, logout_user, current_user
auth = Blueprint('auth', __name__)

@auth.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user:
            if password==user.password:
                login_user(user,remember=True)
                flash("Logged in!",category='sucesss')
                return redirect(url_for('views.home'))
            else:
                flash("Incorrect Credentials")
        else:
            flash("User Does not Exist")
    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

# @auth.route('/sign-up',methods=['GET','POST'])
# def sign_up():
#     if request.method == 'POST':
#         email=request.form.get('email')
#         username=request.form.get('username')
#         password1=request.form.get('password')
#         password2=request.form.get('confirm-password')
#         user = User.query.filter_by(email=email).first()
#         if user:
#             flash('Email already registered.', category='error')
#         elif not email.endswith('@astute.ai'):
#             flash('Permission Denied', category='error')
#         elif len(email) < 4:
#             flash('Email must be greater than 3 characters.', category='error')
#         elif len(username) < 2:
#             flash('First name must be greater than 1 character.', category='error')
#         elif password1 != password2:
#             flash('Passwords don\'t match.', category='error')
#         elif len(password1) < 7:
#             flash('Password must be at least 7 characters.', category='error')
#         else:
#             new_user = User(email=email,username=username,password=password1)
#             db.session.add(new_user)
#             db.session.commit()
#             flash('Account Created!', category='success')
#             login_user(new_user,remember=True)
#             return redirect(url_for('views.home'))

#     return render_template("sign_up.html", user=current_user)
