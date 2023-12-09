import sys
sys.path.append('D:\\2772895\\Poo\\python_poo')
sys.path.append('D:\\2772895\Poo\python_poo\\instancias')
sys.path.append('D:\\2772895\\Poo\\python_poo\\clases')
sys.path.append('D:\\2772895\\Poo\\python_poo\\comic')

# Importa las clases Book, Comic y ShoppingCart desde los respectivos módulos
from clases.book import Book
from clases.comic import Comic
from clases.shoppingcart import ShoppingCart

# Función para mostrar el menú y obtener la opción del usuario
def display_menu():
    print("------ Menu ------")
    print("1. Agregar libro al carrito")
    print("2. Agregar cómic al carrito")
    print("3. Mostrar carrito")
    print("4. Eliminar libro del carrito")
    print("5. Eliminar cómic del carrito")
    print("6. Ver total del carrito")
    print("7. Imprimir ticket")
    print("8. Salir")
    return input("Ingrese el número de la opción deseada: ")

# Crea una instancia de la clase ShoppingCart llamada "cart"
cart = ShoppingCart()

# Bucle principal
while True:
    # Llama a la función display_menu() para mostrar el menú y obtener la opción del usuario
    option = display_menu()

    # Verifica la opción seleccionada por el usuario
    if option == "1":
        # Solicita al usuario ingresar información del libro
        title = input("Ingrese el título del libro: ")
        author = input("Ingrese el autor del libro: ")
        price = float(input("Ingrese el precio del libro: "))
        quantity = int(input("Ingrese la cantidad de libros a agregar al carrito: "))

        # Crea una instancia de la clase Book con la información proporcionada
        book = Book(title, author, price)
        # Agrega productos al carrito utilizando el método add_product() de la instancia "cart"
        cart.add_product(quantity, book.get_price())

    elif option == "2":
        # Solicita al usuario ingresar información del cómic
        title = input("Ingrese el título del cómic: ")
        author = input("Ingrese el autor del cómic: ")
        price = float(input("Ingrese el precio del cómic: "))
        # Divide los ilustradores ingresados por el usuario en una lista
        illustrators = input("Ingrese los ilustradores del cómic (separados por coma): ").split(', ')
        quantity = int(input("Ingrese la cantidad de cómics a agregar al carrito: "))

        # Crea una instancia de la clase Comic con la información proporcionada
        comic = Comic(title, author, price, illustrators)
        # Agrega productos al carrito utilizando el método add_product() de la instancia "cart"
        cart.add_product(quantity, comic.get_price())

    elif option == "3":
        # Muestra los productos en el carrito utilizando el método show_products() de la instancia "cart"
        cart.show_products()

    elif option == "4":
       # Solicita al usuario el título del libro a eliminar
        title_to_remove = input("Ingrese el título del libro a eliminar del carrito: ")
       # Elimina el libro del carrito utilizando el método remove_product() de la instancia "cart"
        cart.remove_product(title_to_remove)

    elif option == "5":
        # Solicita al usuario el título del cómic a eliminar
        title_to_remove = input("Ingrese el título del cómic a eliminar del carrito: ")
        # Elimina el cómic del carrito utilizando el método remove_product() de la instancia "cart"
        cart.remove_product(title_to_remove)

    elif option == "6":
        # Muestra el total del carrito utilizando el método show_total() de la instancia "cart"
        cart.show_total()

    elif option == "7":
        # Imprime el ticket de compra utilizando el método print_ticket() de la instancia "cart"
        cart.print_ticket()

    elif option == "8":
        # Sale del bucle y termina el programa
        print("Saliendo del programa. ¡Hasta luego!")
        break

    else:
        # Imprime un mensaje de error si la opción no es válida
        print("Opción no válida. Por favor, ingrese un número del 1 al 7.")