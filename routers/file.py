from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from isort import file
from models.login import Login
from models.user import User
from services import file_service

router = APIRouter(prefix="/file",)


@router.get("/")
async def example_login_route():
    return file_service.example_login_service()


@router.get("/cv", response_class=FileResponse)
async def cv():
    return file_service.file("files/CV_bruno_mariz.pdf")
