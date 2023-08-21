from api.domain.elevator import Elevator
from api.services.handlers.elevator_handler import ElevatorController


def test_call_elevator():
    elevator = ElevatorController(
        elevator_id=1,
        to_floor=3,
        from_floor=5
    ).call_elevator()
    assert isinstance(elevator, Elevator)
    assert elevator.direction == "down"
    assert elevator.current_floor == 5


def test_log_event():
    query_details = ElevatorController(
        elevator_id=1,
        to_floor=3,
        from_floor=5
    ).log_event(requested_by="test_user")
    assert isinstance(query_details, str)
    assert query_details != False


def test_query_logger():
    query_details = ElevatorController(
        elevator_id=1,
        to_floor=3,
        from_floor=5
    ).save_query_logs(
        requested_by="test_user",
        query="...select * FROM TABLE....",
        function_name="Call elevator"
    )
    assert isinstance(query_details, str)
    assert query_details != False
