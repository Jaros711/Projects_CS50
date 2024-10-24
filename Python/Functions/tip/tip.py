def main():
    dollars = dollars_to_float(input("How much was the meal? "))    # Ask for amout
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip: .2f}")


def dollars_to_float(input):
    amount = float(input.replace("$", ""))  # Remove $ sign and return float amout to
    return(round(amount, 2))


def percent_to_float(input):
    percent = float(input.replace("%", "")) # Remove the trailing %, and return the percentage as a float
    return percent / 100


main()
