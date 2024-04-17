from fastapi import APIRouter
from api.routes import tests

api_router = APIRouter()

api_router.include_router(tests.router, prefix='/tests', tags=['tests'])