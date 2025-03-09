import unittest
from Dec2Hex import decimal_to_hex

class Dec2HexTest(unittest.TestCase):

    def test_conversions(self):
        """Test standard decimal to hex conversions"""
        test_cases = [
            (15, "F"),
            (16, "10"),
            (255, "FF"),
            (10, "A"),
            (11, "B"),
            (12, "C"),
            (13, "D"),
            (14, "E")
        ]
        for decimal, expected in test_cases:
            with self.subTest(decimal=decimal):
                self.assertEqual(decimal_to_hex(decimal), expected)
                
    def test_zero_input(self):
        """Test that zero returns '0' per current implementation"""
        self.assertEqual(decimal_to_hex(0), "0")  # Expected result is "0", not an empty string
        
    def test_power_16(self):
        """Test numbers that are powers of 16"""
        self.assertEqual(decimal_to_hex(16), "10")
        self.assertEqual(decimal_to_hex(256), "100")
        
    def test_invalid_input(self):
        """Test that non-integer input raises a TypeError"""
        with self.assertRaises(TypeError):
            decimal_to_hex("abc")
        with self.assertRaises(TypeError):
            decimal_to_hex(12.5)

    def test_none_input(self):
        """Test that None input raises a ValueError"""
        with self.assertRaises(ValueError):
            decimal_to_hex(None)

if __name__ == '__main__':
    unittest.main(verbosity=2)
