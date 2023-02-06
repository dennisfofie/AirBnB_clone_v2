#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
import os

class State(BaseModel, Base):

    storage_state = os.getenv('HBNB_TYPE_STORAGE')

    if storage_state = 'db':
        """ State class """
        __tablename__ = 'states'

        name = Column(String(128), nullable=False)
        cities = relationship('City', cascade='all, delete', backref='states')
    else:
        name= ''
        state_id = ''