from .layer import Layer


class TemporaryLayer(Layer):
  def reset(self) -> None:
    super().reset()
    self.screen.layers.remove(self)
