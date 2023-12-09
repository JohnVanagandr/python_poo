class Book:
    def __init__(self, title, author, price):
        self.__title = title
        self.__author = author
        self.__price = price

    def getTitle(self):
        return f"El titulo es: {self.__title}"

    def setTitle(self, newTitle):
        self.__title = newTitle

    def getAuthor(self):
        return f"El autor es: {self.__author}"

    def setAuthor(self, newAuthor):
        self.__author = newAuthor

    def getPrice(self):
        return self.__price

    def setPrice(self, newPrice):
        self.__price = newPrice

    def showInformation(self):
        return f"Titulo: {self.__title} \nAutor: {self.__author} \nPrecio: {self.__price}"

  
