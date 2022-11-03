passwords=[]
mayus=False
minus=False
number=False
print('Por favor, ingresa una contraseña:')
while True: 
    password=input()
    if len(password)<8:
        print('Ingrese una contraseña de más de 8 carácteres')
        continue
    for items in password:
        if items.isupper():
            mayus=True
            continue
        if items.islower():
            minus=True
            continue
        if items.isnumeric():
            number=True
            continue
    if mayus==False or minus==False:
        print('Ingrese una contraseña con al menos una minúscula y una mayúscula')
        continue
    if number==False:
        print('Ingrese una contraseña con al menos un número')
        continue
    break
print(f'Su contraseña es: {password}')
passwords.append:password