import sys
sys.path.append('Clases\Book.py')
sys.path.append('Clases\Comic.py')
sys.path.append('Clases\ShopCar.py')

from Clases.Book import Book #importa la clase Book del archivo books
from Clases.Comic import Comic #importa la clase Comic del archivo comics
from Clases.ShopCar import Car #importa la clase ShoppingCart del archivo shoppingcart


def main():
    car = Car()
    books = []
    comics = []

    while True:
        print("\n1. Agregar libro")
        print("2. Agregar cómic")
        print("3. Consultar información")
        print("4. Mostrar carro de compras")
        print("5. Calcular total a pagar")
        print("6. Quitar producto del carro")
        print("7. Salir")

        choice = input("Ingrese el número de la opción deseada: ")

        if choice == "1":
            title = input("Ingrese el título del libro: ")
            author = input("Ingrese el autor del libro: ")
            price = float(input("Ingrese el precio del libro: "))
            book = Book(title, author, price)
            books.append(book)
            add_to_cart = input("¿Desea agregar este libro al carro de compras? (S/N): ").upper()
            if add_to_cart == "S":
                car.add_products(1, price)
                print(f"Libro '{title}' agregado al carro de compras y a la lista de libros.")
            else:
                print(f"Libro '{title}' agregado solo a la lista de libros.")

        elif choice == "2":
            title = input("Ingrese el título del cómic: ")
            author = input("Ingrese el autor del cómic: ")
            price = float(input("Ingrese el precio del cómic: "))
            illustrators = input("Ingrese los ilustradores del cómic (separados por comas): ").split(',')
            comic = Comic(title, author, price, illustrators)
            comics.append(comic)
            add_to_cart = input("¿Desea agregar este cómic al carro de compras? (S/N): ").upper()
            if add_to_cart == "S":
                car.add_products(1, price)
                print(f"Cómic '{title}' agregado al carro de compras y a la lista de cómics.")
            else:
                print(f"Cómic '{title}' agregado solo a la lista de cómics.")

        elif choice == "3":
            print("\nLibros:")
            for book in books:
                print(book.showInformation())

            print("\nCómics:")
            for comic in comics:
                print(comic.showInformation())

        elif choice == "4":
            print(car.show_products())

        elif choice == "5":
            print(car.full_payment())

        elif choice == "6":
            if car.products:
                print("\nProductos en el carro:")
                print(car.show_products())
                product_to_remove = input("Ingrese el nombre del producto que desea quitar del carro: ")
                
                # Verificar si el producto está presente en la lista de productos del carro
                products_to_remove = [product for product in car.products if product.get('title', '') == product_to_remove]
                
                if products_to_remove:
                    # Mostrar los productos encontrados con el nombre dado
                    print(f"Productos encontrados con el nombre '{product_to_remove}':")
                    for idx, product in enumerate(products_to_remove, 1):
                        print(f"{idx}. {product}")
                    
                    # Solicitar al usuario que elija cuál quitar
                    product_index = int(input("Ingrese el número del producto que desea quitar: ")) - 1
                    
                    # Obtener el producto seleccionado y su precio
                    selected_product = products_to_remove[product_index]
                    title_to_remove = selected_product.get('title', '')
                    price_to_remove = selected_product.get('price', 0)
                    
                    # Solicitar la cantidad que se desea quitar
                    lot_to_remove = int(input(f"Ingrese la cantidad que desea quitar del producto '{title_to_remove}': "))
                    
                    # Eliminar la cantidad especificada del producto seleccionado
                    car.remove_products(lot_to_remove, title_to_remove, price_to_remove)
                    print(f"{lot_to_remove} unidades del producto '{title_to_remove}' han sido quitadas del carro.")
                else:
                    print(f"No se encontraron productos con el nombre '{product_to_remove}' en el carro.")
            else:
                print("El carro de compras está vacío.")

        elif choice == "7":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, ingrese un número del 1 al 7.")

if __name__ == "__main__":
    main() 