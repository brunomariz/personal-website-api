from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from isort import file
from services import file_service

router = APIRouter(prefix="/file",)


@router.get("/")
async def example_login_route():
    return file_service.example_login_service()


@router.get("/cv", response_class=FileResponse)
async def cv(lang: str = "eng"):
    if lang == "eng":
        return file_service.file("files/Eng_CV_bruno_mariz.pdf")
    else:
        return file_service.file("files/CV_bruno_mariz.pdf")
