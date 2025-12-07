from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(150), nullable= False)
    email = db.Column(db.String(150), nullable= False, unique= True)
    password = db.Column(db.String(150), nullable= False)
    task = db.relationship('Task', back_populates='owner')

class Task(db.Model):
    task_id = db.Column(db.Integer, primary_key= True)
    task_name = db.Column(db.String(150), nullable= False)
    task_desc = db.Column(db.String(1500))
    com_date = db.Column(db.DateTime, nullable= False)
    task_priority = db.Column(db.String(150))
    category = db.Column(db.String(100), default='no category')
    relation = db.Column(db.Integer,db.ForeignKey('user.id'), nullable= False)
    owner = db.relationship('User', back_populates='task')