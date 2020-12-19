#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship


class Review(BaseModel, Base):
    """ Review classto store review information """
    __tablename__: 'reviews'
    text = Column(String(1024), nullable=True)
    place_id = Column(String(60), nullable=False, ForeignKey('place.id'))
    user_id = Column(String(60), nullable=False, ForeignKey('users.id'))
