from fastapi import APIRouter

router = APIRouter()


@router.get(path="/call")
def call_elevator():
    return "Elevator is coming"


@router.get(path="/position")
def call_elevator():
    return "Elevator is at floor 2"
