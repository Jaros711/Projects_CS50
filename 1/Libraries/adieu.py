import inflect

p = inflect.engine()

# Create the list to keep track od names
name_list = []


while True:
    try:
        # Ask for user input
        user_input = input("Name: ")
        name_list.append(user_input)
    # Scan for ctrl+D and break out of the loop
    except EOFError:
        # When EOF is detected, exit the loop
        print()  # Print a newline for better formatting
        break

# Print using inflect library
output = p.join(name_list)
print("Adieu, adieu, to " + output)
