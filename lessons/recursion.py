"""Introduction to recursion November 15."""

from __future__ import annotations

from typing import Union

class Node:
    data: int
    next: Union[Node, None]
    
    def __init__(self, data: int, next: Union[Node, None]):
        self.data = data
        self.next = next


def sum(node: Node) -> int:
    if node.next == None:
        return node.data
    else:
        return node.data + sum(node.next)


def count(node: Node, current_count: int = 0) -> int:
    if node.next == None:
        return current_count + 1
    else:
        return count(node.next, current_count + 1)

head: Node = Node(3, None)
head = Node(2, head)
head = Node(1, head)
print(sum(head))
print(count(head))


