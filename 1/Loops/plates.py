def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Rule 2: The length must be between 2 and 6 characters
    if not (2 <= len(s) <= 6):
        return False

    # Rule 1: The plate must start with at least two letters
    if not s[0:2].isalpha():
        return False

    # Rule 3: Numbers cannot be in the middle, must be at the end, and no leading zeroes
    number_found = False
    for i, char in enumerate(s):
        if char.isdigit():
            if not number_found and char == '0':
                return False  # Numbers can't start with '0'
            number_found = True
        elif number_found:
            return False  # No letters allowed after numbers start

    # Rule 4: No periods, spaces, or punctuation marks are allowed
    if not s.isalnum():
        return False

    # If all checks passed, the plate is valid
    return True


# Run the main function
main()
