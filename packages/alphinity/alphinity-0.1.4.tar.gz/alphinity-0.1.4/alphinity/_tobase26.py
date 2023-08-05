import string


def tobase26(num: int) -> str:
    """Convert a non-negative integer to a base-26 string.

    Parameters
    ----------
    num : int
        A non-negative integer to be converted.

    Returns
    -------
    str
        The base-26 representation of the input integer.

    Raises
    ------
    ValueError
        If the input integer is negative.

    Examples
    --------
    >>> tobase26(0)
    'a'
    >>> tobase26(25)
    'z'
    >>> tobase26(27)
    'ab'

    Notes
    -----
    This function uses lowercase letters to represent digits in the base-26
    number system.
    """
    if num < 0:
        raise ValueError("Input must be a non-negative integer.")

    numerals = string.ascii_lowercase
    base = len(numerals)

    digits = []
    while num:
        digits.append(numerals[num % base])
        num //= base
    return "".join(digits[::-1]) or numerals[0]
    if num < 0:
        raise ValueError

    numerals = string.ascii_lowercase
    base = len(numerals)

    digits = []
    while num:
        digits.append(numerals[num % base])
        num //= base
    return "".join(digits[::-1]) or numerals[0]
