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

# Build PyInstaller command with optional data files
$pyInstallerArgs = @(
    "--name", "JobNchill",
    "--noconfirm",
    "--windowed",
    "--distpath", "dist",
    "--workpath", "build",
    "--specpath", ".",
    "--onefile",
    "--collect-all", "playwright",
    "--collect-all", "fastapi",
    "--collect-all", "uvicorn",
    "--collect-all", "sqlalchemy",
    "--collect-all", "pydantic",
    "--collect-all", "pydantic_core",
    "--collect-all", "pydantic_settings",
    "--collect-all", "starlette",
    "--collect-all", "requests",
    "--collect-all", "beautifulsoup4",
    "--hidden-import=uvicorn.lifespan",
    "--hidden-import=uvicorn.loops",
    "--hidden-import=uvicorn.protocols",
    "--hidden-import=uvicorn.workers",
    "--hidden-import=fastapi",
    "--hidden-import=pydantic",
    "--hidden-import=pydantic_settings",
    "--hidden-import=sqlalchemy.ext.declarative",
    "--hidden-import=app.config",
    "--hidden-import=app.database",
    "--hidden-import=app.api",
    "--hidden-import=app.services",
    "--hidden-import=app.utils",
    "app\main.py"
)

# Add optional data directories if they exist
if (Test-Path "static") {
    Write-Host "[*] Including static files..." -ForegroundColor Cyan
    $pyInstallerArgs += @("--add-data", "static:static")
}

if (Test-Path "templates") {
    Write-Host "[*] Including templates..." -ForegroundColor Cyan
    $pyInstallerArgs += @("--add-data", "templates:templates")
}

if (Test-Path "extension") {
    Write-Host "[*] Including extension files..." -ForegroundColor Cyan
    $pyInstallerArgs += @("--add-data", "extension:extension")
}

if (Test-Path "app") {
    Write-Host "[*] Including app modules..." -ForegroundColor Cyan
    $pyInstallerArgs += @("--add-data", "app:app")
}

# Run PyInstaller
& pyinstaller @pyInstallerArgs

if ($LASTEXITCODE -eq 0) {
    Write-Host "[+] Build completed successfully!" -ForegroundColor Green
    
    # Check for executable
    if (Test-Path "dist\JobNchill.exe") {
        Write-Host "[+] Executable location: dist\JobNchill.exe" -ForegroundColor Green
        Write-Host "[+] File size: $((Get-Item 'dist\JobNchill.exe').Length / 1MB)MB" -ForegroundColor Cyan
    } elseif (Test-Path "dist\JobNchill\JobNchill.exe") {
        Write-Host "[+] Executable location: dist\JobNchill\JobNchill.exe" -ForegroundColor Green
        Write-Host "[+] File size: $((Get-Item 'dist\JobNchill\JobNchill.exe').Length / 1MB)MB" -ForegroundColor Cyan
    } else {
        Write-Host "[-] Executable not found in expected location!" -ForegroundColor Red
        Write-Host "[*] Checking dist directory..." -ForegroundColor Cyan
        Get-ChildItem -Path "dist" -Recurse
        exit 1
    }
} else {
    Write-Host "[-] Build failed!" -ForegroundColor Red
    exit 1
}
