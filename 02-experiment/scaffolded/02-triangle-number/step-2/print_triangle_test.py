import unittest
import builtins
from print_triangle import print_number_triangle

class TestNumberTriangle(unittest.TestCase):
    def run_test(self, n, expected_lines):
        output_lines = []

        def mock_print(text):
            output_lines.append(text)

        original_print = builtins.print
        builtins.print = mock_print

        try:
            print_number_triangle(n)
        finally:
            builtins.print = original_print

        self.assertEqual(
            len(output_lines), len(expected_lines),
            f"For n = {n}, expected {len(expected_lines)} lines, but got {len(output_lines)}.\n"
        )

        for i, (actual, expected) in enumerate(zip(output_lines, expected_lines), start=1):
            self.assertEqual(
                actual, expected,
                f"Line {i} for n = {n} is incorrect.\n"
                f"Expected: '{expected}'\n"
                f"Got:      '{actual}'\n"
                "Hint:\n"
                "1. Make sure to print n as much as n times.\n"
            )

    def test_triangle_n1(self):
        self.run_test(1, [
            "1"
        ])

    def test_triangle_n2(self):
        self.run_test(2, [
            "2",
            "2"
        ])

    def test_triangle_n3(self):
        self.run_test(3, [
            "3",
            "3",
            "3"
        ])

    def test_triangle_n4(self):
        self.run_test(4, [
            "4",
            "4",
            "4",
            "4"
        ])

    def test_triangle_n5(self):
        self.run_test(5, [
            "5",
            "5",
            "5",
            "5",
            "5"
        ])

if __name__ == '__main__':
    unittest.main()
