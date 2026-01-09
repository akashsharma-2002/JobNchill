"""Automation API endpoints."""
from fastapi import APIRouter

router = APIRouter(prefix="/api/automation", tags=["automation"])

@router.get("/")
def get_automation():
    return {"status": "ok"}
