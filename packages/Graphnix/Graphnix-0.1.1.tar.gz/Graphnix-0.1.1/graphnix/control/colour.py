from __future__ import annotations
from typing import Tuple, Optional, Union
from statistics import mean
from math import ceil
from dataclasses import dataclass


@dataclass(frozen=True)
class TextColour:
  foreground: Optional[Tuple[int]] = None
  background: Optional[Tuple[int]] = None
  
  def __postinit__(self, foreground: Optional[Tuple[int]], background: Optional[Tuple[int]]) -> None:
    self.foreground = foreground if foreground is None else tuple(map(self.limit, foreground))
    self.background = background if background is None else tuple(map(self.limit, background))
    if not (self.has_foreground or self.has_background):
      raise ValueError("No foreground or background colour provided")

  @staticmethod
  def limit(value: int, minimum: int = 0, maximum: int = 255) -> int:
    return minimum if value < minimum else maximum if value > maximum else value

  def __and__(self, other: TextColour) -> TextColour:
    return TextColour(foreground=self.foreground if self.has_foreground else other.foreground, 
                      background=self.background if self.has_background else other.background) \
    if self.has_foreground ^ other.has_foreground else other

  def __sub__(self, other: TextColour) -> Optional[TextColour]:
    return TextColour(
      foreground=self.foreground if other.foreground != self.foreground else None,
      background=self.background if other.background != self.background else None
    )

  def __or__(self, other: TextColour) -> TextColour:
    mix_rgb = lambda rgb1, rgb2: (None if rgb1 is None and rgb2 is None else rgb1 if rgb2 is None else rgb2 if rgb1 is None
                                  else (ceil(mean((val1,val2))) for val1, val2 in zip(rgb1, rgb2)))
    return TextColour(mix_rgb(self.foreground, other.foreground), mix_rgb(self.background, other.background))

  def __add__(self, other: TextColour) -> TextColour:
    mix_rgb = lambda rgb1, rgb2: (None if rgb1 is None and rgb2 is None else rgb1 if rgb2 is None else rgb2 if rgb1 is None
                                  else (min(val1 + val2, 255) for val1, val2 in zip(rgb1, rgb2)))
    return TextColour(mix_rgb(self.foreground, other.foreground), mix_rgb(self.background, other.background))

  def __contains__(self, other: Union[TextColour, Tuple[int]]) -> bool:
    if isinstance(other, TextColour):
      return self == other or self.foreground == other.background or self.background == other.foreground
    elif isinstance(other, tuple):
      return other in (self.foreground, self.background)
    return False

  @property
  def escape_code(self) -> str:
    escape_code = (*((38, 2, *self.foreground) if self.has_foreground else tuple()), *((48, 2, *self.background) if self.has_background else tuple()))
    return ";".join(map(str, escape_code))

  @property
  def has_foreground(self) -> bool:
    return self.foreground is not None

  @property
  def has_background(self) -> bool:
    return self.background is not None

  def __bool__(self) -> bool:
    return self != TextColour(foreground=(192, 192, 192))
