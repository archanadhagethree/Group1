import unittest
import sys
from Dec2Hex import decimal_to_hex

class DecimalToHexTest(unittest.TestCase):
    
    def test_decimal_to_hex(self):
        self.assertEqual(decimal_to_hex(0), '0')  # 0 -> '0'
        self.assertEqual(decimal_to_hex(10), 'A')  # 10 -> 'A'
        self.assertEqual(decimal_to_hex(255), 'FF')  # 255 -> 'FF'
    
    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            decimal_to_hex("abc")  # Non-integer input should raise an error
    
    def test_no_input(self):
        # Ensure no input case is handled properly
        if len(sys.argv) <= 1:
            self.assertRaises(SystemExit, decimal_to_hex, None)

if __name__ == "__main__":
    unittest.main()
