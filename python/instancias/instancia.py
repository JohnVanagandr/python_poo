#import sys
#sys.path.append('/python/clases/')
from ..clases.book import Book #traemos los metodos
from ..clases.comic import Comic #traemos los metodos
from ..clases.shopingcart import ShopingCart #traemos los metodos


cart =  ShopingCart()
book1 =  Book("1984", "G.O", 250)
book2 =  Book("Frankenstein", "M.S", 450)

""" comic1 = Comic("The Killing Joke", "A.M", 230, ["B.B"])
comic1.addIlustrator("J.H")

book1.getAllData()
book2.getAllData()
comic1.getAllData()

cart.addProduct(2, comic1.price)
cart.addProduct(1, book1.price)
cart.addProduct(1, book2.price)

cart.showProducts()
cart.printTicket() """