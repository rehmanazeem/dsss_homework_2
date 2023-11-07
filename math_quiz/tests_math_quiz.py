import unittest
from math_quiz import generate_Random_Int, get_Random_Operation, run_Operation


class TestMathGame(unittest.TestCase):

    def test_generate_Random_Int(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_Random_Int(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_get_Random_Operation(self):
        # TODO
        for _ in range(1000):  # Test a large number of random values
            rand_Operation = get_Random_Operation()
            self.assertTrue(rand_Operation in ['+','-','*'])

    def test_run_Operation(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (1, 3, '+', '1 + 3', 4),
                (-1, 3, '+', '-1 + 3', 2),
                (-1, 3, '*', '-1 * 3', -3),
                (10, 2, '-', '10 - 2', 8),
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                # TODO
                returned_problem, returned_answer = run_Operation(num1, num2, operator)
                self.assertTrue(returned_problem == expected_problem and returned_answer == expected_answer)

if __name__ == "__main__":
    unittest.main()
