// Configuration
const API_URL = 'http://localhost:5000/api';

// Global state
let analysisResults = null;

// Initialize app
document.addEventListener('DOMContentLoaded', function() {
    setupEventListeners();
});

// Event Listeners
function setupEventListeners() {
    const form = document.getElementById('career-form');
    form.addEventListener('submit', handleFormSubmit);
}

// Add new skill input row
function addSkill() {
    const container = document.getElementById('skills-container');
    const newRow = document.createElement('div');
    newRow.className = 'skill-input-row';
    newRow.innerHTML = `
        <input type="text" class="skill-name" placeholder="Skill name (e.g., Python)" required>
        <select class="skill-level" required>
            <option value="">Level...</option>
            <option value="beginner">Beginner</option>
            <option value="intermediate">Intermediate</option>
            <option value="advanced">Advanced</option>
            <option value="expert">Expert</option>
        </select>
        <button type="button" class="btn-remove" onclick="removeSkill(this)">×</button>
    `;
    container.appendChild(newRow);
}

// Remove skill input row
function removeSkill(button) {
    const container = document.getElementById('skills-container');
    if (container.children.length > 1) {
        button.parentElement.remove();
    } else {
        alert('You must have at least one skill!');
    }
}

// Handle form submission
async function handleFormSubmit(e) {
    e.preventDefault();
    
    // Collect form data
    const formData = collectFormData();
    
    if (!validateFormData(formData)) {
        return;
    }
    
    // Show loading, hide form
    showLoading();
    
    try {
        // Call API
        const results = await analyzeProfile(formData);
        
        // Store results
        analysisResults = results;
        
        // Display results
        displayResults(results);
        
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred while analyzing your profile. Please try again.');
        hideLoading();
    }
}

// Collect form data
function collectFormData() {
    const role = document.getElementById('job-role').value;
    const experience = document.getElementById('experience').value;
    const education = document.getElementById('education').value;
    const location = document.getElementById('location').value;
    
    // Collect skills
    const skillRows = document.querySelectorAll('.skill-input-row');
    const skills = {};
    
    skillRows.forEach(row => {
        const name = row.querySelector('.skill-name').value.trim();
        const level = row.querySelector('.skill-level').value;
        if (name && level) {
            skills[name] = level;
        }
    });
    
    return {
        role,
        skills,
        experience,
        education,
        location
    };
}

// Validate form data
function validateFormData(data) {
    if (!data.role) {
        alert('Please select a job role');
        return false;
    }
    
    if (Object.keys(data.skills).length === 0) {
        alert('Please add at least one skill');
        return false;
    }
    
    if (!data.experience || !data.education || !data.location) {
        alert('Please fill in all required fields');
        return false;
    }
    
    return true;
}

// Call API to analyze profile
async function analyzeProfile(data) {
    const response = await fetch(`${API_URL}/analyze`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    });
    
    if (!response.ok) {
        throw new Error('API request failed');
    }
    
    return await response.json();
}

// Display results
function displayResults(results) {
    hideLoading();
    
    // Show results section
    document.getElementById('input-section').classList.add('hidden');
    document.getElementById('results-section').classList.remove('hidden');
    
    // Display each component
    displayScore(results.job_fit_score);
    displaySalary(results.salary_estimate);
    displayStrengths(results.strengths);
    displayGaps(results.skill_gaps);
    displayRecommendations(results.recommendations);
    
    // Scroll to results
    document.getElementById('results-section').scrollIntoView({ behavior: 'smooth' });
}

// Display job fit score
function displayScore(score) {
    const scoreValue = document.getElementById('score-value');
    const scoreCircle = document.getElementById('score-circle');
    const interpretation = document.getElementById('score-interpretation');
    
    // Animate score
    animateValue(scoreValue, 0, score, 1500);
    
    // Set border color based on score
    if (score >= 80) {
        scoreCircle.style.borderColor = 'rgba(16, 185, 129, 0.8)';
        interpretation.textContent = 'Excellent! You\'re highly competitive for this role.';
    } else if (score >= 60) {
        scoreCircle.style.borderColor = 'rgba(245, 158, 11, 0.8)';
        interpretation.textContent = 'Good fit! Some upskilling will make you very competitive.';
    } else if (score >= 40) {
        scoreCircle.style.borderColor = 'rgba(251, 191, 36, 0.8)';
        interpretation.textContent = 'Moderate fit. Focus on key skill gaps to improve your chances.';
    } else {
        scoreCircle.style.borderColor = 'rgba(239, 68, 68, 0.8)';
        interpretation.textContent = 'Significant upskilling needed. Follow the recommendations below.';
    }
}

