import sys


import sys

def decimal_to_hex(value):
    if value is None:
        raise ValueError("Error: No input provided")  # Raise an error instead of sys.exit(1)

    if not isinstance(value, int):  
        raise ValueError("Input must be an integer")

    return hex(value)[2:].upper()  # Convert to hex and remove '0x' prefix

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Error: No input provided")
        sys.exit(1)  # Only exit if run as a script

    try:
        value = int(sys.argv[1])  
        print(decimal_to_hex(value))
    except ValueError:
        print("Error: Input must be an integer")
        sys.exit(1)


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
