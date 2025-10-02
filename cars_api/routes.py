from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select
from schemas import (
    CarRequest,
    CarResponse,
    CarList,
    UserBase,
    Token
)
from database import get_session
from datetime import timedelta
from models import Car, User
from security import (
    get_password_hashed,
    verify_password,
    create_access_token,
    decode_token
)

cars_router = APIRouter(
    prefix='/api/v1/cars',
    tags=['cars'],
    dependencies=[Depends(decode_token)]
)

auth_router = APIRouter(
    prefix='/auth',
    tags=['auth']
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


@auth_router.post(
    path='/register',
    status_code=status.HTTP_201_CREATED
)
def register(user: UserBase, session: Session=Depends(get_session)):
    print(user)
    db_user = session.query(User).filter(User.login == user.login).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Usuário já existe")
    hashed_pw = get_password_hashed(user.password)
    new_user = User(login=user.login, password=hashed_pw)
    session.add(new_user)
    session.commit()
    session.refresh(new_user)

@auth_router.post(
    path='/login',
    status_code=status.HTTP_200_OK,
    response_model=Token
)
def login(user: UserBase, session: Session=Depends(get_session)):
    db_user = session.query(User).filter(User.login == user.login).first()
    if not db_user or not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

    access_token_expires = timedelta(minutes=60)
    token = create_access_token(
        data={"sub": db_user.login}, expires_delta=access_token_expires
    )
    return Token(token=token)