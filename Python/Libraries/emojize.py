import emoji


def main():
    # Prompt the user for input
    user_input = input("Input: ")

    # Convert the input using emojize with aliases
    emojized_output = emoji.emojize(user_input, language='alias')

    # Print the output
    print("Output:", emojized_output)


if __name__ == "__main__":
    main()
