from flask import Blueprint, render_template, flash, redirect, url_for, request
from website.models import Data
from website.forms import PasswordForm
views = Blueprint('views',__name__)


@views.route('/')
def home():
    return render_template('home.html')

@views.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')
@views.route('/create_new_password', methods=['GET' ,'POST'])
def create_new_password():
    form = PasswordForm(request.form)
    if request.method == "POST" and form.validate():
        pass
    return render_template('create_new_password.html', form=form)
