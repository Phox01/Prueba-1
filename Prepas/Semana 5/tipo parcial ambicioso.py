#Numero ambicioso
def ambicioso():
    while True:
        number1=int(input('Por favor, ingrese un número: '))
        n=1
        count=0
        counting2=0
        number=number1
        while True:
            if number%n==0:
                count+=n
                counting2=count
            if number==count:
                print(f'El número {number1} es ambicioso')
                break
            if n==number-1 and count!=1:
                number=counting2
                count=0
                n=0
            n+=1
            if n==number:
                print(f'El número {number1} no es ambicioso')
                break

        if input('Pulse Y para salir, otro caracter para continuar: ')=='Y':
            break
ambicioso()

