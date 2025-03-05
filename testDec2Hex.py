import unittest
from io import StringIO
import sys


class TestDecimalToHex(unittest.TestCase):

    def test_decimal_to_hex(self):
        """Test conversion of decimal to hexadecimal."""
        # Test for valid decimal numbers
        self.assertEqual(decimal_to_hex(255), 'FF')  # 255 -> 'FF'
        self.assertEqual(decimal_to_hex(10), 'A')    # 10 -> 'A'
        self.assertEqual(decimal_to_hex(0), '0')     # 0 -> '0'
        self.assertEqual(decimal_to_hex(1), '1')     # 1 -> '1'

    def test_invalid_input(self):
        """Test invalid input that should raise ValueError."""
        sys.argv = ['script.py', 'abc']  # Simulate invalid input (non-integer)
        with self.assertRaises(ValueError):
            decimal_to_hex(int(sys.argv[1]))

    def test_no_input(self):
        """Test if no input argument is provided."""
        sys.argv = ['script.py']  # No argument passed
        with self.assertRaises(SystemExit):
            decimal_to_hex(int(sys.argv[1]))  # Should exit

if __name__ == "__main__":
    unittest.main()
