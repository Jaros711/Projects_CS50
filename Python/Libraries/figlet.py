import sys
import random
from pyfiglet import Figlet

def main():
    figlet = Figlet()

    # Check command-line arguments
    if len(sys.argv) == 1:
        # No arguments, use random font
        font = random.choice(figlet.getFonts())
    elif len(sys.argv) == 3:
        # Check for -f or --font
        if sys.argv[1] in ["-f", "--font"]:
            font = sys.argv[2]
            # Check if the font is valid
            if font not in figlet.getFonts():
                sys.exit("Invalid usage")
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")

    # Set the font
    figlet.setFont(font=font)

    # Prompt for text input
    text = input("Enter text: ")

    # Generate and print the figlet output
    print(figlet.renderText(text))

if __name__ == "__main__":
    main()
