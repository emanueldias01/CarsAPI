from sqlalchemy import Column, Integer, String, Text

from database import Base

class Car(Base):
    __tablename__ = 'cars'

    id = Column('id', Integer, primary_key=True, index=True, autoincrement=True)
    brand = Column('brand', String, nullable=False)
    model = Column('model', String, nullable=False)
    color = Column('color', String, nullable=True)
    factory_year = Column('factory_year', String, nullable=False)
    model_year = Column('model_year', String, nullable=True)
    description = Column('description', Text, nullable=True)