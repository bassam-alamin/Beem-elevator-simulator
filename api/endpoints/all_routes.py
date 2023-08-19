from fastapi import APIRouter

from api.endpoints.routes import elevator

api_responses = {
    404: {"description": "Object Not Found"},
    422: {"description": "Validation Error"},
    500: {"description": "Internal Server Error"},
}

api_router = APIRouter(
    responses=api_responses,
)

api_router.include_router(elevator.router, prefix="/elevator", tags=["Elevator"])
