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
    _password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    createNote = relationship('Task', lazy=True)

    def get_user_by_email (email):
        user = User.query.filter_by(email=email)
        return user

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

    def to_print_task(self):
        return{
            "id":self.id,
            "text":self.text,
            "status":self.status,
            "id_user":self.id_user
        }

class Task(db.Model):
    __tablename__ = 'task'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column (db.String(250),nullable=False)
    status = db.Column (db.Boolean, default=False )
    id_user = db.Column (db.Integer, ForeignKey("user.id"))
    #, back_populates="user")
    