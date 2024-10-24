import random

# Constants for levels
LEVEL_ONE = 1
LEVEL_TWO = 2
LEVEL_THREE = 3

# Constants for ranges
RANGES = {
    LEVEL_ONE: (0, 9),
    LEVEL_TWO: (10, 99),
    LEVEL_THREE: (100, 999)
}

def main():
    level = get_level()  # Call get_level
    score = simulate(level)  # Get the score
    print("Score:", score)  # Print score

def get_level():
    while True:  # Loop forever
        try:
            level = int(input("Level: "))  # Prompt the user for level
            if level in [LEVEL_ONE, LEVEL_TWO, LEVEL_THREE]:
                return level
        except ValueError:  # Specify exception type
            pass  # Ignore invalid input

def generate_integer(level):
    # Use the defined ranges to generate integers
    x = random.randint(*RANGES[level])
    y = random.randint(*RANGES[level])
    return x, y

def solve_equation(x, y):  # Corrected the function name
    count_tries = 1
    while count_tries <= 3:
        try:
            answer = int(input(f"{x} + {y} = "))
            if answer == (x + y):
                return True
            else:
                count_tries += 1
                print("EEE")  # Incorrect answer
        except ValueError:  # Specify exception type
            count_tries += 1
            print("EEE")  # Invalid input
    print(f"{x} + {y} = {x + y}")  # Show the correct answer after 3 failed attempts
    return False

def simulate(level):
    score = 0
    for _ in range(10):  # Loop to generate 10 problems
        x, y = generate_integer(level)
        if solve_equation(x, y):
            score += 1
    return score

if __name__ == "__main__":
    main()
