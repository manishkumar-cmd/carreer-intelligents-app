# 🚀 QUICK START GUIDE

## Ready to Run in 3 Steps!

### Step 1: Install Dependencies (1 minute)
```bash
cd career-intelligence-app/backend
pip install -r requirements.txt --break-system-packages
```

### Step 2: Start Backend (5 seconds)
```bash
python app.py
```
Leave this running! You should see: `Running on http://0.0.0.0:5000`

### Step 3: Open Frontend (5 seconds)
**Option A:** Double-click `frontend/index.html`

**Option B (Better):** In a NEW terminal:
```bash
cd career-intelligence-app/frontend
python -m http.server 8000
```
Then open: `http://localhost:8000`

## Done! 🎉

Now try it:
1. Select "Data Analyst"
2. Add skills: Python (Intermediate), SQL (Beginner), Excel (Expert)
3. Fill in: Fresher, Bachelor's, Tier 3
4. Click "Analyze My Profile"

---

## What You Get

✅ **Job Fit Score** - How well you match the role (0-100%)  
✅ **Salary Estimate** - Realistic range in INR  
✅ **Strengths** - What you're good at  
✅ **Skill Gaps** - What to learn  
✅ **Recommendations** - Personalized learning path with resources and timeline

---

## Files Overview

```
career-intelligence-app/
├── frontend/               # What users see
│   ├── index.html         # Main page
│   ├── styles.css         # Professional design
│   └── app.js             # Frontend logic
│
├── backend/               # Brain of the app
│   ├── app.py            # Main API server
│   ├── algorithms/       # Prediction logic
│   │   ├── scoring.py
│   │   ├── salary_estimation.py
│   │   └── recommendations.py
│   └── data/            # Market data
│       ├── job_roles.json
│       ├── salary_data.json
│       └── skills_database.json
│
├── docs/                # Documentation
│   ├── SETUP.md         # Detailed setup
│   └── API_DOCS.md      # API reference
│
└── README.md           # Project overview
```

---

## Customization (Easy!)

### Add New Job Role
Edit `backend/data/job_roles.json` - copy existing role and modify

### Update Salaries
Edit `backend/data/salary_data.json` - adjust numbers for current market

### Add Learning Resources
Edit `backend/data/skills_database.json` - add courses, books, etc.

### Change Colors
Edit `frontend/styles.css` - modify `:root` variables

---

## Deploy for Free

### Vercel (Frontend)
```bash
npm install -g vercel
cd frontend
vercel
```

### Render (Backend)
1. Go to render.com
2. New Web Service
3. Connect repo
4. Deploy!

Cost: **$0** ✨

---

## Troubleshooting

**Error: Module not found**
```bash
pip install flask flask-cors --break-system-packages
```

**Error: Connection refused**
- Make sure backend is running
- Check `http://localhost:5000/` shows API status

**Results not showing**
- Open browser console (F12)
- Check for errors
- Verify API_URL in `app.js`

---

## Need Help?

📖 Read: `docs/SETUP.md` (detailed guide)  
📖 Read: `docs/API_DOCS.md` (API reference)  
📖 Read: `README.md` (project overview)

🐛 Issues? Check console errors (F12)  
💡 Questions? Google the error message

---

## This is YOUR App Now!

✨ Customize it  
✨ Deploy it  
✨ Add it to your portfolio  
✨ Share it with friends  
✨ Build on it  

**Good luck with your career! 🚀**
