def calculo_de_primos(counting, number):
    primo=1
    n=1
    count=0
    while True:
        if primo%n==0:
            count+=1
        n+=1
        if n>primo:
            n=1
            if count==2:
                counting.append(primo)
            primo+=1
            count=0            
        if primo>number:
            break
    return counting
def is_this_the_number(counting, counting2, number):
    for primo in counting:
        for primos in counting2:
            is_this_the_number=primo*primos
            if is_this_the_number==number:
                print(f'El número {number} es el producto entre {primo} y {primos}')
                break
            if primo==counting[-1] and primos==counting2[-1]:
                print(f'El número {number} no es el producto entre sus primos divisores')
                break
        else: 
            continue
        break
def primo():
    while True:
        number=int(input('Por favor, ingrese un número: '))
        calculo_de_primos(counting, number)
        counting=[1]
        counting2=counting.copy()
        is_this_the_number(counting, counting2, number)
        #última posición de listas:
        #producto_últimos_numeros=counting[-1]*counting2[-1]
        if input('Pulse Y para salir, otro caracter para continuar: ')=='Y':
            break
primo()