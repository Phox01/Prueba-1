from clases import Recordatorio
def option1():
    nombre=input('Ingresa el nombre del recordatorio: ')
    hora=input('Ingresa la hora a la que quieres que te recuerde: ')
    fecha=input('Ingresa la fecha en la que saldrá el recordatorio: ')
    tarea=input('Ingresa la tarea del recordatorio: ')
    reminder= Recordatorio(nombre, hora, fecha, tarea)
    return reminder

def option4(recordatorios):
    print('Tus recordatorios guardados son')
    for i in recordatorios:
        print(i.nombre)

def option2(recordatorios):
    print('Tus recordatorios son')
    for i in recordatorios:
        print(i.nombre)
    delete=input('Cuál quieres eliminar?')
    recordatorios.remove(delete)
    return recordatorios

def option3(recordatorios):
    while True:
        print('Tus recordatorios son')
        for i in recordatorios:
            print(i.nombre)

        edit=input('Cuál quieres editar? ')
        for i in recordatorios:
            if i.nombre== edit:
                property_edited=int(input('Qué quieres cambiar?\n1-nombre\n2-hora\n3-fecha\n4-tarea\n' ))
                if property_edited==1:
                    i.nombre=input('Coloque la modificación: ')
                elif property_edited==2:
                    i.hora=input('Coloque la modificación: ')
                elif property_edited==3:
                    i.fecha=input('Coloque la modificación: ')
                elif property_edited==4:
                    i.tarea=input('Coloque la modificación: ')
                else:
                    print('Esa opción no está en la lista de recordatorios')
            else:
                print('Esa opción no está en la lista de recordatorios')
        if input('Quiere continuar? Escriba no para detenerse: ')=='no':
            break
    return recordatorios

def main():
    recordatorios=[]
    while True: 
        try:
            option=int(input('Ingresa una de las siguientes opciones: \n1 para ingresar un recordatorio\n2 para eliminar un recordatorio\n3 para modificar un recordatorio\n4 para mostrar la lista de recordatorios\n'))
            print('====================')
            if option==1:
                reminder=option1()
                recordatorios.append(reminder)
                print('====================')
            elif option==2:
                option2(recordatorios)
                print('====================')
            elif option==3:
                option3(recordatorios)
                print('====================')
            elif option==4:
                option4(recordatorios)
                print('====================')

        except SyntaxError and ValueError:
            print('Recuerda que deben ser opciones numéricas del 1 al 5')

main()

