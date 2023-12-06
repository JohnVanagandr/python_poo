from sys import path
from os import getcwd
path.insert(0, getcwd())
from instancia import *
from Carrito import Carrito
print('Libros disponibles:\n')
Libro.get_books()
#Imprime la informacion de todos los libros que estan actualmente.
fin = False#Rompe los bucles al terminar las comprobaciones.
while True:
  if fin:
    break
  e1 = input('Desea agregar algun libro al carrito? y/n: ')
  if e1.upper() == 'Y':
    while True:
      if fin:
        break
      try:
        cod = int(input('Ingrese el codigo del libro que desea comprar: '))
        if Libro.get_existencias(cod) < 1:
            #Ya no quedan libros con ese codigo en el diccionario.
            print('No hay suficientes existencias de ese libro.')
        elif cod in Libro.get_dic_books():
          #Busca el id(codigo) en el diccionario usando el metodo getter.
          while True:
            cnt = int(input('Ingrese la cantidad de libros que desea comprar: '))
            if cnt <= 0:
              print('La cantidad debe ser mayor a cero.')
            else:
              if Libro.set_dic_existencias(cod, cnt):
                print('No hay suficientes libros para realizar esa compra.')
              else:
                break
          Carrito().add_carrito(cod, cnt)#Agrega la compra.
          e2 = input('Desea comprar otro libro? y/n: ')
          if e2.upper() != 'Y':
            vacio = False#Confirmacion del carrito vacio.
            e3 = input('Antes de finalizar, desea eliminar algun producto del carrito? y/n: ')
            if e3.upper() == 'Y':
              #Si desea eliminar algun producto
              while True:
                try:
                  e4 = int(input('Ingrese el codigo del libro: '))
                  print(Carrito.unset_pdto(e4))#Elimina la compra.
                  if len(Carrito.get_carrito()) == 0:
                    #Verifica si el carrito esta vacio.
                    print('Eliminaste todos los productos del carrito.')
                    vacio = True
                    break
                  e5 = input('Desea eliminar otro producto? y/n: ')
                  if e5.upper() != 'Y':
                    #Si no desea eliminar eliminar otro producto.
                    print(Carrito().imprimir_recibo())
                    print('Programa finalizado.')
                    fin = True
                    break
                except ValueError:
                  print('Se debe ingresar un valor entero.')
                except KeyError:
                  print('Ese libro no está en el carrito.\n')
              if vacio:#si el carrito esta vacio.
                e6 = input('Desea agregar mas productos al carrito? y/n: ')
                if e6.upper() == 'N' or e6.upper() != 'Y':
                  #si no desea agregar mas productos.
                  fin = True
                  print('Programa finalizado.')
                  break
            elif e3.upper() == 'N':
              #Si no desea eliminar un producto.
              print(Carrito().imprimir_recibo())
              print('Programa finalizado.')
              fin = True
              break
        else:
          print('No hay un libro con ese código.\n')
      except ValueError:
        print('Se debe ingresar un valor entero.')
      except KeyError:
        print('El código no es válido.')
  elif e1.upper() == 'N':
    print('Programa finalizado.')
    break
  else:
    print('No ha digitado correctamente.')
