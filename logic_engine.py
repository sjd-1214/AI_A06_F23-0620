class PropositionalLogic:
    def __init__(self):
        self.kb = []
        self.symbols = set()

    def add_rule(self, clause):
        if clause and clause not in self.kb:
            self.kb.append(clause)
            for lit in clause:
                symbol = lit.replace('!', '')
                self.symbols.add(symbol)

    def implication_to_cnf(self, antecedent, consequents):
        clause = ['!' + antecedent] + consequents
        return clause

    def ask(self, query):
        steps = []
        steps.append(f"Query: {query}")

        negated = query[1:] if query.startswith('!') else '!' + query
        steps.append(f"Negated Query: {negated}")

        clauses = [list(c) for c in self.kb] + [[negated]]
        clause_strings = set(self._clause_to_string(c) for c in clauses)

        iterations = 0
        max_iterations = 100

        while iterations < max_iterations:
            iterations += 1
            new_clauses = []

            for i in range(len(clauses)):
                for j in range(i + 1, len(clauses)):
                    resolvents = self._resolve(clauses[i], clauses[j])

                    for resolvent in resolvents:
                        if len(resolvent) == 0:
                            steps.append(f"Resolved: {self._clause_to_string(clauses[i])} with {self._clause_to_string(clauses[j])}")
                            steps.append("Result: [] (Empty clause - Contradiction!)")
                            steps.append(f"Therefore, KB ⊨ {query}")
                            return True, steps

                        res_str = self._clause_to_string(resolvent)
                        if res_str not in clause_strings:
                            new_clauses.append(resolvent)
                            clause_strings.add(res_str)
                            if len(steps) < 25:
                                steps.append(f"New: {res_str}")

            if not new_clauses:
                steps.append("No new clauses generated")
                steps.append(f"KB does NOT entail {query}")
                return False, steps

            clauses.extend(new_clauses)

        steps.append("Max iterations reached")
        return False, steps

    def _resolve(self, clause1, clause2):
        resolvents = []

        for lit1 in clause1:
            for lit2 in clause2:
                if self._are_complementary(lit1, lit2):
                    resolvent = []

                    for lit in clause1:
                        if lit != lit1 and lit not in resolvent:
                            resolvent.append(lit)

                    for lit in clause2:
                        if lit != lit2 and lit not in resolvent:
                            resolvent.append(lit)

                    resolvents.append(resolvent)

        return resolvents

    def _are_complementary(self, lit1, lit2):
        if lit1.startswith('!') and not lit2.startswith('!'):
            return lit1[1:] == lit2
        if not lit1.startswith('!') and lit2.startswith('!'):
            return lit1 == lit2[1:]
        return False

    def _clause_to_string(self, clause):
        if not clause:
            return "[]"
        return " ∨ ".join(clause)

    def get_kb_strings(self):
        return [self._clause_to_string(c) for c in self.kb]

    def clear(self):
        self.kb = []
        self.symbols.clear()
