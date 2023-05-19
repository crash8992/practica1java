from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# creo la base de datos

engine = create_engine('sqlite:///BaseCB01.db', echo=True)

# base declarativa

Base = declarative_base

# creación clase

class Estudiante(Base):
    __tablename__ = 'estudiantes'
    id = Column(Integer, primary_key=True)
    nombre = Column (String)
    cedula = Column (Integer)
    edad = Column (Integer)
    carrera = Column (String)
    
#creo la tablas con el método 'create_all()', y paso el objeto Engine

Base.metadata.create_all(engine)


    