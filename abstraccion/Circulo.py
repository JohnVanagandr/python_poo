from Base import Base

class Circulo(Base):
  _pi = 3.1416

  def __init__(self, radio):
    self.radio = radio

  def perimetro(self):
    return 2 * self._pi * self.radio

  def area(self):
    return self._pi * (self._pi ** 2)