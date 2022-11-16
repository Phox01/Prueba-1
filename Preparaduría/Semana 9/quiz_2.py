#======================================================
# Nombre del Estudiante: Joseph Ruiz
# Carnet: 20221110023
#======================================================
# correo a enviar: ja.teixeira@correo.unimet.edu.ve
class Electrodoméstico:
    def __init__(self, codigo_producto, precio, marca, color):
        self.codigo_producto=codigo_producto
        self.precio=precio
        self.marca=marca
        self.color=color

    def mostrar(self):
        print()

class Lavadora(Electrodoméstico):
    def __init__(self, codigo_producto, precio, marca, color, capacidad):
        super().__init__(codigo_producto, precio, marca, color)
        self.capacidad=capacidad

class Horno_Microondas(Electrodoméstico):
    def __init__(self, codigo_producto, precio, marca, color, control):
        super().__init__(codigo_producto, precio, marca, color)
        self.control=control

class Nevera(Electrodoméstico):
    def __init__(self, codigo_producto, precio, marca, color, inc_congelador, compartimientos):
        super().__init__(codigo_producto, precio, marca, color)
        self.inc_congelador=inc_congelador
        self.compartimiento=compartimientos

class Licuadora(Electrodoméstico):
    def __init__(self, codigo_producto, precio, marca, color, material_vaso, velocidades):
        super().__init__(codigo_producto, precio, marca, color)
        self.material_vaso=material_vaso
        self.velocidades=velocidades