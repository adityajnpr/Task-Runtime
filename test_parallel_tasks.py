import unittest
from parallel_tasks import create_tasks, toposort_tasks
import tempfile
import os

TEST_CASES = """
# Test 1: Base use case
Task1, 3, []
Task2, 2, ["Task1"]
Task3, 1, ["Task1"]
Task4, 4, ["Task2", "Task3"]
---
# Test 2: Missing dependency
Task1, 3, []
Task2, 2, ["Task10"]
---
# Test 3: Dependence Loop
Task1, 3, ["Task2"]
Task2, 2, ["Task1"]
---
# Test 4: Dependency not a list
Task1, 3, "Task2"
---
# Test 5: Dependency contains non-string
Task1, 3, [1, "Task3"]
---
# Test 6: Duration not an integer
Task1, three, []
---
# Test 7: Empty task name
, 3, []
"""

def load_test_cases():
    return [block.strip() for block in TEST_CASES.strip().split("---") if block.strip()]

def case_to_temp_file(case_content):
    tmp = tempfile.NamedTemporaryFile(mode="w", delete=False)
    tmp.write(case_content)
    tmp.flush()
    tmp.close()
    return tmp.name

class TestTaskScheduler(unittest.TestCase):

    def setUp(self):
        self.cases = load_test_cases()

    def test_valid_case(self):
        path = case_to_temp_file(self.cases[0])
        tasks = create_tasks(path)
        os.remove(path)
        runtime = toposort_tasks(tasks)
        self.assertEqual(runtime, 9)

    def test_missing_dependency_case(self):
        path = case_to_temp_file(self.cases[1])
        tasks = create_tasks(path)
        os.remove(path)
        with self.assertRaises(ValueError):
            toposort_tasks(tasks)

    def test_loop_case(self):
        path = case_to_temp_file(self.cases[2])
        tasks = create_tasks(path)
        os.remove(path)
        with self.assertRaises(ValueError):
            toposort_tasks(tasks)

    def test_dependency_not_list(self):
        path = case_to_temp_file(self.cases[3])
        with self.assertRaises(TypeError):
            create_tasks(path)
        os.remove(path)


    def test_dependency_contains_non_string(self):
        path = case_to_temp_file(self.cases[4])
        with self.assertRaises(TypeError):
            create_tasks(path)
        os.remove(path)

    def test_duration_not_integer(self):
        path = case_to_temp_file(self.cases[5])
        with self.assertRaises(ValueError):
            create_tasks(path)
        os.remove(path)

    def test_empty_task_name(self):
        path = case_to_temp_file(self.cases[6])
        with self.assertRaises(ValueError):
            create_tasks(path)
        os.remove(path)


if __name__ == "__main__":
    unittest.main()

