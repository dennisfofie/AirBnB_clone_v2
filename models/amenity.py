#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
import os
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    storage_state = os.getenv('HBNB_TYPE_STORAGE')

    if storage_state == 'db':
        __tablename__ = 'amenties'

        name = Column(String(128), nullable=False)
        place_amenities = Column