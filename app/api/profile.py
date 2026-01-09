"""Profile API endpoints."""
from fastapi import APIRouter

router = APIRouter(prefix="/api/profile", tags=["profile"])

@router.get("/")
def get_profile():
    return {"status": "ok"}
