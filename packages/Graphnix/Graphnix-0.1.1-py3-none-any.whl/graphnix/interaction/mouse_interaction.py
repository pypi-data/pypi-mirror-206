from typing import Callable, Dict, Tuple
from ..input import MouseEvent


class MouseInteraction:
  def __init__(self, method: Callable, event: MouseEvent, zone: Dict[Tuple[int, int], Tuple[int, int]]):
    self.method = method
    self.event = event
    self.zone = zone
