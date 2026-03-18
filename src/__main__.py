"""CLI for deepplanner."""
import sys, json, argparse
from .core import Deepplanner

def main():
    parser = argparse.ArgumentParser(description="Agent harness with hierarchical planning tools, filesystem backend, and autonomous subagent spawning")
    parser.add_argument("command", nargs="?", default="status", choices=["status", "run", "info"])
    parser.add_argument("--input", "-i", default="")
    args = parser.parse_args()
    instance = Deepplanner()
    if args.command == "status":
        print(json.dumps(instance.get_stats(), indent=2))
    elif args.command == "run":
        print(json.dumps(instance.decompose(input=args.input or "test"), indent=2, default=str))
    elif args.command == "info":
        print(f"deepplanner v0.1.0 — Agent harness with hierarchical planning tools, filesystem backend, and autonomous subagent spawning")

if __name__ == "__main__":
    main()
