import argparse
import threading
import time
from collections import defaultdict, deque
import pprint

# Attribution: https://www.geeksforgeeks.org/dsa/topological-sorting-indegree-based-solution/
def toposort_tasks(tasks):

    in_degree = {name: 0 for name in tasks}
    graph = defaultdict(list)
    runtime = {name: 0 for name in tasks}

    # Build dependency graph and in-degree count
    for name, task in tasks.items():
        for dep in task["dependencies"]:
            if dep not in tasks:
                raise ValueError(f"Task '{name}' has undefined dependency '{dep}'")
            graph[dep].append(name)
            in_degree[name] += 1

    # Start with tasks that have no dependencies
    queue = deque([name for name in tasks if in_degree[name] == 0])
    for name in queue:
        runtime[name] = tasks[name]["duration"]

    processed = 0

    while queue:
        current = queue.popleft()
        processed += 1

        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            runtime[neighbor] = max(
                runtime[neighbor],
                runtime[current] + tasks[neighbor]["duration"]
            )
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if processed != len(tasks):
        raise ValueError("Loop in task list")

    return max(runtime.values())

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
    
    #For debug
    #pprint.pprint(tasks)
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

