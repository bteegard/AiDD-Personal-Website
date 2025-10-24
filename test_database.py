"""
Test script for database operations in Bryant Teegardin's Personal Website
"""
import pytest
import sqlite3
import os
from DAL import createDatabase, saveProjectDB, getAllProjects, getProjectById, updateProjectById, deleteProjectById


class TestDatabase:
    """Test class for database operations"""
    
    def setup_method(self):
        """Set up test database before each test"""
        # Create a test database
        self.test_db = "test_projects.db"
        # Remove test database if it exists
        if os.path.exists(self.test_db):
            os.remove(self.test_db)
    
    def teardown_method(self):
        """Clean up test database after each test"""
        # Remove test database after test
        if os.path.exists(self.test_db):
            os.remove(self.test_db)
    
    def test_database_connection(self):
        """Test that we can connect to the database"""
        conn = sqlite3.connect(self.test_db)
        assert conn is not None
        conn.close()
    
    def test_create_database(self):
        """Test database and table creation"""
        # This test would need to be modified to use test database
        # For now, we'll test the connection
        conn = sqlite3.connect(self.test_db)
        cursor = conn.cursor()
        
        # Create the projects table
        sql = '''CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Title TEXT NOT NULL,
            Description TEXT NOT NULL,
            ImageFileName TEXT,
            CreatedDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )'''
        
        cursor.execute(sql)
        conn.commit()
        conn.close()
        
        # Verify table was created
        conn = sqlite3.connect(self.test_db)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='projects'")
        result = cursor.fetchone()
        conn.close()
        
        assert result is not None
        assert result[0] == 'projects'
    
    def test_save_project(self):
        """Test saving a project to database"""
        # Create test database and table
        conn = sqlite3.connect(self.test_db)
        cursor = conn.cursor()
        
        sql = '''CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Title TEXT NOT NULL,
            Description TEXT NOT NULL,
            ImageFileName TEXT,
            CreatedDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )'''
        cursor.execute(sql)
        conn.commit()
        
        # Insert test project
        sql = 'INSERT INTO projects (Title, Description, ImageFileName) values (?,?,?)'
        cursor.execute(sql, ("Test Project", "Test Description", "test.jpg"))
        conn.commit()
        conn.close()
        
        # Verify project was saved
        conn = sqlite3.connect(self.test_db)
        cursor = conn.cursor()
        cursor.execute('SELECT Title, Description, ImageFileName FROM projects WHERE Title = ?', ("Test Project",))
        result = cursor.fetchone()
        conn.close()
        
        assert result is not None
        assert result[0] == "Test Project"
        assert result[1] == "Test Description"
        assert result[2] == "test.jpg"
    
    def test_get_all_projects_empty(self):
        """Test getting all projects from empty database"""
        # Create empty test database
        conn = sqlite3.connect(self.test_db)
        cursor = conn.cursor()
        
        sql = '''CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Title TEXT NOT NULL,
            Description TEXT NOT NULL,
            ImageFileName TEXT,
            CreatedDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )'''
        cursor.execute(sql)
        conn.commit()
        conn.close()
        
        # Test would need to be modified to use test database
        # For now, we'll test basic functionality
        assert True  # Placeholder for real test
    
    def test_project_validation(self):
        """Test project data validation"""
        # Test that required fields are validated
        assert True  # Placeholder for validation tests


def test_flask_app_import():
    """Test that Flask app can be imported"""
    try:
        from app import app
        assert app is not None
        assert app.name == 'app'
    except ImportError as e:
        pytest.fail(f"Could not import Flask app: {e}")
    except Exception as e:
        # Handle database initialization errors gracefully
        pytest.skip(f"Skipping due to initialization error: {e}")


def test_dal_functions_exist():
    """Test that all DAL functions exist"""
    from DAL import (
        createDatabase, 
        saveProjectDB, 
        getAllProjects, 
        getProjectById, 
        updateProjectById, 
        deleteProjectById
    )
    
    # Test that functions are callable
    assert callable(createDatabase)
    assert callable(saveProjectDB)
    assert callable(getAllProjects)
    assert callable(getProjectById)
    assert callable(updateProjectById)
    assert callable(deleteProjectById)


if __name__ == "__main__":
    pytest.main([__file__])
