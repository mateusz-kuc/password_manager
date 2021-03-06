from wtforms import Form, StringField, BooleanField , PasswordField, IntegerField, SelectField, validators

class RegistrationForm(Form):
    name = StringField('Name',[validators.Length(min=1,max=50)])
    username = StringField('Username',[validators.Length(min=4,max=25)])
    email = StringField('Email',[validators.Length(min=6,max=50)])
    password = PasswordField('Password',[validators.DataRequired(),
    validators.EqualTo('confirm',message="Passwords do not match")
    ])

    confirm = PasswordField('Confirm Password')





class LoginForm(Form):
    email = StringField('Email',[validators.Length(min=6,max=50)])
    password = PasswordField('Password',[validators.DataRequired()])
    remember = BooleanField('Remember Me')

class PasswordForm(Form):
    name = StringField('Aplication/Site Name',[validators.Length(min=6,max=50)])
    url = StringField('Aplication/Site URL',[validators.Length(min=6,max=50)])
    email = StringField('Email',[validators.Length(min=6,max=50)])
    username = StringField('username (If necessarily)')
    length = SelectField('Password length',choices=[('8', '8'), ('10', '10'), ('12','12'), ('14','14'),('16','16')]) # Maybe select field??
