def special_math(num):
    """ Takes in an integer number greater than or equal to 0 and returns the 
        results of a special math calculation.

        Throws an error if it receives an input that is not a positive integer

        >>> special_math(7)
        79

        >>> special_math(-1)
        Traceback (most recent call last):
        ...
        ValueError: Number must be 0 or larger

        >>> special_math(1.0)
        Traceback (most recent call last):
        ...
        ValueError: Number must be an integer

        >>> special_math('hello')
        Traceback (most recent call last):
        ...
        ValueError: Number must be an integer
    """

    if not isinstance(num, int):
        raise ValueError('Number must be an integer')

    if num < 0:
        raise ValueError('Number must be 0 or larger')

    elif num in [0,1]:
        return num

    prev_prev = 0
    prev = 1
    current = num

    for i in range(2, num + 1):
        current = i + prev + prev_prev
        prev_prev = prev
        prev = current
    
    return current