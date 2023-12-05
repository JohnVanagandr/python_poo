from Book import Book

class Comic(Book):
  def __init__(self, title, author, price, ilustrators):
    self.ilustrators = ilustrators
    super().__init__(title, author, price)
  
  def add_ilistrator(self, new_ilustrator):
    self.ilustrators.append(new_ilustrator)
    