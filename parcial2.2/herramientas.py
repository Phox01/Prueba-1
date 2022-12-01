class Herramienta:
    def __init__(self, marca, color, precio):
        self.marca=marca
        self.color=color
        self.precio=precio


class Plomería(Herramienta):
    def __init__(self, marca, color, precio, pulgadas, ajustable, mantenimiento):
        super().__init__(marca, color, precio)
        self.pulgadas=pulgadas
        self.ajustable=False
        self.mantenimiento=False
    def printing(self):
        if self.ajustable==True:
            self.ajustable="Sí"
        elif self.ajustable==False:
            self.ajustable="No"
        elif self.mantenimiento==True:
            self.mantenimiento="Sí"
        elif self.mantenimiento==False:
            self.mantenimiento="No"

        print(f"Marca {self.marca}, color {self.color}, precio {self.precio}, pulgadas{self.pulgadas}, es ajustable?{self.ajustable}, tiene mantenimiento? {self.mantenimiento}")


class Herrería(Herramienta):
    def __init__(self, marca, color, precio, calor):
        super().__init__(marca, color, precio)
        self.calor=calor
    def printing(self):

        print(f"Marca {self.marca}, color {self.color}, precio {self.precio}, grados que soporta {self.grados}")


    
class Carpintería(Herramienta):
    def __init__(self, marca, color, precio, garantia):
        super().__init__(marca, color, precio)
        self.garantia=garantia
    def printing(self):
        print(f"Marca {self.marca}, color {self.color}, precio {self.precio}, años de garantía {self.garantia}")