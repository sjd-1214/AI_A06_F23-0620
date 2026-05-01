import random

class WumpusWorld:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.pits = set()
        self.wumpus = None
        self.agent_pos = (0, 0)
        self.game_over = False

        self._generate_world()

    def _generate_world(self):
        all_cells = [(r, c) for r in range(self.rows) for c in range(self.cols)]

        all_cells.remove((0, 0))

        self.wumpus = random.choice(all_cells)
        all_cells.remove(self.wumpus)

        num_pits = max(1, int(len(all_cells) * 0.2))
        self.pits = set(random.sample(all_cells, num_pits))

    def get_percepts(self, row, col):
        breeze = False
        stench = False

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = row + dr, col + dc
            if 0 <= nr < self.rows and 0 <= nc < self.cols:
                if (nr, nc) in self.pits:
                    breeze = True
                if (nr, nc) == self.wumpus:
                    stench = True

        return breeze, stench

    def is_safe(self, row, col):
        return (row, col) not in self.pits and (row, col) != self.wumpus

    def move_agent(self, row, col):
        self.agent_pos = (row, col)

        if (row, col) in self.pits or (row, col) == self.wumpus:
            self.game_over = True
            return False
        return True

    def get_state(self):
        return {
            'rows': self.rows,
            'cols': self.cols,
            'agent_pos': self.agent_pos,
            'pits': list(self.pits),
            'wumpus': self.wumpus,
            'game_over': self.game_over
        }
