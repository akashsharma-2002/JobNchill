"""License API endpoints."""
from fastapi import APIRouter

router = APIRouter(prefix="/api/license", tags=["license"])

@router.get("/")
def get_license():
    return {"status": "ok"}
