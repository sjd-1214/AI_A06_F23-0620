from flask import Flask, render_template, jsonify, request
from wumpus_world import WumpusWorld
from wumpus_agent import WumpusAgent

app = Flask(__name__)

game = None
agent = None
steps_taken = 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/new_game', methods=['POST'])
def new_game():
    global game, agent, steps_taken

    data = request.json
    rows = int(data.get('rows', 4))
    cols = int(data.get('cols', 4))

    game = WumpusWorld(rows, cols)
    agent = WumpusAgent(rows, cols)
    steps_taken = 0

    breeze, stench = game.get_percepts(0, 0)
    agent.tell(0, 0, breeze, stench)

    return jsonify({
        'success': True,
        'world': game.get_state(),
        'agent_pos': agent.position,
        'kb_size': agent.get_kb_size(),
        'safe_cells': list(agent.safe_cells),
        'visited': list(agent.visited),
        'steps': steps_taken,
        'percepts': agent.percepts_count,
        'current_percepts': {
            'breeze': breeze,
            'stench': stench
        }
    })

@app.route('/step', methods=['POST'])
def step():
    global game, agent, steps_taken

    if game is None or agent is None:
        return jsonify({'success': False, 'error': 'No game in progress'})

    if game.game_over:
        return jsonify({'success': False, 'error': 'Game over'})

    safe_cells = agent.find_safe_unvisited()

    if not safe_cells:
        return jsonify({
            'success': True,
            'done': True,
            'message': 'No more safe cells to explore'
        })

    next_cell = safe_cells[0]
    steps_taken += 1

    success = game.move_agent(*next_cell)

    if not success:
        return jsonify({
            'success': False,
            'game_over': True,
            'message': 'Agent died!'
        })

    breeze, stench = game.get_percepts(*next_cell)
    agent.tell(*next_cell, breeze, stench)
    agent.position = next_cell

    return jsonify({
        'success': True,
        'agent_pos': agent.position,
        'kb_size': agent.get_kb_size(),
        'safe_cells': list(agent.safe_cells),
        'visited': list(agent.visited),
        'steps': steps_taken,
        'percepts': agent.percepts_count,
        'current_percepts': {
            'breeze': breeze,
            'stench': stench,
            'position': next_cell
        }
    })

@app.route('/get_kb', methods=['GET'])
def get_kb():
    if agent is None:
        return jsonify({'kb': []})

    return jsonify({
        'kb': agent.get_kb_rules()
    })

@app.route('/check_safe', methods=['POST'])
def check_safe():
    if agent is None:
        return jsonify({'success': False, 'error': 'No game in progress'})

    data = request.json
    row = int(data.get('row', 0))
    col = int(data.get('col', 0))

    is_safe, steps = agent.ask_safe(row, col)

    return jsonify({
        'success': True,
        'is_safe': is_safe,
        'resolution_steps': steps
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
