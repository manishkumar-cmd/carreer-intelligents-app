"""
Career Intelligence App - Backend API
A Flask-based backend for career analysis and job fit predictions
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import json
from algorithms.scoring import calculate_job_fit, analyze_strengths, identify_skill_gaps
from algorithms.salary_estimation import estimate_salary
from algorithms.recommendations import generate_recommendations
import os

app = Flask(__name__)
CORS(app)  # Enable cross-origin requests from frontend

# Load job market data
def load_data(filename):
    """Load JSON data files"""
    filepath = os.path.join('data', filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

# Global data stores
JOB_ROLES = load_data('job_roles.json')
SALARY_DATA = load_data('salary_data.json')
SKILLS_DATABASE = load_data('skills_database.json')

@app.route('/')
def home():
    """API health check"""
    return jsonify({
        'status': 'active',
        'message': 'Career Intelligence API is running',
        'version': '1.0.0'
    })

@app.route('/api/roles', methods=['GET'])
def get_roles():
    """Get list of available job roles"""
    roles = list(JOB_ROLES.keys())
    return jsonify({'roles': roles})

@app.route('/api/analyze', methods=['POST'])
def analyze_profile():
    """
    Main endpoint for career analysis
    Expects JSON payload with user profile data
    """
    try:
        data = request.get_json()
        
        # Extract user data
        target_role = data.get('role')
        user_skills = data.get('skills', {})
        experience = data.get('experience', 'fresher')
        education = data.get('education', 'bachelors')
        location = data.get('location', 'tier3')
        
        # Validate role
        if target_role not in JOB_ROLES:
            return jsonify({'error': 'Invalid job role'}), 400
        
        # Calculate job fit score
        fit_score = calculate_job_fit(
            target_role, 
            user_skills, 
            experience, 
            education,
            JOB_ROLES
        )
        
        # Analyze strengths
        strengths = analyze_strengths(
            target_role,
            user_skills,
            JOB_ROLES
        )
        
        # Identify skill gaps
        skill_gaps = identify_skill_gaps(
            target_role,
            user_skills,
            JOB_ROLES
        )
        
        # Estimate salary
        salary_range = estimate_salary(
            target_role,
            location,
            experience,
            fit_score,
            SALARY_DATA
        )
        
        # Generate recommendations
        recommendations = generate_recommendations(
            target_role,
            user_skills,
            skill_gaps,
            experience,
            JOB_ROLES,
            SKILLS_DATABASE
        )
        
        # Prepare response
        response = {
            'job_fit_score': round(fit_score, 1),
            'strengths': strengths,
            'skill_gaps': skill_gaps,
            'salary_estimate': salary_range,
            'recommendations': recommendations,
            'role_info': {
                'title': target_role,
                'description': JOB_ROLES[target_role].get('description', '')
            }
        }
        
        return jsonify(response)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/skills/<role>', methods=['GET'])
def get_role_skills(role):
    """Get required skills for a specific role"""
    if role not in JOB_ROLES:
        return jsonify({'error': 'Role not found'}), 404
    
    return jsonify({
        'role': role,
        'required_skills': JOB_ROLES[role]['required_skills']
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
