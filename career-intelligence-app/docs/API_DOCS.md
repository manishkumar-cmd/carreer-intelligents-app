# API Documentation

## Base URL
```
http://localhost:5000/api
```

## Endpoints

### 1. Health Check
Check if API is running.

**Endpoint:** `GET /`

**Response:**
```json
{
  "status": "active",
  "message": "Career Intelligence API is running",
  "version": "1.0.0"
}
```

---

### 2. Get Available Roles
Retrieve list of supported job roles.

**Endpoint:** `GET /api/roles`

**Response:**
```json
{
  "roles": [
    "Data Analyst",
    "Software Engineer",
    "Product Manager",
    "Digital Marketing Specialist",
    "Business Analyst"
  ]
}
```

---

### 3. Analyze Profile
Main endpoint for career analysis.

**Endpoint:** `POST /api/analyze`

**Request Body:**
```json
{
  "role": "Data Analyst",
  "skills": {
    "Python": "intermediate",
    "SQL": "beginner",
    "Excel": "expert",
    "Power BI": "beginner",
    "Statistics": "intermediate"
  },
  "experience": "fresher",
  "education": "bachelors",
  "location": "tier3"
}
```

**Field Specifications:**

| Field | Type | Required | Options |
|-------|------|----------|---------|
| role | string | Yes | One of the supported roles |
| skills | object | Yes | Key: skill name, Value: proficiency level |
| experience | string | Yes | `fresher`, `1-2`, `3-5`, `5+` |
| education | string | Yes | `diploma`, `bachelors`, `masters`, `phd` |
| location | string | Yes | `tier1`, `tier2`, `tier3`, `remote` |

**Proficiency Levels:**
- `beginner`: Basic understanding
- `intermediate`: Working knowledge
- `advanced`: Strong proficiency
- `expert`: Master level

**Response:**
```json
{
  "job_fit_score": 55.0,
  "strengths": [
    {
      "skill": "Excel",
      "your_level": "Expert",
      "importance": "Important",
      "note": "Advanced Excel including pivot tables and data visualization"
    }
  ],
  "skill_gaps": [
    {
      "skill": "SQL",
      "current_level": "Beginner",
      "required_level": "Advanced",
      "priority": "High",
      "note": "SQL is THE most critical skill for Data Analysts"
    }
  ],
  "salary_estimate": {
    "min": 250000,
    "max": 350000,
    "formatted_range": "₹2.50 L - ₹3.50 L",
    "annual_range": "₹2,50,000 - ₹3,50,000 per annum",
    "monthly_range": "₹20,833 - ₹29,166 per month",
    "factors": {
      "base_role_salary": "₹3,50,000",
      "experience_multiplier": "1.0x",
      "location_adjustment": "0.6x",
      "skill_bonus": "+15%"
    },
    "note": "As a fresher, focus on gaining experience..."
  },
  "recommendations": {
    "immediate_priorities": [
      {
        "action": "Master SQL",
        "reason": "SQL is essential for data extraction",
        "target": "Advanced",
        "estimated_time": "6-8 weeks"
      }
    ],
    "learning_resources": [
      {
        "skill": "SQL",
        "priority": "High",
        "resources": [
          {
            "name": "SQLBolt",
            "type": "Interactive Tutorial",
            "url": "https://sqlbolt.com",
            "cost": "Free",
            "duration": "2-3 weeks"
          }
        ],
        "practice_tips": "Solve at least 50 SQL problems..."
      }
    ],
    "timeline": {
      "ready_for_jobs": "3-4 months",
      "competitive_profile": "6-8 months",
      "milestones": [
        {
          "month": 1,
          "goal": "Complete foundational learning in top priority skills"
        }
      ]
    },
    "job_search_tips": [
      "Highlight Excel and SQL prominently in your resume",
      "Create a GitHub portfolio with 2-3 data analysis projects"
    ],
    "certifications": [
      {
        "name": "Google Data Analytics Certificate",
        "provider": "Coursera",
        "cost": "₹3,000-5,000",
        "duration": "6 months",
        "value": "High - well recognized in Indian market"
      }
    ]
  },
  "role_info": {
    "title": "Data Analyst",
    "description": "Analyzes data to derive insights and support business decision-making"
  }
}
```

