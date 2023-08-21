from fastapi import FastAPI
from starlette.testclient import TestClient

from api.endpoints.all_routes import api_router


def get_test_app():

    test_app = FastAPI()

    test_app.include_router(api_router)

    return test_app


client = TestClient(get_test_app())

client_with_authorisation = TestClient(get_test_app())
