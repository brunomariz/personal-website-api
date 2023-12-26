from fastapi import APIRouter, HTTPException
from app.services import resources_service

router = APIRouter(prefix="/resources",)


@router.get("/")
async def resources_route():
    return resources_service.resources_data()


@router.get("/paths")
async def resources_paths_route():
    return resources_service.resources_list_of_paths("resources")

