# GitHub Setup Instructions

## How to Push This Repository to GitHub

### Step 1: Create a New Repository on GitHub

1. Go to https://github.com/new
2. Repository name: `wumpus-logic-agent` or `AI_A06_F23-0620`
3. Description: "Dynamic Wumpus Logic Agent using Propositional Logic and Resolution Refutation"
4. Keep it **Public** (or Private if preferred)
5. **DO NOT** initialize with README, .gitignore, or license (we already have these)
6. Click "Create repository"

### Step 2: Link Your Local Repository

```bash
cd /home/sjd1214/Documents/AI/Assignments/A06

# Add GitHub as remote origin
git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git

# Verify remote was added
git remote -v
```

### Step 3: Push Your Code

```bash
# Push to main branch (or master)
git push -u origin master

# If your default branch is 'main', first rename:
git branch -M main
git push -u origin main
```

### Step 4: Verify on GitHub

Visit your repository URL and verify:
- ✓ All 7 commits are visible
- ✓ All files are uploaded
- ✓ README.md displays correctly
- ✓ Commit history shows co-authorship

---

## Alternative: Using GitHub CLI

If you have `gh` CLI installed:

```bash
# Create repo and push in one command
gh repo create wumpus-logic-agent --public --source=. --remote=origin --push
```

---

## Repository Links to Include in Submission

After pushing, include these links in your assignment submission:

1. **Repository URL**: `https://github.com/YOUR_USERNAME/REPO_NAME`
2. **Live Demo**: `N/A (runs locally on Flask)`
3. **Commit History**: `https://github.com/YOUR_USERNAME/REPO_NAME/commits/master`

---

## Recommended Repository Settings

### Add Topics (on GitHub)
- `artificial-intelligence`
- `propositional-logic`
- `resolution-refutation`
- `wumpus-world`
- `knowledge-based-agent`
- `flask`
- `python`

### Add Description
```
A web-based Knowledge-Based Agent that navigates Wumpus World using 
Propositional Logic and Resolution Refutation. Implements automated 
reasoning to deduce safe cells from percepts. Built with Python Flask.
```

### Enable GitHub Pages (Optional)
If you want to host the report:
1. Go to Settings > Pages
2. Source: Deploy from branch
3. Branch: master / docs
4. Save

---

## Common Issues & Solutions

### Issue: "remote origin already exists"
```bash
git remote remove origin
git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git
```

### Issue: Authentication failed
Use Personal Access Token instead of password:
1. Go to GitHub Settings > Developer Settings > Personal Access Tokens
2. Generate new token (classic)
3. Select scopes: `repo` (full control)
4. Use token as password when pushing

### Issue: Branch name mismatch
```bash
# Check current branch
git branch

# Rename if needed
git branch -M main

# Then push
git push -u origin main
```

---

## Clone Instructions (For Testing)

To test that your repo is accessible:

```bash
# Clone to a different directory
cd /tmp
git clone https://github.com/YOUR_USERNAME/REPO_NAME.git
cd REPO_NAME

# Verify all files are there
ls -la

# Test the application
pip install -r requirements.txt
python3 test_logic.py
python3 app.py
```

---

## Submission Checklist

Before submitting, verify:

- [ ] Repository is public (or share access with instructor)
- [ ] All 7 commits are visible
- [ ] README.md displays properly
- [ ] All files are present (14 files)
- [ ] Co-authorship attribution appears in commits
- [ ] Repository URL is included in assignment submission
- [ ] Repository name follows naming convention (include student ID)

---

## Example Submission Text

```
Student ID: F23-0620
Assignment: Dynamic Wumpus Logic Agent

GitHub Repository: https://github.com/YOUR_USERNAME/AI_A06_F23-0620
Commit History: https://github.com/YOUR_USERNAME/AI_A06_F23-0620/commits/master

The repository includes:
- Complete Python implementation with Flask web server
- Propositional logic engine with resolution refutation
- Web interface with real-time visualization
- Comprehensive documentation (README, REPORT, SUBMISSION)
- Test demonstrations
- 7 commits showing development history

To run: See README.md in repository
```

---

**Good luck with your submission!**
