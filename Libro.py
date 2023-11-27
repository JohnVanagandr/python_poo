class Libro:

  def __init__(self, autor, titulo, precio, existencias, id):
    self.autor = autor
    self.titulo = titulo
    self.precio = precio
    self.existencias = existencias
    self.id = id

  def informacion(self):
    print(f'Autor: {self.autor} Titulo: {self.titulo} Precio: {self.precio} Existencias: {self.existencias} Id: {self.id}')

  def valor(self):
    print(f'El valor de {self.titulo} es: {self.precio}')

  def cantidad(self):
    print(f'La cantidad en existencia de {self.titulo} es: {self.existencias}')