#!/usr/bin/python3
"""Defines State class."""
import models
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv

class State(BaseModel, Base):
    """Represents a state for MySQL database.

    Inherits from SQLAlchemy Base and links to MySQL table states.

    Attributes:
        __tablename__ (str): The name of the MySQL table to store States.
        name (sqlalchemy String): The name of the state.
        cities (sqlalchemy relationship): The State-City relationship.
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City",  backref="state", cascade="all, delete")
    else:
        @property
        def cities(self):
            """Get a list of City instances with
            state_id equals to current State.id.

            This is getter attribute for FileStrorage
                relationship between State and City.
            """
            city_list = []
            for city in models.storage.all(City).values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list












if models.storage_t != "db":
        @property
        def cities(self):
            """getter for list of city instances related to state"""
            city_list = []
            all_cities = models.storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
