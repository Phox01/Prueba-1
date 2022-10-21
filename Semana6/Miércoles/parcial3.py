#======================================================
# Nombre del Estudiante: Joseph Ruiz
# Carnet: 20221110023
#======================================================
def main():
    
    menu = {
    'T':{
        'description':'Tradicional', 
    'price':8
    },
    'M': {
        'description':'Mixto', 
    'price':12
    },
    'S': {
        'description':'Samán', 
    'price':15
    }
}

    while True:
        data=request_data()
        option=taking_option(menu, data)
        break


def taking_option(menushawa, client):
    while True:
        print('Los Productos son: ')
        for key, value in menushawa.items():
            for inside_key, inside_value in value.items():
                print(f'{key} - {inside_value}')


        product=input('Ingrese una de las sig. opciones en mayúscula: T, M, S ----> ')
        if product!= 'T' and product!= 'M' and product!= 'S':
            print('Selecciona una de las sig. opciones: T, M, S')

        if product== 'M':
            client['mixto']+=1
        if product== 'S':
            client['saman']+=1
        if product== 'T':
            client['tradicional']+=1
        for key, value in client.items():
            if key=='mixto':
                print(f'Tiene {value} {key}')
            if key=='saman':
                print(f'Tiene {value} {key}')
            if key=='tradicional':
                print(f'Tiene {value} {key}')
        client['total']=client['mixto'] + client['saman'] + client['tradicional']
        print('Total es:', client['total'])
        if input("Quieres salir?\nPresiona Y para salir, otro para continuar: ") == "Y":
            break
    return product, client

def request_data():    
    while True:
        client={
            'nombre':input('Ingrese su nombre: '),
            'cédula':input('Ingrese su cédula: '),
            'correo electrónico':input('Ingrese su correo electrónico: '),
            'mixto':0,
            'saman':0,
            'tradicional':0,
            'total':0

        }
        for n in client.get('correo electrónico'):
            if n=='@':
                 break
        else:
            print('Tu correo no tiene ninguna @, por favor, coloca una arroba')
        for s in client.get('correo electrónico'):
            if s==' ':
                print('Tu correo tiene espacios, por favor, colocalo sin espacios')
                break
        if client.get('cédula').isnumeric==False:
            print('Tu cedula no son números, por favor, ingresala de nuevo')
        if s==' ' or n !='@' or client.get('cédula').isnumeric==False:
            print('Ingrese de nuevo los datos')
        break
        
    return client

main()