from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os

# Set the static folder to the parent directory
app = Flask(__name__, static_folder='.', static_url_path='')

# Route for the homepage
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

# Route for about page
@app.route('/about')
def about():
    return send_from_directory('.', 'about.html')

# Route for resume page
@app.route('/resume')
def resume():
    return send_from_directory('.', 'resume.html')

# Route for projects page
@app.route('/projects')
def projects():
    return send_from_directory('.', 'projects.html')

# Route for contact page
@app.route('/contact')
def contact():
    return send_from_directory('.', 'contact.html')

# Route for thank you page
@app.route('/thankyou')
def thankyou():
    return send_from_directory('.', 'thankyou.html')

# Route to serve static files (CSS, JS)
@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

# Route to serve images
@app.route('/images/<path:filename>')
def images(filename):
    return send_from_directory('images', filename)

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
    return send_from_directory('.', 'index.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return send_from_directory('.', 'index.html'), 500

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
    
    app.run(debug=True, host='127.0.0.1', port=8000)
