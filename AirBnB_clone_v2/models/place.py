#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from os import getenv
from sqlalchemy.orm import relationship
import sqlalchemy
import models


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'))
    user_id = Column(String(60), ForeignKey('users.id'))
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    amenities = (
        relationship(
            "Amenity",
            secundary=place_amenity,
            backref='places', viewonly=False
        )
    )

    """ The type of storage used. It can be “file” (using FileStorage) """
    if getenv('HBNB_TYPE_STORAGE') = "db":
        reviews = relationship(
            "Review",
            backref="user",
            cascade="all, delete, delete-orphan"
        )

    """ The type of storage used. db (using DBStorage) """
    else:
        @property
        def reviews_method(self):
            """ Getter reviews """
            list_reviews = []
            for i in list(models.storage.all(Review)):
                if self.id == i.place_id:
                    list_reviews.append(Review)
            return list_reviews

    # Task 10
        place_amenity = Table(
            'place_amenity',
            Base.metadata,
            Column(
                'place_id',
                String(60),
                ForeignKey('places.id'),
                primary_key=True, nullable=False
            ),
            Column(
                'amenity_id',
                String(60),
                ForeignKey('amenities.id'),
                primary_key=True,
                nullable=False
            ),
        )

    @property
    def amenities_linked(self):
        """ Getter amenities """
        amenities_list = []
        for amenity in list(models.storage.all(Amenity).values()):
            if amenity.id in self.amenity_ids:
                amenities_list.append(amenity)
        return amenities_list

    @amenities.setter
    def amenities_linked(self, value):
        if type(value) == Amenity:
            self.amenity_ids.append(value.id)
