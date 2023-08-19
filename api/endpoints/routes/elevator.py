from fastapi import APIRouter

router = APIRouter()


@router.post(path="/call")
def call_elevator():
    return "Elevator is coming"
