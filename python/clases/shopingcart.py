class ShopingCart ():# creamos la clase
     #creamos el metodo constructor 
    #inicializa una clase
    def __init__(self):
        #inicializamos un arreglo
        self.products=[] 
    #creamos el metodo addproduct
    def addProduct(self,amount, price):
        #aumentamos el array
        self.products.extend([price]*amount)
    #creamos el metodo showproducts
    def showProducts(self):
        #retornamos el listado de productos
        return f"Productos: {self.products}"
    
    #creamos el metodo calcTotal
    def calcTotal(self):
        #retornamos la suma de productos
        return sum(self.products)

    #creamos el metodo printTicket
    def printTicket(self):
        #retornamos el total
        return f"Total a pagar: {self.calcTotal()} "
