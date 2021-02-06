from flask import Blueprint, render_template, flash, redirect, url_for, request
from website.models import Data
from website.forms import PasswordForm
from flask_login import current_user, login_required
from . import db
from website.models import User, Data
import random
import pyperclip
def password_create(length):
    created_password = ''
    ALPHABET = ('abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTYVWXYZ', '0123456789', '(,._-*~"<>/|!@#$%^&)+=')
    for i in range(0,length):
        n = random.randint(0,len(ALPHABET)-1)
        symbol = ALPHABET[n]
        n = random.randint(0,len(symbol)-1)
        created_password += symbol[n]

    return created_password




views = Blueprint('views',__name__)

@views.route('/')
def home():
    return render_template('home.html')

@login_required
@views.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')
@views.route('/create_new_password', methods=['GET' ,'POST'])
def create_new_password():
    form = PasswordForm(request.form)
    if request.method == "POST" and form.validate():
        created_password = password_create(form.length.data)
        pyperclip.copy(created_password)
        new_password = Data(username=form.username.data,email=form.email.data,password=created_password,app_name=form.name.data,url=form.url.data,user_id=current_user.id)
        db.session.add(new_password)
        db.session.commit()
        flash(f'You generate new password for {form.name.data}, and it is {created_password} ', 'success')
        return redirect(url_for("views.dashboard"))
    return render_template('create_new_password.html', form=form)

@login_required
@views.route('/search_password', methods=['GET' ,'POST'])
def search_password():

    if request.method == "POST":
        print("Działa")
        print(request.form['name'])
        user = User.query.filter_by(username=current_user.username).first_or_404()
        search = Data.query.filter_by(datas=user, app_name=request.form['name'])

        return render_template('search_password.html',search=search)


    return render_template('search_password.html')
