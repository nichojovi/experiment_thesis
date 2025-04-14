import unittest
import builtins
from print_poem import print_poem

class TestPoem(unittest.TestCase):
    def test_poem(self):
        output_lines = []

        def mock_print(text):
            output_lines.append(text)

        original_print = builtins.print
        builtins.print = mock_print

        try:
            print_poem()
        finally:
            builtins.print = original_print

        expected_lines = [
            "Roses are red,",
            "Violets are blue,",
            "Sugar is sweet,",
        ]

        self.assertEqual(
            len(output_lines), 
            len(expected_lines),
            f"Expected {len(expected_lines)} lines to be printed, but got {len(output_lines)}.\n"
            "Hint:\n"
            "1. Make sure you're using one print statement for each line of the poem. \n"
        )

        for i, (expected, actual) in enumerate(zip(expected_lines, output_lines), start=1):
            self.assertEqual(
                actual, 
                expected,
                f"Line {i} is incorrect.\n"
                f"Expected: \"{expected}\"\n"
                f"Received: \"{actual}\"\n"
                f"Hint: Please check for exact wording, punctuation, and capitalization. \n"
            )

if __name__ == '__main__':
    unittest.main()
