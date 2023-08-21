from contextlib import contextmanager
from sqlalchemy import create_engine, event
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker, Session
import logging
import api.core.settings as s

logging = logging.getLogger("db_session_processes")


@contextmanager
def get_session() -> Session:
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except Exception as error:
        session.rollback()
        raise error
    finally:
        session.close()


captured_logs = []


def set_sqlite_engine():
    print(f"Creating sqlite engine with URI: {s.settings.SQLITE_URI}")

    engine = create_engine(
        s.settings.SQLITE_URI, connect_args={"check_same_thread": False}
    )

    # Add event listener for tracking queries
    @event.listens_for(engine, "before_cursor_execute")
    def before_cursor_execute(conn, cursor, statement, parameters, context, executemany):
        # Log the query and its parameters
        query_info = f"Query: {statement}, Parameters: {parameters}"
        # Log or save query_info into your event log database
        captured_logs.insert(0, query_info)

    event.listen(engine, "connect", lambda c, _: c.execute("pragma foreign_keys=ON;"))
    return engine


def get_engine(db_type: str) -> Engine:
    """Set db engine to use based on the type of db required."""
    map_db_type_to_setter = {
        "sqlite": set_sqlite_engine
    }

    if db_type in map_db_type_to_setter:
        return map_db_type_to_setter[db_type]()
    else:
        raise ValueError("DB type is not recognized.")


engine = get_engine("sqlite")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
