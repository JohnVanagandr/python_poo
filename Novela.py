from Libro import Libro

class Novela(Libro):
  def __init__(self, autor, titulo, precio, existencias, id):
    Libro.__init__(self, autor, titulo, precio, existencias, id)