from fastapi import HTTPException
from fastapi.responses import FileResponse
from models.login import Login
from models.user import User

fake_login_table = {"username": ["admin"], "password": ["admin_"]}


def example_file_service():
    return {"message": "file"}


def file(file_path: str):
    return FileResponse(file_path)
