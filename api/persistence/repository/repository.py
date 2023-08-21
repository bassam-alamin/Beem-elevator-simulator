import abc
import logging
from typing import Any

from api.persistence.models.elevator import ElevatorLogs, QueryLogger
from api.persistence.repository.session import get_session, captured_logs


class SqlaRepositoryError(Exception):
    default_message = "SQLAlchemy repository error."

    def __init__(self, msg=default_message, *args):
        super().__init__(msg, *args)


class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, details: Any):
        raise NotImplementedError


class SqlaRepository(AbstractRepository):
    def __init__(self, sqla_model):
        self.sqla_model = sqla_model

    def add(self, to_create: dict):
        obj_record = self.sqla_model(**to_create)
        try:
            with get_session() as session:
                session.add(obj_record)
                session.commit()
                session.refresh(obj_record)
                print(f"Record added for {self.sqla_model.__name__}")
            return captured_logs[1]
        except Exception as e:
            message = f"Adding record for model {self.sqla_model.__name__} failed: {e}"
            print(message)
            raise SqlaRepositoryError(message)


elevator_log_repository = SqlaRepository(ElevatorLogs)

query_logger_repository = SqlaRepository(QueryLogger)
