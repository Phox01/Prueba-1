class  Cliente:
    def __init__(self, nombre, edad, cedula, telefono, productos, monto):
        self.nombre=nombre
        self.edad=edad
        self.cedula=cedula
        self.telefono=telefono
        self.productos=productos
        self.monto=monto

    def recibo(self):
        print(f"Nombre={self.nombre} edad {self.edad}, cedula {self.cedula}, telefono {self.telefono}")



