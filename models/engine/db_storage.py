#!/usr/bin/python3
""" This is the engine to the DB storage"""
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from os import environ
from models.city import City
from models.state import State
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from sqlalchemy.orm import scoped_session

class DBstorage:
    """class to store in Database
    """
    __engine = None
    __session = None

    def __init__(self):
        user = environ.get('HBNB_MYSQL_USER')
        passwd = environ.get('HBNB_MYSQL_PWD')
        host = environ.get('HBNB_MYSQL_HOST')
        datab = environ.get('HBNB_MYSQL_DB')
        hbn_env = environ.get('HBNB_ENV')
        self.__engine =create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, passwd, host, datab),
                                      pool_pre_ping=True)
        if hbn_env == 'test':
            Base.metadata.drop_all(self.__engine)
        
    def all(self, cls=None):
        """print all the objects
        """
        classes = ["State", "City", "User", "Place", "Review", "Amenity"]
        new_directory = {}

        if cls is None:
            for request in classes:
                for query in self.__session.query(eval(request)).all():
                    result = type(query).__name__
                    new_directory['{}.{}'.format(result, query.id)] = query
        else:
            for query in self.__session.query(eval(request)).all():
                result = type(query).__name__
                new_directory['{}.{}'.format(result, query.id)] = query
        return new_directory
    
    def new(obj):
        """add the object to the current database session
        """
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session 
        """
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
         """create all tables in the database
         """
         Base.metadata.create_all(self.__engine)
         Session = sessionmaker(bind=self.__engine,
                                expire_on_commit=False)
         session_scoped = scoped_session(Session)
         self.__session = Session()

                                