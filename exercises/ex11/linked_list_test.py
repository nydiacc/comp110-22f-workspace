"""Tests for linked list utils."""

import pytest
from exercises.ex11.linked_list import Node, is_equal, last, value_at, max, linkify, scale

__author__ = "730563759"


def test_last_empty() -> None:
    """Last of an empty Linked List should raise a ValueError."""
    with pytest.raises(ValueError):
        last(None)


def test_last_non_empty() -> None:
    """Last of a non-empty list should return its last data value."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert last(linked_list) == 3


def test_value_at_first_index() -> None:
    """Return the value at the initial index."""
    linked_list = Node(10, Node(20, Node(30, None)))
    index: int = 0
    assert value_at(linked_list, index) == 10


def test_value_at_third_index() -> None:
    """Return the value at the third index."""
    linked_list = Node(10, Node(20, Node(30, None)))
    index: int = 2
    assert value_at(linked_list, index) == 30


def test_max_single_node() -> None:
    """Return the max of a single Node."""
    linked_list = Node(10, None)
    assert max(linked_list) == 10


def test_max_in_the_middle() -> None:
    """Return the max of a Linked List when it's in the middle."""
    linked_list = Node(10, Node(30, Node(20, None)))
    assert max(linked_list) == 30


def test_linkify_same_values() -> None:
    """Returns a Linked List with the same values."""
    items: list[int] = [0, 0, 0]
    assert linkify(items) is Node(0, Node(0, Node(0, None)))


def test_linkify_linked_lists() -> None:
    """Returns a Linked List with the same values."""
    items: list[int] = [1, 2, 3]
    assert linkify(items) is Node(1, Node(2, Node(3, None)))


def test_scale_single_list() -> None:
    """Returns a single list scaled by a factor of two."""
    linked_list = Node(10, None)
    factor: int = 2
    assert scale(linked_list, factor) is Node(20, None)


def test_scale_varying_values() -> None:
    """Returns a Linked List of values scaled by a facor of two."""
    linked_list = Node(10, Node(11, Node(12, None)))
    factor: int = 2
    assert scale(linked_list, factor) is Node(20, Node(22, Node(24, None)))
