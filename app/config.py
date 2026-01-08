"""Application configuration management."""
import os
import secrets
import sys
from pathlib import Path
from typing import List, Optional
from pydantic_settings import BaseSettings
from pydantic import Field


def _resolve_base_dir() -> Path:
    """Resolve base directory for packaged and source runs."""
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        return Path(sys._MEIPASS)
    return Path(__file__).parent.parent


BASE_DIR = _resolve_base_dir()
DEFAULT_DATA_DIR = Path.home() / ".jobnchill" if getattr(sys, "frozen", False) else BASE_DIR / "data"
DEFAULT_DB_PATH = DEFAULT_DATA_DIR / "job_automation.db"
DEFAULT_DB_URL = f"sqlite:///{DEFAULT_DB_PATH.as_posix()}"


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""
    
    # Application
    app_name: str = Field(default="JobNchill")
    debug: bool = Field(default=False)
    app_mode: str = Field(default="app")  # "app" or "landing"
    
    # Paths - use defaults that work without .env
    base_dir: Path = Field(default=BASE_DIR)
    data_dir: Path = Field(default=DEFAULT_DATA_DIR)
    resumes_dir: Path = Field(default=DEFAULT_DATA_DIR / "resumes")
    
    # Database
    database_url: str = Field(default=DEFAULT_DB_URL)
    
    # Security
    encryption_key: str = Field(default="")
    google_client_id: str = Field(default="")
    google_client_secret: str = Field(default="")
    google_redirect_uri: str = Field(default="")
    secret_key: str = Field(default="dev-secret-key") # For session signing
    extension_token: str = Field(default="")
    
    # Scheduler
    automation_interval_hours: int = Field(default=2)
    
    # Email Settings (SMTP)
    smtp_host: str = Field(default="smtp.gmail.com")
    smtp_port: int = Field(default=587)
    smtp_user: str = Field(default="")
    smtp_password: str = Field(default="")
    emails_from: str = Field(default="JobNchill <hello@jobnchill.com>")
    
    # Job Search Defaults
    default_job_titles: str = Field(default="Software Engineer,Backend Developer,Python Developer")
    default_locations: str = Field(default="Bangalore,Hyderabad,Remote")
    
    # Daily Application Limits
    linkedin_daily_limit: int = Field(default=25)
    naukri_daily_limit: int = Field(default=30)
    foundit_daily_limit: int = Field(default=30)
    wellfound_daily_limit: int = Field(default=20)
    
    # Referral Settings
    referrals_per_company: int = Field(default=4)
    
    # AI Integration
    gemini_api_key: str = Field(default="")
    
    # Human-like behavior
    min_delay_seconds: float = Field(default=2.0)
    max_delay_seconds: float = Field(default=5.0)
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"
    
    def model_post_init(self, __context) -> None:
        """Initialize derived paths after model creation."""
        if self.data_dir is None:
            self.data_dir = self.base_dir / "data"
        if self.resumes_dir is None:
            self.resumes_dir = self.data_dir / "resumes"
        
        # Ensure directories exist
        self.data_dir.mkdir(parents=True, exist_ok=True)
        self.resumes_dir.mkdir(parents=True, exist_ok=True)

        if self.database_url == DEFAULT_DB_URL:
            db_path = self.data_dir / "job_automation.db"
            self.database_url = f"sqlite:///{db_path.as_posix()}"

        # Handle encryption key persistence
        if not self.encryption_key:
            key_file = self.data_dir / "secret.key"
            if key_file.exists():
                # Read existing key
                self.encryption_key = key_file.read_text().strip()
            else:
                # Generate new key and save it
                from cryptography.fernet import Fernet
                new_key = Fernet.generate_key().decode()
                key_file.write_text(new_key)
                self.encryption_key = new_key

        # Handle extension token persistence
        if not self.extension_token:
            token_file = self.data_dir / "extension.token"
            if token_file.exists():
                self.extension_token = token_file.read_text().strip()
            else:
                new_token = secrets.token_urlsafe(32)
                token_file.write_text(new_token)
                self.extension_token = new_token
    
    @property
    def job_titles_list(self) -> List[str]:
        """Get job titles as a list."""
        return [t.strip() for t in self.default_job_titles.split(",") if t.strip()]
    
    @property
    def locations_list(self) -> List[str]:
        """Get locations as a list."""
        return [l.strip() for l in self.default_locations.split(",") if l.strip()]


# Global settings instance
settings = Settings()
