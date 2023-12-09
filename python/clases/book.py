class Book:
    def __init__(self, title, author, price):
        """
        Constructor de la clase Book.

        Parámetros:
        title (str): Título del libro.
        author (str): Autor del libro.
        price (float): Precio del libro.
        """
        self._title = title
        self._author = author
        self._price = price

    @property
    def title(self):
        """
        Getter para el título del libro.

        Retorna:
        str: Título del libro.
        """
        return self._title

    @title.setter
    def title(self, new_title):
        """
        Setter para actualizar el título del libro.

        Parámetros:
        new_title (str): Nuevo título del libro.
        """
        self._title = new_title

    @property
    def author(self):
        """
        Getter para el autor del libro.

        Retorna:
        str: Autor del libro.
        """
        return self._author

    @author.setter
    def author(self, new_author):
        """
        Setter para actualizar el autor del libro.

        Parámetros:
        new_author (str): Nuevo autor del libro.
        """
        self._author = new_author

    @property
    def price(self):
        """
        Getter para el precio del libro.

        Retorna:
        float: Precio del libro.
        """
        return self._price

    @price.setter
    def price(self, new_price):
        """
        Setter para actualizar el precio del libro.

        Parámetros:
        new_price (float): Nuevo precio del libro.
        """
        self._price = new_price

    def get_all_data(self):
        """
        Método para imprimir todos los datos del libro.
        Imprime el título, autor y precio del libro.
        """
        print(f"\033[3;36mTitulo: {self._title}, Author: {self._author}, Precio: {self._price}\033[0")


