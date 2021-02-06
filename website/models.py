from datetime import datetime
from website import db, login_manager
from flask_login import UserMixin




class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    data = db.relationship('Data', backref='datas', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}'"

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20) )
    email = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(60), nullable=False)
    app_name = db.Column(db.String(60), nullable=False)
    url = db.Column(db.String(60), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}','{self.password}','{self.app_name}','{self.url}' "
