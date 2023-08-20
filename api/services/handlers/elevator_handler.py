from api.domain.elevator import elevators, ElevatorDirection


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
        print(f"Elevator called by: {requested_by}")
        self.elevator.current_floor = self.from_floor
        self.elevator.stop_floor_list.add(self.to_floor)
        if self.from_floor > self.to_floor:
            self.elevator.direction = ElevatorDirection.down
        else:
            self.elevator.direction = ElevatorDirection.UP
        elevators[f"elevator_{self.elevator_id}"] = self.elevator
        return self.elevator




