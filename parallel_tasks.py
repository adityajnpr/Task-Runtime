import argparse
import threading
import time
from collections import defaultdict, deque
import pprint

def toposort_tasks(tasks):
	return(100)

def create_tasks(filepath):

    tasks = {}
    with open(filepath, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            name, duration_str, deps_str = line.split(",",2)
            name = name.strip()
            duration = int(duration_str.strip())

            dependencies = eval(deps_str.strip())
            if not isinstance(dependencies, list):
                raise TypeError("Dependencies should be a list")

            tasks[name] = {
                "duration": duration,
                "dependencies": dependencies
            }
    pprint.pprint(tasks)
    return tasks

def main():
    parser = argparse.ArgumentParser(description="Parallel task Scheduler")
    parser.add_argument("filename", help="Task file")
    parser.add_argument("--validate", action="store_true", help="Validate and displau expected runtime")
    parser.add_argument("--execute", action="store_true",help="Execute tasks and compare runtimes")
    args = parser.parse_args()

    if args.validate:
        try:
            tasks = create_tasks(args.filename)
            expected_runtime = toposort_tasks(tasks)
            print(f"Expected runtime: {expected_runtime} seconds")
        except Exception as e:
            print(f"Error: {e}")
            return

if __name__ == "__main__":
    main()

