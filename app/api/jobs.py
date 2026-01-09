"""Jobs API endpoints."""
from fastapi import APIRouter

router = APIRouter(prefix="/api/jobs", tags=["jobs"])

@router.get("/")
def get_jobs():
    return {"status": "ok"}
