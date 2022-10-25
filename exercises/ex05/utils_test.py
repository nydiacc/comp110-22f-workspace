"""EX05 - Utility Funtions."""

__author__ = "730563759"


from utils import only_evens, sub, concat


# only_evens_edge_case
def test_only_evens_empty() -> None:
    """Given an empty list, return an empty list."""
    list_one: list[int] = []
    assert only_evens(list_one) == []
    return None


# only_evens_use_case
def test_only_evens_only_odds() -> None:
    """Given a list of odd integers, return an empty list."""
    list_one: list[int] = [1, 3, 5]
    assert only_evens(list_one) == []
    return None


# only_evens_use_case
def test_only_evens_alternating_parities() -> None:
    """Given a list of alternating odds and evens, return evens."""
    list_one: list[int] = [0, 1, 2, 3, 4, 5]
    assert only_evens(list_one) == [0, 2, 4]
    return None


# concat_edge_case
def test_concat_empty_list() -> None:
    """Given an empty list and a list, return the first list followed by the second."""
    list_one: list[int] = []
    list_two: list[int] = [0, 1, 2]
    assert concat(list_one, list_two) == [0, 1, 2]
    return None


# concat_use_case
def test_concat_different_length_lists() -> None:
    """Given two lists of varying length, return the first list followed by the second."""
    list_one: list[int] = [0]
    list_two: list[int] = [1, 2, 3, 4]
    assert concat(list_one, list_two) == [0, 1, 2, 3, 4]
    return None


# concat_use_case
def test_concat_single_list() -> None:
    """Given two lists with a single number, return the first list followed by the second."""
    list_one: list[int] = [0]
    list_two: list[int] = [1]
    assert concat(list_one, list_two) == [0, 1]
    return None


# sub_edge_case
def test_sub_out_of_range() -> None:
    """Given a list with the same start and end index, return an empty list."""
    list_one: list[int] = [0, 1, 2, 3, 4]
    start_index: int = 1
    end_index: int = 1
    assert sub(list_one, start_index, end_index) == []
    return None


# sub_use_case
def test_sub_entire_list_range() -> None:
    """Given a list with the same index range as its length, return the entire list."""
    list_one: list[int] = [0, 1, 2, 3, 4]
    start_index: int = 0
    end_index: int = 5
    assert sub(list_one, start_index, end_index) == [0, 1, 2, 3, 4]
    return None


# sub_use_case
def test_sub_single_output_from_list() -> None:
    """Given a list and an index differing by one, return a list of a single value."""
    list_one: list[int] = [0, 1, 2, 3, 4]
    start_index: int = 0
    end_index: int = 1
    assert sub(list_one, start_index, end_index) == [0]
    return None