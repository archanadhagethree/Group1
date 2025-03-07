import sys

def decimal_to_hex(decimal_value, verbose=False):  # Add 'verbose' to suppress print statements in tests

    hex_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

    if decimal_value is None:
        raise ValueError("No input provided")

    # Raise an error if input is not an integer
    if not isinstance(decimal_value, int):
        raise ValueError("Input must be an integer")

    # Handle zero case
    if decimal_value == 0:
        return "0" 
        
    hexadecimal = ""

    num = abs(decimal_value)  # Handle negative numbers correctly

    if verbose:
        print(f"Converting the Decimal Value {num} to Hex...")

    while num != 0:
        rem = num % 16
        hexadecimal = hex_chars[rem] + hexadecimal
        num //= 16

    if verbose:
        print(f"Hexadecimal representation is: {hexadecimal}")

    return hexadecimal if decimal_value >= 0 else "-" + hexadecimal  # Handle negatives

if __name__ == "__main__":
    # Check if an argument is passed
    if len(sys.argv) > 1:
        try:
            decimal_value = int(sys.argv[1])
            print(decimal_to_hex(decimal_value, verbose=True))  # Verbose enabled for CLI
        except ValueError:
            print("Please provide a valid integer.")
    else:
        print("Usage: python script.py <decimal_number>")
