##Decir la posición de cada letra en una lista
lista='Bienvenidos a la prepa de algoritmos'
count=0
print(len(lista))
for i in lista:
    if i=='a':
        if lista[count+1]== 'l':
            print(f'hay una al en el punto {count} y {count+1}')
    count+=1