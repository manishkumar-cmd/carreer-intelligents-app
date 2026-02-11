"""
Salary Estimation Algorithm
Estimates salary range based on role, location, experience, and skills
"""

def estimate_salary(target_role, location, experience, fit_score, salary_data):
    """
    Estimate salary range in INR
    
    Args:
        target_role: Job role
        location: tier1, tier2, tier3, or remote
        experience: fresher, 1-2, 3-5, 5+
        fit_score: Job fit score (0-100)
        salary_data: Salary database
    
    Returns:
        Dict with salary range information
    """
    # Get base salary for the role
    if target_role not in salary_data:
        # Default fallback
        base_salary = 350000
    else:
        role_salary_data = salary_data[target_role]
        base_salary = role_salary_data.get('base_salary', 350000)
    
    # Experience multiplier
    experience_multipliers = {
        'fresher': 1.0,
        '1-2': 1.4,
        '3-5': 2.0,
        '5+': 2.8
    }
    exp_multiplier = experience_multipliers.get(experience, 1.0)
    
    # Location adjustment
    location_multipliers = {
        'tier1': 1.0,
        'tier2': 0.75,
        'tier3': 0.60,
        'remote': 0.70
    }
    loc_multiplier = location_multipliers.get(location.lower(), 0.70)
    
    # Skill fit bonus (up to 30% bonus for high fit scores)
    skill_bonus = (fit_score / 100) * 0.30
    
    # Calculate estimated salary
    estimated_salary = base_salary * exp_multiplier * loc_multiplier * (1 + skill_bonus)
    
    # Create range (±12%)
    min_salary = estimated_salary * 0.88
    max_salary = estimated_salary * 1.12
    
    # Round to nearest 10,000
    min_salary = round(min_salary / 10000) * 10000
    max_salary = round(max_salary / 10000) * 10000
    
    # Format for Indian numbering system
    def format_inr(amount):
        """Format amount in Indian numbering system"""
        amount = int(amount)
        if amount >= 10000000:  # 1 Crore+
            crores = amount / 10000000
            return f"₹{crores:.2f} Cr"
        elif amount >= 100000:  # 1 Lakh+
            lakhs = amount / 100000
            return f"₹{lakhs:.2f} L"
        else:
            thousands = amount / 1000
            return f"₹{thousands:.0f}K"
    
    # Prepare result
    result = {
        'min': int(min_salary),
        'max': int(max_salary),
        'formatted_range': f"{format_inr(min_salary)} - {format_inr(max_salary)}",
        'annual_range': f"₹{int(min_salary):,} - ₹{int(max_salary):,} per annum",
        'monthly_range': f"₹{int(min_salary/12):,} - ₹{int(max_salary/12):,} per month",
        'factors': {
            'base_role_salary': f"₹{int(base_salary):,}",
            'experience_multiplier': f"{exp_multiplier}x",
            'location_adjustment': f"{loc_multiplier}x",
            'skill_bonus': f"+{int(skill_bonus * 100)}%"
        },
        'note': get_salary_note(experience, fit_score, location)
    }
    
    return result

def get_salary_note(experience, fit_score, location):
    """
    Generate contextual note about the salary estimate
    """
    notes = []
    
    if experience == 'fresher':
        notes.append("As a fresher, focus on gaining experience and building skills.")
        if fit_score < 60:
            notes.append("Improving your skill fit score can significantly increase your earning potential.")
    
    if fit_score >= 80:
        notes.append("Your strong skill profile puts you in a competitive position for higher compensation.")
    elif fit_score < 50:
        notes.append("Upskilling in key areas can help you command better salaries.")
    
    if location == 'tier3' or location == 'remote':
        notes.append("Remote roles and tier 1 city positions may offer 20-40% higher salaries.")
    
    notes.append("Salary varies by company size, funding stage, and specific industry.")
    
    return " ".join(notes)
