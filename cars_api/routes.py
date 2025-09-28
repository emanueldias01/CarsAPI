from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select
from schemas import (
    CarRequest,
    CarResponse,
    CarList
)
from database import get_session
from models import Car

cars_router = APIRouter(
    prefix='/api/v1/cars',
    tags=['cars']
)

@cars_router.post(
        path='/',
        response_model=CarResponse,
        status_code=status.HTTP_201_CREATED
)
def create_car(car: CarRequest,session: Session = Depends(get_session)):
    car = Car(**car.model_dump())
    session.add(car)
    session.commit()
    session.refresh(car)
    return car

@cars_router.get(
    path='/',
    response_model=CarList,
    status_code=status.HTTP_200_OK
)
def list_cars(session: Session=Depends(get_session), offset: int=0, limit: int=100):
    cars = session.scalars(select(Car)).all()
    return {'cars' : cars}

@cars_router.get(
    path='/{car_id}',
    response_model=CarResponse,
    status_code = status.HTTP_200_OK
)
def car_by_id(car_id: int, session: Session=Depends(get_session)):
    car = session.get(Car, car_id)
    if not car:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='car not found')
    return car

@cars_router.put(
    path='/{car_id}',
    response_model=CarResponse,
    status_code=status.HTTP_200_OK
)
def uptade_car(car_id: int, car_updated: CarRequest, session: Session=Depends(get_session)):
    car = session.get(Car, car_id)
    if not car:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='car not found')
    
    for field, value in car_updated.model_dump().items():
        setattr(car, field, value)

    session.commit()
    session.refresh(car)
    return car

@cars_router.delete(
    path='/{car_id}',
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_car_by_id(car_id: int, session: Session=Depends(get_session)):
    car = session.get(Car, car_id)
    if not car:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='car not found')
    session.delete(car)
    session.commit()
