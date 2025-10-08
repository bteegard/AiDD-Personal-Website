# Bryant Teegardin's Personal Website

A professional personal website showcasing skills, interests, and accomplishments as an MSIS student at Indiana Kelley School of Business.

## Features

- **Responsive Design**: Works perfectly on desktop, tablet, and mobile devices
- **Dark Purple Theme**: Professional color scheme with appealing gradients
- **Multi-page Navigation**: Home, About Me, Resume, Projects, and Contact pages
- **Contact Form**: Fully validated form with error handling
- **Modern UI**: Clean, professional design with smooth animations
- **Accessibility**: Proper semantic HTML and accessibility features

## Quick Start

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Installation & Setup

1. **Clone or download this repository**
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Flask application:**
   ```bash
   python app.py
   ```

4. **Open your browser and visit:**
   ```
   http://localhost:5000
   ```

## Customization Instructions

### 1. Add Your Profile Photo
- **Your headshot is already in place!** ✅ The file `images/headshot.jpg` is now being used
- Your professional photo is automatically displayed on the About Me page
- The website is already configured to show your actual headshot

### 2. Update Resume Content
- **Your resume PDF is already in place!** ✅ The file `resume.pdf` is ready for download
- Use the template in `resume_content_template.html` to easily copy your resume information
- Open your resume PDF and copy the relevant sections into the template
- Replace the placeholder text in `resume.html` with your actual information
- **Quick Tip:** Copy from your PDF → Paste into template → Copy from template → Paste into resume.html

### 3. Add Your Projects
- Edit `projects.html` to showcase your actual projects
- Replace placeholder project descriptions with real projects
- Add screenshots to the `/images/` directory if needed
- Update GitHub and demo links

### 4. Update Contact Information
- Edit `contact.html` to add your real email address
- Update LinkedIn and GitHub profile links
- Verify all social media links are correct

### 5. Customize Content
- Edit all HTML files to personalize the content
- Update the bio in `about.html`
- Modify project descriptions and achievements
- Add any additional sections as needed

## File Structure

```
├── index.html              # Homepage
├── about.html              # About Me page
├── resume.html             # Resume page
├── projects.html           # Projects showcase
├── contact.html            # Contact form page
├── thankyou.html           # Thank you page after form submission
├── app.py                  # Flask server application
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── .prompt/
│   └── dev_notes.md       # AI development reflection
├── static/
│   └── css/
│       └── styles.css     # Main stylesheet
└── images/                # Directory for images
    └── profile-photo.jpg  # Add your photo here
```

## Technical Details

- **Frontend**: HTML5, CSS3, JavaScript
- **Backend**: Python Flask
- **Styling**: Custom CSS with dark purple theme
- **Responsive**: Mobile-first design approach
- **Form Validation**: HTML5 and JavaScript validation
- **Accessibility**: WCAG compliant structure

## Contact Form Features

The contact form includes:
- First Name (required, minimum 2 characters)
- Last Name (required, minimum 2 characters)
- Email Address (required, valid email format)
- Password (required, minimum 8 characters)
- Confirm Password (required, must match)
- Optional message field
- Real-time validation with error messages
- Accessibility features with proper labels

## Browser Compatibility

This website works on all modern browsers:
- Chrome 70+
- Firefox 65+
- Safari 12+
- Edge 79+

## License

This project is created for educational purposes as part of the MSIS program at Indiana Kelley School of Business.

---

**Created by:** Bryant Teegardin  
**Program:** Master of Science in Information Systems  
**Institution:** Indiana Kelley School of Business  
**Year:** 2024
