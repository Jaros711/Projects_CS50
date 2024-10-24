def main():
    greeting = input("Give me your greeting: ")
    print("$",value(greeting))



def value(greeting):
    greeting = greeting.strip().lower()

    if "hello" in greeting:
        return 0
    elif "h" == greeting[0]:
        return 20
    else:
        return 100


# Call the main function when the script is executed
if __name__ == "__main__":
    main()
