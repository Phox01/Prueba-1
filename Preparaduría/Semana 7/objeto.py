class Caballo:
    raza=0
    def __init__(self, pelaje, color, tamaño, nombre):
        self.pelaje=pelaje
        self.color=color
        self.tamaño=tamaño
        self.nombre=nombre
    def print(self):
        print(f'Su pelaje es {self.pelaje}\nSu color es {self.color}\nSu tamaño es {self.tamaño}\nSu nombre es {self.nombre}')
    def extraer(self):
        return self.pelaje
    def lista(self):
        return [self.color]

class Caballo_de_carga(Caballo):
    def __init__(self, pelaje, color, tamaño, nombre, montura):
        super().__init__(pelaje, color, tamaño, nombre)
        self.montura=montura