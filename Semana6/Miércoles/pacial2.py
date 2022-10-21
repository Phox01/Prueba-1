#======================================================
# Nombre del Estudiante: Joseph Ruiz
# Carnet: 20221110023
#======================================================

def narcisista():
    while True:
        number=int(input('Por favor, ingrese un número: '))
        str(number)
        count=[]
        counting=0
        for n in str(number):
            count.append(n)
            potencia=len(str(number))
        for numbers in count:
            counting+=int(numbers)**potencia
        if counting==number:
            print(f'El número {number} es narcisista')
            break
        if counting>number:
            print(f'El número {number} no es narcisista')
            break

narcisista()