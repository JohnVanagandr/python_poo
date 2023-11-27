from Base import Base
import math

class Cuadrado(Base):

  _lados = 0

  def __init__(self, lado):
    self.lado = lado
    self._lados = 4

  def perimetro(self):
    return self._lados * self.lado
  
  def area(self):
    return math.pow(self.lado, 2)