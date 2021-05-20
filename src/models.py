import os
import sys
from sqlalchemy import Table, Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    createNote = relationship('Task')

    def __repr__(self):
        return '<User %r>' % self.username


    def to_dict(self):
        return {
            "id": self.id,
            "email": self.email,

            # do not serialize the password, its a security breach
        }


    def get_all():
        users = User.query.all()
        users_dict = list(map(lambda x: x.to_dict(), users))
        return users_dict
        
        
    def get_by_email(email):
        user = User.query.filter_by(email=email)
        user_dict = list(map(lambda x: x.to_dict(), user))
        return user_dict

  

class Task(db.Model):
    __tablename__ = 'task'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column (db.String(250),nullable=False)
    status = db.Column (db.Boolean, default=False )
    id_user = db.Column (db.Integer, ForeignKey("user.id"))
    #, back_populates="user")

    def get_task():
        task_dict=Task.query.all()
        task_dict = list(map(lambda x: x.to_dict(), Task))
        return task_dict

    def get_task_user(id_user):
        task_user=Task.query.filter_by(id_user=1)
        task_user = list(map(lambda x: x.to_dict(), task_user))
        return task_user


    def to_print_task(self):
        return{
            "id":self.id,
            "text":self.text,
            "status":self.status,
            "id_user":self.id_user,
        }