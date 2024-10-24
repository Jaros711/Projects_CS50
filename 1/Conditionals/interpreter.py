def calculate(expression):
    # Split the expression into operands and operator
    x, y, z = expression.split()

    # Convert operands to integers
    x = int(x)
    z = int(z)

    # Perform the operation based on the operator
    if y == '+':
        result = x + z
    elif y == '-':
        result = x - z
    elif y == '*':
        result = x * z
    elif y == '/':
        result = x / z

    # Round the result to one decimal place and return as a float
    return float(result)

def main():
    # Prompt the user for an arithmetic expression
    expression = input("Enter an arithmetic expression (e.g., '1 + 1'): ")

    # Calculate the result
    result = calculate(expression)

    # Output the result directly without additional string
    print(result)

if __name__ == "__main__":
    main()
