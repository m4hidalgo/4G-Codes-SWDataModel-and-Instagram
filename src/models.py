import os
import sys
import enum
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

    def to_dict(self):
        return {}

# PROYECTO 1

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    user_name = Column(String(20), nullable=False)
    first_name = Column(String(250))
    last_name = Column(String(250))
    email = Column(String(250), nullable=False)

class Planet(Base):
    __tablename__ = 'planets'

    id = Column(Integer, primary_key=True)
    planet_name = Column(String(250), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "planet_name": self.planet_name
        }

class Character(Base):
    __tablename__ = 'characters'

    id = Column(Integer, primary_key=True)
    character_name = Column(String(250), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "character_name": self.character_name
        }

class Favorite(Base):
    __tablename__ = 'favorites'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    character_id = Column(Integer, ForeignKey('character.id'))

# PROYECTO 2 

class Follower(Base):
    __tablename__ = 'follower'

    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.id'))
    user_to_id = Column(Integer, ForeignKey('user.id'))

class Post(Base):
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))

class Comment(Base):
    __tablename__ = 'comment'

    id = Column(Integer, primary_key=True)
    comment_text = Column(String(500), nullable=False)
    autor_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))

class MyEnum(enum.Enum):
    video = 'video'
    audio = 'audio'

class Media(Base):
    __tablename__ = 'media'

    id = Column(Integer, primary_key=True)
    type = Column('value', Enum(MyEnum))
    url = Column(String(250), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'))


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
