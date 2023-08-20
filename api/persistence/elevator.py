class ElevatorLog:
    def __init__(self, elevator_id, event, timestamp, description):
        self.elevator_id = elevator_id
        self.event = event
        self.timestamp = timestamp
        self.description = description

    def persist_logs(self):
        self._persist_query()
        return

    def _persist_query(self):
        return