# Career Intelligence App 🎯

A complete career analysis application built specifically for the Indian job market. Analyze your profile, get job fit scores, salary estimates, and personalized recommendations.

## 🌟 Features

- **Job Fit Scoring**: AI-powered analysis of your skills against job requirements
- **Salary Estimation**: Realistic salary ranges based on Indian market data
- **Skill Gap Analysis**: Identify exactly what you need to learn
- **Personalized Recommendations**: Custom learning paths, resources, and timelines
- **Cross-Platform**: Works on desktop, mobile, and tablets
- **5 Job Roles Supported**: Data Analyst, Software Engineer, Product Manager, Digital Marketing, Business Analyst

## 📋 Prerequisites

- Python 3.8 or higher
- Web browser (Chrome, Firefox, Safari, or Edge)
- Basic understanding of command line

## 🚀 Quick Start

### Step 1: Install Python Dependencies

```bash
# Navigate to the backend folder
cd career-intelligence-app/backend

# Install required packages
pip install -r requirements.txt --break-system-packages
```

### Step 2: Start the Backend Server

```bash
# From the backend folder
python app.py
```

You should see:
```
* Running on http://0.0.0.0:5000
```

### Step 3: Open the Frontend

```bash
# Open index.html in your web browser
# You can either:
# 1. Double-click frontend/index.html
# 2. Or use a local server (recommended):

# Navigate to frontend folder
cd ../frontend

# If you have Python installed:
python -m http.server 8000

# Then open browser to: http://localhost:8000
```

## 📁 Project Structure

```
career-intelligence-app/
│
├── frontend/
│   ├── index.html          # Main webpage
│   ├── styles.css          # Professional styling
│   └── app.js              # Frontend logic
│
├── backend/
│   ├── app.py              # Flask API server
│   ├── requirements.txt    # Python dependencies
│   │
│   ├── algorithms/
│   │   ├── scoring.py              # Job fit calculation
│   │   ├── salary_estimation.py   # Salary prediction
│   │   └── recommendations.py     # Personalized advice
│   │
│   └── data/
│       ├── job_roles.json         # Job requirements database
│       ├── salary_data.json       # Salary benchmarks
│       └── skills_database.json   # Learning resources
│
├── docs/
│   ├── SETUP.md            # Detailed setup guide
│   └── API_DOCS.md         # API documentation
│
└── README.md               # This file
```

## 🎯 How to Use

1. **Select Your Target Role**: Choose from 5 popular roles
2. **Add Your Skills**: List skills with proficiency levels (Beginner to Expert)
3. **Fill Profile Details**: Experience, education, target location
4. **Analyze**: Get instant results with:
   - Job Fit Score (0-100%)
   - Salary Range (in INR)
   - Strength Analysis
   - Skill Gaps
   - Personalized Recommendations

## 🛠️ Customization

### Adding New Job Roles

Edit `backend/data/job_roles.json`:

```json
{
  "Your New Role": {
    "description": "Role description",
    "required_skills": {
      "Skill Name": {
        "importance": 0.9,
        "min_level": "intermediate",
        "note": "Why this skill matters"
      }
    },
    "certifications": [...]
  }
}
```

### Updating Salary Data

Edit `backend/data/salary_data.json`:

```json
{
  "Role Name": {
    "base_salary": 350000,
    "by_experience": {
      "fresher": {...},
      "1-2": {...}
    }
  }
}
```

### Adding Learning Resources

Edit `backend/data/skills_database.json`:

```json
{
  "Skill Name": {
    "category": "Technical",
    "resources": [
      {
        "name": "Course Name",
        "type": "Course",
        "url": "https://...",
        "cost": "Free",
        "duration": "4 weeks"
      }
    ],
    "practice_tips": "Helpful tips..."
  }
}
```

## 📊 How Predictions Work

### Job Fit Score Calculation

```python
Score = (Skill Matching Score) + (Experience Bonus) + (Education Bonus)

Where:
- Skill Matching: Based on proficiency level × skill importance
- Experience Bonus: 0-15 points based on years
- Education Bonus: 0-10 points based on degree
```

### Salary Estimation

```python
Salary = Base Salary × Experience Multiplier × Location Multiplier × (1 + Skill Bonus)

Multipliers:
- Experience: 1.0x (fresher) to 2.8x (5+ years)
- Location: 0.6x (tier 3) to 1.0x (tier 1)
- Skill Bonus: Up to 30% based on fit score
```

## 🔒 Data Accuracy & Limitations

**Data Sources:**
- Job posting analysis from major Indian job portals
- Salary data from Glassdoor, AmbitionBox, Naukri
- Industry reports from NASSCOM, LinkedIn
- Skill demand trends from 2024-2025

**Important Disclaimers:**
- Predictions are estimates, not guarantees
- Actual salaries vary by company size, funding, industry
- Hiring decisions involve subjective factors
- Market conditions change rapidly
- Individual results may vary

**Target Accuracy:** 70-85% for salary ranges and skill requirements

## 🌐 Deployment Options

### Option 1: Free Hosting (Vercel + Render)

**Frontend (Vercel):**
```bash
# Install Vercel CLI
npm install -g vercel

# Deploy
cd frontend
vercel
```

**Backend (Render):**
1. Create account at render.com
2. Connect your GitHub repo
3. Deploy as Web Service
4. Update API_URL in frontend/app.js

### Option 2: Heroku

```bash
# Install Heroku CLI
# Create Procfile in backend/:
web: python app.py

# Deploy
heroku create career-intelligence-api
git push heroku main
```

### Option 3: Self-Hosted

Use Docker:

```dockerfile
# Dockerfile for backend
FROM python:3.9
WORKDIR /app
COPY backend/ .
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
```

## 🐛 Troubleshooting

**Problem: "Connection refused" error**
- Solution: Make sure backend is running on port 5000
- Check: `http://localhost:5000/` should show API status

**Problem: CORS errors**
- Solution: Ensure flask-cors is installed
- Check: `pip list | grep flask-cors`

**Problem: Skills not loading**
- Solution: Check JSON syntax in data files
- Validate: Use jsonlint.com

**Problem: Inaccurate predictions**
- Solution: Update data files with latest market info
- Frequency: Update quarterly for best accuracy

## 📈 Future Enhancements

- [ ] Add more job roles (10+ roles)
- [ ] User authentication and profile saving
- [ ] Portfolio project builder
- [ ] Interview preparation tips
- [ ] Company-specific insights
- [ ] Mobile app (React Native)
- [ ] Real-time job market data integration
- [ ] Resume builder integration
- [ ] Mock interview simulator

## 🤝 Contributing

This is a portfolio project, but contributions are welcome!

1. Update job market data in `/backend/data/`
2. Add new algorithms in `/backend/algorithms/`
3. Improve UI/UX in `/frontend/`
4. Add new features

## 📝 License

This project is open source and available for personal and educational use.

## 📧 Contact

Built as a portfolio project demonstrating:
- Full-stack development
- Data analysis
- API design
- Indian job market knowledge

## 🙏 Acknowledgments

- Job market data from various Indian portals
- Inspiration from LinkedIn, Glassdoor
- Built for Indian job seekers

---

**Version:** 1.0.0  
**Last Updated:** February 2025  
**Made with ❤️ for Indian Job Seekers**
