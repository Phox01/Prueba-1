#284 y 220
s1=1
s2=1
cont=2
n1=int(input('Por favor, ingrese el primer número: '))
n2=int(input('Por favor, ingrese el segundo número: '))

while True:
    resto=n1%cont
    if resto==0:
        s1+=cont
    cont+=1
    if cont> (n1/2):
        break
if s1==n2:
    cont=2
    while True:
        resto= n2%cont
        if resto==0:
            s2+=cont
        cont+=1
        if cont>(n2/2):
            break
    if s2==n1:
        print(f'los números {n1} y {n2} son **AMIGOSS**')
    else:
        print(f'los números {n1} y {n2} no son **AMIGOSS**')
else:
    print(f'los números {n1} y {n2} no son **AMIGOSS**')

##los numeros amigos son los que la suma de los divisores de uno equivalga al otro,
## y la suma de los divisores del otro equivalga al primero