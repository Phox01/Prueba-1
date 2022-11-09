import random
from articulo import Artículo

class Persona:
    def __init__(self, nombre, cédula):
        self.nombre=nombre
        self.cédula=cédula

class Redactor(Persona):
    def __init__(self, nombre, cédula, sección):
        super().__init__(nombre, cédula)
        self.sección=sección
    
    def Redacción(self):
        print('Para comenzar a redactar, se debe introducir: ')
        article= Artículo(
            input('título: '),
            self.nombre
            #input('resumen: '),
            #input('cuerpo: '),
            #input('imágenes: '),
            #input('fecha de publicación: '), 
            #input('fecha de creación: '),
            #input('redactor: ')
        )
        print(f'El artículo redactado tiene por título: {article.título}')
        return article

class Jefe(Redactor):
    def __init__(self, nombre, cédula, sección, grupo):
        super().__init__(nombre, cédula, sección)
        self.grupo=grupo

    def Decisión(self, article):
        if random.random>0.5:
            print(f'El artículo {article} fue aprobado 👍')
            article.fechap=True
            
        else:
            print(f'El artículo {article} no fue aprobado 👎')
            article.fechap=False
        return article

class Cliente(Persona):
    def __init__(self, nombre, cédula):
        super().__init__(nombre, cédula)

