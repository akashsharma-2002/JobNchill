# Windows Build Guide - JobNchill Desktop App

## Complete Setup and Build Instructions for Windows

---

## **Overview**

This guide explains how to build `JobNchill.exe` for Windows using GitHub Actions automation. The executable is a standalone desktop application that runs the JobNchill job automation system.

**Download Link:** https://drive.google.com/file/d/1e9T4spiVtOXcBf7htUS2hZqvKA2kzyKO/view?usp=drive_link

---

## **What is JobNchill.exe?**

- **Standalone Desktop Application** for Windows
- **Automated Job Applications** across LinkedIn, Indeed, and Naukri
- **Built with PyInstaller** from Python source
- **All-in-One Package** - no Python installation required
- **Web Dashboard** at http://localhost:8000

---

## **Features Included**

✅ Automated job applications  
✅ Resume parsing and form autofill  
✅ Dashboard for tracking and configuration  
✅ Multi-platform support (LinkedIn, Indeed, Naukri)  
✅ Scheduled automation  
✅ Local data storage (privacy-first)

---

## **System Requirements**

**Minimum:**
- Windows 7 or later
- 2GB RAM
- 500MB disk space
- Internet connection

**Recommended:**
- Windows 10 or 11
- 4GB RAM
- 1GB disk space
- Chrome/Edge browser

---

## **How to Build (Step-by-Step)**

### **Method 1: Automatic Build via GitHub Actions (Recommended)**

#### Step 1: Access GitHub Actions
1. Go to: https://github.com/akashsharma-2002/JobNchill
2. Click on the **"Actions"** tab
3. Select **"Build Windows App"** from the left sidebar

#### Step 2: Trigger the Workflow
4. Click the **"Run workflow"** button (top right)
5. A dropdown appears - click **"Run workflow"** again to confirm
6. The build process starts automatically

#### Step 3: Wait for Completion
7. Watch the workflow progress (takes 5-10 minutes)
8. You'll see a green ✅ checkmark when complete
9. If it fails, you'll see a red ❌ - check the logs for errors

#### Step 4: Download the Executable
10. Click on the completed workflow run
11. Scroll down to **"Artifacts"** section
12. Click **"JobNchill-win"** to download the .zip file
13. Extract the zip file to get `JobNchill.exe`

---

### **Method 2: Manual Build on Windows Machine**

If you prefer to build locally on your Windows machine:

#### Prerequisites:
```powershell
# Install Python 3.12 or later
# https://www.python.org/downloads/

# Install required packages
pip install -r requirements.txt
pip install pyinstaller
```

#### Build Steps:
```powershell
# Navigate to project directory
cd C:\path\to\JobNchill

# Run the build script
powershell -ExecutionPolicy Bypass -File .\scripts\build_windows.ps1

# Find your executable at:
# dist\JobNchill\JobNchill.exe
```

---

## **Using JobNchill.exe**

### **First Run:**
1. Extract `JobNchill.exe` from the zip file
2. Double-click `JobNchill.exe` to start
3. Your default browser opens to `http://localhost:8000`
4. The dashboard loads automatically

### **Dashboard Setup:**
1. Upload your resume (PDF or DOCX)
2. Fill in your profile information
3. Add LinkedIn, Indeed, Naukri credentials
4. Configure job search criteria
5. Click "Start Automation"

### **Features:**
- **Profile Management** - Upload and manage your resume
- **Platform Settings** - Configure credentials for each platform
- **Job Search** - Set locations, roles, and salary expectations
- **Automation** - Schedule automated applications
- **Dashboard** - Track applications and results

---

## **Troubleshooting**

### **Issue: "Windows Protected Your PC" Warning**
- This is normal for unsigned executables
- Click "More info" → "Run anyway"
- The app will run after this

### **Issue: Port 8000 Already in Use**
```powershell
# Find the process using port 8000
netstat -ano | findstr :8000

# Kill the process (replace PID with the number found)
taskkill /PID <PID> /F

# Then restart JobNchill.exe
```

### **Issue: Browser Won't Open**
- Manually open browser and go to: http://localhost:8000
- The dashboard should load

### **Issue: Application Crashes on Startup**
- Check the console for error messages
- Try deleting the `data/` folder and restart
- If error persists, check GitHub Issues

---

## **Building New Versions**

Every time you update the code:

1. Push changes to GitHub (`main` branch)
2. Go to Actions → "Build Windows App"
3. Click "Run workflow"
4. Download the new `.exe` when complete

The GitHub Actions workflow automatically handles:
- ✅ Installing dependencies
- ✅ Building the executable
- ✅ Packaging into .zip
- ✅ Creating downloadable artifact

---

## **Build Workflow Details**

**File:** `.github/workflows/build-windows.yml`

**What it does:**
1. Sets up Windows environment
2. Installs Python 3.12
3. Installs all dependencies from `requirements.txt`
4. Runs PyInstaller build script
5. Creates .zip archive
6. Uploads as artifact

**Build Time:** ~5-10 minutes  
**Output:** `JobNchill-win.zip` containing `JobNchill.exe`

---

## **File Structure**

```
JobNchill-win.zip
├── JobNchill.exe          (Main executable)
├── app/                   (Python modules)
├── static/                (CSS, JS assets)
├── extension/             (Chrome extension)
└── [Supporting files]
```

---

## **Customization**

### **Change Application Name:**
Edit `scripts/build_windows.ps1`:
```powershell
--name "YourAppName"
```

### **Change Icon:**
Replace `app/desktop.py` icon reference or create custom icon:
```powershell
--icon "path/to/icon.ico"
```

### **Bundle Additional Files:**
```powershell
--add-data "path/to/files;destination"
```

---

## **Performance Notes**

- **First Launch:** Takes 5-10 seconds (extracts files)
- **Subsequent Launches:** ~2-3 seconds
- **Memory Usage:** ~200-300 MB
- **Disk Usage:** ~300 MB for all files

---

## **Security & Privacy**

✅ **No Telemetry** - No data sent to external servers  
✅ **Local Storage** - All data stored on your computer  
✅ **Open Source** - Source code available on GitHub  
✅ **No Auto-Updates** - You control when to update  
✅ **Offline Capable** - Can run without internet (except for job searches)

---

## **Antivirus Warnings**

Some antivirus software may flag PyInstaller executables. This is normal because:
- The `.exe` is a custom Python application
- It's not a signed/certified executable
- Antivirus software flags unknown executables for safety

**Safe to Proceed:**
- The source code is open on GitHub
- No malicious code is included
- If concerned, scan with VirusTotal.com

---

## **Next Steps**

1. ✅ Download `JobNchill.exe` from the Drive link
2. ✅ Extract and run on Windows machine
3. ✅ Upload your resume
4. ✅ Configure job search settings
5. ✅ Start automating job applications!

---

## **Support & Issues**

**Issues?** Check:
- GitHub Issues: https://github.com/akashsharma-2002/JobNchill/issues
- Privacy Policy: [PRIVACY_POLICY.md](PRIVACY_POLICY.md)
- Chrome Store Guide: [CHROME_STORE_GUIDE.md](CHROME_STORE_GUIDE.md)

---

**Version:** 0.1.3  
**Last Updated:** January 9, 2026  
**Download:** https://drive.google.com/file/d/1e9T4spiVtOXcBf7htUS2hZqvKA2kzyKO/view?usp=drive_link
