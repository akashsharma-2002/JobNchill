# Chrome Web Store Publishing Guide - JobNchill Autofill

## Complete Step-by-Step Instructions

### Step 1: Developer Account Setup ✓

1. **Access Chrome Web Store Developer Console**
   - Visit: https://chrome.google.com/webstore/devconsole
   - Sign in with your Google account

2. **Pay Registration Fee**
   - One-time $5 USD fee
   - Use your Google Play account or credit card

3. **Complete Developer Profile**
   - Add your name and email
   - Verify your identity (usually automatic)

---

### Step 2: Create Your Extension Package

**Option A: Create a .zip file locally**

```bash
cd /Users/akashsharma/PycharmProjects/job_automation/extension
zip -r JobNchill-extension.zip .
# This creates: JobNchill-extension.zip
```

**Files to include:**
- `manifest.json`
- `content.js`
- `popup.html`
- `popup.js`
- `options.html`
- `options.js`
- `styles.css`
- `icon.png`

**Files to EXCLUDE:**
- `.DS_Store`
- `__pycache__`
- Any build files

---

### Step 3: Prepare Store Listing Assets

#### Required Images:
1. **Icon (128x128px)** - You have: `icon.png` ✓
   - Must be PNG, JPG, or GIF
   - Square format recommended

2. **Screenshots (1280x800 or 640x400px)**
   - Minimum: 1 screenshot
   - Maximum: 5 screenshots
   - Show the popup UI and options page

3. **Promo Tile (920x680px)** - Optional but recommended
   - Shows in Chrome Web Store

#### Text Content Needed:
- **Name**: "JobNchill Autofill"
- **Short Description** (132 chars max):
  ```
  Automated job application autofill for LinkedIn, Indeed, Glassdoor, and more.
  ```
- **Full Description**:
  ```
  JobNchill Autofill helps you apply to jobs faster by automatically filling 
  out application forms with your information across multiple job boards.
  
  Supports:
  • LinkedIn
  • Indeed
  • Glassdoor
  • Naukri
  • Foundit
  • Wellfound
  • Greenhouse
  • Lever
  
  Features:
  ✓ One-click autofill
  ✓ Save your profile information
  ✓ Works across all major job boards
  ✓ Privacy-first: All data stored locally
  
  Privacy:
  We don't collect any personal data. All your information is stored locally 
  on your device. See our full privacy policy for details.
  ```

---

### Step 4: Submit to Chrome Web Store

1. **Go to Developer Console**
   - https://chrome.google.com/webstore/devconsole

2. **Click "New Item"**

3. **Upload Your .zip File**
   - Upload: `JobNchill-extension.zip`
   - Wait for upload to complete

4. **Fill in Store Listing**
   - **Name**: JobNchill Autofill
   - **Summary**: Automated autofill for job applications
   - **Description**: (use full description from Step 3)
   - **Category**: Productivity
   - **Language**: English
   - **Websites**: https://github.com/akashsharma-2002/JobNchill

5. **Upload Assets**
   - Icon (128x128)
   - At least 1 screenshot
   - Promo tile (optional)

6. **Privacy**
   - Add Privacy Policy URL (point to GitHub)
   - Check "This extension doesn't require sensitive host permissions"
   - Add privacy policy content

7. **Content Rating**
   - Select your age rating
   - Check appropriate boxes

8. **Review Policies**
   - Read and accept Chrome Web Store policies
   - Ensure manifest.json complies with policies

---

### Step 5: Review & Submit

1. **Review All Information**
   - Double-check all fields
   - Verify screenshots look good
   - Test the .zip file locally

2. **Test Your Extension**
   ```bash
   # Load unpacked extension for testing
   # In Chrome: Settings → Extensions → "Load unpacked"
   # Select: /Users/akashsharma/PycharmProjects/job_automation/extension
   ```

3. **Submit for Review**
   - Click "Submit for Review"
   - Google will review (usually 1-3 hours, sometimes up to 24 hours)

---

### Step 6: After Submission

**What happens next:**
- ✓ Automated scanning for malware
- ✓ Review of manifest.json and permissions
- ✓ Verification of privacy policy
- ✓ Manual review by Google team (optional)

**Possible Outcomes:**
- ✅ **Approved**: Extension goes live on Chrome Web Store
- ⚠️ **Rejected**: Will receive email with reasons
- 🔄 **Resubmit**: Fix issues and resubmit

**Share Your Extension:**
- Chrome Web Store Link: `https://chrome.google.com/webstore/detail/[extension-id]`
- You'll receive this ID after approval

---

## Important Notes

### Manifest Compliance
Your current manifest.json ✓ is compliant:
- ✓ Manifest v3 (latest standard)
- ✓ Proper permissions declared
- ✓ No prohibited permissions

### Common Rejection Reasons
❌ Don't do these:
- Misleading functionality
- Unclear privacy policy
- Excessive permissions not explained
- Low quality screenshots
- Policy violations (no malware, etc.)

### Updating Your Extension
1. Increment `version` in manifest.json
2. Create new .zip file
3. Upload new .zip to developer console
4. Update store listing if needed
5. Resubmit for review (usually faster)

---

## Quick Commands

```bash
# Navigate to extension
cd /Users/akashsharma/PycharmProjects/job_automation/extension

# Create zip file
zip -r JobNchill-extension.zip . -x "*.DS_Store" "*.git*"

# Check manifest validity (requires jq)
cat manifest.json | jq '.'
```

---

## Resources

- Chrome Web Store Developer Console: https://chrome.google.com/webstore/devconsole
- Manifest v3 Documentation: https://developer.chrome.com/docs/extensions/mv3/
- Chrome Web Store Policies: https://developer.chrome.com/docs/webstore/policies/
- Icon Guidelines: https://developer.chrome.com/docs/webstore/images/

---

## Support

- GitHub Repository: https://github.com/akashsharma-2002/JobNchill
- Create an Issue for support: https://github.com/akashsharma-2002/JobNchill/issues

Good luck with your submission! 🚀
