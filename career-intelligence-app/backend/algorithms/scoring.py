"""
Job Fit Scoring Algorithm
Calculates how well a candidate matches a job role
"""

def get_proficiency_weight(proficiency_level):
    """
    Convert proficiency level to numerical weight
    """
    weights = {
        'expert': 1.0,
        'advanced': 0.75,
        'intermediate': 0.5,
        'beginner': 0.25
    }
    return weights.get(proficiency_level.lower(), 0.25)

def calculate_job_fit(target_role, user_skills, experience, education, job_roles):
    """
    Calculate job fit score (0-100)
    
    Args:
        target_role: Job role the user is targeting
        user_skills: Dict of {skill_name: proficiency_level}
        experience: Experience level (fresher, 1-2, 3-5, 5+)
        education: Education level
        job_roles: Job roles database
    
    Returns:
        Float score between 0-100
    """
    if target_role not in job_roles:
        return 0.0
    
    role_requirements = job_roles[target_role]['required_skills']
    
    # Base score from skills matching
    skill_score = 0
    total_weight = 0
    
    for skill, requirements in role_requirements.items():
        importance = requirements['importance']  # 0-1 scale
        required_level = requirements.get('min_level', 'beginner')
        
        total_weight += importance
        
        if skill.lower() in [s.lower() for s in user_skills.keys()]:
            # Find the matching skill (case-insensitive)
            user_skill = next(s for s in user_skills.keys() if s.lower() == skill.lower())
            user_level = user_skills[user_skill]
            
            # Get proficiency weight
            proficiency_weight = get_proficiency_weight(user_level)
            
            # Calculate contribution to score
            skill_score += (proficiency_weight * importance * 100)
    
    # Normalize skill score
    if total_weight > 0:
        base_score = skill_score / total_weight
    else:
        base_score = 0
    
    # Adjust for experience
    experience_bonus = {
        'fresher': 0,
        '1-2': 5,
        '3-5': 10,
        '5+': 15
    }.get(experience, 0)
    
    # Adjust for education
    education_bonus = {
        'phd': 10,
        'masters': 5,
        'bachelors': 0,
        'diploma': -5
    }.get(education.lower(), 0)
    
    # Calculate final score
    final_score = min(base_score + experience_bonus + education_bonus, 100)
    final_score = max(final_score, 0)  # Ensure non-negative
    
    return final_score

def analyze_strengths(target_role, user_skills, job_roles):
    """
    Identify user's key strengths for the role
    
    Returns:
        List of dicts with skill strengths
    """
    if target_role not in job_roles:
        return []
    
    role_requirements = job_roles[target_role]['required_skills']
    strengths = []
    
    for skill, requirements in role_requirements.items():
        if skill.lower() in [s.lower() for s in user_skills.keys()]:
            user_skill = next(s for s in user_skills.keys() if s.lower() == skill.lower())
            user_level = user_skills[user_skill]
            proficiency_weight = get_proficiency_weight(user_level)
            importance = requirements['importance']
            
            # Consider it a strength if proficiency >= 0.5 (intermediate+) 
            # and importance >= 0.6
            if proficiency_weight >= 0.5 and importance >= 0.5:
                strengths.append({
                    'skill': skill,
                    'your_level': user_level.capitalize(),
                    'importance': 'Critical' if importance > 0.8 else 'Important',
                    'note': requirements.get('note', f'Strong {skill} skills are valuable for this role')
                })
    
    # Sort by importance
    strengths.sort(key=lambda x: 1 if x['importance'] == 'Critical' else 0, reverse=True)
    
    return strengths

def identify_skill_gaps(target_role, user_skills, job_roles):
    """
    Identify missing or weak skills
    
    Returns:
        List of dicts with skill gaps
    """
    if target_role not in job_roles:
        return []
    
    role_requirements = job_roles[target_role]['required_skills']
    gaps = []
    
    # Normalize user skills to lowercase for comparison
    user_skills_lower = {k.lower(): v for k, v in user_skills.items()}
    
    for skill, requirements in role_requirements.items():
        importance = requirements['importance']
        min_level = requirements.get('min_level', 'intermediate')
        
        skill_lower = skill.lower()
        
        # Check if skill is missing
        if skill_lower not in user_skills_lower:
            if importance >= 0.6:  # Only flag important skills
                gaps.append({
                    'skill': skill,
                    'current_level': 'None',
                    'required_level': min_level.capitalize(),
                    'priority': 'High' if importance > 0.8 else 'Medium',
                    'note': requirements.get('note', f'{skill} is essential for this role')
                })
        else:
            # Check if proficiency is below required
            user_level = user_skills_lower[skill_lower]
            user_weight = get_proficiency_weight(user_level)
            required_weight = get_proficiency_weight(min_level)
            
            if user_weight < required_weight and importance >= 0.6:
                gaps.append({
                    'skill': skill,
                    'current_level': user_level.capitalize(),
                    'required_level': min_level.capitalize(),
                    'priority': 'High' if importance > 0.8 else 'Medium',
                    'note': f'Need to improve {skill} to {min_level} level'
                })
    
    # Sort by priority
    priority_order = {'High': 0, 'Medium': 1, 'Low': 2}
    gaps.sort(key=lambda x: priority_order.get(x['priority'], 3))
    
    return gaps
