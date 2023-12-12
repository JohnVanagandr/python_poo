from sys import path
from os import getcwd
path.append(getcwd())
try:
  from Biblioteca import biblioteca # Importacion 1 de b
  from Libro import Libro # Importacion 1 de Libro
  from Comic import Comic # Importacion 1 de Comic
except ImportError:
  pass
try:
  from Libreria.clases.Biblioteca import b # Importacion 2 de b
  from Libreria.clases.Libro import Libro # Importacion 2 de Libro
  from Libreria.clases.Comic import Comic # Importacion 2 de Comic
  #from Libreria.clases.Carrito import c # Importacion 2 de c
except ImportError:
  pass
def libros():
  '''Contiene las instancias de los libros y los agrega a la biblioteca.\n
  Retorna el diccionario con la informacion de los libros.'''
  l1 = Libro('George R.R. Martin', 'Festin de Cuervos', 60000, 7)
  l2 = Libro('Gabriel Garcia Marquez', 'Cien Años de Soledad', 50000, 12)
  l3 = Libro('Pierre Lemaitre', 'El ancho mundo', 45000, 5)
  l4 = Libro('Luz Gabas', 'Lejos de Luisiana', 52000, 10)
  l5 = Comic('Miguel Anxo Prado', 'Trazo de Tiza', 25000, 4, 'Norma Editorial')
  l6 = Libro('Gabriel Garcia Marquez', 'El amor en los tiempos del colera', 40000, 5)
  l7 = Libro('Frank G. Slaughter', 'En un Jardin Oscuro', 37000, 9)
  #añadimos cada libro al diccionario principal(books)
  biblioteca.add_books([l1, l2, l3, l4, l5, l6, l7])
  return biblioteca.get_books()
def login(name, password):
  pass
