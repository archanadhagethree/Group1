import unittest
from io import StringIO
import sys
from Dec2Hex import decimal_to_hex

class TestDecimalToHex(unittest.TestCase):
    
    def test_valid_decimal(self):
        """Test with a valid decimal value (e.g., 255)"""
        decimal_value = 255
        expected_output = "Hexadecimal representation is: FF"
        
        captured_output = StringIO()
        sys.stdout = captured_output  # Redirect stdout
        try:
            decimal_to_hex(decimal_value)
        finally:
            sys.stdout = sys.__stdout__  # Reset stdout
        
        self.assertIn(expected_output, captured_output.getvalue())

    def test_input_is_not_integer(self):
        """Test if the function raises TypeError for non-integer input"""
        with self.assertRaises(TypeError):
            decimal_to_hex("string")

    def test_decimal_less_than_one(self):
        """Test if the function handles a decimal value less than 1 (e.g., 0)"""
        captured_output = StringIO()
        sys.stdout = captured_output  # Redirect stdout
        try:
            decimal_to_hex(0)
        finally:
            sys.stdout = sys.__stdout__  # Reset stdout
        
        self.assertIn("Please provide Decimal value greater than 0", captured_output.getvalue())

    def test_valid_edge_case(self):
        """Test with another valid decimal value (e.g., 16)"""
        decimal_value = 16
        expected_output = "Hexadecimal representation is: 10"
        
        captured_output = StringIO()
        sys.stdout = captured_output  # Redirect stdout
        try:
            decimal_to_hex(decimal_value)
        finally:
            sys.stdout = sys.__stdout__  # Reset stdout
        
        self.assertIn(expected_output, captured_output.getvalue())

    def test_invalid_input(self):
        """Test when no input is provided (simulating missing argument)"""
        captured_output = StringIO()
        sys.stdout = captured_output  # Redirect stdout
        try:
            decimal_to_hex(None)  # Assuming function handles None as missing input
        finally:
            sys.stdout = sys.__stdout__  # Reset stdout
        
        self.assertIn("Error: No input provided. Please provide a decimal number.", captured_output.getvalue())

if __name__ == "__main__":
    unittest.main()
