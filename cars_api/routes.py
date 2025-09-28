from fastapi import APIRouter

cars_router = APIRouter(prefix='/api/v1/cars', tags=['cars'])

@cars_router.get('/')
def get_cars():
    return {'cars' : [
            {'id' : 1, 'model' : 'onix'},
            {'id' : 2, 'model' : 'opala'},
            {'id' : 3, 'model' : 'mercedes'}
        ]
    }