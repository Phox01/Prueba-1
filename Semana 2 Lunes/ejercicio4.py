numero1= float(input ('Escribe un número '))
numero2= float(input ('Escribe otro número '))
if numero2==0:
    print('Error')
else:
    d= float (numero1/numero2)
    print(f'Estos dos números serán divididos: {numero1}/{numero2}')
    print(f'La division da {d}')
