const _private = new WeakMap();

class Book {
  constructor(title, author, price) {
    const properties = {
      _title: title,
      _author: author,
      _price: price,
    };

    _private.set(this, { properties });
  }

  get title() {
    return _private.get(this).properties["_title"];
  }
  set title(newTitle) {
    return (_private.get(this).properties["_title"] = newTitle);
  }
  get author() {
    return _private.get(this).properties["_author"];
  }
  set author(newAuthor) {
    return (_private.get(this).properties["_author"] = newAuthor);
  }
  get price() {
    return _private.get(this).properties["_price"];
  }
  set price(newPrice) {
    return (_private.get(this).properties["_price"] = newPrice);
  }

  getAllData() {
    console.log(
      `Titulo: ${this.title}, Author: ${this.author}, Precio: ${this.price}`
    );
  }
}

class Comic extends Book {
  constructor(title, author, price, ilustrators) {
    super(title, author, price);
    this.ilustrators = ilustrators;
  }
  addIlustrator(newIlustrator = []) {
    this.ilustrators.push(newIlustrator);
  }
}

class ShopingCart {
  constructor() {
    this.products = [];
  }

  addProduct(amount, price) {
    this.products.push(...Array(amount).fill(price));
  }

  showProducts() {
    console.log("Cart: ", this.products);
  }

  total() {
    return this.products
      .map((price) => price)
      .reduce((ac, price) => ac + price, 0);
  }

  ticket() {
    console.log(`Total a pagar: ${this.total()}`);
  }
}

cart = new ShopingCart();
const book1 = new Book("1984", "G.O", 250);
const book2 = new Book("Frankenstein", "M.S", 450);

const comic1 = new Comic("The Killing Joke", "A.M", 230, ["B.B"]);
comic1.addIlustrator("J.H");

book1.getAllData();
book2.getAllData();
comic1.getAllData();

cart.addProduct(2, comic1.price);
cart.addProduct(1, book1.price);
cart.addProduct(1, book2.price);

cart.showProducts();
cart.ticket();