// Animate number
function animateValue(element, start, end, duration) {
    let startTimestamp = null;
    const step = (timestamp) => {
        if (!startTimestamp) startTimestamp = timestamp;
        const progress = Math.min((timestamp - startTimestamp) / duration, 1);
        element.textContent = Math.floor(progress * (end - start) + start);
        if (progress < 1) {
            window.requestAnimationFrame(step);
        }
    };
    window.requestAnimationFrame(step);
}

// Display salary estimate
function displaySalary(salary) {
    const container = document.getElementById('salary-info');
    
    container.innerHTML = `
        <div class="salary-range">
            <h3>Annual Salary Range</h3>
            <p style="font-size: 1.75rem; font-weight: 700; margin: 1rem 0;">
                ${salary.formatted_range}
            </p>
            <p style="opacity: 0.9;">${salary.annual_range}</p>
        </div>
        
        <div class="salary-details">
            <div class="salary-detail">
                <label>Monthly Range</label>
                <strong>${salary.monthly_range}</strong>
            </div>
            <div class="salary-detail">
                <label>Base Salary Factor</label>
                <strong>${salary.factors.base_role_salary}</strong>
            </div>
            <div class="salary-detail">
                <label>Experience Multiplier</label>
                <strong>${salary.factors.experience_multiplier}</strong>
            </div>
            <div class="salary-detail">
                <label>Location Adjustment</label>
                <strong>${salary.factors.location_adjustment}</strong>
            </div>
        </div>
        
        <p class="mt-2" style="background: var(--bg-color); padding: 1rem; border-radius: 8px; margin-top: 1rem;">
            <strong>Note:</strong> ${salary.note}
        </p>
    `;
}

// Display strengths
function displayStrengths(strengths) {
    const container = document.getElementById('strengths-list');
    
    if (strengths.length === 0) {
        container.innerHTML = '<p>No major strengths identified for this role. Focus on building the required skills.</p>';
        return;
    }
    
    container.innerHTML = strengths.map(strength => `
        <div class="strength-item">
            <h4>${strength.skill}</h4>
            <span class="badge badge-success">${strength.your_level}</span>
            <span class="badge ${strength.importance === 'Critical' ? 'badge-critical' : 'badge-warning'}">
                ${strength.importance}
            </span>
            <p class="mt-1">${strength.note}</p>
        </div>
    `).join('');
}

// Display skill gaps
function displayGaps(gaps) {
    const container = document.getElementById('gaps-list');
    
    if (gaps.length === 0) {
        container.innerHTML = '<p style="color: var(--secondary-color); font-weight: 600;">Great! No critical skill gaps identified.</p>';
        return;
    }
    
    container.innerHTML = gaps.map(gap => `
        <div class="gap-item">
            <h4>${gap.skill}</h4>
            <span class="badge badge-warning">Current: ${gap.current_level}</span>
            <span class="badge badge-critical">Required: ${gap.required_level}</span>
            <span class="badge ${gap.priority === 'High' ? 'badge-critical' : 'badge-warning'}">
                ${gap.priority} Priority
            </span>
            <p class="mt-1">${gap.note}</p>
        </div>
    `).join('');
}

