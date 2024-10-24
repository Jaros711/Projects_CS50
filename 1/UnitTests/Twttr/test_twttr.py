from twttr import shorten


# Call test function
def main():
    test_upper_lower()
    test_numbers()
    test_punctuation()

# Test upper and lower letters


def test_upper_lower():
    assert shorten("twitter") == "twttr"
    assert shorten("TWITTER") == "TWTTR"

# Test numbers


def test_numbers():
    assert shorten("9876") == "9876"

# Test punctuation


def test_punctuation():
    assert shorten("<>?") == "<>?"


if __name__ == "__main__":
    main()
