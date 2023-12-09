# Importa la clase Book del módulo book
from book import Book

# Define la clase Comic que hereda de la clase Book
class Comic(Book):
    # Constructor de la clase Comic, que toma como parámetros título, autor, precio e ilustradores
    def __init__(self, title, author, price, illustrators):
        # Llama al constructor de la clase base (Book) utilizando super()
        super().__init__(title, author, price)
        # Añade un nuevo atributo "illustrators" específico de la clase Comic
        self.illustrators = illustrators

    # Método para añadir un nuevo ilustrador a la lista de ilustradores
    def add_illustrator(self, new_illustrator):
        self.illustrators.append(new_illustrator)