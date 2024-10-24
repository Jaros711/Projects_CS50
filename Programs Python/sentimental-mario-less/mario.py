# Get size of pyramid
while True:
    try:
        n = int(input("Height: "))
        if 1 <= n <= 8:
            break
    except ValueError:
        print("Enter a number 1-8")

# Print grid of bricks
for i in range(n):
    for j in range(n):
        if i + j < n - 1:
            print(" ", end="")
        else:
            print("#", end="")
    print()
