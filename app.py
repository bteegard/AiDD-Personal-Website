from flask import Flask, render_template, request, redirect, url_for, send_from_directory, flash
import os
from DAL import getAllProjects, saveProjectDB, getProjectById, updateProjectById, deleteProjectById

# Initialize Flask app with templates and static folders
app = Flask(__name__, 
            template_folder='templates',
            static_folder='static')

# Set secret key for flash messages
app.secret_key = 'your-secret-key-here'

# Route to serve images from the static/images directory
@app.route('/images/<path:filename>')
def serve_image(filename):
    return send_from_directory('static/images', filename)

# Route to serve resume PDF
@app.route('/resume.pdf')
def serve_resume():
    return send_from_directory('.', 'resume.pdf')

# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route for about page
@app.route('/about')
def about():
    return render_template('about.html')

# Route for resume page
@app.route('/resume')
def resume():
    return render_template('resume.html')

# Route for projects page
@app.route('/projects')
def projects():
    # Get all projects from the database
    projects_list = getAllProjects()
    return render_template('projects.html', projects=projects_list)

# Route for contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Route for add project form page
@app.route('/add_project')
def add_project():
    return render_template('add_project.html')

# Route for handling project form submission
@app.route('/submit_project', methods=['POST'])
def submit_project():
    # Get form data
    title = request.form.get('title')
    description = request.form.get('description')
    image_filename = request.form.get('image_filename')
    
    # Basic validation
    if not title or not description:
        flash('Title and Description are required fields.', 'error')
        return redirect(url_for('add_project'))
    
    # If no image filename provided, use placeholder
    if not image_filename:
        image_filename = "placeholder.png"
    
    try:
        # Save project to database
        saveProjectDB(title, description, image_filename)
        flash('Project added successfully!', 'success')
        return redirect(url_for('projects'))
    except Exception as e:
        flash(f'Error adding project: {str(e)}', 'error')
        return redirect(url_for('add_project'))

# Route for editing a project
@app.route('/edit_project/<int:project_id>')
def edit_project(project_id):
    project = getProjectById(project_id)
    if not project:
        flash('Project not found.', 'error')
        return redirect(url_for('projects'))
    return render_template('edit_project.html', project=project, project_id=project_id)

# Route for handling project update
@app.route('/update_project/<int:project_id>', methods=['POST'])
def update_project(project_id):
    # Get form data
    title = request.form.get('title')
    description = request.form.get('description')
    image_filename = request.form.get('image_filename')
    
    # Basic validation
    if not title or not description:
        flash('Title and Description are required fields.', 'error')
        return redirect(url_for('edit_project', project_id=project_id))
    
    # If no image filename provided, use placeholder
    if not image_filename:
        image_filename = "placeholder.png"
    
    try:
        # Update project in database
        success = updateProjectById(project_id, title, description, image_filename)
        if success:
            flash('Project updated successfully!', 'success')
        else:
            flash('Project not found or no changes made.', 'error')
        return redirect(url_for('projects'))
    except Exception as e:
        flash(f'Error updating project: {str(e)}', 'error')
        return redirect(url_for('edit_project', project_id=project_id))

# Route for deleting a project
@app.route('/delete_project/<int:project_id>', methods=['POST'])
def delete_project(project_id):
    try:
        success = deleteProjectById(project_id)
        if success:
            flash('Project deleted successfully!', 'success')
        else:
            flash('Project not found.', 'error')
    except Exception as e:
        flash(f'Error deleting project: {str(e)}', 'error')
    return redirect(url_for('projects'))

# Route for thank you page
@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

# Handle form submission from contact page
@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    # Get form data
    first_name = request.form.get('firstName')
    last_name = request.form.get('lastName')
    email = request.form.get('email')
    password = request.form.get('password')
    confirm_password = request.form.get('confirmPassword')
    message = request.form.get('message')
    
    # Basic validation
    if not first_name or not last_name or not email or not password or not confirm_password:
        return redirect(url_for('contact') + '?error=missing_fields')
    
    if password != confirm_password:
        return redirect(url_for('contact') + '?error=password_mismatch')
    
    if len(password) < 8:
        return redirect(url_for('contact') + '?error=password_too_short')
    
    # In a real application, you would save this data to a database
    # For now, we'll just redirect to the thank you page
    return redirect(url_for('thankyou'))

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return render_template('index.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('index.html'), 500

if __name__ == '__main__':
    print("=" * 60)
    print("Bryant Teegardin's Personal Website")
    print("=" * 60)
    print("MSIS Student at Indiana Kelley School of Business")
    print("Passionate about kayaking, rock climbing, and weight lifting")
    print("Website theme: Dark Purple")
    print("=" * 60)
    print("Starting Flask server...")
    print("Your website will be available at: http://localhost:8000")
    print("=" * 60)
    print("Instructions:")
    print("   1. Add your profile photo to the /images/ directory")
    print("   2. Update your resume content in resume.html")
    print("   3. Add your actual project details in projects.html")
    print("   4. Update contact information with your real details")
    print("   5. Upload your resume as resume.pdf in the root directory")
    print("=" * 60)
    print("Press Ctrl+C to stop the server")
    print("=" * 60)
    
    app.run(debug=True, host='0.0.0.0', port=8000)
