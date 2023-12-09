from .Book import Book

class Comic(Book):
    def __init__(self, title, author, price, illustrators):
        self.illustrators = illustrators
        super().__init__(title, author, price)
    
    def add_illustrator(self, new_illustrator):
        self.illustrators.append(new_illustrator)