from typing import Any


class KeyboardEvent:
  UNRECOGNIZED = "Unrecognized"
  ANY = "Any"
  
  def __init__(self, event: str) -> None:
    self.event = event

  def __str__(self) -> str:
    return f"{self.event} Pressed"

  def __eq__(self, other: Any) -> bool:
    if isinstance(other, str):
      return other.lower() == self.event.lower()
    elif isinstance(other, KeyboardEvent):
      return other.event.lower() == self.event.lower()
    return False
