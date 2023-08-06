from __future__ import annotations
from typing import Tuple, Union, List, Set, Optional, Callable
import string
from .colour import TextColour
from .style import TextStyle


class Text(str):
  END = TextStyle("0")
  BOLD = TextStyle("1")
  DIM = TextStyle("2")
  ITALIC = TextStyle("3")
  UNDERLINE = TextStyle("4")
  HIDE = TextStyle("8")
  CROSS = TextStyle("9")
  
  F_BLACK = TextColour(foreground=(0, 0, 0))
  F_WHITE = TextColour(foreground=(255, 255, 255))
  F_RED = TextColour(foreground=(255, 0, 0))
  F_GREEN = TextColour(foreground=(0, 255, 0))
  F_BLUE = TextColour(foreground=(0, 0, 255))
  F_YELLOW = TextColour(foreground=(255, 255, 0))
  F_CYAN = TextColour(foreground=(0, 255, 255))
  F_MAGENTA = TextColour(foreground=(255, 0, 255))
  F_ORANGE = TextColour(foreground=(255, 165, 0))
  F_PURPLE = TextColour(foreground=(230, 230, 250))
  F_GREY = TextColour(foreground=(142, 142, 142))
  F_BROWN = TextColour(foreground=(162, 162, 42))
  F_DEFAULT = TextColour(foreground=(192, 192, 192))

  B_BLACK = TextColour(background=(0, 0, 0))
  B_WHITE = TextColour(background=(255, 255, 255))
  B_RED = TextColour(background=(255, 0, 0))
  B_GREEN = TextColour(background=(0, 255, 0))
  B_BLUE = TextColour(background=(0, 0, 255))
  B_YELLOW = TextColour(background=(255, 255, 0))
  B_CYAN = TextColour(background=(0, 255, 255))
  B_MAGENTA = TextColour(background=(255, 0, 255))
  B_ORANGE = TextColour(background=(255, 165, 0))
  B_PURPLE = TextColour(background=(230, 230, 250))
  B_GREY = TextColour(background=(142, 142, 142))
  B_BROWN = TextColour(background=(162, 162, 42))

  ZERO_WIDTH = "​"
  BACKSPACE = "\b"
  NEWLINE = "\n"
  TAB = "\t"
  CARRIAGE_RETURN = "\r"
  FORM_FEED = "\f"

  def __new__(cls, text: str, styles: Optional[Set[TextStyle]] = None, colour: Optional[Set[TextColour]] = None) -> Text:
    return super().__new__(cls, text)

  def __init__(self, text: str, styles: Optional[Set[TextStyle]] = None, colour: Optional[Set[TextColour]] = None) -> None:
    self.text = text
    self.styles = set() if styles is None else styles
    self._colours = self.F_DEFAULT if colour is None else colour
    if self.colours is None or self.colours == Text.F_DEFAULT:
      pass

  def __str__(self) -> str:
    if self.has_effects():
      return f"{Text.ZERO_WIDTH}\033[{self.chain_effects(*self.effects)}m{Text.ZERO_WIDTH}{Text.BACKSPACE}{self.text}{Text.ZERO_WIDTH}\033[{self.END.escape_code}m{Text.ZERO_WIDTH}"
    return self.text

  @classmethod
  def parse(cls, text: str) -> Tuple[bool, str]:
    if isinstance(text, Text):
      for character in text:
        yield character
      return
    buffer = ""
    is_effect = False
    for character in text:
      is_effect = not is_effect if character == Text.ZERO_WIDTH else is_effect
      if character in (Text.BACKSPACE, Text.ZERO_WIDTH):
        continue
      buffer += character
      if not is_effect:
        yield buffer
        buffer = ""

  def __repr__(self) -> str:
    return f"Text(text={self.text!r}, styles=[{', '.join(map(repr, self.styles)) if self.styles else None}], colour={repr(self.colours) if self.colours else None})"    

  def chain_effects(self, *effects: int) -> str:
    to_escape_code = lambda effect: effect.escape_code
    return ";".join(map(to_escape_code, effects))

  def apply(self, *styles: int) -> Text:
    for style in styles:
      self.styles.add(style)
    return self

  def colour(self, *colours: Tuple[int]) -> Text:
    for colour in colours:
      self.colours &= colour
    return self

  def __add__(self, other: str) -> str:
    if isinstance(other, Text):
      self.text = f"{self.text}{other.text}"
      self.styles = other.styles + self.styles
      self.colours = other.colours & self.colours
    else:
      self.text = f"{self.text}{other}"
    return self

  def __radd__(self, other: str) -> str:
    if isinstance(other, Text):
      self.text = f"{other.text}{self.text}"
      self.styles += other.styles
      self.colours &= other.colours
    else:
      self.text = f"{other}{self.text}"
    return self

  def __contains__(self, item: Union[TextStyle, TextColour, str, Tuple[int]]) -> bool:
    if isinstance(item, TextStyle):
      return item in self.styles
    elif isinstance(item, TextColour) or isinstance(item, tuple):
      return item in self.colours
    elif isinstance(item, str):
      return item in self.text
    return False

  @property
  def effects(self) -> List[Union[TextStyle, TextColour]]:
    return {*self.styles, self.colours}

  def has_effects(self) -> bool:
    return self.styles or self.colours

  def __mul__(self, n: int) -> Text:
    return Text(self.text * n, styles=self.styles, colour=self.colours)

  def __getitem__(self, value: Union[int, slice]):
    return Text(self.text.__getitem__(value), styles=self.styles, colour=self.colours)

  def split(self, criterion: Optional[Callable] = None) -> List[str]:
    if criterion is None:
      split_text = list(self.text)
    else:
      split_text = [[]]
      last_match_idx = idx = 0
      for character_idx, match_idx in enumerate((idx := idx + 1) if criterion(self.text[i]) else idx for i in range(len(self.text))):
        if last_match_idx != match_idx:
          split_text.append([])
        else:
          split_text[match_idx].append(self.text[character_idx])
        last_match_idx = match_idx
      split_text = list(map("".join, split_text))

    if self.has_effects():
      split_text[0] = f"\033[{self.chain_effects(*self.effects)}m" + split_text[0]
      split_text[-1] += f"\033[{self.END.escape_code}m"
    return split_text

  def title(self) -> Text:
    non_capitalized = (
      "a", "an", "and", "as", "as if", "as long as", "at", "but", "by", "even if", "for", "from", 
      "if", "if only", "in", "into", "like", "near", "now that", "nor", "of", "off", 
      "on", "on top of", "once", "onto", "or", "out of", "over", "past", "so", "so that", 
      "than", "that", "the", "till", "to", "up", "upon", "with", "when", "yet"
    )
    n = len((words := self.text.split(" "))) - 1
    self.text = " ".join(character if len(character) < 2 and character in non_capitalized 
                         and idx not in (0, n) else character.title() for idx, character in enumerate(words))
    return self

  def upper(self) -> Text:
    return Text(self.text.upper(), styles=self.styles, colour=self.colours)

  def lower(self) -> Text:
    self.text = self.text.lower()
    return self

  def swap_case(self) -> Text:
    self.text = self.text.swapcase()
    return self

  def reversed(self) -> Text:
    self.text = "".join(reversed(self.text))
    return self

  def sorted(self, reverse: bool = False, key: Optional[Callable] = None) -> Text:
    self.text = "".join(sorted(self.text, reverse=reverse, key=key))
    return self

  def strip(self) -> Text:
    self.text = self.text.strip()
    return self

  def lstrip(self) -> Text:
    self.text = self.text.lstrip()
    return self.text

  def rstrip(self) -> Text:
    self.text = self.text.rstrip()
    return self

  def replace(self, old: str, new: str) -> Text:
    self.text = self.text.replace(old, new)
    return self

  def __iter__(self) -> Iterator[str]:
    for character in self.split():
      yield character

  def __len__(self) -> int:
    return len(self.text)

  def discard_styles(self, *styles: TextStyle) -> None:
    if not styles:
      self.styles = set()
      return
    for style in styles:
      self.styles.remove(style)

  def discard_colours(self, *colours: Union[TextColour, Tuple[int]]) -> None:
    if not colours:
      self.colours = self.F_WHITE
      return
    for colour in colours:
      self.colours -= colour
    if self.colours is None:
      self.colours = self.F_WHITE

  @property
  def colours(self):
    return self._colours

  @colours.setter
  def colours(self, value):
    assert value is not None
    assert value != Text.F_DEFAULT
    self._colours = value

  def __eq__(self, other: Any) -> bool:
    if not isinstance(other, str):
      return
    return str(self) == str(other)
