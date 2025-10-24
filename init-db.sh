#!/bin/bash

# Database initialization script for Docker container
# This script ensures the database is properly set up

echo "Initializing database..."

# Create data directory if it doesn't exist
mkdir -p /app/data

# Change to app directory
cd /app

# Initialize the database using Python
python3 -c "
import sys
sys.path.append('/app')
from DAL import createDatabase
createDatabase()
print('Database initialized successfully!')
"

# Add some sample data if the database is empty
python3 -c "
import sys
sys.path.append('/app')
from DAL import getAllProjects, saveProjectDB

# Check if database has any projects
projects = getAllProjects()
if len(projects) == 0:
    print('Adding sample project...')
    saveProjectDB(
        'Sample Project', 
        'This is a sample project to demonstrate the website functionality.', 
        'placeholder.png'
    )
    print('Sample project added!')
else:
    print(f'Database already contains {len(projects)} projects.')
"

echo "Database initialization complete!"
