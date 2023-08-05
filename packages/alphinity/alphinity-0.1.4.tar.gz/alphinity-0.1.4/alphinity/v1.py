import string

from ._tobase26 import tobase26


def _encode(value: int) -> str:
    """Implementation detail."""
    chars = string.ascii_lowercase
    base = len(chars)
    n = 0

    while value >= base**n:
        value -= base**n
        n += 1

    digits = tobase26(value)
    return chars[n] + digits.rjust(n, "a") if n else digits


def encode(value: int) -> str:
    """Encode a non-negative integer into a string representation that
    alphabetizes in ascending order.

    Parameters
    ----------
    value : int
        A non-negative integer to be encoded.

    Returns
    -------
    str
        The base-26 representation of the input integer.

    Raises
    ------
    ValueError
        If the input integer is negative.
    """
    if value < 0:
        raise ValueError("value must be a non-negative integer")
    try:
        return _encode(value)
    except IndexError:
        raise ValueError("value is too large")
