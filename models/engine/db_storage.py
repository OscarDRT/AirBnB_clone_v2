#!/usr/bin/python3
"""DBStorage"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine, MetaData
from models.base_model import Base
from os import getenv


class DBStorage:

    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(getenv("HBNB_MYSQL_USER"),
                                              getenv("HBNB_MYSQL_PWD"),
                                              getenv("HBNB_MYSQL_HOST"),
                                              getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        new_dict = {}
        classes = {"City": City, "Place": Place, "Review": Review,
                   "Amenity": Amenity, "State": State, "User": User}
        if cls is not None:
            if cls in classes:
                see = self.__session.query(classes[cls])
            else:
                see = self.__session.query(cls)
            for instance in see:
                key = instance.__class__.__name__ + "." + instance.id
                new_dict[key] = instance

        if cls is None:
            for clas in classes.keys():
                see = self.__session.query(classes[clas])
                for instance in see:
                    key = instance.__class__.__name__ + "." + instance.id
                    new_dict[key] = instance
        return (new_dict)

    def new(self, obj):
        self.__session.add(obj)
        self.save()

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj is not None:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        Base.metadata.create_all(bind=self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine,
                                 expire_on_commit=False))
        self.__session = Session()

    def close(self):
        self.__session.close()
