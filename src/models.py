import os
import sys
from sqlalchemy import Table, Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import exc



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

        #creacion del usuario
    def create_user(self):
        db.session.add(self)
        db.session.commit()
        return self.to_dict

#hacer con metodh y la comprension list 
    def get_all():
        users = User.query.all()
        users_dict = list(map(lambda x: x.to_dict(), users))
        return users_dict
        
#hacer con metodh y la comprension list 

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

    def to_print_task(self):
        return{
            "id":self.id,
            "text":self.text,
            "status":self.status,
            "id_user":self.id_user,
        }

    @classmethod#era por esto tio 
    def get_task(cls):
        to_print_task=Task.query.all()
            
        tasks=cls.query.all()
        return [tasks.to_print_task()for task in tasks]
    @classmethod
    def get_task_user(cls,email):
        to_print_task=Task.query.filter_by(id_user=id_user)
        users=cls.query.all()
        return [user.to_print_task()for user in users]
"""
    @classmethod
    def get_all(cls):
        users=cls.query.all()
        return [user.to_dict()for user in users]

    @classmethod
    def get_by_email(cls,email):
        tasks=cls.query.all()
        return [tasks.to_print_task()for task in tasks]
    """