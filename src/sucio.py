main 


from flask_sqlalchemy import SQLAlchemy
import os
import sys
from sqlalchemy import Table, Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)

class Note(Base):
    __tablename__ = 'note'
    id = Column(Integer, primary_key=True)
    text = Column (String(),nullable=False)
    status = Column (Boolean, default=False )
    id_user = Column (Integer, ForeignKey("user.id"))
    createNote = relationship("User",lazy=True  )#, back_populates="user")
    

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }



module


from flask_sqlalchemy import SQLAlchemy
import os
import sys
from sqlalchemy import Table, Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)

class Note(Base):
    __tablename__ = 'note'
    id = Column(Integer, primary_key=True)
    text = Column (String(),nullable=False)
    status = Column (Boolean, default=False )
    id_user = Column (Integer, ForeignKey("user.id"))
    createNote = relationship("User",lazy=True  )#, back_populates="user")
    

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }