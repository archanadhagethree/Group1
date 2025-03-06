import sys


def decimal_to_hex(decimal_value):

    hex_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

    # Handle zero Input
    if decimal_value == 0: 
        return "0"


    hexadecimal = ""

    num = decimal_value

    print(f"Converting the Decimal Value {num} to Hex...")

    while num != 0:

        rem = num % 16

        hexadecimal = hex_chars[rem] + hexadecimal

        num //= 16

    print(f"Hexadecimal representation is: {hexadecimal}")

    return hexadecimal # Return the hexadecimal value for testing

if __name__ == "__main__":

    # Check 1 argument is passed or not
    if len(sys.argv) == 2:
        
        try:

            decimal_value = int(sys.argv[1])

            decimal_to_hex(decimal_value)

        except ValueError:

            print("Please provide a valid integer.")
    else:
        print("Usage: python script.py <decimal_number>")
else:

    print("Usage: python script.py <decimal_number>")
