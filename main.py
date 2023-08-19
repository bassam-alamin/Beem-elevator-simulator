import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from api.endpoints.all_routes import api_router
from docs.open_api.api_metadata import title, description
import api.core.settings as s

app = FastAPI(
    title=title,
    description=description,
    # dependencies=[Depends(JWTBearer())],
)

# Set all CORS enabled origins
if s.settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in s.settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router, prefix=s.settings.API_PREFIX)


def start():
    if s.settings.IS_TEST:
        uvicorn.run("main:app")


if __name__ == "__main__":
    # Start must be located here, to avoid async error when running uvicorn.
    start()
