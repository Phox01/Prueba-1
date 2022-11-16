##listas

def recursividad(lista, option, index=0):
    if option==lista[index]:
                return option
    if index==len(lista)-1:
        if option==lista[index]:
            return option
        else: 
            return
    if option==lista[index]:
        return option
    else:
        if index==len(lista)-1:
            if option==lista[index]:
                return option
        else: 
            return
    return recursividad(lista, option, index+1) 




def main():
    lista=["a", "b", "c", "d", "e"]
    option=input('Ingrese una letra')
    recursividad(lista, option)


main()
