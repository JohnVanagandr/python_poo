class Libro:
  """Clase libro. Contiene los metodos para agregar la info de los libros.\n
  La clave en cada diccionario será el id de cada libro."""
  __books = {}#Guardará la informacion completa de los libros.
  __prices = {}#Guardará solo los precios.
  __titles = {}#Guardará solo los titulos.
  __exts = {}#Guardará solo las existencias.
  __instances = {}#Guardará las instancias de los libros. <--(KeyError)
  '''Falta solucionar error de llave (KeyError) al recorrer el dict
  para poder trabajar todo directamente con las instancias'''
  def __init__(self, a, t, p, e, i):
    self.__autor, self.__titulo, self.__precio, self.__existencias, self.__id = a, t, p, e, i
  def info(self):
    '''Metodo que retorna un string con la informacion del libro'''
    return 'Titulo: {}\nAutor: {}\nPrecio: ${}\nExistencias: {}\nCodigo: {}'\
        .format(self.__titulo, self.__autor, self.__precio, self.__existencias, self.__id)
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
  def get_existencias(cod):
    return Libro.__exts[cod]
  def set_existencias(self, n):
    self.__existencias = n
  def set_dic_existencias(cod, cnt):
    '''Valida si quedan suficientes libros para realizar la venta.\n
    Retorna un boleano con la confirmacion.'''
    agotado = False
    #-->Falta solucionar error de 'llave' en dict "instancias"
    #-->No retorna el valor de dict(instancia)
    #if Libro.__instances[cod].__existencias - cnt < 0:<--(KeyError)
    if Libro.__exts[cod] - cnt < 0:
      #Si no hay suficientes libros, no se puede realizar la compra.
      agotado = True
    else:
      #De lo contrario se puede realizar la compra.
      #Libro.__instances[cod].__existencias -= cnt <--(KeyError)
      Libro.__exts[cod] -= cnt
    return agotado
  def add_books(libros=[]):
    '''Agrega los libros instanciados a los diccionarios(propiedades de clase)\n
    (books, prices, titles, exts, instances)'''
    for libro in libros:
      Libro.__books[libro.get_id()] = libro.info()
      """Agrega el id(codigo) como 'llave' y la informacion como 'valor'."""
      Libro.__prices[libro.get_id()] = libro.__precio
      """Agrega el id(codigo) como 'llave' y el precio como 'valor'."""
      Libro.__titles[libro.get_id()] = libro.__titulo
      """Agrega el id(codigo) como 'llave' y el titulo como 'valor'."""
      Libro.__exts[libro.get_id()] = libro.__existencias
      """Agrega el id(codigo) como 'llave' y las existencias como 'valor'."""
      Libro.__instances[libro.get_id] = libro
      """Agrega el id(codigo) como 'llave' y la instancia como 'valor'."""
  def get_books():
    '''Metodo getter para acceder al diccionario (books)\n
    Muestra en pantalla la info de los libros.'''
    c = 1
    for inf in Libro.__books.values():#bucle para recorrer el diccionario
      print('Libro {}:\n{}\n'.format(c, inf))
      c += 1
  def get_dic_books():
    '''Metodo getter para acceder al diccionario (books).\n
    Retorna el diciconario completo con la informacion de los libros.'''
    return Libro.__books
  def get_price(codigo):
    '''Accede al precio del libro utilizando el id(codigo).'''
    return Libro.__prices[codigo]
  def get_title(codigo):
    '''Accede al titulo del libro utilizando el id(codigo)'''
    return Libro.__titles[codigo]
#def unset_exts(codigo, cantidad):
#  return instancia.set_existencias(cantidad)
