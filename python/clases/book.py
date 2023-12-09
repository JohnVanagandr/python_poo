class Book:
    def __init__(self,title,author,price):
        self.__title = title
        self.__author = author
        self.__price = price

    def get_title(self):
        return f"El titulo es: {self.__title}"
    
    def set_title(self,new_title):
        self.__title=new_title  

    def get_author(self):
        return f"El autor es: {self.__author}"
    
    def set_author(self,new_author):
        self.__author=new_author

    def get_price(self):
        return f"El precio es: {self.__price}"

    def set_price(self,new_price):
            self.__price=new_price

    def getAllData(self):
         return f"Titulo: {self.__title}, Autor: {self.__author}, Precio: {self.__price}"
    
    