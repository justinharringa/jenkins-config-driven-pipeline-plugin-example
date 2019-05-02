from hello import add_it_up, hello


def test_add_it_up():
    assert add_it_up(3, 2) == 5


def test_hello():
    assert hello("kitty") == "Hello kitty!"
