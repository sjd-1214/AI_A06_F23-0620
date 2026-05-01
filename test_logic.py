"""
Test script to demonstrate the propositional logic and resolution
Student ID: F23-0620
"""

from logic_engine import PropositionalLogic
from wumpus_agent import WumpusAgent
from wumpus_world import WumpusWorld

def test_resolution():
    print("=" * 60)
    print("Testing Resolution Refutation Algorithm")
    print("=" * 60)

    logic = PropositionalLogic()

    # Example: If we have breeze at (1,1), then adjacent cells have pits
    # B_1_1 => (P_0_1 v P_1_0 v P_2_1 v P_1_2)
    # This becomes: !B_1_1 v P_0_1 v P_1_0 v P_2_1 v P_1_2

    print("\nAdding rule: B_1_1 => (P_0_1 ∨ P_1_0 ∨ P_2_1 ∨ P_1_2)")
    clause = logic.implication_to_cnf("B_1_1", ["P_0_1", "P_1_0", "P_2_1", "P_1_2"])
    logic.add_rule(clause)

    print("Adding fact: B_1_1 (we sense a breeze)")
    logic.add_rule(["B_1_1"])

    print("Adding fact: !P_0_1 (no pit at 0,1)")
    logic.add_rule(["!P_0_1"])

    print("Adding fact: !P_1_0 (no pit at 1,0)")
    logic.add_rule(["!P_1_0"])

    print("Adding fact: !P_2_1 (no pit at 2,1)")
    logic.add_rule(["!P_2_1"])

    print("\nKnowledge Base:")
    for i, rule in enumerate(logic.get_kb_strings(), 1):
        print(f"  {i}. {rule}")

    print("\n" + "=" * 60)
    print("Query: Can we prove P_1_2 (pit at 1,2)?")
    print("=" * 60)

    result, steps = logic.ask("P_1_2")

    print("\nResolution Steps:")
    for step in steps:
        print(f"  {step}")

    print(f"\nResult: {'KB entails P_1_2' if result else 'KB does not entail P_1_2'}")

def test_wumpus_world():
    print("\n\n" + "=" * 60)
    print("Testing Wumpus World Agent")
    print("=" * 60)

    world = WumpusWorld(4, 4)
    agent = WumpusAgent(4, 4)

    print(f"\nWorld Configuration:")
    print(f"  Grid size: {world.rows}x{world.cols}")
    print(f"  Wumpus at: {world.wumpus}")
    print(f"  Pits at: {world.pits}")

    print(f"\nAgent starts at (0, 0)")
    breeze, stench = world.get_percepts(0, 0)
    print(f"  Percepts: Breeze={breeze}, Stench={stench}")

    agent.tell(0, 0, breeze, stench)

    print(f"\nKnowledge Base has {agent.get_kb_size()} rules")
    print("Sample rules:")
    for i, rule in enumerate(agent.get_kb_rules()[:5], 1):
        print(f"  {i}. {rule}")

    print("\nTesting safety of cell (0, 1):")
    is_safe, steps = agent.ask_safe(0, 1)
    print(f"  Result: {'SAFE' if is_safe else 'UNSAFE or UNKNOWN'}")
    print(f"  Reasoning steps: {len(steps)} steps taken")

    print(f"\nSafe cells identified: {agent.safe_cells}")

if __name__ == "__main__":
    test_resolution()
    test_wumpus_world()

    print("\n" + "=" * 60)
    print("All tests completed!")
    print("Run 'python app.py' to start the web interface")
    print("=" * 60)
