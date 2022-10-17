#Numero ambicioso
def ambicioso():
    while True:
        number=int(input('Por favor, ingrese un número: '))
        n=1
        count=0
        while True:
            if number%n==0:
                count+=n
            if number==count:
                print(f'El número {number} es ambicioso')
                break
            n+=1
            if n>number:
                print(f'El número {number} no es ambicioso')
                break
        if input('Pulse Y para salir, otro caracter para continuar: ')=='Y':
            break
ambicioso()

