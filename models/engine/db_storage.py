#!/usr/bin/python3
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        ''' initializing our database using our environment variables'''

        USER = os.getenv('HBNB_MYSQL_USER')
        PASSWD = os.getenv('HBNB_MYSQL_PWD')
        HOST = os.getenv('HBNB_MYSQL_HOST')
        DATABASE = os.getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine(f'mysql+mysqldb://{USER}:{PASSWD}@HOST{}/{DATABASE}', pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def new(self, obj):
        ''' adding obj to the session '''
        if obj:
            self.__session.add(obj)

    def save(self):
        ''' save to the database '''
        self.__session.commit()

    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)

    def reload(self):
        ''' reloading from database '''
        relay = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(relay)

