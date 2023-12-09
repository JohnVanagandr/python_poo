#import mysql.connector
#from sql import *
#from sql.aggregate import *
#from sql.conditionals import *
#import pyodbc
import mysql.connector
host = 'localhost'
user = 'root'
password = ''
mydb = mysql.connector.connect()
cursor = mydb.cursor()
cursor.execute("USE Libreria")
