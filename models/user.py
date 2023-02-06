#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os

class User(BaseModel, Base):

   storage_state = os.getenv('HBNB_TYPE_STORAGE')
   if storage_state == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=False)
        last_name = Column(String(128), nullable=False)
        places = relationship('places', cascade='all, delete', backref='users')
        reviews = relationship('reviews', cascade='all, delete', backref='users')
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''