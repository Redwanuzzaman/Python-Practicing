# TypeConversion from decimal with base 10
# to hexadecimal form with base 16


# Taking input from user
# an integer with base 10
number = int(input("Enter a number with base 10\n"))

# The choices present to the user
print("1. Decimal to Hexadecimal ")
print("2. Decimal to Octal")
print("3. Decimal to Binary")

# taking user input
print("Enter your choice :- ")
choice = int(input())

# Running a variable choice
# Hexadecimal form if choice
# is set to 'a'
if choice == 1:
    # lstrip helps remove "0x" from the left
    # rstrip helps remove "L" from the right,
    # L represents a long number
    print("Hexadecimal form of " + str(number) +
          " is " + hex(number).lstrip("0x").rstrip("L"))

if choice == 2:
    # Octal representation is done
    # by adding a prefix "0o"
    print("Octal form of " + str(number) +
          " is " + oct(number).lstrip("0o").rstrip("L"))

if choice == 3:
    # Binary representation is done by
    # the addition of prefix "0b"
    print("Binary form of " + str(number) +
          " is " + bin(number).lstrip("0b").rstrip("L"))
