#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String
from models.base_model import Base
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """Represent an Amenity for a MySQL database.
    Inherits from SQLAlchemy and links to MySQL table amenities

    Attributes:
        __tablename__(str): The name of MySQL table to store Amenities
        name(str): Amenity name
        place_amenities(relationship): Place-Amenity Relationship.
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    if storage_type == 'db':
        place_amenities = relationship("Place", secondary="place_amenity",
                                    viewonly=False)
    else:
        name = ""
