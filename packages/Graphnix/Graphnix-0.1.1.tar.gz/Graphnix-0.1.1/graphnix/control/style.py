from __future__ import annotations


class TextStyle:
  styles = {
    "0": "blank", 
    "1": "bold", 
    "2": "dim", 
    "3": "italic", 
    "4": "underline", 
    "8": "hide", 
    "9": "cross", 
  }
  
  def __init__(self, *style_codes: str) -> None:
    if "0" in style_codes:
      style_codes = ("0",)
    self.style_codes = set(*style_codes)
    self._escape_code = ";".join(self.style_codes)

  def __str__(self) -> str:
    if "0" in self.style_codes:
      return "TextStyle(blank=True)"
    attributes = ", ".join(f"{self.styles.get(style_code)}=True" for style_code in self.style_codes)
    return f"TextStyle({attributes})"

  def __repr__(self) -> str:
    if "0" in self.style_codes:
      return "TextStyle(blank=True)"
    attributes = ", ".join(f"{self.styles.get(style_code)}=True" for style_code in self.style_codes)
    return f"TextStyle({attributes})"

  def __add__(self, other: TextStyle) -> TextStyle:
    return TextStyle(*(self.style_codes | other.style_codes))

  @property
  def escape_code(self) -> str:
    return self._escape_code
