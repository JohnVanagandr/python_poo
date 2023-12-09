from .book import Book #traemos los metodos de laclase book

class Comic(Book): #creamos la clase comic Hereda de book
    #creamos el metodo constructor 
    #inicializa una clase
    def __init__(self,title, author, price, ilustrators):
        #inicializamos los atributos
        self.ilustrators=ilustrators
        #llamamos la superclase Book y enviamos los parametros
        Book().__init__(title, author, price)

    #creamos el metodo
    def addIlustrator(self,newIlustrators):
        #agregar nuevo ilustrador
        self.ilustrators.append(newIlustrators)
