import pytest

from api.domain.elevator import Building, elevators, ElevatorStates

floors = Building().floors


def test_open_door():
    elevator = elevators["elevator_1"]
    assert elevator.open_door() == True
    assert elevator.state == ElevatorStates.DOOR_OPEN


def test_close_door():
    elevator = elevators["elevator_1"]
    assert elevator.close_door() == True
    assert elevator.state == ElevatorStates.DOOR_CLOSED


def test_move_to_next_floor():
    elevator = elevators["elevator_1"]
    elevator.current_floor = 3
    elevator.stop_floor_list.add(2)
    moved = elevator.move_to_next_floor()

    assert elevator.current_floor == 2
    assert elevator.state == ElevatorStates.IDLE
    assert moved == True


def run_all():
    test_open_door()
    test_close_door()
    test_move_to_next_floor()
    return


if __name__ == '__main__':
    run_all()
