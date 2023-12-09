#import sys
#sys.path.append('/python/clases/')
from clases.book import Book #traemos los metodos
from clases.comic import Comic #traemos los metodos
from clases.shopingcart import ShopingCart #traemos los metodos


# from collections import defaultdict

# class ShopingCart:
#     def __init__(self):
#         self.products = defaultdict(int)

#     def addProduct(self, quantity, price):
#         self.products[price] += quantity

#     def showProducts(self):
#         for price, quantity in self.products.items():
#             print(f"Quantity: {quantity}, Price: {price}")

#     def printTicket(self):
#         total = sum(price * quantity for price, quantity in self.products.items())
#         print(f"Total: {total}")

# class Book:
#     def __init__(self, title, author, price):
#         self.title = title
#         self.author = author
#         self.price = price

#     def getAllData(self):
#         print(f"Title: {self.title}, Author: {self.author}, Price: {self.price}")

# class Comic:
#     def __init__(self, title, author, price, illustrators):
#         self.title = title
#         self.author = author
#         self.price = price
#         self.illustrators = illustrators

#     def addIlustrator(self, illustrator):
#         self.illustrators.append(illustrator)

#     def getAllData(self):
#         print(f"Title: {self.title}, Author: {self.author}, Price: {self.price}, Illustrators: {self.illustrators}")

# cart = ShopingCart()
# book1 = Book("1984", "G.O", 250)
# book2 = Book("Frankenstein", "M.S", 450)
# comic1 = Comic("The Killing Joke", "A.M", 230, ["B.B"])
# comic1.addIlustrator("J.H")
# book1.getAllData()
# book2.getAllData()
# comic1.getAllData()
# cart.addProduct(2, comic1.set_price)
# cart.addProduct(1, book1.set_price)
# cart.addProduct(1, book2.set_price)
# cart.showProducts()
# cart.printTicket()

# from books import Book #importa la clase Book del archivo books
# from comics import Comic #importa la clase Comic del archivo comics
# from shoppingcart import ShoppingCart #importa la clase ShoppingCart del archivo shoppingcart



def display_menu():
    """
    Muestra el menú de opciones para el carrito de compras.
    """
    print("\n")
    print("\033[1;32mWelcome to the shopping cart. Select an option:\033[0m")
    print("\n")
    print("\033[4;36m1. Add a book to the cart\033[0m")
    print("\033[4;36m2. Add a comic to the cart\033[0m")
    print("\033[4;36m3. Show products in the cart\033[0m")
    print("\033[4;36m4. Calculate total\033[0m")
    print("\033[4;36m5. Print ticket\033[0m")
    print("\033[4;36m6. Show books in the cart\033[0m")
    print("\033[4;36m7. Show comics in the cart\033[0m")
    print("\033[4;36m0. Exit\033[0m")


countBooks = [] # crea una lista vacia en donde se ingresaran los libros
countComics = [] # crea una lista vacia en donde se ingresaran los comics
   
cart = ShopingCart() # Crea una instancia de la clase ShoppingCart

while True:
    display_menu()  # Muestra el menú
    print("\n")
    choice = input("\033[1;32mEnter the number of the option you want:\033[0m")

    if choice == "1":
        # Agrega un libro al carrito
        print("\n")
        title = input("\033[3;33mEnter the title of the book:\033[0m ")
        author = input("\033[3;33mEnter the author of the book:\033[0m ")
        price = float(input("\033[3;33mEnter the price of the book:\033[0m "))
        quantity = int(input("\033[3;33mEnter the quantity:\033[0m "))
        book = Book(title, author, price) # Crea una instancia de la clase Book
        countBooks.append(book) #se agrega la instancia de la clase Book a la lista
        cart.add_product(quantity, book.price) # Agrega el producto al carrito
        print("\n")
        print(f"{quantity} '{title}'\033[1;32madded to the cart ✔.\033[0m")
        

    elif choice == "2":
        # Agrega un cómic al carrito
        print("\n")
        title = input("\033[3;33mEnter the title of the comic: \033[0m")
        author = input("\033[3;33mEnter the author of the comic:\033[0m")
        price = float(input("\033[3;33mEnter the price of the comic:\033[0m "))
        illustrators = input("\033[3;33mEnter the illustrators (comma-separated): \033[0m").split(",")
        quantity = int(input("\033[3;33mEnter the quantity: \033[0m"))
        comic = Comic(title, author, price, illustrators) # Crea una instancia de la clase Comic
        countComics.append(comic) #se agrega la instancia de la clase Comic a la lista
        cart.add_product(quantity, comic.price) # Agrega el producto al carrito
        print("\n")
        print(f"{quantity} '{title}'\033[1;32madded to the cart ✔. \033[0m")
        

    elif choice == "3":
        # Muestra los productos en el carrito
        print("\n")
        cart.show_products()

    elif choice == "4":
        # Calcula el total a pagar por los productos en el carrito
        print("\n")
        total = cart.calc_total()
        print(f"\033[35mTotal to pay: {total}\033[0")

    elif choice == "5":
        # Imprime el ticket con el total a pagar
        print("\n")
        cart.print_ticket()

    elif choice == "6":
        # Muestra la informacion de los libros que hay en el carrito
        print("\n")
        for i in countBooks:
            i.get_all_data()
        print("\n")

    elif choice == "7":
        # Muestra la informacion de los comics que hay en el carrito
        print("\n")
        for i in countComics:
            i.get_all_data()
        print("\n")

    elif choice == "0":
         # Sale del programa
        print("\n")
        print("\033[1;34mThank you for using the shopping cart. Goodbye!\033[0")
        break
    else:
        print("\n")
        print("\033[1;31mInvalid option. Please enter a valid number.\033[0")
        




