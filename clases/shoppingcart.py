from book import Book


# Define la clase ShoppingCart
class ShoppingCart:
    # Constructor de la clase, se ejecuta al crear una nueva instancia de la clase
    def __init__(self):
        # Inicializa un atributo llamado "products" que es una lista vacía
        self.products = []

    # Método para agregar productos al carrito
    def add_product(self, amount, price):
        # Extiende la lista de productos con una cantidad específica de elementos, cada uno con el precio dado
        self.products.extend([price] * amount)

    # Método para mostrar los productos en el carrito
    def show_products(self):
        # Imprime la lista de productos en el carrito
        print("Cart:", self.products)

    # Método para calcular el total de la compra
    def calc_total(self):
        # Suma todos los precios en la lista de productos y devuelve el resultado
        return sum(self.products)

    # Método para imprimir el ticket de compra con el total a pagar
    def print_ticket(self):
        # Imprime el total a pagar utilizando el método calc_total()
        print(f"Total to pay: {self.calc_total()}")

    # Método para eliminar un producto del carrito por título
    def remove_product(self, title):
        # Filtra la lista de productos excluyendo aquellos con el título proporcionado (para libros)
        self.products = [product for product in self.products if not (isinstance(product, Book) and product.title == title)]

    # Método para mostrar el total del carrito
    def show_total(self):
        # Imprime el total del carrito utilizando el método calc_total()
        print(f"Total in the cart: {self.calc_total()}")