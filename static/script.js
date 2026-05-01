let gameState = null;
let autoRunning = false;
let autoInterval = null;

const canvas = document.getElementById('gridCanvas');
const ctx = canvas.getContext('2d');

async function newGame() {
    const rows = parseInt(document.getElementById('rows').value);
    const cols = parseInt(document.getElementById('cols').value);

    const response = await fetch('/new_game', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({rows, cols})
    });

    const data = await response.json();

    if (data.success) {
        gameState = data;
        document.getElementById('stepBtn').disabled = false;
        document.getElementById('autoBtn').disabled = false;
        updateUI(data);
        drawGrid(data);
        loadKB();
        updatePercepts(data.current_percepts);
    }
}

async function step() {
    const response = await fetch('/step', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'}
    });

    const data = await response.json();

    if (data.success) {
        if (data.done) {
            alert(data.message);
            stopAuto();
            return;
        }

        gameState = {...gameState, ...data};
        updateUI(data);
        drawGrid(data);
        loadKB();
        updatePercepts(data.current_percepts);

        if (data.current_percepts && data.current_percepts.position) {
            await checkSafe(data.current_percepts.position[0], data.current_percepts.position[1]);
        }
    } else if (data.game_over) {
        alert(data.message);
        stopAuto();
    }
}

async function autoRun() {
    if (autoRunning) {
        stopAuto();
    } else {
        autoRunning = true;
        document.getElementById('autoBtn').textContent = 'Stop';
        autoInterval = setInterval(async () => {
            await step();
        }, 1500);
    }
}

function stopAuto() {
    autoRunning = false;
    if (autoInterval) {
        clearInterval(autoInterval);
        autoInterval = null;
    }
    document.getElementById('autoBtn').textContent = 'Auto Run';
}

async function loadKB() {
    const response = await fetch('/get_kb');
    const data = await response.json();

    const kbContent = document.getElementById('kbContent');
    if (data.kb.length === 0) {
        kbContent.innerHTML = '<p class="placeholder">No rules yet</p>';
    } else {
        kbContent.innerHTML = data.kb.map(rule =>
            `<div class="kb-rule">${rule}</div>`
        ).join('');
        kbContent.scrollTop = kbContent.scrollHeight;
    }
}

async function checkSafe(row, col) {
    const response = await fetch('/check_safe', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({row, col})
    });

    const data = await response.json();

    if (data.success) {
        const resContent = document.getElementById('resolutionContent');
        resContent.innerHTML = data.resolution_steps.map(step =>
            `<div class="resolution-step">${step}</div>`
        ).join('');
        resContent.scrollTop = resContent.scrollHeight;
    }
}

function updateUI(data) {
    document.getElementById('steps').textContent = data.steps || 0;
    document.getElementById('percepts').textContent = data.percepts || 0;
    document.getElementById('kbSize').textContent = data.kb_size || 0;
    document.getElementById('safeCells').textContent = (data.safe_cells || []).length;
}

function updatePercepts(percepts) {
    const perceptContent = document.getElementById('perceptsContent');

    if (!percepts) {
        perceptContent.innerHTML = '<p class="placeholder">No percepts</p>';
        return;
    }

    let html = '';
    if (percepts.position) {
        html += `<div class="percept-item">Position: (${percepts.position[0]}, ${percepts.position[1]})</div>`;
    }
    html += `<div class="percept-item">Breeze: ${percepts.breeze ? 'YES' : 'NO'}</div>`;
    html += `<div class="percept-item">Stench: ${percepts.stench ? 'YES' : 'NO'}</div>`;

    perceptContent.innerHTML = html;
}

function drawGrid(data) {
    const rows = data.world ? data.world.rows : 4;
    const cols = data.world ? data.world.cols : 4;

    const cellSize = 400 / Math.max(rows, cols);
    canvas.width = cellSize * cols;
    canvas.height = cellSize * rows;

    ctx.clearRect(0, 0, canvas.width, canvas.height);

    const agentPos = data.agent_pos || [0, 0];
    const safeCells = data.safe_cells || [];
    const visited = data.visited || [];
    const world = data.world;

    for (let r = 0; r < rows; r++) {
        for (let c = 0; c < cols; c++) {
            const x = c * cellSize;
            const y = r * cellSize;

            let color = '#adb5bd';

            if (safeCells.some(cell => cell[0] === r && cell[1] === c)) {
                color = '#28a745';
            }

            if (agentPos[0] === r && agentPos[1] === c) {
                color = '#ffc107';
            }

            if (world && world.pits) {
                if (world.pits.some(pit => pit[0] === r && pit[1] === c)) {
                    if (visited.some(v => v[0] === r && v[1] === c)) {
                        color = '#dc3545';
                    }
                }
            }

            if (world && world.wumpus) {
                if (world.wumpus[0] === r && world.wumpus[1] === c) {
                    if (visited.some(v => v[0] === r && v[1] === c)) {
                        color = '#dc3545';
                    }
                }
            }

            ctx.fillStyle = color;
            ctx.fillRect(x, y, cellSize, cellSize);

            ctx.strokeStyle = '#495057';
            ctx.lineWidth = 2;
            ctx.strokeRect(x, y, cellSize, cellSize);

            ctx.fillStyle = '#000';
            ctx.font = `${cellSize * 0.2}px Arial`;
            ctx.fillText(`${r},${c}`, x + 5, y + 15);

            if (agentPos[0] === r && agentPos[1] === c) {
                ctx.fillStyle = '#000';
                ctx.font = `${cellSize * 0.4}px Arial`;
                ctx.textAlign = 'center';
                ctx.textBaseline = 'middle';
                ctx.fillText('A', x + cellSize / 2, y + cellSize / 2);
                ctx.textAlign = 'left';
                ctx.textBaseline = 'alphabetic';
            }
        }
    }
}

window.addEventListener('load', () => {
    ctx.fillStyle = '#f8f9fa';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    ctx.fillStyle = '#6c757d';
    ctx.font = '20px Arial';
    ctx.textAlign = 'center';
    ctx.fillText('Click "New Episode" to start', canvas.width / 2, canvas.height / 2);
});
