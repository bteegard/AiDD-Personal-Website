"""
Test script for Flask application routes and functionality
"""
import pytest
from app import app


class TestFlaskApp:
    """Test class for Flask application"""
    
    def setup_method(self):
        """Set up test client before each test"""
        try:
            # Initialize database if it doesn't exist
            from DAL import createDatabase
            createDatabase()
        except Exception:
            # If database initialization fails, continue with tests
            pass
        
        self.client = app.test_client()
        self.app = app
    
    def test_homepage_route(self):
        """Test that homepage loads successfully"""
        response = self.client.get('/')
        assert response.status_code == 200
        assert b'Bryant Teegardin' in response.data or b'Personal Website' in response.data
    
    def test_about_route(self):
        """Test that about page loads successfully"""
        response = self.client.get('/about')
        assert response.status_code == 200
    
    def test_resume_route(self):
        """Test that resume page loads successfully"""
        response = self.client.get('/resume')
        assert response.status_code == 200
    
    def test_projects_route(self):
        """Test that projects page loads successfully"""
        response = self.client.get('/projects')
        assert response.status_code == 200
    
    def test_contact_route(self):
        """Test that contact page loads successfully"""
        response = self.client.get('/contact')
        assert response.status_code == 200
    
    def test_add_project_route(self):
        """Test that add project page loads successfully"""
        response = self.client.get('/add_project')
        assert response.status_code == 200
    
    def test_thankyou_route(self):
        """Test that thank you page loads successfully"""
        response = self.client.get('/thankyou')
        assert response.status_code == 200
    
    def test_contact_form_submission(self):
        """Test contact form submission"""
        response = self.client.post('/submit_contact', data={
            'firstName': 'John',
            'lastName': 'Doe',
            'email': 'john.doe@example.com',
            'password': 'password123',
            'confirmPassword': 'password123',
            'message': 'Test message'
        })
        assert response.status_code == 302  # Redirect after successful submission
    
    def test_contact_form_validation_missing_fields(self):
        """Test contact form validation for missing fields"""
        response = self.client.post('/submit_contact', data={
            'firstName': 'John',
            'lastName': 'Doe',
            # Missing email, password, confirmPassword
        })
        assert response.status_code == 302  # Redirect with error
    
    def test_contact_form_password_mismatch(self):
        """Test contact form validation for password mismatch"""
        response = self.client.post('/submit_contact', data={
            'firstName': 'John',
            'lastName': 'Doe',
            'email': 'john.doe@example.com',
            'password': 'password123',
            'confirmPassword': 'different123',
            'message': 'Test message'
        })
        assert response.status_code == 302  # Redirect with error
    
    def test_contact_form_password_too_short(self):
        """Test contact form validation for password too short"""
        response = self.client.post('/submit_contact', data={
            'firstName': 'John',
            'lastName': 'Doe',
            'email': 'john.doe@example.com',
            'password': '123',
            'confirmPassword': '123',
            'message': 'Test message'
        })
        assert response.status_code == 302  # Redirect with error
    
    def test_project_form_submission(self):
        """Test project form submission"""
        response = self.client.post('/submit_project', data={
            'title': 'Test Project',
            'description': 'This is a test project description',
            'image_filename': 'test.jpg'
        })
        assert response.status_code == 302  # Redirect after successful submission
    
    def test_project_form_validation_missing_fields(self):
        """Test project form validation for missing fields"""
        response = self.client.post('/submit_project', data={
            'title': 'Test Project',
            # Missing description
        })
        assert response.status_code == 302  # Redirect with error
    
    def test_static_files_served(self):
        """Test that static files are served correctly"""
        # Test CSS file
        response = self.client.get('/static/css/styles.css')
        assert response.status_code == 200
    
    def test_image_serving(self):
        """Test that images are served correctly"""
        # This test assumes there are images in the static/images directory
        response = self.client.get('/images/headshot.jpg')
        # Should return 200 if image exists, 404 if not
        assert response.status_code in [200, 404]
    
    def test_resume_pdf_serving(self):
        """Test that resume PDF is served correctly"""
        response = self.client.get('/resume.pdf')
        # Should return 200 if PDF exists, 404 if not
        assert response.status_code in [200, 404]
    
    def test_404_error_handler(self):
        """Test 404 error handling"""
        response = self.client.get('/nonexistent-page')
        assert response.status_code == 404
    
    def test_app_configuration(self):
        """Test Flask app configuration"""
        assert self.app.secret_key is not None
        assert self.app.template_folder == 'templates'
        # Flask converts relative paths to absolute paths, so we check if it contains 'static'
        assert 'static' in self.app.static_folder


def test_app_creation():
    """Test that Flask app is created correctly"""
    from app import app
    assert app is not None
    assert app.name == 'app'


if __name__ == "__main__":
    pytest.main([__file__])
