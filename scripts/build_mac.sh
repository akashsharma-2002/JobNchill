#!/usr/bin/env bash
set -euo pipefail

echo "[*] Building JobNchill for macOS..."

# Install dependencies
echo "[*] Installing dependencies..."
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install pyinstaller

# Clean up old builds
echo "[*] Cleaning up old builds..."
rm -rf build dist JobNchill.spec

echo "[*] Building executable..."

# Build the executable with all dependencies
pyinstaller \
  --name JobNchill \
  --noconfirm \
  --windowed \
  --onefile \
  --distpath "dist" \
  --workpath "build" \
  --specpath "." \
  --collect-all "playwright" \
  --collect-all "cryptography" \
  --collect-all "fastapi" \
  --collect-all "uvicorn" \
  --collect-all "sqlalchemy" \
  --collect-all "pydantic" \
  --collect-all "pydantic_core" \
  --collect-all "pydantic_settings" \
  --collect-all "starlette" \
  --collect-all "requests" \
  --collect-all "beautifulsoup4" \
  --collect-all "jinja2" \
  --collect-all "aiofiles" \
  --collect-all "multipart" \
  --collect-all "lxml" \
  --collect-all "pdf2image" \
  --collect-all "pptx" \
  --collect-all "docx" \
  --collect-all "PIL" \
  --collect-all "schedule" \
  --collect-all "psutil" \
  --collect-all "dotenv" \
  --hidden-import=uvicorn.lifespan \
  --hidden-import=uvicorn.loops \
  --hidden-import=uvicorn.protocols \
  --hidden-import=uvicorn.workers \
  --hidden-import=fastapi \
  --hidden-import=pydantic \
  --hidden-import=pydantic_settings \
  --hidden-import=sqlalchemy.ext.declarative \
  --hidden-import=app.config \
  --hidden-import=app.database \
  --hidden-import=app.api \
  --hidden-import=app.services \
  --hidden-import=app.utils \
  --hidden-import=cryptography \
  --add-data "templates:templates" \
  --add-data "static:static" \
  --add-data "extension:extension" \
  --add-data "app:app" \
  app/main.py

if [ $? -eq 0 ]; then
    echo "[+] Build completed successfully!"
    
    if [ -f "dist/JobNchill" ]; then
        FILE_SIZE=$(du -h dist/JobNchill | cut -f1)
        echo "[+] Executable location: dist/JobNchill"
        echo "[+] File size: $FILE_SIZE"
        
        # Create zip for distribution
        echo "[*] Creating zip package..."
        cd dist && zip -r JobNchill-mac.zip JobNchill && cd ..
        ZIP_SIZE=$(du -h dist/JobNchill-mac.zip | cut -f1)
        echo "[+] Zip created: dist/JobNchill-mac.zip ($ZIP_SIZE)"
    else
        echo "[-] Executable not found!"
        exit 1
    fi
else
    echo "[-] Build failed!"
    exit 1
fi
