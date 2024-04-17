from fastapi import APIRouter
from api.routes import tests, user

api_router = APIRouter()

api_router.include_router(tests.router, prefix='/tests', tags=['tests'])
api_router.include_router(user.router, prefix='/user', tags=['user'])