#Ejercicio largo de la clase. Restaurant Italiano
option= input('Por favor, escoge una opcion \n1:Vegetariana \n2:No vegetariana \n')
if option=='1':
    ingr1= input('Los ingredientes disponibles son \n1:Pimenton \n2:Tofu \n')
    if ingr1== '1':
        ingr1='Pimenton'
    elif ingr1== '2':
        ingr1= 'Tofu'
    else:
        print('Escoja un numero del 1 al 2')
    print(f'La pizza es vegetariana y tiene: Queso, Salsa y {ingr1}')
elif option=='2':
    ingr1= input('Los ingredientes disponibles son \n1:Peperonni \n2:Jamon \n3:Salmon \n')
    if ingr1== '1':
        ingr1='Peperonni'
    elif ingr1== '2':
        ingr1== 'Jamon'
    elif ingr1== '3':
        ingr1== 'Salmon'
    else:
        print('Escoja un numero del 1 al 3')
    print(f'La pizza es no vegetariana y tiene: queso, salsa y {ingr1}')
else:
    print('Escoja un numero del 1 al 2')