// Display recommendations
function displayRecommendations(recommendations) {
    const container = document.getElementById('recommendations-content');
    
    let html = '';
    
    // Immediate Priorities
    if (recommendations.immediate_priorities && recommendations.immediate_priorities.length > 0) {
        html += `
            <div class="recommendation-section">
                <h3>🎯 Immediate Priorities (Next 3 Months)</h3>
                <ul class="priority-list">
                    ${recommendations.immediate_priorities.map(priority => `
                        <li>
                            <strong>${priority.action}</strong>
                            <p>${priority.reason}</p>
                            <p style="color: var(--text-secondary); font-size: 0.875rem; margin-top: 0.5rem;">
                                Target: ${priority.target} | Est. Time: ${priority.estimated_time}
                            </p>
                        </li>
                    `).join('')}
                </ul>
            </div>
        `;
    }
    
    // Learning Resources
    if (recommendations.learning_resources && recommendations.learning_resources.length > 0) {
        html += `
            <div class="recommendation-section">
                <h3>📚 Learning Resources</h3>
                ${recommendations.learning_resources.map(resource => `
                    <div class="resource-card">
                        <h5>${resource.skill} <span class="badge badge-${resource.priority === 'High' ? 'critical' : 'warning'}">${resource.priority}</span></h5>
                        <p style="margin-bottom: 0.75rem;">${resource.practice_tips}</p>
                        ${resource.resources && resource.resources.length > 0 ? `
                            <ul style="margin-left: 1.5rem; color: var(--text-secondary);">
                                ${resource.resources.map(r => `
                                    <li><strong>${r.name}</strong> - ${r.type} (${r.cost}, ${r.duration})</li>
                                `).join('')}
                            </ul>
                        ` : ''}
                    </div>
                `).join('')}
            </div>
        `;
    }
    
    // Timeline
    if (recommendations.timeline) {
        const timeline = recommendations.timeline;
        html += `
            <div class="recommendation-section">
                <h3>📅 Realistic Timeline</h3>
                <p><strong>Ready for job applications:</strong> ${timeline.ready_for_jobs}</p>
                <p><strong>Competitive profile:</strong> ${timeline.competitive_profile}</p>
                
                ${timeline.milestones && timeline.milestones.length > 0 ? `
                    <div style="margin-top: 1.5rem;">
                        ${timeline.milestones.map(milestone => `
                            <div class="timeline-item">
                                <strong>Month ${milestone.month}</strong>
                                <p>${milestone.goal}</p>
                            </div>
                        `).join('')}
                    </div>
                ` : ''}
            </div>
        `;
    }
    
    // Job Search Tips
    if (recommendations.job_search_tips && recommendations.job_search_tips.length > 0) {
        html += `
            <div class="recommendation-section">
                <h3>💼 Job Search Strategy</h3>
                <div class="tips-grid">
                    ${recommendations.job_search_tips.map(tip => `
                        <div class="tip-card">
                            <p>✓ ${tip}</p>
                        </div>
                    `).join('')}
                </div>
            </div>
        `;
    }
    
    // Certifications
    if (recommendations.certifications && recommendations.certifications.length > 0) {
        html += `
            <div class="recommendation-section">
                <h3>🎓 Recommended Certifications</h3>
                ${recommendations.certifications.map(cert => `
                    <div class="resource-card">
                        <h5>${cert.name}</h5>
                        <p><strong>Provider:</strong> ${cert.provider}</p>
                        <p><strong>Cost:</strong> ${cert.cost} | <strong>Duration:</strong> ${cert.duration}</p>
                        <p><strong>Value:</strong> ${cert.value}</p>
                    </div>
                `).join('')}
            </div>
        `;
    }
    
    container.innerHTML = html;
}

// Show/hide loading
function showLoading() {
    document.getElementById('loading').classList.remove('hidden');
    document.getElementById('input-section').style.opacity = '0.5';
}

function hideLoading() {
    document.getElementById('loading').classList.add('hidden');
    document.getElementById('input-section').style.opacity = '1';
}

// Reset form
function resetForm() {
    // Hide results, show form
    document.getElementById('results-section').classList.add('hidden');
    document.getElementById('input-section').classList.remove('hidden');
    
    // Reset form
    document.getElementById('career-form').reset();
    
    // Reset to single skill input
    const container = document.getElementById('skills-container');
    container.innerHTML = `
        <div class="skill-input-row">
            <input type="text" class="skill-name" placeholder="Skill name (e.g., Python)" required>
            <select class="skill-level" required>
                <option value="">Level...</option>
                <option value="beginner">Beginner</option>
                <option value="intermediate">Intermediate</option>
                <option value="advanced">Advanced</option>
                <option value="expert">Expert</option>
            </select>
            <button type="button" class="btn-remove" onclick="removeSkill(this)">×</button>
        </div>
    `;
    
    // Scroll to top
    window.scrollTo({ top: 0, behavior: 'smooth' });
}
