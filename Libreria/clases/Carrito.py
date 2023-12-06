from Biblioteca import b#, Biblioteca
class Carrito:
  '''Clase "Carrito de compras". Agrega o quita las compras.\n
  Muestra los productos agregados e imprime el valor total.'''
  __carrito = {}#Diccionario anidado. Almacenará el id(codigo), titulo y el costo.
  """Ejemplo: {1005(id):{Trazo de Tiza(titulo):25000(costo)}} 
  El costo es el producto del precio multiplicado por la cantidad de libros comprados."""
  def __init__(self):
    pass
  def add_carrito(self, codigo, cantidad):
    '''Agrega la compra al diccionario(carrito).\n
    Modifica las existencias del libro que se agrega.\n
    Retorna un string con la confirmacion.'''
    titulo = b.get_value(codigo).get_titulo()
    # 'titulo' busca el titulo del libro
    total = b.get_value(codigo).get_precio() * cantidad
    # 'total' busca el precio y calcula el total
    if codigo in self.__carrito:# Si el libro ya ha sido agregado al carrito
      """Esta condicion evita que se creen claves duplicadas."""
      for id, libro in self.__carrito.items():
        # recorremos el diccionario
        for titulo, valor in libro.items():
          # Recorremos el diccionario anidado
          if id == codigo:
            # Cuando los codigos coincidan se suma el costo total
            total += valor
      del self.__carrito[codigo]
      # eliminamos esta clave para luego crearla con el precio correcto
    self.__carrito[codigo] = {titulo:total}
    """Creamos la clave del diccionario con el id(codigo) del libro
    y le asignamos como valor otro diccionario, lo que crea la anidacion.
    El nuevo diccionario tiene como clave el titulo y como valor el costo(precio*cantidad)"""
    b.get_value(codigo).set_existencias(cantidad, True)
    # Se modifican las existencias
    return 'Agregado al carrito.\n'
  def unset_pdto(self, codigo, cantidad):
    '''Elimina un producto del carrito.\n
    Reestablece las existencias del libro.\n
    Retorna un string con la confirmacion.'''
    del self.__carrito[codigo]#del -> delete
    #Se elimina del "carrito" la clave(codigo) y con ella su valor(titulo:precio)
    b.get_value(codigo).set_existencias(cantidad, False)
    # Se modifican las existencias
    return 'Producto eliminado.'
  def mostrar_productos(self):
    '''Muestra los productos agregados al carrito.\n
    Retorna un string con el titulo y el valor total o retorna "vacio"\n
    si nada se ha agreagado aun.'''
    if len(self.__carrito) == 0:
      return 'El carrito está vacío.'
    else:
      pdts = ''#String que será llenado con la info del carrito
      for c in self.__carrito.values():#Recorremos lo productos del 'carrito'
        #Accedemos al diccionario anidado
        for t,v in c.items():#Recorremos el diccionario, {titulo:valor}
          #Concatenamos la informacion y la agregamos a la cadena.
          pdts += '\nTitulo: {}\nValor total: ${}\n'\
              .format(t, v)
      return pdts
  def get_carrito(self):
    '''Accede al diccionario "Carrito".\n
    Retorna el diccionario completo.'''
    return self.__carrito
  def calcular_total(self):
    """Calcula el valor total de la compra.
    Retorna un entero con el valor total."""
    total = 0#acumulador
    #recorremos los valores(titulo-precio) del diccionario
    for tp in self.__carrito.values():
      #ingresamos al diccionario anidado.
      for precio in tp.values():#recorremos los valores(precio).
        total += precio#sumamos el precio de cada lilbro agregado.
    return total
  def imprimir_recibo(self):
    '''Crea un archivo de extension ".txt" con la información de la compra.\n
    Retorna un string con la confirmacion.'''
    c = 'Libros comprados:\n{}\nTotal a pagar: ${}\n'\
        .format(self.mostrar_productos(), self.calcular_total())
        #Texto que será impreso en el recibo.
    print(c)#mostramos al usuario la informacion del recibo.
    r = open('recibo.txt', 'w')#creamos el archivo en modo escritura.
    r.write(c)#escribimos en el archivo la informacion.
    r.close()#cerramos el archivo.
    return 'Se ha impreso el recibo.'
c = Carrito()
# 'c' única instancia de 'Carrito' que será utilizada en toda la ejecucion
