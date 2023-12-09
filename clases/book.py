# Definición de la clase Book
class Book:
    # Constructor de la clase, se ejecuta al crear una nueva instancia de la clase
    def __init__(self, title, author, price):
        # Atributos de instancia (encapsulados con el prefijo '_')
        self._title = title
        self._author = author
        self._price = price

    # Método para obtener el título
    def get_title(self):
        return self._title

    # Método para establecer un nuevo título
    def set_title(self, new_title):
        self._title = new_title

    # Método para obtener el autor
    def get_author(self):
        return self._author

    # Método para establecer un nuevo autor
    def set_author(self, new_author):
        self._author = new_author

    # Método para obtener el precio
    def get_price(self):
        return self._price

    # Método para establecer un nuevo precio
    def set_price(self, new_price):
        self._price = new_price

    # Método para imprimir todos los datos del libro
    def get_all_data(self):
        print(f"Title: {self.get_title()}, Author: {self.get_author()}, Price: {self.get_price()}")

