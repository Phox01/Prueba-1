##Escribir un programa que cree un diccionario vacío 
# y lo vaya llenado con información sobre una persona 
#(por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) 
# que se le pida al usuario. Cada vez que se añada un nuevo dato debe
#  imprimirse el contenido del diccionario.

info_personal={'Nombre':0, 'Edad':0,'Sexo':0, 'Telefono':0}
info_personal['Nombre']=input('Escribe tu nombre: ')
info_personal['Edad']=input('Escribe tu edad: ')
info_personal['Telefono']=input('Escribe tu telefono: ')
for elementos, key in info_personal.items():
    print('Tu {} es: {}'.format(elementos, key))
