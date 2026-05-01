# Assignment 6 Report: Dynamic Wumpus Logic Agent

**Student ID:** F23-0620  
**Course:** Artificial Intelligence  
**Date:** 2026-05-01

---

## 1. Project Overview

This project implements a web-based Knowledge-Based Agent that navigates a Wumpus World environment using Propositional Logic and Resolution Refutation. The agent maintains a knowledge base of logical rules derived from percepts and uses automated reasoning to deduce safe cells.

---

## 2. Implementation Details

### 2.1 Environment Specifications

The Wumpus World environment supports:

- **Dynamic Grid Sizing**: User-configurable rows and columns (3-10 each)
- **Random Generation**: Pits and Wumpus are randomly placed at game start
- **Percept Generation**: 
  - **Breeze**: Generated when agent is adjacent to a Pit
  - **Stench**: Generated when agent is adjacent to the Wumpus
- **Safety Guarantee**: Starting position (0,0) is always safe

### 2.2 Propositional Logic Representation

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

### 2.3 Resolution Refutation Algorithm

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

### 2.4 Agent Behavior

The agent uses this strategy:

1. **Percept Processing**: When visiting a cell, add rules to KB
2. **Safety Checking**: Use resolution to prove `!P_r_c ∧ !W_r_c`
3. **Movement**: Move to safe unvisited cells
4. **Exploration**: Continue until no safe cells remain

---

## 3. Technical Architecture

### 3.1 Core Components

#### `logic_engine.py`
- `PropositionalLogic` class
- CNF clause management
- Resolution refutation implementation
- Complementary literal detection

#### `wumpus_world.py`
- Grid environment management
- Random Pit/Wumpus placement
- Percept generation
- Ground truth tracking

#### `wumpus_agent.py`
- Knowledge Base management
- Percept-to-rule conversion
- Safety query interface
- Safe cell tracking

#### `app.py`
- Flask web server
- REST API endpoints
- Game state management
- Session handling

### 3.2 Web Interface

- **HTML/CSS**: Responsive layout with color-coded visualization
- **JavaScript**: Real-time updates via fetch API
- **Canvas**: Grid rendering with agent position
- **Displays**: KB rules, percepts, resolution steps

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

## 5. Challenges & Solutions

### Challenge 1: Resolution Complexity
**Problem**: Resolution can generate many redundant clauses  
**Solution**: Use set-based deduplication and limit iteration depth

### Challenge 2: Safety Checking
**Problem**: Must prove both `!P` AND `!W` for safety  
**Solution**: Perform two separate queries and combine results

### Challenge 3: Movement Strategy
**Problem**: Simple greedy strategy may not be optimal  
**Solution**: Current implementation prioritizes closest safe cells

---

## 6. Testing

### Test Results

```bash
$ python3 test_logic.py
```

**Test 1: Resolution Proof**
- Query: Can we prove P_1_2?
- Result: ✓ KB entails P_1_2
- Reasoning: Empty clause found via resolution

**Test 2: Wumpus World Agent**
- Grid: 4x4
- Wumpus: (1, 2)
- Pits: {(1, 0), (3, 3)}
- Result: ✓ Agent correctly identifies safe cells

---

## 7. How to Run

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

## 8. Git Repository

### Commit History

```
7b373e0 - Add run script for easy startup
b153803 - Add test script demonstrating resolution refutation
9bb7543 - Add .gitignore and update README with Python instructions
ef0ecbe - Add Flask web interface with visualization
7b010f4 - Initial commit: Add core logic engine and Wumpus World classes
```

### Repository Structure

```
A06/
├── logic_engine.py       # Propositional logic & resolution
├── wumpus_world.py       # Environment simulation
├── wumpus_agent.py       # Knowledge-based agent
├── app.py                # Flask web application
├── test_logic.py         # Test demonstrations
├── run.sh                # Startup script
├── requirements.txt      # Python dependencies
├── templates/
│   └── index.html        # Web interface
├── static/
│   ├── style.css         # Styling
│   └── script.js         # Client-side logic
└── README.md             # Documentation
```

---

## 9. Screenshots & Demonstration

The web interface provides:

1. **Control Panel**: Grid configuration and action buttons
2. **Grid Visualization**: Color-coded cells showing agent reasoning
3. **Metrics Dashboard**: Real-time statistics
4. **Knowledge Base Display**: All logical rules in CNF
5. **Percepts Display**: Current sensory information
6. **Resolution Steps**: Inference reasoning trace

---

## 10. Conclusion

This project successfully implements a Knowledge-Based Agent using Propositional Logic and Resolution Refutation. The agent demonstrates:

- Logical reasoning under uncertainty
- Automated theorem proving via resolution
- Safe exploration through inference
- Real-time visualization of reasoning process

The implementation follows AI textbook principles (Russell & Norvig) for logic-based agents and provides an educational tool for understanding automated reasoning in the Wumpus World domain.

---

## 11. Future Enhancements

Possible improvements:

- Implement forward chaining for faster inference
- Add Wumpus shooting capability
- Optimize clause resolution order
- Implement more sophisticated movement strategies
- Add gold collection objective
- Support for First-Order Logic representation

---

## 12. References

- Russell, S., & Norvig, P. (2020). *Artificial Intelligence: A Modern Approach* (4th ed.)
- Flask Documentation: https://flask.palletsprojects.com/
- Propositional Logic & Resolution: AI Course Materials

---

**End of Report**
