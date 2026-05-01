#!/bin/bash
# Run script for Dynamic Wumpus Logic Agent
# Student ID: F23-0620

echo "================================"
echo "Dynamic Wumpus Logic Agent"
echo "================================"
echo ""

# Check if Flask is installed
if ! python3 -c "import flask" 2>/dev/null; then
    echo "Installing dependencies..."
    pip install -r requirements.txt
    echo ""
fi

echo "Starting Flask server..."
echo "Open your browser and go to: http://localhost:5000"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

python3 app.py
