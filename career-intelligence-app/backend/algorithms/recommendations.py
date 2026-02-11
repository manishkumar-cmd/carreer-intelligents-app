"""
Recommendations Engine
Generates personalized learning paths and career advice
"""

def generate_recommendations(target_role, user_skills, skill_gaps, experience, job_roles, skills_database):
    """
    Generate comprehensive recommendations for career improvement
    
    Returns:
        Dict with categorized recommendations
    """
    recommendations = {
        'immediate_priorities': [],
        'learning_resources': [],
        'timeline': {},
        'job_search_tips': [],
        'certifications': []
    }
    
    # Immediate priorities (top 3 skill gaps)
    high_priority_gaps = [gap for gap in skill_gaps if gap['priority'] == 'High'][:3]
    
    for gap in high_priority_gaps:
        skill = gap['skill']
        recommendations['immediate_priorities'].append({
            'action': f"Master {skill}",
            'reason': gap['note'],
            'target': gap['required_level'],
            'estimated_time': get_learning_time(gap['current_level'], gap['required_level'])
        })
    
    # Learning resources for each skill gap
    for gap in skill_gaps[:5]:  # Top 5 gaps
        skill = gap['skill']
        if skill in skills_database:
            skill_info = skills_database[skill]
            recommendations['learning_resources'].append({
                'skill': skill,
                'priority': gap['priority'],
                'resources': skill_info.get('resources', []),
                'practice_tips': skill_info.get('practice_tips', '')
            })
    
    # Timeline estimation
    recommendations['timeline'] = generate_timeline(skill_gaps, experience)
    
    # Job search tips based on profile
    recommendations['job_search_tips'] = generate_job_search_tips(
        target_role, 
        experience, 
        len(skill_gaps)
    )
    
    # Relevant certifications
    if target_role in job_roles:
        role_certs = job_roles[target_role].get('certifications', [])
        recommendations['certifications'] = role_certs
    
    return recommendations

def get_learning_time(current_level, target_level):
    """
    Estimate learning time to reach target proficiency
    """
    level_order = ['none', 'beginner', 'intermediate', 'advanced', 'expert']
    
    current_idx = level_order.index(current_level.lower()) if current_level.lower() in level_order else 0
    target_idx = level_order.index(target_level.lower()) if target_level.lower() in level_order else 2
    
    gap = target_idx - current_idx
    
    time_estimates = {
        1: "2-4 weeks",
        2: "6-8 weeks",
        3: "3-4 months",
        4: "6-8 months"
    }
    
    return time_estimates.get(abs(gap), "4-8 weeks")

def generate_timeline(skill_gaps, experience):
    """
    Generate realistic timeline for improvement
    """
    num_critical_gaps = len([g for g in skill_gaps if g['priority'] == 'High'])
    
    if experience == 'fresher':
        if num_critical_gaps <= 2:
            return {
                'ready_for_jobs': '3-4 months',
                'competitive_profile': '6-8 months',
                'milestones': [
                    {'month': 1, 'goal': 'Complete foundational learning in top priority skills'},
                    {'month': 2, 'goal': 'Build 1-2 portfolio projects'},
                    {'month': 3, 'goal': 'Start applying to internships and entry-level roles'},
                    {'month': 6, 'goal': 'Achieve competitive skill level, actively interview'}
                ]
            }
        else:
            return {
                'ready_for_jobs': '6-8 months',
                'competitive_profile': '10-12 months',
                'milestones': [
                    {'month': 1, 'goal': 'Focus on SQL and primary tool (Power BI/Tableau)'},
                    {'month': 3, 'goal': 'Complete 2 substantial projects'},
                    {'month': 6, 'goal': 'Start applying, continue upskilling secondary skills'},
                    {'month': 10, 'goal': 'Strong portfolio, competitive for most positions'}
                ]
            }
    else:
        return {
            'ready_for_jobs': '1-2 months',
            'competitive_profile': '3-4 months',
            'milestones': [
                {'month': 1, 'goal': 'Address critical skill gaps'},
                {'month': 2, 'goal': 'Update resume and portfolio with new skills'},
                {'month': 3, 'goal': 'Actively apply and interview'}
            ]
        }

def generate_job_search_tips(target_role, experience, num_gaps):
    """
    Generate role and profile-specific job search advice
    """
    tips = []
    
    # Role-specific tips
    role_tips = {
        'Data Analyst': [
            "Highlight Excel and SQL prominently in your resume",
            "Create a GitHub portfolio with 2-3 data analysis projects",
            "Target companies: Analytics services, startups, BFSI sector",
            "Job titles to search: Junior Data Analyst, MIS Executive, Business Analyst"
        ],
        'Software Engineer': [
            "Focus on DSA (Data Structures & Algorithms) practice",
            "Build 3-5 full-stack projects showcasing different technologies",
            "Target: Product companies, startups, service-based companies",
            "Practice on LeetCode, HackerRank for interview prep"
        ],
        'Product Manager': [
            "Create case studies of product analysis and strategy",
            "Network extensively on LinkedIn with PMs",
            "Target: Startups, tech companies, e-commerce platforms",
            "Demonstrate analytical and communication skills in applications"
        ]
    }
    
    tips.extend(role_tips.get(target_role, [
        "Research companies hiring for this role in India",
        "Tailor your resume to highlight relevant skills",
        "Network with professionals in this field"
    ]))
    
    # Experience-based tips
    if experience == 'fresher':
        tips.extend([
            "Consider internships (3-6 months) as entry points",
            "Use Internshala, AngelList for startup opportunities",
            "Attend virtual career fairs and webinars",
            "Join relevant LinkedIn groups and engage with content"
        ])
    
    # Gap-based advice
    if num_gaps > 3:
        tips.append("Focus on upskilling before mass applying - quality over quantity")
        tips.append("Consider freelance projects on Upwork/Fiverr to gain practical experience")
    else:
        tips.append("Your profile is competitive - start applying actively")
    
    return tips[:8]  # Return top 8 tips
