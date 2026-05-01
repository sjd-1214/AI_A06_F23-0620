from logic_engine import PropositionalLogic

class WumpusAgent:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.logic = PropositionalLogic()
        self.position = (0, 0)
        self.safe_cells = set()
        self.safe_cells.add((0, 0))
        self.visited = set()
        self.percepts_count = 0

    def get_neighbors(self, row, col):
        neighbors = []
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = row + dr, col + dc
            if 0 <= nr < self.rows and 0 <= nc < self.cols:
                neighbors.append((nr, nc))
        return neighbors

    def tell(self, row, col, breeze, stench):
        self.percepts_count += 1
        self.visited.add((row, col))

        neighbors = self.get_neighbors(row, col)

        if breeze:
            pit_literals = [f"P_{nr}_{nc}" for nr, nc in neighbors]
            clause = self.logic.implication_to_cnf(f"B_{row}_{col}", pit_literals)
            self.logic.add_rule(clause)

            self.logic.add_rule([f"B_{row}_{col}"])
        else:
            for nr, nc in neighbors:
                self.logic.add_rule([f"!P_{nr}_{nc}"])

        if stench:
            wumpus_literals = [f"W_{nr}_{nc}" for nr, nc in neighbors]
            clause = self.logic.implication_to_cnf(f"S_{row}_{col}", wumpus_literals)
            self.logic.add_rule(clause)
            self.logic.add_rule([f"S_{row}_{col}"])
        else:
            for nr, nc in neighbors:
                self.logic.add_rule([f"!W_{nr}_{nc}"])

    def ask_safe(self, row, col):
        result_pit, steps_pit = self.logic.ask(f"!P_{row}_{col}")

        result_wumpus, steps_wumpus = self.logic.ask(f"!W_{row}_{col}")

        is_safe = result_pit and result_wumpus

        if is_safe:
            self.safe_cells.add((row, col))

        return is_safe, steps_pit + ["---"] + steps_wumpus

    def find_safe_unvisited(self):
        safe_unvisited = []
        for r in range(self.rows):
            for c in range(self.cols):
                if (r, c) not in self.visited:
                    if (r, c) in self.safe_cells:
                        safe_unvisited.append((r, c))
                    else:
                        is_safe, _ = self.ask_safe(r, c)
                        if is_safe:
                            safe_unvisited.append((r, c))
        return safe_unvisited

    def get_kb_size(self):
        return len(self.logic.kb)

    def get_kb_rules(self):
        return self.logic.get_kb_strings()
