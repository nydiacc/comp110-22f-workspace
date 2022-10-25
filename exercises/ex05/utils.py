"""EX05 - Utility Funtions."""

__author__ = "730563759"


def only_evens(x: list[int]) -> list[int]:
    """This function will return a list of even integers."""
    list_evens: list[int] = []
    i: int = 0
    while i < len(x):
        # this loop will index the list to append even numbers to list_evens.
        if x[i] % 2 == 0:
            list_evens.append(x[i])
            i += 1
        else:
            i += 1
    return list_evens


def concat(x: list[int], xs: list[int]) -> list[int]:
    """This function will combine two lists."""
    concat_list: list[int] = []
    i: int = 0
    while i < len(x):
        # this loop appends every index of x, to concat_list. 
        concat_list.append(x[i])
        i += 1
    i = 0
    while i < len(xs):
        # this loop appends every index of xs, to concat_list. 
        concat_list.append(xs[i])
        i += 1

    return concat_list


def sub(x: list[int], start_index: int, end_index: int) -> list[int]:
    """This function will return a list between the given indexes."""
    i: int = start_index
    idx: int = end_index
    sub_list: list[int] = []
    empty_list: list[int] = []

    if len(x) == 0 or i >= len(x) or idx <= 0:
        return empty_list
    if i < 0:
        i = 0
    if idx > len(x):
        idx = len(x)

    while i < idx:
        # this loop appends from the given start_index and end_index to our sub_list.
        sub_list.append(x[i])
        i += 1
    return sub_list