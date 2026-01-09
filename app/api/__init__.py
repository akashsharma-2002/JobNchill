"""API routers."""
from fastapi import APIRouter

router = APIRouter()

@router.get("/api/profile")
def get_profile():
    """Get user profile."""
    return {"status": "ok"}
