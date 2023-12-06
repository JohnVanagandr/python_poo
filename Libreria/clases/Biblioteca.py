class Biblioteca:
  '''Clase biblioteca. Almacena las instancias de los libros.\n
  Contiene los metodos para agregar libros al diccionario,\n
  asi como para acceder a su informacion.'''
  __books = {}
  # 'books' guardará las instancias de los libros.
  def __init__(self):
    self.__codigo = 1001
    # 'codigo' será asignado a cada libro.
  def get_books(self):
    '''Metodo getter para acceder al diccionario (books)\n
    Muestra en pantalla la info de los libros.'''
    c = 1
    for inf in self.__books.values():
      #bucle para recorrer el diccionario
      print('Libro {}:\n{}\n'.format(c, inf.info()))
      c += 1
  def add_books(self, libros):
    '''Agrega las instacias de los libros al diccionario "books".\n
    La clave es el atributo "codigo".'''
    for libro in libros:
      self.__books[self.__codigo] = libro
      libro.set_id(self.__codigo)
      self.__codigo += 1
  def get_value(self, codigo):
    """Accede al dict 'books' con el codigo del libro.\n
    Se usa para acceder a la informacion de cada libro.\n
    Retorna la instancia del libro"""
    return self.__books[codigo]
  def get_dic_books(self):
    '''Metodo getter para acceder al diccionario (books).\n
    Retorna el diciconario completo con la informacion de los libros.'''
    return self.__books
b = Biblioteca()
# 'b' única instancia de 'Biblioteca' que será utilizada en toda la ejecucion
