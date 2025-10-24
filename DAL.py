# A. Import the sqlite library
import sqlite3

#######################################################
# 1. ADD PROJECT TO DB
#######################################################
def saveProjectDB(Title, Description, ImageFileName):
    #A. Make a connection to the database
    conn = None
    conn = sqlite3.connect("projects.db")

    #B. Write a SQL statement to insert a specific row (based on Title name)
    sql = 'INSERT INTO projects (Title, Description, ImageFileName) values (?,?,?)'

    # B. Create a workspace (aka Cursor)
    cur = conn.cursor()

    # C. Run the SQL statement from above and pass it 1 parameter for each ?
    cur.execute(sql, (Title, Description, ImageFileName,))

    # D. Save the changes
    conn.commit()
    if conn:
        conn.close()

#######################################################
# 2. SHOW PROJECTS IN A TABLE
#######################################################
#   THIS RETURNS AS LIST OF DICTIONARIES
def getAllProjects():
    # A. Connection to the database
    conn = sqlite3.connect('projects.db')

    # B. Create a workspace (aka Cursor)
    cursorObj = conn.cursor()

    # D. Run the SQL Select statement to retrieve the data
    cursorObj.execute('SELECT id, Title, Description, ImageFileName FROM projects;')

    # E. Tell Python to 'fetch' all of the records and put them in
    #     a list called allRows
    allRows = cursorObj.fetchall()

    projectListOfDictionaries = []

    for individualRow in allRows:
        # Make sure we have an image name
        if individualRow[3] is not None and individualRow[3] != "":
            Image = individualRow[3]
        else:
            Image = "placeholder.png"
        # Create a dictionary for each row
        p = {"id": individualRow[0], "Title": individualRow[1], "Description": individualRow[2], "Image": Image}
        projectListOfDictionaries.append(p)

    if conn:
        conn.close()

    return projectListOfDictionaries

#######################################################
# 3. CREATE DATABASE AND TABLE
#######################################################
def createDatabase():
    # A. Make a connection to the database
    conn = sqlite3.connect("projects.db")
    
    # B. Create a workspace (aka Cursor)
    cur = conn.cursor()
    
    # C. Create the projects table
    sql = '''CREATE TABLE IF NOT EXISTS projects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Title TEXT NOT NULL,
        Description TEXT NOT NULL,
        ImageFileName TEXT,
        CreatedDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )'''
    
    # D. Execute the SQL statement
    cur.execute(sql)
    
    # E. Save the changes
    conn.commit()
    
    if conn:
        conn.close()
    
    print("Database and table created successfully!")

#######################################################
# 4. GET PROJECT BY ID
#######################################################
def getProjectById(project_id):
    # A. Connection to the database
    conn = sqlite3.connect('projects.db')
    
    # B. Create a workspace (aka Cursor)
    cursorObj = conn.cursor()
    
    # C. Run the SQL Select statement to retrieve the data
    cursorObj.execute('SELECT Title, Description, ImageFileName FROM projects WHERE id = ?', (project_id,))
    
    # D. Fetch the single record
    row = cursorObj.fetchone()
    
    if row:
        # Make sure we have an image name
        if row[2] is not None and row[2] != "":
            Image = row[2]
        else:
            Image = "placeholder.png"
        # Create a dictionary for the row
        project = {"Title": row[0], "Description": row[1], "Image": Image}
    else:
        project = None
    
    if conn:
        conn.close()
    
    return project

#######################################################
# 5. UPDATE PROJECT BY ID
#######################################################
def updateProjectById(project_id, Title, Description, ImageFileName):
    # A. Make a connection to the database
    conn = sqlite3.connect("projects.db")
    
    # B. Create a workspace (aka Cursor)
    cur = conn.cursor()
    
    # C. Write a SQL statement to update a specific row
    sql = 'UPDATE projects SET Title = ?, Description = ?, ImageFileName = ? WHERE id = ?'
    
    # D. Run the SQL statement
    cur.execute(sql, (Title, Description, ImageFileName, project_id))
    
    # E. Save the changes
    conn.commit()
    
    if conn:
        conn.close()
    
    return cur.rowcount > 0

#######################################################
# 6. DELETE PROJECT BY ID
#######################################################
def deleteProjectById(project_id):
    # A. Make a connection to the database
    conn = sqlite3.connect("projects.db")
    
    # B. Create a workspace (aka Cursor)
    cur = conn.cursor()
    
    # C. Write a SQL statement to delete a specific row
    sql = 'DELETE FROM projects WHERE id = ?'
    
    # D. Run the SQL statement
    cur.execute(sql, (project_id,))
    
    # E. Save the changes
    conn.commit()
    
    if conn:
        conn.close()
    
    return cur.rowcount > 0
