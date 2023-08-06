from __future__ import annotations
from typing import Tuple, Callable, TYPE_CHECKING
from collections import defaultdict
from contextlib import contextmanager
import re
from ..control import Cursor

if  TYPE_CHECKING:
    from .screen import Screen


class Layer:
    def __init__(self, screen: Screen, name: str, floating: bool) -> None:
        self.screen = screen
        self.name = name
        self.floating = floating
        self._content = defaultdict(lambda: ' ')
    
    def write(self, pos: Tuple[int, int], string: str) -> None:
        x, y = pos
        self._content[pos] = string
    
    def reset(self) -> None:
        self._content = defaultdict(lambda: ' ')
    
    def clear(self) -> None:
        for x, y in self.content.keys():
            self.erase_at(x, y)
        self.reset()

    def __str__(self) -> str:
        max_x, max_y = self.get_size()
        return "\n".join("".join(self.content[x, y] for x in range(max_x + 1)).rstrip() for y in range(max_y + 1))
    
    def __repr__(self) -> str:
        max_x, max_y = self.get_size()
        return f"Layer(name={self.name}, size={self.get_size()})"
    
    def get_size(self) -> Tuple[int, int]:
        if not self._content:
            return (0, 0)
        return max(map(lambda it: it[0], self.content.keys())), max(map(lambda it: it[1], self.content.keys()))

    def can_print_at(self, x: int, y: int) -> bool:
        if self is self.screen.top_layer:
            return True
        for layer in self.screen.traverse_layers(start=self.screen.top_layer.index, end=self.index + 1):
            if layer.occupies(x, y):
                return False
        return True

    def occupies(self, x: int, y: int) -> bool:
        return (x, y) in self.content

    def change_at(self, x: int, y: int, string: str) -> None:
        with self.as_active():
            Cursor.go_to(x, y)
            self.screen.print(string, end="", flush=True)

    def erase_at(self, x: int, y: int) -> None:
        if (x, y) not in self.content:
            return
        del self.content[x, y]  # Deletes from content
    
        if not self.can_print_at(x, y):
            return

        if any((layer := _layer).occupies(x, y) for _layer in self.screen.traverse_layers(start=self.index - 1, end=0)):
            self.change_at(x, y, layer.content[x, y])
            return
        self.change_at(x, y, " ")
    
    def replace_all(self, new_character: str, criterion: Callable) -> None:
        for coordinates, character in self.content.items():
            if criterion(character):
                self.change_at(*coordinates, new_character)

    @property
    def content(self) -> defaultdict:
        return self._content

    @property
    def index(self) -> int:
        return self.screen.layers.index(self)

    @contextmanager
    def as_active(self) -> Layer:
        old_active_layer = self.screen.active_layer
        try:
            self.screen.set_active(self)
            yield self
        finally:
            self.screen.set_active(old_active_layer)
    
    def __add__(self, n: int) -> Layer:
        return self.screen.layers[self.index + n]
    
    def __sub__(self, n: int) -> Layer:
        return self.screen.layers[self.index - n]
    