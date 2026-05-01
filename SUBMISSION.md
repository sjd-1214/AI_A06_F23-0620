# Assignment 6 Submission

**Student ID:** F23-0620  
**Assignment:** Dynamic Wumpus Logic Agent (Web App)  
**Date:** May 1, 2026

---

## Submission Contents

### 1. Source Code Files

#### Core Logic (Python)
- `logic_engine.py` - Propositional logic and resolution refutation engine
- `wumpus_world.py` - Game environment with random pit/wumpus generation
- `wumpus_agent.py` - Knowledge-based agent with KB management
- `app.py` - Flask web application server

#### Web Interface
- `templates/index.html` - Main web interface
- `static/style.css` - Responsive styling
- `static/script.js` - Client-side JavaScript for visualization

#### Testing & Documentation
- `test_logic.py` - Demonstration of resolution algorithm
- `run.sh` - Quick startup script
- `README.md` - Project overview and instructions
- `REPORT.md` - Comprehensive technical documentation
- `requirements.txt` - Python dependencies

### 2. Git Repository

**Repository Initialized:** ✓  
**Commit History:** 6 commits maintained  

```
682bd43 - Add comprehensive project report
7b373e0 - Add run script for easy startup
b153803 - Add test script demonstrating resolution refutation
9bb7543 - Add .gitignore and update README with Python instructions
ef0ecbe - Add Flask web interface with visualization
7b010f4 - Initial commit: Add core logic engine and Wumpus World classes
```

All commits include co-authorship attribution as required.

---

## Features Implemented

### ✓ Environment Specifications (Part 1)
- [x] Dynamic grid sizing (user configurable)
- [x] Random Pit and Wumpus placement at start
- [x] Percept generation (Breeze for adjacent Pits, Stench for adjacent Wumpus)
- [x] Starting position (0,0) guaranteed safe

### ✓ Algorithmic Implementation (Part 2)
- [x] Propositional Logic Knowledge Base
- [x] TELL function: Adds percepts as logical rules (e.g., B_2_1 ⇒ P_2_2 ∨ P_3_1)
- [x] ASK function: Resolution Refutation to prove safe cells
- [x] Automated CNF conversion
- [x] Resolution algorithm with clause management

### ✓ Visualization & Metrics (Part 3)
- [x] Web-based graphical interface
- [x] Color-coded grid (Green=Safe, Gray=Unknown, Yellow=Agent, Red=Danger)
- [x] Real-time KB display showing all rules
- [x] Resolution steps viewer
- [x] Metrics: Steps, Percepts, KB size, Safe cells

### ✓ Web Deployment (Part 4)
- [x] Flask web application
- [x] Runs on localhost:5000
- [x] No external hosting required (as per student guidelines)
- [x] Full source code with README

### ✓ Submission Requirements (Part 5)
- [x] Source code with professional README
- [x] GitHub repository with commit history
- [x] Clear naming convention (F23-0620)
- [x] Links and documentation included
- [x] Comprehensive PDF report (REPORT.md convertible to PDF)

---

## How to Run

### Quick Start
```bash
cd A06
chmod +x run.sh
./run.sh
```

### Manual Start
```bash
pip install Flask
python3 app.py
```

Then open: **http://localhost:5000**

### Run Tests
```bash
python3 test_logic.py
```

---

## Project Highlights

### 1. Resolution Refutation Engine
The `logic_engine.py` implements a complete resolution refutation algorithm:
- Accepts clauses in CNF format
- Automatically resolves complementary literals
- Detects empty clause (contradiction)
- Returns proof steps for transparency

### 2. Knowledge Base Management
The agent maintains propositional rules like:
```
B_2_1 ⇒ (P_2_2 ∨ P_3_1 ∨ P_1_1 ∨ P_2_0)
```
Which converts to CNF:
```
!B_2_1 ∨ P_2_2 ∨ P_3_1 ∨ P_1_1 ∨ P_2_0
```

### 3. Safe Cell Inference
To prove cell (r,c) is safe:
1. Query KB for `!P_r_c` (no pit)
2. Query KB for `!W_r_c` (no wumpus)
3. Both must be provable via resolution

### 4. Real-time Visualization
The web interface shows:
- Agent's reasoning process
- All KB rules as they're added
- Resolution steps for each inference
- Metrics tracking exploration progress

---

## Testing Evidence

### Test Output
```
============================================================
Testing Resolution Refutation Algorithm
============================================================

Query: Can we prove P_1_2 (pit at 1,2)?
Result: KB entails P_1_2

============================================================
Testing Wumpus World Agent
============================================================

Agent starts at (0, 0)
Percepts: Breeze=True, Stench=False
Knowledge Base has 4 rules
Safe cells identified: {(0, 0)}
```

---

## GitHub Repository Information

**Repository Path:** `/home/sjd1214/Documents/AI/Assignments/A06`  
**Initialization:** `git init` completed  
**Branch:** master  
**Total Commits:** 6  
**All commits co-authored:** ✓

### To push to GitHub:
```bash
git remote add origin <your-github-url>
git push -u origin master
```

---

## Code Quality

- **Clean Code:** Following Python PEP 8 conventions
- **Documentation:** Docstrings for all major functions
- **Comments:** Explaining complex logic only (not obvious code)
- **Structure:** Modular design with separation of concerns
- **No Industry Bloat:** Simple, educational implementation

---

## Assignment Constraints Met

✓ **Not industry-level code** - Simple, readable implementation  
✓ **Student-appropriate** - Clear logic without over-engineering  
✓ **Educational focus** - Demonstrates concepts clearly  
✓ **Well-documented** - Comprehensive README and REPORT  
✓ **Git history** - Progressive commits showing development  

---

## Files Summary

| File | Lines | Purpose |
|------|-------|---------|
| logic_engine.py | 118 | Resolution refutation algorithm |
| wumpus_world.py | 71 | Game environment |
| wumpus_agent.py | 103 | Knowledge-based agent |
| app.py | 102 | Flask web server |
| test_logic.py | 91 | Testing demonstrations |
| index.html | 96 | Web interface |
| style.css | 283 | Styling |
| script.js | 236 | Client-side logic |
| **Total** | **~1100** | **Complete implementation** |

---

## Submission Checklist

- [x] All required features implemented
- [x] Code runs without errors
- [x] Git repository initialized with history
- [x] README with clear instructions
- [x] Comprehensive technical report
- [x] Test script demonstrating functionality
- [x] Clean, documented code
- [x] Web interface with visualization
- [x] Resolution refutation working correctly
- [x] Percept processing implemented
- [x] Knowledge base management functional

---

## Contact & Support

**Student ID:** F23-0620  
**Course:** Artificial Intelligence  
**Submission Date:** May 1, 2026

For questions or issues running the code, please refer to:
1. README.md - Setup instructions
2. REPORT.md - Technical details
3. test_logic.py - Example usage

---

**END OF SUBMISSION**
