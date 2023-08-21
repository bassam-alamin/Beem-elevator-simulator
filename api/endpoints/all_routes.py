from fastapi import APIRouter

from api.endpoints.routes import elevator

api_router = APIRouter()

api_router.include_router(elevator.router, prefix="/elevator", tags=["Elevator"])
