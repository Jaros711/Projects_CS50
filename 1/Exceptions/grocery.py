# grocery.py

def main():
    grocery_list = {}  # Dictionary to store items and their quantities

    while True:
        try:
            item = input().strip()  # Read input and remove leading/trailing whitespace

            # Convert to uppercase and treat input case-insensitively
            item_upper = item.upper()

            # Update the dictionary with the item count
            if item_upper in grocery_list:
                grocery_list[item_upper] += 1
            else:
                grocery_list[item_upper] = 1

        except EOFError:
            break  # Exit the loop on EOF

    # Output the sorted grocery list
    for item in sorted(grocery_list.keys()):
        print(f"{grocery_list[item]} {item}")


if __name__ == "__main__":
    main()
