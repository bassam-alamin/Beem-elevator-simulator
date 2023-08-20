from functools import lru_cache
from pathlib import Path
from typing import List, Union, Optional, Dict, Any

from pydantic.v1 import BaseSettings, validator, AnyHttpUrl


class Settings(BaseSettings):
    IS_TEST: bool = False
    ENVIRONMENT: str = "dev"
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = ["http://127.0.0.1"]
    API_PREFIX: str = "/api/v1"
    SQLITE_DB_LOCATION: Optional[str]
    SQLITE_DB: Optional[str] = "test_db.db"
    SQLITE_URI: Optional[str] = "sqlite:///elevator_db.db"

    DB_TYPE: str = "sqlite"
    TEST_DB_TYPE: str = "sqlite"

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    @validator("SQLITE_URI")
    def assemble_sqlite_connection(
            cls, v: Optional[str], values: Dict[str, Any]
    ) -> Any:
        if isinstance(v, str) and v != "":
            print("Returning v: ", v)
            return v
        db_path = (
                Path(__file__).parent.parent.parent
                / values.get("SQLITE_DB_LOCATION")
                / values.get("SQLITE_DB")
        )
        sqlite_path = "sqlite:///" + db_path.as_posix()
        return str(sqlite_path)


@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    print(f"Loading settings for: {settings.ENVIRONMENT}")

    return settings


settings = get_settings()
