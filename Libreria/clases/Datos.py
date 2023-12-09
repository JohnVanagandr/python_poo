class Datos:
  '''Contiene como atributos los datos de los usuarios y administradores.\n
  Contiene los metodos para agregar y eliminar usuarios'''
  __admin = {2000:{'Alejo':'ba17'}}
  __user = {}
  def __init__(self, n, p):
    self.__name, self.__password = n, p
    self.__id = 2001
  def get_name(self):
    return self.__name
  def validar(self, n, p):
    '''Valida que los datos de logeo sean de un usuario o de un administrador.\n
    Retorna un string con la confirmacion.'''
    admin = False
    user = False
    for account in self.__admin.values():
      for n, p in account.items():
        if n == self.__name and p == self.__password:
          admin = True
    for account in self.__user.values():
      for n, p in account.items():
        if n == self.__name and p == self.__password:
          user = True
    if admin:
      return 'Administrador'
    elif user:
      return 'Usuario'
    else:
      return 'No encontrado'
  def add_users(self, usuarios):
    '''Crea una cuenta de usuario solo si se esta logueado como "administrador".\n
    Retorna un string con la confirmacion.'''
    if self.validar(self.__name, self.__password) == 'Administrador':
      for usuario in usuarios:
        self.__user[self.__id] = usuario
        self.__id += 1
      return 'Accion realizada.'
    else:
      return 'La accion no se puede realizar.'
a = Datos('Alejo', 'ba17')
print(a.add_users([{'Brayan':'al98'}, {'Daniel':'da23'}, {'Andres':'an34'}]))
print(Datos._Datos__user)
