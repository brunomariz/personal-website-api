from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from isort import file
from app.services import file_service

router = APIRouter(prefix="/file",)


@router.get("/")
async def example_login_route():
    return file_service.example_file_service()


@router.get("/cv", response_class=FileResponse)
async def cv(lang: str = "en-US"):
    if lang in ["pt-BR", "pt"]:
        return file_service.file("app/files/CV_bruno_mariz.pdf")
    else:
        return file_service.file("app/files/Eng_CV_bruno_mariz.pdf")
