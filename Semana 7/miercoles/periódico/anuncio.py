class Anuncio:
    def __init__(self, cliente, sección, título, cuerpo):
        self.cliente=cliente
        self.sección=sección
        self.título=título
        self.cuerpo=cuerpo

class Anuncio_Clasificado(Anuncio):
    def __init__(self, cliente, sección, título, cuerpo, precio, fechap, días):
        super().__init__(cliente, sección, título, cuerpo)
        self.precio=precio
        self.fecha_de_publicación= fechap
        self.cantidad_de_días=días

class Anuncio_Vehículo(Anuncio_Clasificado):
    def __init__(self, cliente, sección, título, cuerpo, precio, fechap, días, marca, modelo, año, color, kilometraje):
        super().__init__(cliente, sección, título, cuerpo, precio, fechap, días)
        self.marca=marca
        self.modelo=modelo
        self.año=año
        self.color=color
        self.kilometraje=kilometraje

class Anuncio_Vivienda(Anuncio_Clasificado):
    def __init__(self, cliente, sección, título, cuerpo, precio, fechap, días, m2, cuartos, baños, puestos, leyP):
        super().__init__(cliente, sección, título, cuerpo, precio, fechap, días)
        self.m2=m2
        self.cantidad_de_cuartos=cuartos
        self.cantidad_de_baños= baños
        self.cantidad_de_puestos= puestos
        self.ley_de_política=leyP
