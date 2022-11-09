import random
from personas import Redactor, article
from articulo import Artículo

def Redactores():
    redactores=[Redactor('Joseph', 1, 'Deportes'),
    Redactor('Andrea', 2, 'Casas'),
    Redactor('Gabs', 3, 'Social')]
    x=random.choice(redactores)
    print(f'El redactor seleccionado para el trabajo es: {x}')
    
    return redactores, x

def who_redacts():
    print('El ')