from Base import Base
import math

class Hexagono(Base):
  _lados = 6

  def __init__(self, lado, apotema):
    self.lado = lado
    self.apotema = apotema

  def perimetro(self):
    return self._lados * self.lado
  
  def area(self):
    return (self.perimetro() * self.apotema) / 2