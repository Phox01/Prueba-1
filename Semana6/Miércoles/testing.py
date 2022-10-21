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
    clients=[]
    clientsQ=[]
    clientsB=[]
    clientsF=[]
    total_price=0
    iva_per_paymentC=0
    iva_per_paymentR=0
    biggest_sale=0
    while True:
        data=request_data()
        #option=taking_option(menu)
        break

def request_data():    
    while True:
        client={
            'nombre':input('Ingrese su nombre: '),
            'cédula':input('Ingrese su cédula: '),
            'correo electrónico':input('Ingrese su correo electrónico: ')
        }
        cedula_number=client.get('cédula')
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