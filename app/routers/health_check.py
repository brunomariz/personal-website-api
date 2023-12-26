from fastapi import APIRouter

router = APIRouter(prefix="/health_check",)


@router.get("/")
async def health_check_route():
    return {"message": "Bruno Mariz Personal Website API"}
