from fastapi import FastAPI
from routes import cars_router, auth_router

app = FastAPI()

app.include_router(cars_router)
app.include_router(auth_router)