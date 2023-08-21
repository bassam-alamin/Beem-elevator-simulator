import datetime

from starlette import status
from starlette.exceptions import HTTPException
from starlette.responses import JSONResponse

from api.domain.elevator import elevators, ElevatorDirection, ElevatorStates
from api.persistence.repository.repository import elevator_log_repository, query_logger_repository


class ElevatorController:
    def __init__(self, elevator_id: int,
                 direction=None, to_floor=None,
                 from_floor=None):
        self.elevator_id = elevator_id
        self.elevator = elevators.get(str(f"elevator_{elevator_id}"))
        self.direction = direction
        self.to_floor = to_floor
        self.from_floor = from_floor

    # Function to move elevator
    def call_elevator(self, requested_by=None):
        if self.elevator is None:
            raise HTTPException(
                status_code=404,
                detail=f"Elevator of id {self.elevator_id} "
                       f"does not exist."
            )
        if self.elevator.state != ElevatorStates.IDLE:
            raise HTTPException(
                status_code=404,
                detail=f"Elevator of id {self.elevator_id} "
                       f"is busy please call another one "
                       f"or wait."
            )
        self.elevator.current_floor = self.from_floor
        self.elevator.stop_floor_list.add(self.to_floor)
        if self.from_floor > self.to_floor:
            self.elevator.direction = ElevatorDirection.down
        else:
            self.elevator.direction = ElevatorDirection.UP
        elevators[f"elevator_{self.elevator_id}"] = self.elevator
        # add elevator logs to db
        self.log_event(requested_by=requested_by)
        return self.elevator

    def log_event(self, requested_by=None):
        try:
            query_details = elevator_log_repository.add(
                to_create={
                    "elevator_id": self.elevator_id,
                    "event": "Elevator Call",
                    "timestamp": datetime.datetime.utcnow(),
                    "description": f"Elevator {self.elevator_id} is called "
                                   f"from {self.from_floor} to {self.to_floor}"
                }
            )
            self.save_query_logs(
                query=query_details,
                requested_by=requested_by,
                function_name="ElevatorController.call_elevator"
            )
            return query_details
        except Exception as error:
            print(error)
            return False

    def save_query_logs(self, query=None, requested_by=None, function_name=None):
        try:
            query_details = query_logger_repository.add(
                to_create={
                    "user_name": requested_by,
                    "query": query,
                    "location": function_name
                }
            )
            return query_details
        except Exception as error:
            print(error)
            return False
