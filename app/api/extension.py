"""Extension API endpoints."""
from fastapi import APIRouter

router = APIRouter(prefix="/api/extension", tags=["extension"])

@router.get("/")
def get_extension():
    return {"status": "ok"}
