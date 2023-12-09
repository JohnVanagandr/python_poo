class ShopingCart:
    def __init__(self):
        """
        Constructor de la clase ShoppingCart.

        Inicializa una lista vacía para almacenar los productos.
        """
        self.products = []

    def add_product(self, amount, price):
        """
        Método para agregar productos al carrito.

        Parámetros:
        amount (int): Cantidad de productos a agregar.
        price (float): Precio unitario del producto a agregar.
        """
        self.products.extend([price] * amount)

    def show_products(self):
        """ 
        Método para mostrar los productos en el carrito.
        """
        print("\033[35mCart: \033[0", self.products)

    def calc_total(self):
        """
        Método para calcular el total a pagar por todos los productos en el carrito.

        Retorna:
        float: Total a pagar por los productos en el carrito.
        """
        return sum(self.products)

    def print_ticket(self):
        """
        Método para imprimir el ticket de compra con el total a pagar.
        """
        print(f"\033[35mTotal a pagar: {self.calc_total()}\033[0")
