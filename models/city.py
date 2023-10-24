#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel):
    """ The city class, contains state ID and name """
    # Set the table name for this class

    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    # Define the 'state_id' column with constraints and set it as a foreign key
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)

    # Establish a relationship with the State class
    places = relationship("Place", backref="cities", cascade="delete")
