class Book:
  def __init__(self, title,author,price):
    self.__title = title
    self.__author = author
    self.__price = price
  
  def getTitle(self):
    return f"El titulo es: {self.__title}"
  
  def setTitle(self, newTitle):
    self.__title = newTitle
  
  def getAuthor(self):
    return f"El autor es: {self.__author}"
  
  def setTitle(self, newAuthor):
    self.__title = newAuthor

  def getPrice(self):
    return f"El precio es:{self.__price}"
  
  def setTitle(self, newPrice):
    self.__title = newPrice

  def showInformation(self):
    return f"Titulo del libro: {self.__title} \nAutor del libro: {self.__author} \nPrecio del libro: {self.__price}"
  
