"""
A collection of tools relating to cursor manipulation
"""


from __future__ import annotations
from typing import Tuple, TYPE_CHECKING
import sys

if TYPE_CHECKING:
  from ..interaction import Screen


class Cursor:
  """
  A static class containing different functionality relating to the cursor
  """
  _position = [0, 0]

  @staticmethod
  def get_position() -> Tuple[int, int]:
    """
    Returns the current position of the cursor
    """
    return tuple(Cursor._position)
  
  @staticmethod
  def up(n: int=1) -> None:
    """
    Move the cursor up 'n' spaces
    """
    Cursor._position[1] -= n
    sys.__stdout__.write(f"\033[{n}A")
    sys.__stdout__.flush()

  @staticmethod
  def down(n: int=1) -> None:
    """
    Move the cursor down 'n' spaces
    """
    Cursor._position[1] += n
    sys.__stdout__.write(f"\033[{n}B")
    sys.__stdout__.flush()

  @staticmethod
  def forward(n: int=1) -> None:
    """
    Move the cursor forward 'n' spaces
    """
    Cursor._position[0] += n
    sys.__stdout__.write(f"\033[{n}C")
    sys.__stdout__.flush()

  @staticmethod
  def back(n: int=1) -> None:
    """
    Move the cursor back 'n' spaces
    """
    Cursor._position[0] -= n
    sys.__stdout__.write(f"\033[{n}D")
    sys.__stdout__.flush()

  @staticmethod
  def carriage_return() -> None:
    """
    Return to the beginning of the same line to overwrite the previous input
    """
    Cursor._position[0] = 0
    sys.__stdout__.write("\r")
    sys.__stdout__.flush()

  @staticmethod
  def go_to(x: int, y: int) -> None:
    """
    Moves cursor to specified coordinates
    """
    Cursor._position = [x, y]
    sys.__stdout__.write(f"\033[{y + 1};{x + 1}H")
    sys.__stdout__.flush()

  @staticmethod
  def to_bottom(screen: Screen) -> None:
    """
    Move cursor to bottom of provided screen
    """
    Cursor.go_to(0, screen.get_size()[1])

  @staticmethod
  def _update_on_write(character: str) -> None:
    """
    Ensures the tracked position is correct after any implicit changes due to the character being printed
    """
    if character == "\n":
      Cursor._position[0] = 0
      Cursor._position[1] += 1
    else:
      Cursor._position[0] += 1
