from books import Book; #importa la clase Book del archivo books

class Comic(Book):
    def __init__(self, title, author, price, illustrators):
        """
        Constructor de la clase Comic, que hereda de la clase Book.

        Parámetros:
        title (str): Título del cómic.
        author (str): Autor del cómic.
        price (float): Precio del cómic.
        illustrators (list): Lista de ilustradores del cómic.
        """
        super().__init__(title, author, price)
        self.illustrators = illustrators

    def add_illustrator(self, new_illustrator):
        """
        Método para agregar un nuevo ilustrador a la lista de ilustradores del cómic.

        Parámetros:
        new_illustrator (str): Nuevo ilustrador a agregar.
        """
        self.illustrators.append(new_illustrator)

    def get_all_data(self):
        """
        Método para imprimir todos los datos del libro.
        Imprime el título, autor y precio del libro.
        """
        print(f"\033[3;36mTitulo: {self._title}, Author: {self._author}, Precio: {self._price}, Ilustradores: {self.illustrators}\033[0")  