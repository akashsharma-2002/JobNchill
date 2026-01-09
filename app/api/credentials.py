"""Credentials API endpoints."""
from fastapi import APIRouter

router = APIRouter(prefix="/api/credentials", tags=["credentials"])

@router.get("/")
def get_credentials():
    return {"status": "ok"}
