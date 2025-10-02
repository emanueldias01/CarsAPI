from sqlalchemy import Column, Integer, String, Text

from database import Base

class Car(Base):
    __tablename__ = 'cars'

    id = Column('id', Integer, primary_key=True, index=True, autoincrement=True)
    brand = Column('brand', String, nullable=False)
    model = Column('model', String, nullable=False)
    color = Column('color', String, nullable=True)
    factory_year = Column('factory_year', Integer, nullable=False)
    model_year = Column('model_year', Integer, nullable=True)
    description = Column('description', Text, nullable=True)

class User(Base):
    __tablename__='tab_users'
    id = Column('id', Integer, primary_key=True, index=True, autoincrement=True)
    login = Column('login', String, unique=True, nullable=False)
    password = Column('password', String, nullable=False)