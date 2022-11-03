from objeto import Caballo
def main():
    
    x=input('Ingrese el color ')
    
    caballo1= Caballo('Rizo', x, 'Chiquito', 'Veloz')
    print(caballo1.pelaje)
    #Rizo
    
    print(caballo1.color)
    

    ##caballo1.print()
    ###Su pelaje es Rizo
    ### Su color es Marrón
    ### Su tamaño es Chiquito
    ### Su nombre es Veloz
##
    ##pelaje=caballo1.extraer()
    ##print(pelaje)
    ###Rizo
##
    ##lista=caballo1.lista()
##
    ##lista.append('rojo')
    ##print(lista)
    ###['Marrón', 'rojo']
    
main()