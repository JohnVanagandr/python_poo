#import sys, os
#sys.path.insert(0, os.getcwd())
from Libro import Libro
class Comic(Libro):
  def __init__(self, a, t, p, e, i, il):
    super().__init__(a, t, p, e, i)
    self.__titulo = t
    self.__autor = a
    self.__precio = p
    self.__existencias = e
    self.__id = i
    self.__ilustrador = il
  def info(self):
    """Retorna un string con la informacion del comic."""
    return 'Titulo: {}\nAutor: {}\nPrecio: ${}\nExistencias: {}\nEditorial: {}\nCodigo: {}'\
        .format(self.__titulo, self.__autor, self.__precio, self.__existencias, self.__ilustrador, self.__id)
