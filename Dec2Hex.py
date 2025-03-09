import sys

def decimal_to_hex(decimal_value):
    if decimal_value == 0:
        return "0"

    hex_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    hexadecimal = ""
    num = ""
    num = decimal_value

    while num != 0:
        rem = num % 16
        hexadecimal = hex_chars[rem] + hexadecimal
        num //= 16

    print(f"Hexadecimal representation is : {hexadecimal}")

    return hexadecimal

if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            decimal_value = int(sys.argv[1])
            verbose = '--verbose' in sys.argv
            hexadecimal = decimal_to_hex(decimal_value)
            print(f"Hexadecimal: {hexadecimal}")
        except ValueError:
            print("Please provide a valid integer.")
        except TypeError:
            print("Input must be an integer.")
    else:
        print("Usage: python script.py <decimal_number> [--verbose]")
