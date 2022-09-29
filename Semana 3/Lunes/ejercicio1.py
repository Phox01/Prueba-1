##Impares
number=(input('Ingrese un número '))
aux=1
if number.isnumeric():
    number=int(number)
    while aux <= number:
        if aux+2>=number:
            print(aux)
        else:
            print(aux, end=',')
        aux+=2
else: 
    print('Ingrese un número')