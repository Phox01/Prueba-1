class Alimento:
    def __init__(self, nombre, precio):
        self.nombre= nombre
        self.precio=precio
        
class Comida(Alimento):
    def __init__(self, nombre, precio, sabor, platillo):
        super().__init__(nombre, precio)
        self.sabor= sabor
        self.platillo=platillo

class Bebida(Alimento):
    def __init__(self, nombre, precio, alcohol, temperatura):
        super().__init__(nombre, precio)
        self.alcohol= alcohol
        self.temperatura= temperatura