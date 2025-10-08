# How to Push Your Website to GitHub

## Step-by-Step Instructions

### 1. Initialize Git Repository (if not already done)
```bash
cd "C:\Users\cteeg\Downloads\AiDD Assignment 5"
git init
```

### 2. Configure Git (if first time)
```bash
git config --global user.name "Your Name"
git config --global user.email "bteegard@iu.edu"
```

### 3. Add Remote Repository
```bash
git remote add origin https://github.com/bteegard/Assignment5-Ai-Update.git
```

### 4. Check Current Status
```bash
git status
```

### 5. Add All Files to Staging
```bash
git add .
```

### 6. Commit Your Changes
```bash
git commit -m "Initial commit: Complete personal website with resume and contact info"
```

### 7. Push to GitHub
```bash
git push -u origin main
```

**Note:** If you get an error about the branch name, try:
```bash
git branch -M main
git push -u origin main
```

### 8. Subsequent Updates
For future updates, use these commands:
```bash
git add .
git commit -m "Description of your changes"
git push
```

## Common Issues & Solutions

### Issue: Repository already exists
If you get an error that the repository already exists:
```bash
git pull origin main --allow-unrelated-histories
git push -u origin main
```

### Issue: Authentication required
You may need to use a Personal Access Token instead of a password.
1. Go to GitHub.com → Settings → Developer settings → Personal access tokens
2. Generate new token with 'repo' permissions
3. Use the token as your password when prompted

### Issue: Merge conflicts
If there are conflicts:
```bash
git pull origin main
# Resolve conflicts in files
git add .
git commit -m "Resolved merge conflicts"
git push
```

## Quick Commands Reference

| Command | Description |
|---------|-------------|
| `git status` | Check current status |
| `git add .` | Add all files |
| `git commit -m "message"` | Commit with message |
| `git push` | Push to GitHub |
| `git pull` | Pull latest changes |
| `git log` | View commit history |

## What's Included in Your Repository

✅ All HTML pages (index, about, resume, projects, contact, thankyou)
✅ CSS styles with dark purple theme
✅ Python Flask application (app.py)
✅ Images directory (with your headshot)
✅ Resume PDF
✅ AI development notes (.prompt/dev_notes.md)
✅ README and documentation
✅ .gitignore file (excludes unnecessary files)

---

**Your Repository URL:** https://github.com/bteegard/Assignment5-Ai-Update

Good luck with your assignment! 🚀

