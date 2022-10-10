##TriangulitoO
number=input('Escribe un número: ')
if number.isnumeric:
    number=int(number)
    for ast in range (1, number+1):
        print('*'*ast)