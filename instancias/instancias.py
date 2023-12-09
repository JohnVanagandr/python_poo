import sys
sys.path.append('D:\\2772895\\Poo\\python_poo')
sys.path.append('D:\\2772895\Poo\python_poo\\instancias')
sys.path.append('D:\\2772895\\Poo\\python_poo\\clases')

# Importa las clases Book, Comic y ShoppingCart desde los respectivos módulos
from clases.book import Book
from clases.comic import Comic
from clases.shoppingcart import ShoppingCart

# Crea una instancia de la clase ShoppingCart llamada "cart"
cart = ShoppingCart()

# Crea instancias de la clase Book con diferentes atributos
book1 = Book("1984", "G.O", 250)
book2 = Book("Frankenstein", "M.S", 450)

# Crea una instancia de la clase Comic con atributos específicos y una lista de ilustradores
comic1 = Comic("The Killing Joke", "A.M", 230, ["B.B"])
comic1.add_illustrator("J.H")

# Imprime los datos de cada libro y cómic utilizando el método get_all_data()
book1.get_all_data()
book2.get_all_data()
comic1.get_all_data()

# Agrega productos al carrito utilizando el método add_product() de la instancia "cart"
cart.add_product(2, comic1.get_price())
cart.add_product(1, book1.get_price())
cart.add_product(1, book2.get_price())

# Muestra los productos en el carrito utilizando el método show_products() de la instancia "cart"
cart.show_products()

# Imprime el ticket de compra utilizando el método print_ticket() de la instancia "cart"
cart.print_ticket()