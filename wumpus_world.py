"""
Wumpus World Environment
Manages the grid, pits, wumpus, and percepts
"""

import random

class WumpusWorld:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.pits = set()
        self.wumpus = None
        self.agent_pos = (0, 0)
        self.game_over = False

        # Generate random pits and wumpus
        self._generate_world()

    def _generate_world(self):
        """Randomly place pits and wumpus"""
        all_cells = [(r, c) for r in range(self.rows) for c in range(self.cols)]

        # Remove start position (0, 0) from possible danger locations
        all_cells.remove((0, 0))

        # Place wumpus randomly
        self.wumpus = random.choice(all_cells)
        all_cells.remove(self.wumpus)

        # Place pits randomly (about 20% of cells)
        num_pits = max(1, int(len(all_cells) * 0.2))
        self.pits = set(random.sample(all_cells, num_pits))

    def get_percepts(self, row, col):
        """
        Get percepts at a location
        Returns: (breeze: bool, stench: bool)
        """
        breeze = False
        stench = False

        # Check neighbors for pits (breeze)
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = row + dr, col + dc
            if 0 <= nr < self.rows and 0 <= nc < self.cols:
                if (nr, nc) in self.pits:
                    breeze = True
                if (nr, nc) == self.wumpus:
                    stench = True

        return breeze, stench

    def is_safe(self, row, col):
        """Check if a cell is actually safe (ground truth)"""
        return (row, col) not in self.pits and (row, col) != self.wumpus

    def move_agent(self, row, col):
        """Move agent to a new position"""
        self.agent_pos = (row, col)

        # Check if agent died
        if (row, col) in self.pits or (row, col) == self.wumpus:
            self.game_over = True
            return False
        return True

    def get_state(self):
        """Get current world state"""
        return {
            'rows': self.rows,
            'cols': self.cols,
            'agent_pos': self.agent_pos,
            'pits': list(self.pits),
            'wumpus': self.wumpus,
            'game_over': self.game_over
        }
