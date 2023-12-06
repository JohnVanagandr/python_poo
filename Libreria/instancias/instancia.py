'''
#import mysql.connector
import MySQLdb
db_host = 'localhost'
db_user = 'root'
db_pass = 'mysqlroot'
db_name = 'a'
def consulta(query=''):
  datos = [db_host, db_user, db_pass, db_name]
  conn = MySQLdb.connect(*datos)#Conectar a la base de datos.
  cursor = conn.cursor()#Crear un cursor.
  cursor.execute(query)#Ejecutar una consulta.
  if query.upper().startswith('SELECT'):
    data = cursor.fetchall()#Traer los resultados de un select.
  else:
    conn.commit()#hacer efectiva la consulta.
    data = None
  cursor.close()#Cerrar el cursor.
  conn.close()#Cerrar la coneccion.
  return data
'''
import sys
sys.path.insert(0, '/d/2772895/python_poo/Libreria/clases/Carrito/')
from clases.Carrito import Libro, Comic
#instancias de los libros con su informacion
l1 = Libro('George R.R. Martin', 'Cancion de Hielo y Fuego', 60000, 7, 1001)
l2 = Libro('Gabriel Garcia Marquez', 'Cien Años de Soledad', 50000, 12, 1002)
l3 = Libro('Pierre Lemaitre', 'El ancho mundo', 45000, 5, 1003)
l4 = Libro('Luz Gabas', 'Lejos de Luisiana', 52000, 10, 1004)
l5 = Comic('Miguel Anxo Prado', 'Trazo de Tiza', 25000, 4, 1005, 'Norma Editorial')
l6 = Libro('Gabriel Garcia Marquez', 'El amor en los tiempos del colera', 40000, 5, 1006)
#añadimos cada libro al diccionario principal(books)
Libro.add_books([l1, l2, l3, l4, l5, l6])
"""
l2.add_book(l2)
l3.add_book(l3)
l4.add_book(l4)
l5.add_book(l5)
l6.add_book(l6)
"""
