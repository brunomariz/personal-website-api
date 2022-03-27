from fastapi import APIRouter, HTTPException
from models.login import Login
from models.user import User
from services import login_service

router = APIRouter(prefix="/login",)


@router.get("/")
async def example_login_route():
    return login_service.example_login_service()


@router.post("/", response_model=User)
async def login(login_info: Login):
    return login_service.login(login_info)
