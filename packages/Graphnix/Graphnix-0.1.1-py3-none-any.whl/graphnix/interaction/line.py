from __future__ import annotations
from typing import Tuple


class Line:
  def __init__(self, start: Tuple[float, float], end: Tuple[float, float]):
    self.start = start
    self.end = end

  def __contains__(self, point: Tuple[int, int]) -> bool:
    return ((self.end[0] <= max(self.start[0], point[0])) and 
            (self.end[0] >= min(self.start[0], point[0])) and 
            (self.end[1] <= max(self.start[1], point[1])) and 
            (self.end[1] >= min(self.start[1], point[1])))

  def get_orientation(self, point: Tuple[int, int]) -> str:
    orientations = {lambda o: not o: "Collinear", 
                    lambda o: o > 0: "Clockwise", 
                    lambda o: o < 0: "Anticlockwise"
                   }
    for orientation in orientations:
      if orientation(((self.end[1] - self.start[1]) * 
                      (point[0] - self.end[0])) - 
                     ((self.end[0] - self.start[0]) * 
                      (point[1] - self.end[1]))
                    ): return orientations.get(orientation)

  def intersects(self, other: Line) -> bool:
    orientations = [
      self.get_orientation(other.start), 
      self.get_orientation(other.end), 
      other.get_orientation(self.start), 
      other.get_orientation(self.end)
    ]
   
    return ((orientations[0] != orientations[1]) and (orientations[2] != orientations[3]) or  # General Case
            (orientations[0] == "Collinear" and 
            self.end in Line(self.start, other.start)) or
            (orientations[1] == "Collinear" and 
            self.end in Line(self.start, other.end)) or 
            (orientations[2] == "Collinear" and 
            other.end in Line(other.start, self.start)) or 
            (orientations[3] == "Collinear" and 
            other.end in Line(other.start, self.end))
           )
    
  def __str__(self) -> str:
    return f"Line[{self.start} --> {self.end}]"
