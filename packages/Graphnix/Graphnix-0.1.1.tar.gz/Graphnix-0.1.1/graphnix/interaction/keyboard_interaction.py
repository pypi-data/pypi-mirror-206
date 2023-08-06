from typing import Callable, Union
from ..input import KeyboardEvent


class KeyboardInteraction:
    def __init__(self, method: Callable, event: Union[str, KeyboardEvent]):
        self.method = method
        self.event = event
