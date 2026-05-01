# Assignment 6 Report: Dynamic Wumpus Logic Agent

**Student ID:** F23-0620  
**Course:** Artificial Intelligence  
**Date:** 2026-05-01  
**GitHub Repository:** https://github.com/sjd-1214/AI_A06_F23-0620.git  
**Live Demo:** https://ai-a06-f23-0620.vercel.app/

---

## 1. Project Overview

This project implements a web-based Knowledge-Based Agent that navigates a Wumpus World environment using Propositional Logic and Resolution Refutation. The agent maintains a knowledge base of logical rules derived from percepts and uses automated reasoning to deduce safe cells.

---

## 2. Screenshots

### Application Interface - Main View
![Screenshot 1](screenshot1.png)

The interface shows:
- Grid visualization with color-coded cells
- Agent position marked as 'A' in yellow
- Knowledge Base displaying propositional logic rules
- Current percepts (Breeze/Stench status)
- Real-time metrics dashboard

### Resolution Steps and Inference
![Screenshot 2](screenshot2.png)

This view demonstrates:
- Step-by-step resolution refutation process
- KB rules in CNF format
- Metrics showing 15 steps taken, 16 percepts received
- 51 KB rules generated
- 14 safe cells identified

---

## 3. Implementation Details

### 3.1 Environment Specifications

The Wumpus World environment supports:

- **Dynamic Grid Sizing**: User-configurable rows and columns (3-10 each)
- **Random Generation**: Pits and Wumpus are randomly placed at game start
- **Percept Generation**: 
  - **Breeze**: Generated when agent is adjacent to a Pit
  - **Stench**: Generated when agent is adjacent to the Wumpus
- **Safety Guarantee**: Starting position (0,0) is always safe

### 3.2 Propositional Logic Representation

#### Symbols Used

- `P_r_c`: Pit exists at cell (r, c)
- `W_r_c`: Wumpus exists at cell (r, c)
- `B_r_c`: Breeze sensed at cell (r, c)
- `S_r_c`: Stench sensed at cell (r, c)

#### Example Rules

When the agent receives a Breeze at (2, 1):

```
B_2_1 => (P_2_2 ∨ P_3_1 ∨ P_1_1 ∨ P_2_0)
```

In CNF (Conjunctive Normal Form):

```
!B_2_1 ∨ P_2_2 ∨ P_3_1 ∨ P_1_1 ∨ P_2_0
```

When NO Breeze is sensed at (2, 2):

```
!P_2_3 ∧ !P_3_2 ∧ !P_1_2 ∧ !P_2_1
```

### 3.3 Resolution Refutation Algorithm

The inference engine uses Resolution Refutation to prove queries:

#### Algorithm Steps:

1. **Negate the Query**: To prove `q`, add `!q` to KB
2. **Apply Resolution**: Resolve pairs of clauses
   - Find complementary literals (e.g., `P` and `!P`)
   - Create resolvent by combining remaining literals
3. **Check for Contradiction**: Empty clause `[]` proves the query
4. **Repeat**: Until contradiction found or no new clauses

#### Example Resolution

Given KB:
```
1. !B_1_1 ∨ P_0_1 ∨ P_1_0 ∨ P_2_1 ∨ P_1_2
2. B_1_1
3. !P_0_1
4. !P_1_0
5. !P_2_1
```

Query: `P_1_2`

Negated: `!P_1_2`

Resolution steps:
- Resolve (1) and (2): `P_0_1 ∨ P_1_0 ∨ P_2_1 ∨ P_1_2`
- Resolve with (3): `P_1_0 ∨ P_2_1 ∨ P_1_2`
- Resolve with (4): `P_2_1 ∨ P_1_2`
- Resolve with (5): `P_1_2`
- Resolve with negated query `!P_1_2`: **`[]` (Empty clause!)**

**Conclusion**: KB ⊨ P_1_2 (Pit confirmed at position 1,2)

### 3.4 Agent Behavior

The agent uses this strategy:

1. **Percept Processing**: When visiting a cell, add rules to KB
2. **Safety Checking**: Use resolution to prove `!P_r_c ∧ !W_r_c`
3. **Movement**: Move to safe unvisited cells
4. **Exploration**: Continue until no safe cells remain

---

## 4. Key Features Implemented

### 4.1 Required Features

✓ **Dynamic Grid Sizing**: Configurable rows and columns  
✓ **Random Generation**: Pits and Wumpus placed randomly  
✓ **Percept Processing**: Breeze and Stench correctly generated  
✓ **Knowledge Base**: Maintains propositional logic rules  
✓ **Resolution Refutation**: Automated CNF conversion and resolution  

### 4.2 Visualization

✓ **Color-coded Grid**:
- Green: Safe (confirmed by KB)
- Gray: Unknown
- Yellow: Agent position
- Red: Danger (if visited)

✓ **Real-time Metrics**:
- Steps taken
- Percepts received
- KB size
- Safe cells found

✓ **KB Display**: Shows all propositional rules in CNF
✓ **Resolution Steps**: Shows inference reasoning for queries

---

## 5. How to Run

### Option 1: Using run script
```bash
chmod +x run.sh
./run.sh
```

### Option 2: Manual startup
```bash
pip install -r requirements.txt
python3 app.py
```

Then open browser to: `http://localhost:5000`

---

## 6. Conclusion

This project successfully implements a Knowledge-Based Agent using Propositional Logic and Resolution Refutation. The agent demonstrates:

- Logical reasoning under uncertainty
- Automated theorem proving via resolution
- Safe exploration through inference
- Real-time visualization of reasoning process

The implementation follows AI textbook principles (Russell & Norvig) for logic-based agents and provides an educational tool for understanding automated reasoning in the Wumpus World domain.

---
**End of Report**
---