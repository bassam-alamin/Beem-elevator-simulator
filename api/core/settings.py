from functools import lru_cache
from typing import List, Union

from pydantic.v1 import BaseSettings, validator, AnyHttpUrl


class Settings(BaseSettings):
    IS_TEST: bool = False
    ENVIRONMENT: str = "dev"
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = ["http://127.0.0.1"]
    API_PREFIX: str = "/api/v0"

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)


@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    print(f"Loading settings for: {settings.ENVIRONMENT}")
    return settings


settings = get_settings()
