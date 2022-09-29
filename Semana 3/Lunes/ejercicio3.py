##Triangulo
number=input('Escribe un número: ')
num=1
if number.isnumeric:
    number=int(number)
    for number_for in range (1, number+1,2):
        aux= number_for
        while aux >=1:
            if aux ==1:
                print(aux)
            else:
                print (aux , end=' ')
            aux-=2
else:
    print('Invalid number')