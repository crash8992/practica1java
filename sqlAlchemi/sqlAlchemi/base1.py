from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database01.db', echo=True)

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    edad = Column(Integer)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

nuevo_usuario = Usuario(nombre='John Doe', edad=30)
session.add(nuevo_usuario)
session.commit()

usuarios = session.query(Usuario).all()
for usuario in usuarios:
    print(usuario.nombre, usuario.edad)



