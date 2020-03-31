#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from os import environ
from sqlalchemy.orm import relationship
import models
from models.city import City


class State(BaseModel):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

    if environ['HBNB_TYPE_STORAGE'] != 'db':
        @property
        def cities(self):
            '''fileStorage instead of DbStorage between State and City
            '''
            cities = models.storage.all(City)
            relation = []

            for value in cities:
                if city.state_id == self.id:
                    relation.append(value)
            return relation