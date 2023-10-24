#!/usr/bin/python3

""" State Module for HBNB project """

from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel):
    """ State class """

    # Define the table name
    __tablename__ = "states"

    # Define a column for the 'name' attribute
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state",
        cascade="all, delete-orphan")

    @property
    def cities(self):
        """ Getter attribute for cities """
        from models import storage
        city_list = []
        for city in storage.all("City").values():
            if city.state_id == self.id:
                city_list.append(city)
        return city_list


storage = FileStorage()
storage.reload()
