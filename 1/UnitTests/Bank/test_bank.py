from bank import value


def main():
    test_greeting_starts_hello()
    test_greeting_starts_h()
    test_greeting_starts_unique()


def test_greeting_starts_hello():
    assert value("hello") == 0
    assert value("hello 123") == 0
    assert value("Hello") == 0


def test_greeting_starts_h():
    assert value("h123") == 20
    assert value("hey") == 20
    assert value("hi") == 20


def test_greeting_starts_unique():
    assert value("JHJGF") == 100
    assert value("1234") == 100
    assert value("<>?") == 100


if __name__ == "__main__":
    main()
