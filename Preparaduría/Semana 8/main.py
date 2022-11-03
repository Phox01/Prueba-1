from Alimento import Alimento
from Alimento import Comida
from Alimento import Bebida
from usuario import Usuario

def usuario(cliente):
    try:
        nombre=input('Ingrese su nombre ')
        apellido=input('Ingrese su apellido ')
        nacimiento=int(input('Ingrese su fecha de nacimiento '))
        cédula=int(input('Ingrese su cédula '))
        cuenta=0
        cliente= Usuario(nombre, apellido, nacimiento, cédula, cuenta)
    except SyntaxError:
        print('ingrese sus datos de nuevo ')
    return cliente

def alimento(cliente, comida):
    
    while True:
        comida_o_bebida=int(input('Ingrese 1 si es comida, 2 si es una bebida '))
        nombre=input('Ingrese el nombre del alimento ')
        precio=int(input('Ingrese el precio de ese alimento '))
        if comida_o_bebida==1:
            sabor=input('Ingrese si es salado o si es dulce ')
            platillo=('¿Es un platillo principal o un postre? ')
            x = Comida(nombre, precio, sabor, platillo)
        elif comida_o_bebida==2:
            porcentaje=input('¿Qué porcentaje de alcohol tiene? ')
            temperatura=input('¿Qué porcentaje de alcohol tiene? ')
            x= Bebida(nombre, precio, porcentaje, temperatura)
        else:
            print('Escribe un número entre 1 y 2 ')
        comida.append(x)
        Usuario.cuenta+=precio

        if input('Quieres salir? Escribe Y si quieres salir ')=='Y':
            break
    return comida

def dictionary(comida, cliente, almacén):
    almacén={'Comidas':comida, 'Cliente':cliente}
    return almacén

def factura1(cliente):
    cliente.factura()
    return

def main():
    Almacén={}
    Cliente=0
    comida=[]
    usuario(Cliente)
    alimento(Cliente, comida)
    dictionary(comida, Cliente, Almacén)
    factura1(Cliente)


main()


        
    