from sys import path
from os import getcwd
path.insert(0, getcwd())
try:
  from Biblioteca import Biblioteca
  # Importacion 1 de Biblioteca
except ImportError:
  pass
try:
  from Libreria.clases.Biblioteca import Biblioteca
  # Importacion 2 de Biblioteca
except ImportError:
  pass
class Libro(Biblioteca):
  """Contiene los metodos para agregar la info de los libros.\n
  La clave en cada diccionario será el id de cada libro."""
  def __init__(self, a, t, p, e):
    self.__autor = a
    self.__titulo = t
    self.__precio = p
    self.__existencias = e
    self.__id = 0
    # 'id' será asignado por 'biblioteca'
  def get_id(self):
    return self.__id
  def set_id(self, n):
    self.__id = n
  def get_titulo(self):
    return self.__titulo
  def set_titulo(self, n):
    self.__titulo = n
  def get_autor(self):
    return self.__autor
  def set_autor(self, n):
    self.__autor = n
  def get_precio(self):
    return self.__precio
  def set_precio(self, n):
    self.__precio = n
  def get_existencias(self):
    return self.__existencias
  def set_existencias(self, n, restar = False):
    '''Modifica las existencias de acuerdo a lo indicado por "Carrito"'''
    # 'restar' parametro pasado por 'add_carrito' y 'unset_carrito'
    # indica si se deben incrementar o disminuir las existencias
    if restar:
      self.__existencias -= n
    else:
      self.__existencias += n
  def info(self):
    '''Metodo que retorna un string con la informacion del libro'''
    return 'Titulo: {}\nAutor: {}\nPrecio: ${}\nExistencias: {}\nCodigo: {}'\
        .format(self.__titulo, self.__autor, self.__precio, self.__existencias, self.__id)
