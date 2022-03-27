from fastapi import HTTPException
from fastapi.responses import FileResponse
from models.login import Login
from models.user import User


def example_resources_service():
    return {"message": "resources"}


def resources_metadata():
    return {"resources": []}
