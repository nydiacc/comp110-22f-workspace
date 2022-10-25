"""EX04 - Utils."""

__author__ = "730563759"


def all(integers: list[int], integer: int) -> bool:
    """This function checks if the given integer matches the list of integers."""
    i: int = 0 
    if len(integers) == 0:
        return False
    while i < len(integers):
        # loop to check if list of numbers matches given integer.
        current: int = integers[i]
        if integer == current:
            i += 1
        else:
            return False
    return True


def max(integers: list[int]) -> int:
    """This function will return the largest number in the list."""
    if len(integers) == 0:
        raise ValueError("max() arg is an empty List")
    max_value: int = integers[0]
    i: int = 1
    while i < len(integers):
        if integers[i] > max_value:
            max_value = integers[i]
        i += 1
    return max_value


def is_equal(input: list[int], input_two: list[int]) -> bool:
    """This function checks if the lists match at each index."""
    i: int = 0
    if len(input) != len(input_two):
        return False
    while i < len(input):
        # loop to check if list of numbers matches given integer.
        current: int = input[i]
        current_two: int = input_two[i]
        if current_two == current:
            i += 1
        else:
            return False
    return True