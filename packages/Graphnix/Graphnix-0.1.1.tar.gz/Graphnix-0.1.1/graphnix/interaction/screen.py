from typing import Union, List, Callable, Tuple, Optional, Any
import inspect
import sys
import os
import multiprocessing
import contextlib
from collections import defaultdict
from .keyboard_interaction import KeyboardInteraction as KBInteraction
from .mouse_interaction import MouseInteraction
from .polygon import Polygon
from .layer import Layer
from .singleton import Singleton
from .temporary_layer import TemporaryLayer
from ..input import read_console, console_inputs, KeyboardEvent, MouseEvent
from ..control import Cursor, Text


"""
Print should check it can within itself to halve traversals
To check, should traverse from end
"""


class Screen:
  BASE = 0
  TOP = None
  
  def __init__(self, default_layer_name: str = "Base") -> None:
    self.stdout = sys.stdout
    sys.stdout = self

    self._layers = []
    self.active_layer = self.add_layer(default_layer_name)
    self.keyboard_interactions = self.get_keyboard_interactions()
    self.mouse_interactions = self.get_mouse_interactions()
    self.is_running = False

  def __str__(self) -> str:
    return self.read()

  def get_keyboard_interactions(self) -> List[KBInteraction]:
    return [interaction[1] for interaction in inspect.getmembers(self.__class__, predicate=lambda member: isinstance(member, KBInteraction))]

  def get_mouse_interactions(self) -> List[MouseInteraction]:
    return [interaction[1] for interaction in inspect.getmembers(self.__class__, predicate=lambda member: isinstance(member, MouseInteraction))]

  def KeyboardInteraction(event: Union[str, KeyboardEvent]) -> Callable:
    def _KeyboardInteraction(method: Callable) -> KBInteraction:
      return KBInteraction(method, event)
    return _KeyboardInteraction

  def MouseInteractionZone(event: Union[str, MouseEvent], zone: Polygon) -> Callable:
    def _MouseInteractionZone(method: Callable) -> MouseInteraction:
      return MouseInteraction(method, event, zone)
    return _MouseInteractionZone

  def write(self, string: str) -> None:
    for character in Text.parse(string):
      cursor_position = Cursor.get_position()
      Cursor._update_on_write(character)
      if self.active_layer.can_print_at(*cursor_position):
        sys.__stdout__.write(character)
      else:
        Cursor.go_to(*Cursor.get_position())
      self.active_layer.write(cursor_position, character)

  def print(self, *objects: Any, layer: Layer = None, end: str = "\n", flush: bool = False, sep: str = " ") -> None:
    if layer is None:
      layer = self.active_layer
    last_index = len(objects) - 1
    
    strings = [(o if isinstance(o, str) else str(o)) + (sep if i < last_index else end) for i, o in enumerate(objects)]

    if not objects:
      strings = (end,)

    with layer.as_active():
      for string in strings:
        self.write(string)
    if flush:
      self.flush()

  def read(self) -> str:
    throwaway_layer = Layer(self, "Throwaway")
    throwaway_layer._content = self.collate_layers()
    return str(throwaway_layer)

  def flush(self) -> None:
    sys.__stdout__.flush()

  def clear(self) -> None:
    os.system("clear")
    Cursor.go_to(0, 0)
    for layer in self._layers:
      layer.reset()

  @contextlib.contextmanager
  def start(self) -> None:
    p = multiprocessing.Process(target=self.run)
    p.start()
    try:
      yield self
    finally:
        self.stop()
        p.terminate()

  def stop(self) -> None:
    self.is_running = False

  def run(self) -> None:
    self.is_running = True
    with console_inputs():
      while self.is_running:
        self.update()
      Cursor.go_to(0, self.get_size()[1])
  
  def update(self) -> None:
    console_input = read_console()  # Hangs here until detection.
    if isinstance(console_input, KeyboardEvent):
      for interaction in self.keyboard_interactions:
        if console_input == interaction.event:
          interaction.method(self, console_input)
        if KeyboardEvent.ANY in list(map(lambda interaction: interaction.event, self.keyboard_interactions)):
          interaction.method(self, console_input)

    elif isinstance(console_input, MouseEvent):
      for interaction in self.mouse_interactions:
        if console_input == interaction.event and (console_input.x, console_input.y) in interaction.zone:
          interaction.method(self, console_input)

  def get_size(self) -> Tuple[int, int]:
    return tuple(max(map(lambda it: it.get_size()[i], self._layers)) for i in (0, 1))

  def get_layer(self, identifier: Union[str, int]) -> Layer:
    if isinstance(identifier, int):
      if identifier >= len(self._layers):
        raise ValueError(f"Layer '{identifier}', does not exist")
      return self._layers[identifier]

    matches = self.get_layers(lambda layer: layer.name == identifier)
    if not matches:
      raise ValueError(f"Layer '{identifier}', does not exist")
    return matches[0]

  def get_layers(self, criterion: Optional[Callable] = None) -> List[Layer]:
    if criterion is None:
      return self._layers
    return list(filter(criterion, self._layers))

  def change_at(self, x: int, y: int, string: str, layer: Optional[Layer] = None) -> None:
    if layer is None:
      layer = self.active_layer
    layer.change_at(x, y, string)

  def erase_at(self, x: int, y: int, layer: Layer) -> None:
    layer.erase_at(x, y)

  def add_layer(self, name: str, priority: Optional[int] = None, temporary: bool = False, floating: bool = False) -> Layer:
    LayerClass = TemporaryLayer if temporary else Layer
    if priority is self.TOP:
      if floating:
        index = len(self.layers) - 1
      else:
        index = 0
        for i, layer in enumerate(self.layers):
          if layer.floating:
            break
          index = i
      self.layers.insert(index + 1, layer := LayerClass(self, name, floating))
    else:
      first_floating_index = next(filter(lambda it: it.floating, self.layers))
      index = (first_floating_index if not floating else len(self.layers) if priority < 0 else 0) + priority
      self.layers.insert(index, layer := LayerClass(self, name, floating))
    return layer

  def set_active(self, layer: Layer) -> None:
    self.active_layer = layer

  def traverse_layers(self, start: Optional[int] = None, end: Optional[int] = None) -> Layer:
    if start is None:
      start = 0
    if end is None:
      end = len(self._layers) - 1
    interval = -1 if start > end else 1

    for layer_idx in range(start, end + interval, interval):
      yield self.get_layer(layer_idx)

  def collate_layers(self, start: Optional[int] = None, end: Optional[int] = None) -> Layer:
    collated = defaultdict(lambda: " ")
    for layer in self.traverse_layers(start=start, end=end):
      for key in layer.content:
        if key in collated:
          collated[key].update(layer.content[key])
        else:
          collated[key] = layer.content[key]
    return collated

  @property
  def layers(self) -> List[Layer]:
    return self._layers

  @property
  def top_layer(self) -> Layer:
    return self.layers[-1]
