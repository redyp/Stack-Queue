from __future__ import annotations
from dataclasses import dataclass, field

@dataclass
class Node:
    value: int
    _next = Node = None

@dataclass
class Stack:
    value: int = field(repr=False, default=None)
    head: Node = field(init=False, default=None)
    lenght: int = field(init=False, default=0)

    def __post_init__(self):
        if self.value is not None:
            new_node = Node(self.value)
            self.head = new_node
            self.lenght = 1

    def __str__(self) -> str:
        if self.head == None:
            return 'Stack Kosong'
        temp = self.head
        temp_str = ''
        while temp:
            temp_str += f'{temp.value} -> '
            temp = temp._next
        temp_str += 'None'
        return temp_str
