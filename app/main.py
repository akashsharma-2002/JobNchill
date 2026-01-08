"""FastAPI main application entry point."""
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from pathlib import Path

from app.config import settings
from app.services.license import load_license
from app.database import init_db
from app.api import profile, credentials, jobs, automation, auth, extension, license
from app.services.scheduler import get_scheduler
from app.services.orchestrator import run_automation_cycle


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan events."""
    # Startup
    print("🚀 Starting JobNchill...")
    init_db()
    print("✅ Database initialized")
    
    # Setup scheduler callback
    scheduler = get_scheduler()
    scheduler.set_automation_callback(run_automation_cycle)
    
    yield
    
    # Shutdown
    print("🛑 Shutting down...")
    scheduler.stop()
    from app.utils.browser import close_shared_browser
    await close_shared_browser()


# Create FastAPI app
app = FastAPI(
    title=settings.app_name,
    description="Automated job application system with safe, hybrid approach",
    version="1.0.0",
    lifespan=lifespan
)

# CORS middleware (added first, executes last)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost", "http://localhost:8000", "http://127.0.0.1", "http://127.0.0.1:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Session Middleware (added second, executes first)
app.add_middleware(SessionMiddleware, secret_key=settings.secret_key)

# Mount static files
static_path = settings.base_dir / "static"
static_path.mkdir(exist_ok=True)
app.mount("/static", StaticFiles(directory=str(static_path)), name="static")

# Templates
templates_path = settings.base_dir / "templates"
templates_path.mkdir(exist_ok=True)
templates = Jinja2Templates(directory=str(templates_path))

# Include API routers
app.include_router(auth.router, prefix="/auth")
app.include_router(profile.router, prefix="/api")
app.include_router(credentials.router, prefix="/api")
app.include_router(jobs.router, prefix="/api")
app.include_router(automation.router, prefix="/api")
app.include_router(extension.router, prefix="/api")
app.include_router(license.router, prefix="/api")


@app.get("/")
async def home(request: Request):
    """Serve the main dashboard or public landing page."""
    user = request.session.get("user")
    if settings.app_mode.lower() == "landing":
        return templates.TemplateResponse(
            "landing.html",
            {"request": request}
        )
    license_data = load_license()
    license_plan = (license_data.get("plan") or "free").lower()
    display_token = license_data.get("token") if license_plan == "booster" else ""
    display_expiry = license_data.get("expires_at") if license_plan == "booster" else ""
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "user": user,
            "extension_token": display_token or "",
            "extension_token_expires_at": display_expiry or ""
        }
    )


@app.get("/app")
async def app_dashboard(request: Request):
    """Serve the main dashboard explicitly."""
    user = request.session.get("user")
    license_data = load_license()
    license_plan = (license_data.get("plan") or "free").lower()
    display_token = license_data.get("token") if license_plan == "booster" else ""
    display_expiry = license_data.get("expires_at") if license_plan == "booster" else ""
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "user": user,
            "extension_token": display_token or "",
            "extension_token_expires_at": display_expiry or ""
        }
    )


@app.get("/api/health")
async def health_check():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "app": settings.app_name,
        "debug": settings.debug
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
