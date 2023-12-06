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