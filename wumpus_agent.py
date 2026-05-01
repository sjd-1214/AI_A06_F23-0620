"""
Wumpus World Knowledge-Based Agent
Uses propositional logic to reason about safe cells
"""

from logic_engine import PropositionalLogic

class WumpusAgent:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.logic = PropositionalLogic()
        self.position = (0, 0)
        self.safe_cells = set()
        self.safe_cells.add((0, 0))  # Start is always safe
        self.visited = set()
        self.percepts_count = 0

    def get_neighbors(self, row, col):
        """Get valid neighboring cells"""
        neighbors = []
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = row + dr, col + dc
            if 0 <= nr < self.rows and 0 <= nc < self.cols:
                neighbors.append((nr, nc))
        return neighbors

    def tell(self, row, col, breeze, stench):
        """
        Tell the agent about percepts at a location
        Adds rules to KB based on percepts
        """
        self.percepts_count += 1
        self.visited.add((row, col))

        # Get neighboring cells
        neighbors = self.get_neighbors(row, col)

        # Breeze implies adjacent Pit
        if breeze:
            # B_r_c => (P_n1_r_n1_c v P_n2_r_n2_c v ...)
            pit_literals = [f"P_{nr}_{nc}" for nr, nc in neighbors]
            clause = self.logic.implication_to_cnf(f"B_{row}_{col}", pit_literals)
            self.logic.add_rule(clause)

            # Also add that we have a breeze here
            self.logic.add_rule([f"B_{row}_{col}"])
        else:
            # No breeze means no adjacent pits
            for nr, nc in neighbors:
                self.logic.add_rule([f"!P_{nr}_{nc}"])

        # Stench implies adjacent Wumpus
        if stench:
            wumpus_literals = [f"W_{nr}_{nc}" for nr, nc in neighbors]
            clause = self.logic.implication_to_cnf(f"S_{row}_{col}", wumpus_literals)
            self.logic.add_rule(clause)
            self.logic.add_rule([f"S_{row}_{col}"])
        else:
            # No stench means no adjacent wumpus
            for nr, nc in neighbors:
                self.logic.add_rule([f"!W_{nr}_{nc}"])

    def ask_safe(self, row, col):
        """
        Check if a cell is safe using resolution
        Safe means: !P_r_c AND !W_r_c
        """
        # Check if no pit
        result_pit, steps_pit = self.logic.ask(f"!P_{row}_{col}")

        # Check if no wumpus
        result_wumpus, steps_wumpus = self.logic.ask(f"!W_{row}_{col}")

        is_safe = result_pit and result_wumpus

        if is_safe:
            self.safe_cells.add((row, col))

        return is_safe, steps_pit + ["---"] + steps_wumpus

    def find_safe_unvisited(self):
        """Find safe cells that haven't been visited"""
        safe_unvisited = []
        for r in range(self.rows):
            for c in range(self.cols):
                if (r, c) not in self.visited:
                    if (r, c) in self.safe_cells:
                        safe_unvisited.append((r, c))
                    else:
                        # Try to infer if it's safe
                        is_safe, _ = self.ask_safe(r, c)
                        if is_safe:
                            safe_unvisited.append((r, c))
        return safe_unvisited

    def get_kb_size(self):
        """Return number of rules in KB"""
        return len(self.logic.kb)

    def get_kb_rules(self):
        """Get all KB rules as strings"""
        return self.logic.get_kb_strings()
