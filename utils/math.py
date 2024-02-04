def round_up(x, base):
    """Round x to the nearest multiple of base.
    
    Example:
    >>> round_up(3, 4)
    4

    >>> round_up(5, 4)
    8

    >>> round_up(0, 4)
    0
    """
    return ((x + base - 1) // base) * base