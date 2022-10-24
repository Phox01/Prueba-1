def main():
    products_dict = {
    'Q':{
        'description':'quimico', 
    'price':1000
    },
    'F': {
        'description':'farmacéutico', 
    'price':2500
    },
    'B': {
        'description':'biológico', 
    'price':4000
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
        option=taking_option(products_dict)
        data=request_data(option)
        theiva=get_iva(products_dict, data)
        priceis= real_amount(products_dict, theiva, data)
        get_receipt(data, theiva, priceis, products_dict)
        clients.append(data)
        if data.get('product')=='Q':
            clientsQ.append(data)
        if data.get('product')=='B':
            clientsB.append(data)
        if data.get('product')=='F':
            clientsF.append(data)
        total_price+=priceis
        if data.get('payment_method')=='R':
            iva_per_paymentR+=theiva
        if data.get('payment_method')=='C':
            iva_per_paymentC+=theiva
        if input("Do you want to quit?\nPress Y to quit, other to continue: ") == "Y":
            break
    
    for data in clients:
        for key, value in data.items():
            if key=='real amount':
                if value>biggest_sale:
                    biggest_sale=value
    last_receipt(clients, iva_per_paymentR, iva_per_paymentC, total_price)
    for data in clients:
        for key, value in data.items():
            if key=='real amount':
                if value==biggest_sale:
                    print('The client with the biggest price to pay has this rif:', data.get('rif'))


    

def taking_option(productsdict):
    while True:
        print('The products are: ')
        for key, value in productsdict.items():
            for inside_key, inside_value in value.items():
                print(f'{key} - {inside_value}')
        product=input('Please, enter an option in uppercase (Q, F or B): ')
        if product!= 'Q' and product!= 'F' and product!= 'B':
            print('That option is not valid, please enter one of these options: Q, F or B')
        break
    return product

def request_data(product):    
    while True:
        client={
            'rif':input('Please, enter your rif: '),
            'payment_method':input('Please, enter the method of payment used: Credito (R) or Contado (C) '),
            'product':product
        }
        if client.get('payment_method')!= 'R' and client.get('payment_method')!= 'C':
            print('That option is not valid, please enter one of these options: R or C')
        break
    return client

def get_iva(productsdict, client):
    iva=0
    if client.get('product')=='Q':
        iva+= productsdict.get(client.get('product')).get('price')*0.12
    if client.get('product')=='B':
        iva+= productsdict.get(client.get('product')).get('price')*0.15
    
    return iva

def real_amount(productsdict, iva, client):
    return productsdict.get(client.get('product')).get('price')-iva

def get_receipt(client, iva, real_amount_is, productsdict):
    print('*****Receipt*****')
    print('rif:', client['rif'])
    print('price:', productsdict[client[('product')]].get('price'))
    print(f'Iva is: {iva}')
    print('----------------------')
    print(f'Real price is: {real_amount_is}')
    client['real amount']=real_amount_is

def last_receipt(clients, iva_per_paymentR, iva_per_paymentC, total_price):
    print('******Summary******')
    print(f'The amount of clients is: {len(clients)}')
    print(f'The total iva of credit payment is: {iva_per_paymentR}')
    print(f'The total iva of contado payment is: {iva_per_paymentC}')
    print(f'The total payment is: {total_price}')

main()