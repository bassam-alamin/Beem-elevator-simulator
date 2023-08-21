import time
from enum import Enum

elevators = {}

elevator_logs = []


class EventTypes(str, Enum):
    """
    Enums to hold event types
    """
    ElEVATOR_CALL = "Elevator_call"


class ElevatorStates(str, Enum):
    IDLE = "idle"
    MOVING = "moving"
    DOOR_OPEN = "door open"
    DOOR_CLOSED = "door closed"


class ElevatorDirection(str, Enum):
    DEFAULT = None
    UP = "up"
    down = "down"


class Building:
    def __init__(self):
        self.floors = 7
        self.number_of_elevators = 2

    def configure_elevators(self):
        for i in range(self.number_of_elevators):
            elevators[f"elevator_{str(i + 1)}"] = Elevator(elevator_id=i + 1)
        return elevators


class Elevator:
    def __init__(
            self, elevator_id: int,
            state=ElevatorStates.IDLE,
            current_floor=0,
            direction: ElevatorDirection = ElevatorDirection.DEFAULT
    ):
        self.state = state
        self.elevator_id = elevator_id
        self.current_floor = current_floor
        self.direction = direction
        self.stop_floor_list = set()

    def open_door(self):
        print(f"Elevator: {self.elevator_id} Door Opening")
        self.state = ElevatorStates.DOOR_OPEN
        time.sleep(2)
        return True

    def close_door(self):
        print(f"Elevator: {self.elevator_id} Door Closing")
        self.state = ElevatorStates.DOOR_CLOSED
        time.sleep(2)
        return True

    def move_to_next_floor(self):
        if self.stop_floor_list:
            self.state = ElevatorStates.MOVING
            if self.direction == ElevatorDirection.down:
                next_floor = min(self.stop_floor_list)
            else:
                next_floor = max(self.stop_floor_list)
            step = -1 if next_floor < self.current_floor else 1
            # Simulate elevator's movement
            for floor in range(self.current_floor, next_floor + step, step):
                self.current_floor = floor
                # print the floor in real time
                self.print_current_floor()
                time.sleep(5)
            self.stop_floor_list.clear()
            self.open_door()
            self.close_door()
            self.state = ElevatorStates.IDLE
            self.direction = ElevatorDirection.DEFAULT
            print(f"Elevator {self.elevator_id} is IDLE, Ready for another request")
        return True

    def print_current_floor(self):
        print(f"Elevator {self.elevator_id} is on floor {self.current_floor}")
        return


Building().configure_elevators()


def move_elevators(elevator):
    print(f"Elevator {elevator.elevator_id} Starting to move")
    elevator.move_to_next_floor()
    return

