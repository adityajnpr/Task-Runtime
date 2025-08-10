# Task-Runtime
Coding Challange

# Problem Description
Write a command line tool to schedule and optionally run a series of tasks in parallel,
according to a task list specification input in text.
The schema for the task list is:
name, duration in seconds, dependencies (as a list of names)
...
Include an option to validate the input task list and output the expected total runtime
without running the tasks.
Include a second option to run the tasks and determine the difference in the actual
runtime versus the expected runtime.

# Solution Approach
The solution key is to figure out this is a directed graph problem with topological sort.
This elements are topologically sorted, the graph can be traversed to find the max interval.
There are 2 approaches that can be used:
* DFS Search
* Kahn's algorithm

Choice of implementation was based on simplicity of the code and ease of explaination during
the interview :)

# Code Flow
<img width="805" height="413" alt="image" src="https://github.com/user-attachments/assets/380b16f0-5313-47a9-86a9-88d046eaa64d" />


# Instructions for User
## Downloading Files

From the github page, download files directly on your laptop by clicking the green code button on the page.
Alternative execute the github cli to clone the repo:

```gh repo clone adityajnpr/Task-Runtime```

### Executing the script
Validate option:

``` python3 parallel_tasks.py tasks.txt --validate ```

Execute option:

```python3 parallel_tasks.py tasks.txt --execute```

User can also modify the tasks.txt file to try different scenerios

### Running unit test module

```python3 -m unittest test_parallel_tasks.py  ```



