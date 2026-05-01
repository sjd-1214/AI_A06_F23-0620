# Dynamic Wumpus Logic Agent

A web-based knowledge-based agent that navigates a Wumpus World grid using Propositional Logic and Resolution Refutation.

## Project Overview

This application implements an intelligent agent that:
- Navigates a dynamically-sized grid with randomly placed Pits and Wumpus
- Uses Propositional Logic to maintain a Knowledge Base
- Employs Resolution Refutation to deduce safe cells
- Provides real-time visualization of the agent's reasoning process

## Features

- **Dynamic Grid Configuration**: Set custom grid dimensions (Rows × Columns)
- **Propositional Logic KB**: Maintains logical rules based on percepts
- **Resolution Engine**: Automated CNF conversion and clause resolution
- **Visual Interface**: Color-coded cells (Green=Safe, Gray=Unknown, Red=Danger)
- **Real-time Metrics**: Tracks inferences, steps, and percepts

## How to Run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the Flask application:
   ```bash
   python app.py
   ```

3. Open your browser and navigate to:
   ```
   http://localhost:5000
   ```

4. Configure grid size and click "New Episode" to start

## Student Information

- **Student ID**: F23-0620
- **Assignment**: AI Assignment 6
- **Course**: Artificial Intelligence

## Technology Stack

- Python 3.x
- Flask (Web framework)
- HTML5/CSS3
- Vanilla JavaScript (ES6+)

## Project Structure

```
A06/
├── index.html          # Main web interface
├── style.css           # Styling
├── logic.js            # Propositional logic and resolution engine
├── agent.js            # Agent behavior and KB management
├── game.js             # Game environment and grid management
└── README.md           # This file
```
