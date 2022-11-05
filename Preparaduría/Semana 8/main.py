from Alimento import Alimento
from Alimento import Comida
from Alimento import Bebida
from usuario import Usuario

def usuario():
    while True:
        try:
            nombre=input('Ingrese su nombre: --> ')
            apellido=input('Ingrese su apellido: --> ')
            nacimiento=input('Ingrese su fecha de nacimiento dividida por barras (así 1/01/01): --> ')
            cédula=int(input('Ingrese su cédula:--> '))
            cuenta=0
            cliente= Usuario(nombre, apellido, nacimiento, cédula, cuenta)
            if nombre.isnumeric== False and apellido.isnumeric==False:
                break
            else:
                print('Ingrese sus datos de nuevo')
        except SyntaxError and ValueError:
            print('Ingrese sus datos de nuevo')
    return cliente

def alimento(cliente, comida):
    
    while True:
        while True:
            
            nombre=input('Ingrese el nombre del alimento: --> ')
            precio=int(input('Ingrese el precio de ese alimento:--> '))
            comida_o_bebida=int(input('Ingrese 1 si es comida, 2 si es una bebida: -->  '))
            if comida_o_bebida==1:
                sabor=input('Ingrese si es salado o si es dulce: --> ')
                platillo=('¿Es un platillo principal o un postre?: --> ')
                x = Comida(nombre, precio, sabor, platillo)
                break
            elif comida_o_bebida==2:
                porcentaje=input('¿Qué porcentaje de alcohol tiene?: --> ')
                temperatura=input('¿Qué temperatura tiene?: --> ')
                x= Bebida(nombre, precio, porcentaje, temperatura)
                break
            else:
                print('Escribe un número entre 1 y 2')
        comida.append(x)
        cliente.cuenta+=x.precio

        if input('Quieres salir? Escribe Y si quieres salir: --> ')=='Y':
            break
    return comida

def dictionary(comida, cliente):
    almacén={'Comidas':comida, 'Cliente':cliente}
    for value, key in almacén.items():
        if value== 'Comidas':
            for i in key:
                print(f'Las comidas son: {i.nombre}')
        elif key==cliente:
            print(f'El usuario es: {key.nombre}')
    return almacén

def factura1(cliente):
    cliente.factura()
    return

def main():
    comida=[]
    cliente=usuario()
    alimento(cliente, comida)
    dictionary(comida, cliente)
    factura1(cliente)


main()


        
    