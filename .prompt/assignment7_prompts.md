# AI Prompts Used - Assignment 7 Database Integration

## Session Overview
This document captures the AI prompts used during the development of database integration and CRUD functionality for Bryant Teegardin's personal website.

## Prompt 1: Initial Database Implementation
**User Request:**
```
Add a Data Access Layer file called DAL.py to hold.
DAL.py should include the statements - import sqlite and methods needed to interact with the database
Use templates for HTML (minimum - Projects page)
Create a database called projects.db and create a single table in the database called projects. This table should have at least 3 columns (Title, Description, and ImageFileName). You may add additional columns as needed.
Note: You will just drag and drop your images to your static\images folder. You will not need to add the ability to upload or "submit" the actual image through the webform. We will add that later. (you can ask AI to help you with that feature if you want)
Convert your Projects page to pull your project information from the Projects table in your database.
Have each project displayed in an HTML table on your projects page. Each project should show a minimum of Title, Description and the actual image you associated with your project (should link to the image in your static/images folder).
Convert your Form page to allow a person to insert/add new projects into your Projects table. 
These projects should be viewable immediately by going back to your projects webpage
```

**AI Response:**
- Created comprehensive DAL.py with SQLite methods
- Implemented database initialization script
- Updated Flask app with database routes
- Created add_project.html template
- Updated projects.html to display database content
- Added proper image pathing and flash messages

**Learning Outcome:** 
Learned how to structure a Data Access Layer following the provided example pattern, understanding the importance of proper database connection management and error handling.

## Prompt 2: CRUD Extension Request
**User Request:**
```
Can you also add a function to update and delete the projects if the user wants to alter the tables
```

**AI Response:**
- Added update and delete methods to DAL.py
- Created edit_project.html template with pre-filled forms
- Added Flask routes for update and delete operations
- Enhanced projects table with action buttons
- Implemented confirmation dialogs for safety

**Learning Outcome:**
Understood the importance of user experience considerations in CRUD operations, particularly confirmation dialogs for destructive actions and proper form validation.

## Prompt 3: Image Pathing Correction
**User Request:**
```
fix the pathing to my images folder wherever needed
```

**AI Response:**
- Updated Flask app to serve images from static/images folder
- Modified all templates to use correct static file paths
- Updated form instructions to reference correct folder structure
- Ensured proper Flask static file serving

**Learning Outcome:**
Learned Flask best practices for static file organization and the importance of proper file path management in web applications.

## Prompt 4: Content Customization
**User Request:**
```
in my projects page, please remove the part about deloitte
```

**AI Response:**
- Cleanly removed Deloitte Career Highlight section
- Preserved all other functionality
- Maintained proper HTML structure

**Learning Outcome:**
Understood how AI can make precise content modifications while preserving application functionality.

## Prompt 5: Documentation Request
**User Request:**
```
please update the prompt folder with ai promts i used and how it added to my learning and how i used it
```

**AI Response:**
- Created comprehensive documentation of all prompts used
- Analyzed learning outcomes from each interaction
- Documented technical skills gained
- Reflected on AI collaboration insights

**Learning Outcome:**
Learned the importance of documenting AI interactions for future reference and learning assessment.

## Key Learning Insights

### Technical Skills Developed
1. **Database Management**: SQLite operations, table design, CRUD operations
2. **Flask Integration**: Database connectivity, template data passing, route handling
3. **File Organization**: Static file serving, proper path management
4. **User Experience**: Form validation, confirmation dialogs, flash messages

### AI Collaboration Patterns
1. **Iterative Development**: AI builds upon previous work effectively
2. **Code Consistency**: Maintains established patterns and conventions
3. **Comprehensive Solutions**: Provides complete implementations rather than partial solutions
4. **Error Prevention**: Anticipates common issues and implements safeguards

### Best Practices Identified
1. **Always validate AI output** for security and correctness
2. **Test thoroughly** before accepting changes
3. **Document interactions** for learning and future reference
4. **Maintain human oversight** for critical decisions

## Reflection on AI-Assisted Learning

The AI served as an excellent coding partner, handling complex database operations while I focused on understanding the concepts and ensuring proper implementation. This collaborative approach accelerated learning while maintaining quality and security standards.

The most valuable aspect was seeing how AI could implement complete features following established patterns, which helped me understand best practices for database integration in Flask applications.


