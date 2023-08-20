from fastapi import APIRouter
from starlette.background import BackgroundTasks

from api.domain.elevator import elevators, move_elevators
from api.endpoints.schemas.elevator_schema import CallRequestSchema
from api.services.handlers.elevator_handler import ElevatorController

router = APIRouter()


@router.post(path="/call")
def call_elevator(details: CallRequestSchema, background_tasks: BackgroundTasks):
    elevator_controller = ElevatorController(
        elevator_id=details.elevator_id, to_floor=details.to_floor,
        from_floor=details.from_floor
    )
    elevator = elevator_controller.call_elevator(
        requested_by="Bassam")
    background_tasks.add_task(move_elevators, elevator)
    return elevator


@router.get(path="/position")
def get_elevator_position():
    return elevators
