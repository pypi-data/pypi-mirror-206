from typing import Any


class Singleton(type):
  _instances = {}
  
  def __call__(cls, *args, **kwargs) -> Any:
    if cls not in cls._instances:  # If identical class hasn't already been created, return the class as normal
      cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
    return cls._instances.get(cls)  # Otherwise return the identical class
