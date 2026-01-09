# Build script for Windows
Write-Host "🔨 Building JobNchill for Windows..." -ForegroundColor Green

# Install dependencies
Write-Host "📦 Installing dependencies..." -ForegroundColor Cyan
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install pyinstaller

# Create build directory
if (!(Test-Path "dist")) {
    New-Item -ItemType Directory -Path "dist" | Out-Null
}

# Build the executable
Write-Host "🏗️  Building executable..." -ForegroundColor Cyan
pyinstaller `
  --name JobNchill `
  --noconfirm `
  --windowed `
  --distpath "dist" `
  --buildpath "build" `
  --specpath "." `
  --add-data "templates;templates" `
  --add-data "static;static" `
  --add-data "extension;extension" `
  app\desktop.py

if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ Build completed successfully!" -ForegroundColor Green
    Write-Host "📁 Executable location: dist\JobNchill\JobNchill.exe" -ForegroundColor Green
} else {
    Write-Host "❌ Build failed!" -ForegroundColor Red
    exit 1
}
