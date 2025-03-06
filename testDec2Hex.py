import unittest
from io import StringIO
import sys
from Dex2Hex import decimal_to_hex


class DecimalToHexTest(unittest.TestCase):

    def test_decimal_to_hex(self):
        # Test for valid decimal to hex numbers
        self.assertEqual(decimal_to_hex(0), '0')     # 0 -> '0'
        self.assertEqual(decimal_to_hex(1), '1')     # 1 -> '1'
        self.assertEqual(decimal_to_hex(255), 'FF')  # 255 -> 'FF'
        self.assertEqual(decimal_to_hex(10), 'A')    # 10 -> 'A'

    def test_invalid_input(self):
        #Test invalid input with error
        sys.argv = ['script.py', 'xyz']
        with self.assertRaises(ValueError):
            decimal_to_hex(int(sys.argv[1]))

    def test_no_input(self):
        #Test if no input argument is given
        sys.argv = ['script.py'] 
        with self.assertRaises(SystemExit):
            decimal_to_hex(int(sys.argv[1]))  # Should exit

if __name__ == "__main__":
    unittest.main()
