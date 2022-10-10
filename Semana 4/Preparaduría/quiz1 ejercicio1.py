#======================================================
# Nombre del Estudiante: Joseph Ruiz
# Carnet: 20221110023
#======================================================
# correo a enviar: ja.teixeira@correo.unimet.edu.ve
nro= 1
penta = [[45,78,65],[12,35,70],[51,3,105],[22,12,85]]
for list in penta:
    for numbers in list:
        print(numbers)
        while True:
            nro_pentagonal= int(((3*(nro**2))-nro)/2)
            if numbers==nro_pentagonal:
                print(f'El número {numbers} es pentagonal')
                break
            nro+=1
            if nro_pentagonal>numbers:
                print(f'El número {numbers} no es pentagonal')
                nro=1
                break
            

