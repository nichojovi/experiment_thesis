import unittest
import builtins
from number_stair import print_number_stair

class TestNumberStair(unittest.TestCase):
    def run_test(self, start, step, n, expected_result):
        output_lines = []

        def mock_print(text):
            output_lines.append(text)

        original_print = builtins.print
        builtins.print = mock_print

        try:
            print_number_stair(start, step, n)
        finally:
            builtins.print = original_print

        self.assertEqual(
            len(output_lines), 1,
            f"For start={start}, step={step}, n={n}, expected 1 line of output, but got {len(output_lines)}.\n"
            "Hint:\n"
            "1. Don't forget to print the result.\n"
            "2. You should only print the final computed result once.\n"
        )

        self.assertEqual(
            output_lines[0], expected_result,
            f"For start={start}, step={step}, n={n}, the output is incorrect.\n"
            f"Expected: '{expected_result}'\n"
            f"Got:      '{output_lines[0]}'\n"
            "Hint:\n"
            "1. Make sure you are using the formula: start + step * n\n"
        )

    def test_staircase_1(self):
        self.run_test(2, 3, 5, 17)

    def test_staircase_2(self):
        self.run_test(10, 0, 1, 10)

    def test_staircase_3(self):
        self.run_test(1, 2, 4, 9)

    def test_staircase_4(self):
        self.run_test(0, 2, 5, 10)

    def test_staircase_5(self):
        self.run_test(1, 1, 1, 2)

if __name__ == '__main__':
    unittest.main()
