import sys

def decimal_to_hex(decimal_value):
    if decimal_value is None:
        raise ValueError("Input cannot be None")  # Handle None properly
    
    if not isinstance(decimal_value, int):
        raise TypeError("Input must be an integer")  # Ensure only integers are allowed

    if decimal_value == 0:
        return "0"

    hex_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    hexadecimal = ""
    num = decimal_value

    while num != 0:
        rem = num % 16
        hexadecimal = hex_chars[rem] + hexadecimal  # Ensure concatenation works
        num //= 16

    return hexadecimal

if __name__ == "__main__":

    if len(sys.argv) < 2:  # Check if an argument is provided
        print("No input provided!. Please provide a decimal number as an argument.")
        sys.exit(1)

    decimal_value = int(sys.argv[1])
    hexadecimal = decimal_to_hex(decimal_value)
    print(f"Converting the Decimal Value {decimal_value} to Hex.\n Hexadecimal representation is: {hexadecimal}")
