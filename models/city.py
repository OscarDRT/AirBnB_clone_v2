#!/usr/bin/python3
"""This is the city class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from os import environ
from sqlalchemy.orm import relationship
import models

class City(BaseModel):
    """This is the class for City
    Attributes:
        state_id: The state id
        name: input name
    """
    __tablename__ = 'cities'
    state_id = Column(String(60), ForeignKey('state.id'), nullable=False)
    name = Column(String(128), nullable=False)
    place = relationship("Place", backref="cities", cascade="all, delete" )
