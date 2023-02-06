#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
import os


class City(BaseModel, Base):

    storage_state = os.getenv('HBNB_TYPE_STORAGE')
    if storage_state == 'db':
    """ The city class, contains state ID and name """
        __tablename__ = 'cities'

        name = Column(String(128), nullable=False)
        state_id = Column(String(60), nullable=False, ForeignKey('states.id'))
        places = relationship('place', cascade='all, delete-orphan', backref='cities')
    else:
        name = ''
        state_id = ''