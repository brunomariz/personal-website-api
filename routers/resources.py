from fastapi import APIRouter, HTTPException
from services import resources_service

router = APIRouter(prefix="/resources",)


@router.get("/")
async def example_resources_route():
    return resources_service.example_resources_service()


@router.get("/meta")
async def resources():
    return resources_service.resources_metadata()
