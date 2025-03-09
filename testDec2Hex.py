import unittest
from Dec2Hex import decimal_to_hex

class TestDecimalToHex(unittest.TestCase):

    def test_valid_decimal(self):
        self.assertEqual(decimal_to_hex(255), "FF")
        self.assertEqual(decimal_to_hex(0), "0")
        self.assertEqual(decimal_to_hex(-255), "FF")
        self.assertEqual(decimal_to_hex(16), "10")

    def test_verbose_output(self):
        # Capturing output for verbose=True
        import sys
        from io import StringIO
        sys.stdout = StringIO()
        decimal_to_hex(255, verbose=True)
        output = sys.stdout.getvalue()
        self.assertIn("Converting the Decimal Value 255 to Hex...", output)
        self.assertIn("Hexadecimal representation is : FF", output)
        self.assertIn("The Decimal value for this is: 255", output)
        sys.stdout = sys.__stdout__  # Reset stdout

    def test_invalid_input(self):
        # Test for None input
        with self.assertRaises(ValueError):
            decimal_to_hex(None)

        # Test for non-integer input
        with self.assertRaises(TypeError):
            decimal_to_hex("hello")

    def test_edge_case_zero(self):
        # Test for zero case
        self.assertEqual(decimal_to_hex(0), "0")

if __name__ == "__main__":
    unittest.main()
