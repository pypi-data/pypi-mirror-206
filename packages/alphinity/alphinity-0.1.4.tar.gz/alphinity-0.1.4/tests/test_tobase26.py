from alphinity._tobase26 import tobase26


def test_tobase26() -> None:
    # Test converting a single-digit number to base-26
    assert tobase26(0) == "a"
    assert tobase26(1) == "b"
    assert tobase26(2) == "c"
    assert tobase26(25) == "z"

    # Test converting a double-digit number to base-26
    assert tobase26(26) == "ba"
    assert tobase26(27) == "bb"
    assert tobase26(51) == "bz"
    assert tobase26(52) == "ca"

    # Test converting a triple-digit number to base-26
    assert tobase26(676) == "baa"
    assert tobase26(677) == "bab"
    assert tobase26(701) == "baz"
    assert tobase26(702) == "bba"

    # Test converting zero to base-26
    assert tobase26(0) == "a"

    # Test converting a negative number to base-26 (should raise a ValueError)
    try:
        tobase26(-1)
    except ValueError:
        pass
    else:
        assert False, "Expected a ValueError to be raised"
