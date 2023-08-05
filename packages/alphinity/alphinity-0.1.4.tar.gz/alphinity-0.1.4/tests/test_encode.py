from alphinity import encode


def test_alphabetical() -> None:
    assert sorted(map(encode, range(100000))) == [*map(encode, range(100000))]


def test_big() -> None:
    assert len(encode(10**20)) < 20
