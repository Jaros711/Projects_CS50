def camel_to_snake(camel_case):
    # Create empty string to store the result
    snake_case = ""

    # Loop through each character in the input string
    for char in camel_case:
        # Check if the character is uppercase
        if char.isupper():
            # Add an underscore and the lowercase version of the character
            snake_case += '_' + char.lower()
        else:
            # Add a character if is lowercase
            snake_case += char

    # Return the final snake_case
    return snake_case


# Prompt the user for input
camel_case_input = input("Enter a camelCase string: ")

# Call the function and print the result
print("The snake_case is: ", camel_to_snake(camel_case_input))
