from typing import List, Tuple
from .line import Line


class Polygon:
  def __init__(self, verticies: List[Tuple[int, int]]):
    if self.is_valid(verticies):
      self.verticies = verticies
    self.edges = [Line(vertex, self.verticies[(vertex_idx + 1) % len(self.verticies)])
                       for vertex_idx, vertex in enumerate(self.verticies)]

  @staticmethod
  def is_valid(verticies: List[Tuple[int, int]]):
    return len(set(verticies)) == len(verticies) and len(verticies) > 2
  
  def __contains__(self, point: Tuple[int, int]) -> bool:
    if not isinstance(point, tuple):
      return False
         
    ray = Line(point, (10_000, point[1]))
    intersection_count = 0
     
    for current, edge in enumerate(self.edges):
      next = (current + 1) % len(self.verticies)
       
      if edge.intersects(ray):
        if (line := Line(self.verticies[current], point)).get_orientation(self.verticies[next]) == "Collinear":
          return self.verticies[next] in line
        intersection_count += 1

    return (intersection_count % 2 == 1)
