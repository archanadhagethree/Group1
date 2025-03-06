import unittest
from Dec2Hex import decimal_to_hex

class DecimalToHexTest(unittest.TestCase):

    def test_decimal_to_hex(self):
        self.assertEqual(decimal_to_hex(0), '0')  
        self.assertEqual(decimal_to_hex(10), 'A')  
        self.assertEqual(decimal_to_hex(255), 'FF')  

    def test_invalid_input(self):
        with self.assertRaises(ValueError):  
            decimal_to_hex("abc")  # Non-integer input should raise an error

        with self.assertRaises(ValueError):
            decimal_to_hex(12.5)  # Float should also raise an error

    def test_no_input(self):
        with self.assertRaises(SystemExit):  
            decimal_to_hex(None)  # No input should cause the function to exit

if __name__ == "__main__":
    unittest.main()
