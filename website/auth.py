from flask import Blueprint, render_template, flash, redirect, url_for, request
from website.forms import RegistrationForm, LoginForm
from website.models import User
from flask_login import login_user, current_user, logout_user, login_required
from . import db, bcrypt
auth = Blueprint('auth',__name__)

@auth.route('/register', methods=['GET' ,'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == "POST" and form.validate():
        check_username = User.query.filter_by(username=form.username.data).first()
        check_email = User.query.filter_by(username=form.email.data).first()
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        if check_username:
            flash(f'That username is taken. Please choose a different one.', 'danger')
            return render_template('register.html', form=form)
        elif check_email:
            flash(f'That email is taken. Please choose a different one.', 'danger')
            return render_template('register.html', form=form)
        else:
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            user = User(username=form.username.data, email=form.email.data, password=hashed_password)
            db.session.add(user)
            db.session.commit()
            flash(f'Account created for {form.username.data}!', 'success')
            return redirect(url_for('login'))

    return render_template('register.html',form=form)

@auth.route('/login', methods=['GET' ,'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == "POST" and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('views.dashboard'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', form=form)
