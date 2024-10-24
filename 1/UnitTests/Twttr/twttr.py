def main():
    # Prompt the user for input
    user_input = input("Input: ")

    # Call the function to remove vowels and print the result
    print("Output:", shorten(user_input))


def shorten(text):
    vowels = "aeiouAEIOU"
    result = ""  # Initialize an empty string for the result

    # Loop through each character in the input text
    for char in text:
        # If the character is not a vowel, add it to the result
        if char not in vowels:
            result += char

    return result


# Call the main function when the script is executed
if __name__ == "__main__":
    main()
