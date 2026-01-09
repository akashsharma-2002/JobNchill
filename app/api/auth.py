"""Auth API endpoints."""
from fastapi import APIRouter

router = APIRouter(prefix="/api/auth", tags=["auth"])

@router.get("/")
def get_auth():
    return {"status": "ok"}
