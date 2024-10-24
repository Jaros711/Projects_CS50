# Replace smiley text for emoticon

def convert(text):
    text = text.replace(':)', '🙂')
    text = text.replace(':(', '🙁')
    return text

def main():
    text = input("Enter a string: ")
    converted = convert(text)
    print(converted)

main()

