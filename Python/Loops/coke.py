def coke_machine():
    amount_due = 50  # Total amount due is 50 cents
    valid_coins = [25, 10, 5]  # Only accept 25, 10, and 5 cent coins

    # Continue asking for coins until the amount due is 0 or less
    while amount_due > 0:
        print(f"Amount Due: {amount_due}")
        coin = int(input("Insert Coin: "))

        # Check if the inserted coin is valid
        if coin in valid_coins:
            amount_due -= coin
        # If coin is not valid, just ignore it and continue
        else:
            continue

    # After the loop ends, calculate if any change is owed
    if amount_due < 0:
        print(f"Change Owed: {abs(amount_due)}")
    else:
        print("Change Owed: 0")

    # Call the function to start the program
coke_machine()
