from .Book import Book

class Car:
  def __init__(self):
    self.products = []
  
  def add_products(self, lot, price):
    self.products.extend(([price])* lot)
    
  def show_products(self):
    return f"Carro: {self.products}"
  
  def remove_products(self, lot, price):
        for _ in range(lot):
            self.products.remove(price)
  
  def calc_total(self):
    total_products = sum(self.products)
    return total_products
  
  def full_payment(self):
    return f"Total a pagar: {self.calc_total()}"