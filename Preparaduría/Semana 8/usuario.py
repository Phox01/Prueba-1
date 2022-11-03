class Usuario:
    def __init__(self, nombre, apellido, nacimiento, cédula, cuenta):
        self.nombre= nombre
        self.apellido=apellido
        self.nacimiento=nacimiento
        self.cédula=cédula
        self.cuenta=cuenta

    def factura(self):
        print('****Factura****')
        print(f'El nombre y el apellido del cliente es: {self.nombre}, {self.apellido}')
        print(f'Su fecha de nacimiento es: {self.nacimiento}')
        print(f'Su cédula es: {self.cédula}')
        print(f'El monto que debe es de: {self.cuenta} $')