**Error Responses:**

400 Bad Request:
```json
{
  "error": "Invalid job role"
}
```

500 Internal Server Error:
```json
{
  "error": "Error message description"
}
```

---

### 4. Get Role Skills
Get required skills for a specific role.

**Endpoint:** `GET /api/skills/<role>`

**Example:** `GET /api/skills/Data Analyst`

**Response:**
```json
{
  "role": "Data Analyst",
  "required_skills": {
    "SQL": {
      "importance": 0.95,
      "min_level": "advanced",
      "note": "SQL is the most critical skill..."
    },
    "Excel": {
      "importance": 0.85,
      "min_level": "advanced",
      "note": "Advanced Excel including pivot tables..."
    }
  }
}
```

**Error Response (404):**
```json
{
  "error": "Role not found"
}
```

---

## Data Models

### Job Fit Score Algorithm

```
Base Score = Σ(User Proficiency Weight × Skill Importance × 100) / Total Importance

Proficiency Weights:
- Expert: 1.0
- Advanced: 0.75
- Intermediate: 0.5
- Beginner: 0.25

Experience Bonuses:
- Fresher: +0
- 1-2 years: +5
- 3-5 years: +10
- 5+ years: +15

Education Bonuses:
- PhD: +10
- Masters: +5
- Bachelors: +0
- Diploma: -5

Final Score = min(Base Score + Experience Bonus + Education Bonus, 100)
```

### Salary Calculation

```
Estimated Salary = Base Salary × Experience Multiplier × Location Multiplier × (1 + Skill Bonus)

Experience Multipliers:
- Fresher: 1.0x
- 1-2 years: 1.4x
- 3-5 years: 2.0x
- 5+ years: 2.8x

Location Multipliers:
- Tier 1: 1.0x
- Tier 2: 0.75x
- Tier 3: 0.60x
- Remote: 0.70x

Skill Bonus: (Job Fit Score / 100) × 0.30 (up to 30% bonus)

Range: ±12% of estimated salary
```

---

## Rate Limits

Currently no rate limits implemented (local development).

For production deployment, recommended limits:
- 100 requests per hour per IP
- 1000 requests per day per IP

---

## CORS

CORS is enabled for all origins in development.

For production, configure allowed origins:
```python
CORS(app, origins=["https://yourdomain.com"])
```

---

## Error Handling

All endpoints return appropriate HTTP status codes:

- `200 OK`: Successful request
- `400 Bad Request`: Invalid input
- `404 Not Found`: Resource not found
- `500 Internal Server Error`: Server error

Error responses include a JSON object with an `error` field describing the issue.

---

## Sample Integration

### JavaScript (Fetch)

```javascript
const analyzeProfile = async () => {
  const response = await fetch('http://localhost:5000/api/analyze', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      role: 'Data Analyst',
      skills: {
        'Python': 'intermediate',
        'SQL': 'beginner'
      },
      experience: 'fresher',
      education: 'bachelors',
      location: 'tier3'
    })
  });
  
  const data = await response.json();
  console.log(data);
};
```

### Python (Requests)

```python
import requests

url = 'http://localhost:5000/api/analyze'
payload = {
    'role': 'Data Analyst',
    'skills': {
        'Python': 'intermediate',
        'SQL': 'beginner'
    },
    'experience': 'fresher',
    'education': 'bachelors',
    'location': 'tier3'
}

response = requests.post(url, json=payload)
data = response.json()
print(data)
```

### cURL

```bash
curl -X POST http://localhost:5000/api/analyze \
  -H "Content-Type: application/json" \
  -d '{
    "role": "Data Analyst",
    "skills": {
      "Python": "intermediate",
      "SQL": "beginner"
    },
    "experience": "fresher",
    "education": "bachelors",
    "location": "tier3"
  }'
```

---

## Testing

Test the API using tools like:
- Postman
- Insomnia
- Thunder Client (VS Code extension)
- Browser DevTools

---

## Version History

- **v1.0.0** (Feb 2025): Initial release
  - 5 job roles supported
  - Job fit scoring
  - Salary estimation
  - Personalized recommendations
