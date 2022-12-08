from fastapi import APIRouter

from routers.currency import router as currency_router
from routers.users import router as user_router

api_router = APIRouter()

api_router.include_router(currency_router)  # /currency
api_router.include_router(user_router)  # /user
