# Define a dictionary with fruits and their corresponding calories
fruit_calories = {
    "apple": 130,
    "avocado": 50,
    "banana": 110,
    "cantaloupe": 50,
    "grapefruit": 60,
    "grapes": 90,
    "honeydew melon": 50,
    "kiwifruit": 90,
    "lemon": 15,
    "lime": 20,
    "nectarine": 60,
    "orange": 80,
    "peach": 60,
    "pear": 100,
    "pineapple": 50,
    "plums": 70,
    "strawberries": 50,
    "sweet cherries": 100,
    "tangerine": 50,
    "watermelon": 80
}

# Prompt the user for a fruit name (case-insensitive)
fruit = input("Enter a fruit: ").strip().lower()

# Check if the fruit is in the dictionary
if fruit in fruit_calories:
    # Output the number of calories
    print(f"Calories: {fruit_calories[fruit]}")

