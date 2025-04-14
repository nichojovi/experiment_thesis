import unittest
import builtins
from number_stair import print_number_stair

class TestNumberStair(unittest.TestCase):
    def run_test(self, start, step, n, expected_lines):
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
            len(output_lines), len(expected_lines),
            f"For start={start}, step={step}, n={n}, expected {len(expected_lines)} lines, but got {len(output_lines)}.\n"
            "Hint:\n"
            "1. Make sure you're printing one number per line using a loop.\n"
        )

        for i, (actual, expected) in enumerate(zip(output_lines, expected_lines), start=1):
            self.assertEqual(
                actual, expected,
                f"Line {i} is incorrect for start={start}, step={step}, n={n}.\n"
                f"Expected: '{expected}'\n"
                f"Got:      '{actual}'\n"
                "Hint:\n"
                "1. Make sure you're using the formula: start + step * i\n"
            )

    def test_staircase_1(self):
        self.run_test(2, 3, 5, [
            2,
            5,
            8,
            11,
            14
        ])

    def test_staircase_2(self):
        self.run_test(10, 0, 1, [
            10
        ])

    def test_staircase_3(self):
        self.run_test(1, 2, 4, [
            1,
            3,
            5,
            7
        ])

    def test_staircase_4(self):
        self.run_test(0, 2, 5, [
            0,
            2,
            4,
            6,
            8
        ])
    
    def test_staircase_5(self):
        self.run_test(1, 1, 1, [
            1
        ])

if __name__ == '__main__':
    unittest.main()
