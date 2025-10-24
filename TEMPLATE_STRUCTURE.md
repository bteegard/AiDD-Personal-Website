# Flask Template Structure Documentation

## Overview

This project uses Flask's Jinja2 template engine with template inheritance for a clean, maintainable codebase.

## Directory Structure

```
project/
├── app.py                          # Flask application
├── templates/                      # Template directory
│   ├── base.html                  # Base template (parent)
│   ├── index.html                 # Homepage (extends base)
│   ├── about.html                 # About page (extends base)
│   ├── resume.html                # Resume page (extends base)
│   ├── projects.html              # Projects page (extends base)
│   ├── contact.html               # Contact page (extends base)
│   └── thankyou.html              # Thank you page (extends base)
├── static/                        # Static files
│   ├── css/
│   │   └── styles.css            # Main stylesheet
│   └── js/                       # JavaScript files (if any)
└── images/                       # Image files
    └── headshot.jpg              # Profile photo
```

## Base Template (base.html)

The `base.html` file serves as the parent template and contains:

- **Common HTML structure** (DOCTYPE, html, head, body tags)
- **Header navigation** with links to all pages
- **Footer** with copyright and GitHub link
- **Jinja2 blocks** for child templates to override

### Blocks in base.html:

```jinja
{% block title %}        # Page title (in <head>)
{% block extra_css %}    # Additional CSS files
{% block content %}      # Main page content
{% block extra_js %}     # Additional JavaScript
```

## Child Templates

All page-specific templates extend `base.html` and only need to define the content that changes.

### Example Structure:

```jinja
{% extends "base.html" %}

{% block title %}Your Page Title{% endblock %}

{% block content %}
<!-- Your page-specific HTML here -->
{% endblock %}

{% block extra_js %}
<!-- Optional: Page-specific JavaScript -->
{% endblock %}
```

## Flask URL Functions

Templates use Flask's `url_for()` function for dynamic URL generation:

```jinja
<a href="{{ url_for('index') }}">Home</a>
<a href="{{ url_for('about') }}">About</a>
<link rel="stylesheet" href="{{ url_for('static', filename='css/styles.css') }}">
<img src="{{ url_for('static', filename='../images/headshot.jpg') }}">
```

### Benefits:
- ✅ Automatically handles URL changes
- ✅ Works regardless of application deployment path
- ✅ Prevents broken links

## Template Inheritance Benefits

1. **DRY Principle**: Don't Repeat Yourself - header/footer defined once
2. **Easy Maintenance**: Update navigation in one place, applies to all pages
3. **Consistency**: All pages automatically have same structure
4. **Flexibility**: Individual pages can override blocks as needed
5. **Professional**: Industry-standard Flask best practice

## How It Works

### Before (Static HTML):
Each page repeated the same header/footer code:
```html
<!-- index.html -->
<header>...</header>
<main><!-- content --></main>
<footer>...</footer>

<!-- about.html -->
<header>...</header>  <!-- DUPLICATE -->
<main><!-- content --></main>
<footer>...</footer>   <!-- DUPLICATE -->
```

### After (Template Inheritance):
```html
<!-- base.html -->
<header>...</header>
{% block content %}{% endblock %}
<footer>...</footer>

<!-- index.html -->
{% extends "base.html" %}
{% block content %}<!-- unique content -->{% endblock %}

<!-- about.html -->
{% extends "base.html" %}
{% block content %}<!-- unique content -->{% endblock %}
```

## Flask App Routes

The `app.py` file uses `render_template()` to serve templates:

```python
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')
```

## Static Files

Static files (CSS, JS, images) are served from the `static/` directory:

```python
app = Flask(__name__, 
            template_folder='templates',
            static_folder='static')
```

Access in templates:
```jinja
{{ url_for('static', filename='css/styles.css') }}
{{ url_for('static', filename='js/script.js') }}
```

## Images

Images are stored in the `images/` directory and accessed via:
```jinja
<img src="{{ url_for('static', filename='../images/headshot.jpg') }}">
```

Or more cleanly with a custom route:
```python
@app.route('/images/<filename>')
def image(filename):
    return send_from_directory('images', filename)
```

Then in templates:
```jinja
<img src="{{ url_for('image', filename='headshot.jpg') }}">
```

## Making Changes

### To update header/footer on all pages:
1. Edit `templates/base.html`
2. Changes automatically apply to all pages

### To update a specific page:
1. Edit the corresponding template in `templates/`
2. Only modify the `{% block content %}` section

### To add a new page:
1. Create new template extending base:
   ```jinja
   {% extends "base.html" %}
   {% block content %}...{% endblock %}
   ```
2. Add route in `app.py`:
   ```python
   @app.route('/newpage')
   def newpage():
       return render_template('newpage.html')
   ```

## Best Practices

✅ **DO:**
- Use `url_for()` for all links
- Extend `base.html` for all pages
- Keep page-specific code in child templates
- Use meaningful block names

❌ **DON'T:**
- Hardcode URLs (use `url_for()` instead)
- Duplicate header/footer code
- Put navigation in child templates
- Mix static paths with Flask paths

## Converting Static HTML to Templates

To convert existing static HTML files:

1. **Keep only the content** (remove <!DOCTYPE>, <html>, <head>, <body>, header, footer)
2. **Add template inheritance**:
   ```jinja
   {% extends "base.html" %}
   ```
3. **Wrap content in block**:
   ```jinja
   {% block content %}
   <!-- your page content -->
   {% endblock %}
   ```
4. **Update links** to use `url_for()`
5. **Update static file references** to use `url_for('static', filename='...')`

## Troubleshooting

### Template Not Found Error:
- Ensure file is in `templates/` directory
- Check filename spelling matches route
- Verify `template_folder` is set correctly in `app.py`

### Static Files Not Loading:
- Check `static_folder` configuration
- Use `url_for('static', filename='path/to/file')`
- Verify file path relative to `static/` directory

### CSS Not Applying:
- Check browser console for 404 errors
- Verify CSS path in base.html
- Clear browser cache (Ctrl+Shift+R)

## Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Jinja2 Template Documentation](https://jinja.palletsprojects.com/)
- [Flask Template Inheritance](https://flask.palletsprojects.com/en/latest/patterns/templateinheritance/)

---

**Last Updated:** 2025
**Project:** Bryant Teegardin Personal Website
**Course:** AI-Driven Development Assignment 5

