# Build script for Windows
Write-Host "[*] Building JobNchill for Windows..." -ForegroundColor Green

# Install dependencies
Write-Host "[*] Installing dependencies..." -ForegroundColor Cyan
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install pyinstaller

# Create build directory
if (!(Test-Path "dist")) {
    New-Item -ItemType Directory -Path "dist" | Out-Null
}

# Clean up old builds
Write-Host "[*] Cleaning up old builds..." -ForegroundColor Cyan
if (Test-Path "build") {
    Remove-Item -Path "build" -Recurse -Force | Out-Null
}
if (Test-Path "dist") {
    Remove-Item -Path "dist" -Recurse -Force | Out-Null
}
if (Test-Path "JobNchill.spec") {
    Remove-Item -Path "JobNchill.spec" -Force | Out-Null
}

# Recreate dist directory
New-Item -ItemType Directory -Path "dist" | Out-Null

# Build the executable
Write-Host "[*] Building executable..." -ForegroundColor Cyan
pyinstaller `
  --name JobNchill `
  --noconfirm `
  --windowed `
  --distpath "dist" `
  --workpath "build" `
  --specpath "." `
  --add-data "static;static" `
  --add-data "extension;extension" `
  app\desktop.py

if ($LASTEXITCODE -eq 0) {
    Write-Host "[+] Build completed successfully!" -ForegroundColor Green
    Write-Host "[+] Executable location: dist\JobNchill\JobNchill.exe" -ForegroundColor Green
} else {
    Write-Host "[-] Build failed!" -ForegroundColor Red
    exit 1
}
