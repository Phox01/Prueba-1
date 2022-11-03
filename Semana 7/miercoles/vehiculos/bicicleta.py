from vehiculo import Vehicle

class Bicicleta(Vehicle):
    def __init__(self, ruedas, color, tipo):
        super().__init__(ruedas, color)
        self.tipo = tipo

class Motocicleta(Bicicleta):
    def __init__(self, ruedas, color, tipo, cc, velocidad):
        super().__init__(ruedas, color, tipo)
        self.velocidad=velocidad
        self.cc= cc