import unittest
from submission import submit_task

class TestSubmitTask(unittest.TestCase):

    def test_successful_submission(self):
        result = submit_task("123", "task1", "My answer")
        self.assertEqual(result, "Submission successful")

    def test_empty_submission(self):
        result = submit_task("123", "task1", "")
        self.assertEqual(result, "Submission cannot be empty")

if __name__ == "__main__":
    unittest.main()