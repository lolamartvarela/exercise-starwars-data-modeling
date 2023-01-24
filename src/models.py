import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer)
    nombre = Column(String(250), nullable=False)
    apellido = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    favoritos_id = Column(Integer, ForeignKey('favoritos.id'))

class Favoritos(Base):
    __tablename__ = 'favoritos'
    id = Column(Integer, primary_key=True)
    favoritos_id = Column(Integer)
    personajes_id = Column(Integer, ForeignKey('personajes.id'))
    planetas_id = Column(Integer, ForeignKey('planetas.id'))
    vehiculos_id = Column(Integer, ForeignKey('vehiculos.id'))

class Personajes(Base):
    __tablename__ = 'personajes'
    id = Column(Integer, primary_key=True)
    perosnajes_id = Column(Integer)
    name = Column(String(250))
    gender = Column(String(250))
    skin_color = Column(String(250))
    eye_color = Column(String(250))

class Planetas(Base):
    __tablename__ = 'planetas'
    id = Column(Integer, primary_key=True)
    planetas_id = Column(Integer)
    name = Column(String(250))
    gravity = Column(String(250))
    climate = Column(String(250))
    terrain = Column(String(250))

class Vehiculos(Base):
    __tablename__ = 'vehiculos'
    id = Column(Integer, primary_key=True)
    vehiculos_id = Column(Integer)
    model = Column(String(250))
    manufacturer = Column(String(250))
    length = Column(String(250))
    crew = Column(String(250))


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
