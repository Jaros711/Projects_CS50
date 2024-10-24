# taqueria.py

# Menu dictionary with item prices
menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    total_cost = 0.0

    while True:
        try:
            # Prompt user for input
            item = input("Enter an item: ").strip()  # Read input and remove any leading/trailing whitespace

            # Normalize input to title case for dictionary lookup
            item_normalized = item.title()

            # Check if the item is in the menu
            if item_normalized in menu:
                total_cost += menu[item_normalized]  # Add to total cost
            elif item:  # Only prompt for invalid items if input is not empty
                print("Item not on the menu, please try again.")

            # Print the total formatted to two decimal places
            print(f"Total: ${total_cost:.2f}\n")  # Print total with newline for formatting

        except EOFError:
            # When EOF is detected, exit the loop
            print()  # Print a newline for better formatting
            break

if __name__ == "__main__":
    main()
