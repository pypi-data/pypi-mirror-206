from typing import Any


class MouseEvent:
  UNRECOGNIZED = "Unrecognized"
  
  def __init__(self, event: str, x_position: int, y_position: int, is_down: bool=True, is_button: bool=True) -> None:
    self.event = event
    self.x = x_position
    self.y = y_position
    self.is_down = is_down
    self.is_button = is_button

  def __str__(self) -> str:
    return f"{self.event}{' Down' if self.is_down and self.is_button else ' Up' if self.is_button else ''} ({self.x}, {self.y})"

  def __eq__(self, other: Any) -> bool:
    if isinstance(other, str):
      return other.lower() == f"{self.event}{' Down' if self.is_down and self.is_button else ' Up' if self.is_button else ''}".lower()
    elif isinstance(other, MouseEvent):
      return other.event.lower() == self.event.lower() and other.is_down == self.is_down
    return False
