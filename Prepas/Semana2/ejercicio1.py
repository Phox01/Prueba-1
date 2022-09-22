##Decir la posición de cada letra en una lista
lista='Bienvenidos a la prepa de algoritmos'
cont=0
for i in lista:
    if i=='a':
        print(f'hay una a en el punto {cont}')
    if i=='p':
        print(f'hay una p en el punto {cont}')
    cont+=1