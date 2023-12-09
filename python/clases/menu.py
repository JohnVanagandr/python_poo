from book import Book #importa la clase Book del archivo books
from comic import Comic #importa la clase Comic del archivo comics
from shopingcart import ShopingCart #importa la clase ShoppingCart del archivo shoppingcart



def display_menu():
    """
    Muestra el menú de opciones para el carrito de compras.
    """
    print("\n")
    print("\033[1;32mBienvenido al carrito de compras. Seleccione una opción:\033[0m")
    print("\n")
    print("\033[4;36m1. Añade un libro al carrito\033[0m")
    print("\033[4;36m2. Añade un cómic al carrito.\033[0m")
    print("\033[4;36m3. Mostrar productos en el carrito\033[0m")
    print("\033[4;36m4. Calcular el total\033[0m")
    print("\033[4;36m5. Imprimir boleto\033[0m")
    print("\033[4;36m6. Mostrar libros en el carrito\033[0m")
    print("\033[4;36m7. Muestra cómics en el carrito.\033[0m")
    print("\033[4;36m0. Exit\033[0m")


countBooks = [] # crea una lista vacia en donde se ingresaran los libros
countComics = [] # crea una lista vacia en donde se ingresaran los comics

cart = ShoppingCart() # Crea una instancia de la clase ShoppingCart

while True:
    display_menu()  # Muestra el menú
    print("\n")
    choice = input("\033[1;32mIntroduce el número de la opción que deseas:\033[0m")

    if choice == "1":
        # Agrega un libro al carrito
        print("\n")
        title = input("\033[3;33mIntroduce el título del libro:\033[0m ")
        author = input("\033[3;33mIngrese el autor del libro:\033[0m ")
        price = float(input("\033[3;33mIntroduce el precio del libro:\033[0m "))
        quantity = int(input("\033[3;33mIntroduzca la cantidad:\033[0m "))
        book = Book(title, author, price) # Crea una instancia de la clase Book
        countBooks.append(book) #se agrega la instancia de la clase Book a la lista
        cart.add_product(quantity, book.price) # Agrega el producto al carrito
        print("\n")
        print(f"{quantity} '{title}'\033[1;32madded to the cart ✔.\033[0m")
        

    elif choice == "2":
        # Agrega un cómic al carrito
        print("\n")
        title = input("\033[3;33mIntroduce el título del libro: \033[0m")
        author = input("\033[3;33mEntra el autor del cómic.:\033[0m")
        price = float(input("\033[3;33mIntroduce el precio del cómic.:\033[0m "))
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