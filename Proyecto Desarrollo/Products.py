class Product:
    def __init__(self, name, quantity, price, type, aditional, restaurant, bought):
        self.name=name
        self.quantity=quantity
        self.price=price
        self.type=type
        self.aditional=aditional
        self.restaurant=restaurant
        self.bought=bought
    def Show(self):
        print(f"Producto: {self.name}\nPrecio: {self.price}$ con iva\nCantidad: {self.quantity}\nInformación adicional:{self.aditional}")
        print("---------------------------------------------------")

class Beverage(Product):
    def __init__(self, name, quantity, price, type, aditional, restaurant, bought):
        super().__init__(name, quantity, price, type, aditional, restaurant, bought)
    def Show(self):
        return super().Show()

class Food(Product):
    def __init__(self, name, quantity, price, type, aditional, restaurant, bought):
        super().__init__(name, quantity, price, type, aditional, restaurant, bought)
    def Show(self):
        return super().Show()