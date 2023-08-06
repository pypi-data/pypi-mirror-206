from typing import Union, Tuple, Callable
import sys
import termios
import string
import os
import contextlib
import io
import threading
import time
import pty
import subprocess
from .keyboard_event import KeyboardEvent
from .mouse_event import MouseEvent


class ConsoleInput:
  BASIC_UNICODE_CODES = {
    8: "Shift + Backspace", 
    9: "Tab", 
    10: "Enter", 
    127: "Backspace"
  }
  BASIC_CSI_SEQUENCES = {
    "[A": "Up Arrow", 
    "[B": "Down Arrow", 
    "[D": "Left Arrow", 
    "[C": "Right Arrow", 
    "[F": "End", 
    "[Z": "Shift + Tab"
  }
  MOUSE_CODES = {
    0: "Left Mouse Button",
    1: "Middle Mouse Button",
    2: "Right Mouse Button",
    32: "Left Mouse Button (Dragged)",
    33: "Middle Mouse Button (Dragged)",
    34: "Right Mouse Button (Dragged)",
    35: "Move",
    64: "Scroll Up",
    65: "Scroll Down"
  }
  SPECIAL_CODES = {
    2: "Insert", 
    3: "Delete", 
    5: "Page Up", 
    6: "Page Down", 
    15: "F5", 
    17: "F6", 
    18: "F7", 
    19: "F8", 
    20: "F9", 
    21: "F10", 
    23: "F11", 
    24: "F12"
  }
  NUMPAD_KEYS = {
    "A": "Up Arrow", 
    "B": "Down Arrow", 
    "C": "Left Arrow", 
    "D": "Right Arrow", 
    "F": "End", 
    "H": "Home"
  }
  
  def __init__(self, read_key: str) -> None:
    self.read_key = read_key
    self.key_code = ord(self.read_key)
    self.translation = self.decipher()

  def decipher(self) -> Union[KeyboardEvent, MouseEvent]:
    if self.key_code in range(32, 127):
      return KeyboardEvent(self.read_key)
    elif self.key_code == 27:
      return self.decode_csi()
    elif self.key_code in self.BASIC_UNICODE_CODES:
      return KeyboardEvent(self.BASIC_UNICODE_CODES[self.key_code])
    return KeyboardEvent(KeyboardEvent.UNRECOGNIZED)

  @staticmethod
  def is_valid_csi(csi: str) -> bool:
    return csi and csi in (string.ascii_letters + "<~")

  @staticmethod
  def csi_is_function_key_1to4(escape_code: str) -> int:
    if escape_code == "O":
      return ord(sys.stdin.read(1)) - 79
    return 0

  @staticmethod
  def csi_is_mouse(escape_code: str) -> bool:
    return escape_code == "[<"

  def decode_csi(self) -> Union[KeyboardEvent, MouseEvent]:
    escape_code = ""
    text = ""
    while not self.is_valid_csi(text):
      text = sys.stdin.read(1)
      escape_code += text

    if escape_code in self.BASIC_CSI_SEQUENCES:
      return KeyboardEvent(self.BASIC_CSI_SEQUENCES[escape_code])
    elif (function_key_n := self.csi_is_function_key_1to4(escape_code)):
      return KeyboardEvent(f"F{function_key_n}")
    elif self.csi_is_mouse(escape_code):
      return self.decode_mouse()
    elif escape_code[-1] in "~ABCDFH":
      return self.decode_special(escape_code[1:])
    return KeyboardEvent(KeyboardEvent.UNRECOGNIZED)

  @staticmethod
  def mouse_is_down(last_input: str) -> bool:
    return last_input == "M"

  def decode_mouse(self) -> MouseEvent:
    mouse_id = ""
    text = ""
    while not text == ";":
      text = sys.stdin.read(1)
      mouse_id += text if text != ";" else ""
    x_position = ""
    text = ""
    while not text == ";":
      text = sys.stdin.read(1)
      x_position += text if text != ";" else ""
    y_position = ""
    text = ""
    while not text or not text in "Mm":
      text = sys.stdin.read(1)
      y_position += text if not text in "Mm" else ""

    x_position = int(x_position) - 1
    y_position = int(y_position) - 1
    mouse_id = int(mouse_id)
    if mouse_id in self.MOUSE_CODES:
      return MouseEvent(self.MOUSE_CODES[mouse_id], x_position, y_position, self.mouse_is_down(text), mouse_id in (0, 1, 2))
    return MouseEvent(MouseEvent.UNRECOGNIZED, x_position, y_position, self.mouse_is_down(text), mouse_id in (0, 1, 2))

  def decode_special(self, escape_code: str) -> KeyboardEvent:
    escape_code, escape_code_type = escape_code[:-1], escape_code[-1]
    if escape_code_type == "~" and int(escape_code.split(";")[0]) in self.SPECIAL_CODES:
      return KeyboardEvent(self.SPECIAL_CODES[int(escape_code.split(";")[0])])
    elif escape_code_type in self.NUMPAD_KEYS:
      return KeyboardEvent(self.NUMPAD_KEYS[escape_code_type])
    return KeyboardEvent(KeyboardEvent.UNRECOGNIZED)


def _mock_input():
  communicate_argument = ""
  p = subprocess.Popen([sys.executable, "mock_input.py"], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.STDOUT, encoding="utf-8")
  return p.communicate(communicate_argument)


@contextlib.contextmanager
def console_inputs() -> None:
    pid = pty.fork()  # Connect to pseudo-terminal
    if pid:
        yield
        return
    original_state = termios.tcgetattr(sys.stdin)
    new_state = termios.tcgetattr(sys.stdin)
    sys.__stdout__.write("\033[?7l")  # Prevent line wrapping
    sys.__stdout__.write("\033[?25l")  # Hide the cursor
    sys.__stdout__.write("\033[?1003h")  # Setup click detection
    sys.__stdout__.write("\033[?1006h")  # ...
    new_state[3] &= ~(termios.ECHO | termios.ICANON)  # Setup console changes (Turning off echo and icanon)
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, new_state)  # Execute console changes
    sys.__stdout__.write("\n\033[1A")  # Line break then bring cursor upwards again
    try:
        yield None
    finally:
        sys.__stdout__.write("\033[?1003l")
        _mock_input()  # WTF???
        sys.__stdout__.write("\033[?1006l")
        sys.__stdout__.write("\033[?25h")
        sys.__stdout__.write("\033[?7h")  # Reset Escape Codes
    
    
def read_console() -> Union[KeyboardEvent, MouseEvent]:
    try:
        key = ConsoleInput(sys.stdin.read(1))
    except TypeError:  # Process terminated
        return
    return key.translation
