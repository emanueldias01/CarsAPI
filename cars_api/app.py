from fastapi import FastAPI
from routes import cars_router

app = FastAPI()

app.include_router(cars_router)