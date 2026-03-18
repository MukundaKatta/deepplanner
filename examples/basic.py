"""Basic usage example for deepplanner."""
from src.core import Deepplanner

def main():
    instance = Deepplanner(config={"verbose": True})

    print("=== deepplanner Example ===\n")

    # Run primary operation
    result = instance.decompose(input="example data", mode="demo")
    print(f"Result: {result}")

    # Run multiple operations
    ops = ["decompose", "execute_plan", "spawn_subagent]
    for op in ops:
        r = getattr(instance, op)(source="example")
        print(f"  {op}: {"✓" if r.get("ok") else "✗"}")

    # Check stats
    print(f"\nStats: {instance.get_stats()}")

if __name__ == "__main__":
    main()
