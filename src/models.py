from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, Column , Integer , Table , ForeignKey
from sqlalchemy.orm import Mapped, mapped_column , relationship

db = SQLAlchemy()
favorite_planet=db.Table(
    "favorite_planet",
    Column("user_id",Integer, ForeignKey("user.id"), primary_key=True),
    Column("planet_id",Integer, ForeignKey("planet.id"),primary_key=True)
)
favorite_character=db.Table(
    "favorite_character",
    Column("user_id",Integer, ForeignKey("user.id"), primary_key=True),
    Column("character_id",Integer, ForeignKey("character.id"),primary_key=True)
)

class User(db.Model):
    _tablename_ ="user"
    id= Column(Integer , primary_key=True)
    email= Column(String(120) , unique=True, nullable=False)
    favorite_planet = relationship("Planet", secondary = favorite_planet)
    favorite_character = relationship("Character", secondary = favorite_character)

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "favorite_planet": [item.serialize() for item in self.favorite_planet],
            "favorite_character": [item.serialize() for item in self.favorite_character]
            # do not serialize the password, its a security breach
        }

class Planet(db.Model):
    id= Column(Integer , primary_key=True)
    name = Column(String(120), unique=False, nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            # do not serialize the password, its a security breach
        }
    
class Character(db.Model):
    id= Column(Integer , primary_key=True)
    name = Column(String(120), unique=False, nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            # do not serialize the password, its a security breach
        }    