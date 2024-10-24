import random
# Get level value
while True:
    try:
        value = int(input("Level: "))
        if value > 0:
            break
    except:
        pass
# Set random number
number = random.randint(1, value)

while True:
    try:
        input_guess = int(input("Guess: "))
        if input_guess > 0:
            if input_guess > number:
                print("Too large!")
            elif input_guess < number:
                print("Too small!")
            else:
                print("Just right!")
                break
    except:
        pass

