# Projects Database Integration

This project now includes a Data Access Layer (DAL) and database integration for managing projects with full CRUD (Create, Read, Update, Delete) functionality.

## Files Added/Modified

### New Files:
- `DAL.py` - Data Access Layer with SQLite database methods
- `templates/add_project.html` - Form page for adding new projects
- `templates/edit_project.html` - Form page for editing existing projects
- `projects.db` - SQLite database file (created automatically)

### Modified Files:
- `app.py` - Updated with database integration and CRUD routes
- `templates/base.html` - Added "Add Project" navigation link
- `templates/projects.html` - Updated to display projects from database in table format with action buttons

## Database Structure

The `projects` table includes:
- `id` (INTEGER PRIMARY KEY AUTOINCREMENT)
- `Title` (TEXT NOT NULL)
- `Description` (TEXT NOT NULL)
- `ImageFileName` (TEXT)
- `CreatedDate` (TIMESTAMP DEFAULT CURRENT_TIMESTAMP)

## Features

1. **Projects Page**: Displays all projects from the database in a clean table format with action buttons
2. **Add Project Form**: Allows users to add new projects with title, description, and image filename
3. **Edit Project Form**: Allows users to update existing projects with pre-filled form data
4. **Delete Projects**: One-click deletion with confirmation dialog
5. **Image Support**: Projects can include images from the `/static/images/` folder
6. **Flash Messages**: Success/error messages for all operations
7. **Responsive Design**: All pages maintain the existing dark purple theme
8. **Confirmation Dialogs**: Safety prompts for destructive actions

## Usage

1. **View Projects**: Navigate to `/projects` to see all projects in a table with action buttons
2. **Add Project**: Click "Add Project" in navigation or go to `/add_project`
3. **Edit Project**: Click the "Edit" button next to any project in the table
4. **Delete Project**: Click the "Delete" button next to any project (with confirmation)
5. **Image Management**: Place images in the `/static/images/` folder and reference them by filename

## Database Methods (DAL.py)

- `createDatabase()` - Creates database and table structure
- `saveProjectDB(title, description, image_filename)` - Adds new project
- `getAllProjects()` - Retrieves all projects as list of dictionaries (includes ID)
- `getProjectById(project_id)` - Gets specific project by ID
- `updateProjectById(project_id, title, description, image_filename)` - Updates existing project
- `deleteProjectById(project_id)` - Deletes project by ID

## Routes

- `GET /projects` - Display all projects
- `GET /add_project` - Show add project form
- `POST /submit_project` - Handle new project submission
- `GET /edit_project/<id>` - Show edit project form
- `POST /update_project/<id>` - Handle project update
- `POST /delete_project/<id>` - Handle project deletion

## Sample Data

The database is initialized with 3 sample projects:
1. Enterprise Business Architecture Tool
2. Technology Education Program  
3. Deloitte Data Challenge Case Competition

## Running the Application

1. Run `python app.py` to start the Flask server
2. Visit `http://localhost:8000/projects` to view projects
3. Visit `http://localhost:8000/add_project` to add new projects
4. Click "Edit" or "Delete" buttons in the projects table for management actions

## Security Features

- Form validation for required fields
- Confirmation dialogs for destructive actions
- Error handling with user-friendly messages
- SQL injection protection through parameterized queries
