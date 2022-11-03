class Persona:
    def __init__(self, nombre, cédula):
        self.nombre=nombre
        self.cédula=cédula

class Redactor(Persona):
    def __init__(self, nombre, cédula, sección):
        super().__init__(nombre, cédula)
        self.sección=sección

class Jefe(Redactor):
    def __init__(self, nombre, cédula, sección, grupo):
        super().__init__(nombre, cédula, sección)
        self.grupo=grupo

class Sección:
    def __init__(self, jefe, grupo):
        self.jefe=jefe
        self.grupo=grupo

class Artículo:
    def __init__(self, título, resumen, cuerpo, imágenes, fechap, fechac, Redactor):
        self.título= título
        self.resumen= resumen
        self.cuerpo= cuerpo
        self.imágenes= imágenes
        self.fechap= fechap
        self.fechac= fechac
        self.redactor= Redactor

class Cliente(Persona):
    def __init__(self, nombre, cédula):
        super().__init__(nombre, cédula)