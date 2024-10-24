def fraction():
    while True:
        try:
            # Take input from user
            fraction = input("Fraction: ")

            # Split the input by '/' to get numerator and denominator
            x, y = fraction.split("/")

            # Convert x and y to integers
            x = int(x)
            y = int(y)

            # Check if X is greater than Y
            if x > y:
                print("Numerator cannot be greater than denominator. Try again.")
                continue

            return x, y

        except (ValueError, ZeroDivisionError):
            # Handle both ValueError and ZeroDivisionError together
            print("Invalid input. Either non-integer values or zero denominator. Try again.")


def fraction_to_percent(numerator, denominator):
    decimal_value = numerator / denominator
    percentage = decimal_value * 100
    return round(percentage)


# Get fraction input from user
x, y = fraction()

# Convert fraction to percentage
result = fraction_to_percent(x, y)
if result <= 1:
    print("E")
elif result >= 99:
    print("F")
else:
    print(f"{result}%")
