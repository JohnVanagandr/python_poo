from Book import Book
from Comic import Comic
from ShopCar import Car


car = Car()

book1 = Book("1984", "G.O", 250)
book2 = Book("Frankenstein", "M.S", 450)

comic1 = Comic("The Killing Joke", "A.M", 230, ["B.B"])
comic1.add_ilistrator("J.H")

car.add_products(2, comic1.getPrice())
car.add_products(1, book1.getPrice())
car.add_products(1, book2.getPrice())

car.show_products()
car.full_payment() 

print(book1.showInformation(),book2.showInformation(),comic1.showInformation())