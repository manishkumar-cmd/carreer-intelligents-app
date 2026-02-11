# Detailed Setup Guide

This guide will walk you through setting up the Career Intelligence App step-by-step, even if you're a complete beginner.

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
3. [Running the App](#running-the-app)
4. [Testing](#testing)
5. [Deployment](#deployment)
6. [Troubleshooting](#troubleshooting)

---

## Prerequisites

### 1. Check if Python is Installed

**Windows:**
```bash
# Open Command Prompt (Win + R, type 'cmd')
python --version
```

**Mac/Linux:**
```bash
# Open Terminal
python3 --version
```

You should see something like `Python 3.9.7`. If not, install Python:

**Install Python:**
- Windows: Download from [python.org](https://www.python.org/downloads/)
  - ✅ Check "Add Python to PATH" during installation
- Mac: `brew install python3` (if you have Homebrew) or download from python.org
- Linux: `sudo apt-get install python3` (Ubuntu/Debian)

### 2. Verify pip (Python Package Manager)

```bash
pip --version
# or
pip3 --version
```

Should show something like `pip 21.x.x`.

---

## Installation

### Step 1: Download the Project

If you haven't already, get the project files on your computer.

### Step 2: Navigate to the Backend Folder

**Windows:**
```bash
cd C:\Users\YourName\career-intelligence-app\backend
```

**Mac/Linux:**
```bash
cd ~/career-intelligence-app/backend
```

**Tip:** You can drag the folder into Terminal/Command Prompt to auto-fill the path!

### Step 3: Install Python Dependencies

```bash
pip install -r requirements.txt --break-system-packages
```

**What this does:**
- Installs Flask (web framework)
- Installs flask-cors (enables frontend-backend communication)
- Installs Werkzeug (Flask dependency)

**If you get errors:**

**Error: "pip not found"**
```bash
# Try pip3 instead
pip3 install -r requirements.txt --break-system-packages
```

**Error: "Permission denied"**
```bash
# Windows: Run Command Prompt as Administrator
# Mac/Linux: Add sudo
sudo pip install -r requirements.txt --break-system-packages
```

**Error: "externally-managed-environment"**
```bash
# This is why we use --break-system-packages flag
# Or create a virtual environment (advanced):
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

---

## Running the App

### Step 1: Start the Backend Server

**From the backend folder:**
```bash
python app.py
```

**Expected output:**
```
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://0.0.0.0:5000
 * Running on http://127.0.0.1:5000
```

✅ **Success!** Your backend is now running.

**Keep this terminal window open!** The server needs to stay running.

### Step 2: Open the Frontend

**Option A: Simple (Double-click)**
1. Navigate to `career-intelligence-app/frontend/`
2. Double-click `index.html`
3. It will open in your default browser

**Option B: Local Server (Recommended)**

Open a **NEW** terminal/command prompt window:

```bash
cd career-intelligence-app/frontend

# Python 3
python -m http.server 8000

# Or Python 2
python -m SimpleHTTPServer 8000
```

Then open your browser to:
```
http://localhost:8000
```

### Step 3: Test the App

1. Select "Data Analyst" as your target role
2. Add some skills:
   - Python: Intermediate
   - SQL: Beginner
   - Excel: Expert
3. Fill in:
   - Experience: Fresher
   - Education: Bachelor's
   - Location: Tier 3 or Remote
4. Click "Analyze My Profile"

You should see results within 1-2 seconds!

---

## Testing

### Manual Testing Checklist

- [ ] Backend starts without errors
- [ ] Frontend loads in browser
- [ ] Can select a job role
- [ ] Can add multiple skills
- [ ] Can remove skills
- [ ] Form validation works (try submitting empty form)
- [ ] Results display correctly
- [ ] All sections show data (score, salary, strengths, gaps, recommendations)
- [ ] "Analyze Another Profile" resets the form

### API Testing with Browser

Open browser console (F12) and run:

```javascript
fetch('http://localhost:5000/api/roles')
  .then(r => r.json())
  .then(d => console.log(d));
```

Should show list of roles.

### Testing Different Profiles

Try these test cases:

**Test 1: Weak Profile**
- Role: Software Engineer
- Skills: HTML (Beginner)
- Expected: Low score (20-30%), many gaps

**Test 2: Strong Profile**
- Role: Data Analyst
- Skills: SQL (Advanced), Python (Advanced), Excel (Expert), Power BI (Intermediate)
- Experience: 3-5 years
- Expected: High score (80-90%), few gaps

**Test 3: Edge Cases**
- Add 10+ skills
- Try all job roles
- Test all locations and experience levels

---

## Deployment

### Option 1: Deploy to Render (Free)

**Backend:**

1. Create account at [render.com](https://render.com)
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Settings:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python app.py`
   - **Environment:** Python 3
5. Click "Create Web Service"
6. Copy your app URL (e.g., `https://career-api.onrender.com`)

**Frontend:**

1. Create account at [vercel.com](https://vercel.com)
2. Click "New Project"
3. Import your repository
4. Set root directory to `frontend`
5. Update `frontend/app.js`:
   ```javascript
   const API_URL = 'https://career-api.onrender.com/api';
   ```
6. Deploy!

**Cost:** FREE! ✨

### Option 2: Deploy to Heroku

1. Install Heroku CLI: [devcenter.heroku.com/articles/heroku-cli](https://devcenter.heroku.com/articles/heroku-cli)

2. Create `Procfile` in backend folder:
   ```
   web: python app.py
   ```

3. Deploy:
   ```bash
   heroku login
   heroku create career-intelligence
   git push heroku main
   ```

### Option 3: Self-Hosting

**Requirements:**
- A server (AWS EC2, DigitalOcean Droplet, etc.)
- Domain name (optional but recommended)

**Steps:**

1. SSH into your server
2. Install Python, git, nginx
3. Clone repository
4. Set up as systemd service
5. Configure nginx as reverse proxy

(Detailed guide available in community forums)

---

## Troubleshooting

### Problem: "Connection refused" / "Failed to fetch"

**Symptoms:**
- Form submits but nothing happens
- Console shows network error

**Solutions:**

1. **Check backend is running:**
   ```bash
   # Visit in browser:
   http://localhost:5000/
   # Should show: {"status": "active", ...}
   ```

2. **Check CORS:**
   - Make sure `flask-cors` is installed
   - Verify `CORS(app)` is in `app.py`

3. **Check API URL:**
   - In `frontend/app.js`, verify:
   ```javascript
   const API_URL = 'http://localhost:5000/api';
   ```

4. **Firewall:**
   - Windows: Allow Python through firewall
   - Mac: System Preferences → Security

### Problem: "Module not found" Error

**Symptoms:**
```
ModuleNotFoundError: No module named 'flask'
```

**Solution:**
```bash
pip install flask flask-cors --break-system-packages
```

### Problem: JSON Parsing Errors

**Symptoms:**
- Backend crashes with JSON error
- `json.decoder.JSONDecodeError`

**Solution:**

1. Validate JSON files:
   - Visit [jsonlint.com](https://jsonlint.com)
   - Paste contents of each `.json` file
   - Fix any errors (missing commas, brackets, etc.)

2. Common issues:
   - Trailing commas in JSON
   - Missing closing brackets
   - Unescaped quotes

### Problem: Inaccurate Predictions

**Not really a "problem" but:**

**Understanding:**
- Predictions are estimates based on general data
- Market conditions vary
- Individual circumstances differ

**Improving Accuracy:**

1. Update data files with latest market info
2. Add more specific roles and skills
3. Gather user feedback and refine algorithms
4. Update quarterly

### Problem: Frontend Not Loading

**Solutions:**

1. **Check file paths:**
   - Ensure `index.html`, `styles.css`, `app.js` are in same folder
   - Check `<link>` and `<script>` tags in HTML

2. **Browser cache:**
   - Hard refresh: `Ctrl + Shift + R` (Windows) or `Cmd + Shift + R` (Mac)
   - Or clear browser cache

3. **Console errors:**
   - Open DevTools (F12)
   - Check Console tab for errors
   - Google the error message

### Problem: Port Already in Use

**Symptoms:**
```
OSError: [Errno 48] Address already in use
```

**Solutions:**

**Option 1: Change port**
```python
# In app.py, change:
app.run(debug=True, host='0.0.0.0', port=5001)
```

**Option 2: Kill process on port 5000**

**Windows:**
```bash
netstat -ano | findstr :5000
taskkill /PID <PID_NUMBER> /F
```

**Mac/Linux:**
```bash
lsof -ti:5000 | xargs kill -9
```

---

## Performance Tips

1. **Optimize JSON files:**
   - Remove unnecessary whitespace
   - Minify for production

2. **Add caching:**
   - Cache API responses in frontend
   - Use browser localStorage

3. **Lazy loading:**
   - Load resources on demand
   - Defer non-critical scripts

4. **CDN:**
   - Host static files on CDN for faster load times

---

## Security Best Practices

1. **Never commit sensitive data:**
   - API keys
   - Passwords
   - Private user data

2. **Environment variables:**
   ```python
   import os
   API_KEY = os.environ.get('API_KEY')
   ```

3. **Input validation:**
   - Already implemented in `validateFormData()`
   - Add backend validation too

4. **HTTPS in production:**
   - Use SSL certificates
   - Free: Let's Encrypt

---

## Getting Help

**Resources:**

1. **Documentation:**
   - README.md
   - API_DOCS.md
   - This file (SETUP.md)

2. **Online Communities:**
   - Stack Overflow
   - Reddit: r/learnprogramming, r/webdev
   - Discord: The Programmer's Hangout

3. **Debugging Steps:**
   - Read error messages carefully
   - Google the exact error
   - Check file paths and names
   - Verify all dependencies are installed
   - Test one component at a time

**Asking for Help:**

When asking questions, include:
- What you're trying to do
- What you expected to happen
- What actually happened
- Error messages (full text)
- What you've tried already

---

## Next Steps

Once you have the app running:

1. **Customize it:**
   - Add your own branding
   - Modify colors in CSS
   - Add new job roles

2. **Improve it:**
   - Add user authentication
   - Save user profiles
   - Add more features

3. **Share it:**
   - Deploy to production
   - Share with friends
   - Add to your portfolio

---

## Success Checklist

- [ ] Python installed
- [ ] Dependencies installed
- [ ] Backend runs without errors
- [ ] Frontend loads in browser
- [ ] Can analyze a profile
- [ ] Results display correctly
- [ ] Understand how to customize
- [ ] Know where to get help

**If all checked, congratulations! You're ready to use and customize your Career Intelligence App! 🎉**
