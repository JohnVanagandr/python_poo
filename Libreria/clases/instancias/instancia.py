from sys import path
from os import getcwd
path.append(getcwd())
from Biblioteca import b
from Libro import Libro
from Comic import Comic
from Carrito import c
def libros():
  '''Contiene las instancias de los libros y los agrega a la biblioteca.\n
  Retorna el diccionario con la informacion de los libros.'''
  l1 = Libro('George R.R. Martin', 'Cancion de Hielo y Fuego', 60000, 7)
  l2 = Libro('Gabriel Garcia Marquez', 'Cien Años de Soledad', 50000, 12)
  l3 = Libro('Pierre Lemaitre', 'El ancho mundo', 45000, 5)
  l4 = Libro('Luz Gabas', 'Lejos de Luisiana', 52000, 10)
  l5 = Comic('Miguel Anxo Prado', 'Trazo de Tiza', 25000, 4, 'Norma Editorial')
  l6 = Libro('Gabriel Garcia Marquez', 'El amor en los tiempos del colera', 40000, 5)
  #añadimos cada libro al diccionario principal(books)
  b.add_books([l1, l2, l3, l4, l5, l6])
  return b.get_books()