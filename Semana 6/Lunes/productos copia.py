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
    
    while True:
        taking_option(products_dict)
        request_data(taking_option)
        get_iva(products_dict, request_data)
        #priceis= real_amount(products_dict, ivas, client)
        get_receipt(request_data, get_iva)
        ##client.append(request_data)
        if input("Do you want to quit?\nPress Y to quit, other to continue: ") == "Y":
            break
    
def taking_option(products_dict):
    while True:
        print('The products are: ')
        for key, value in products_dict.items():
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
            "rif":input('Please, enter your rif: '),
            ##code_product=input('Please, enter your product code in uppercase (Q, F or B): ')
            "payment_method":input('Please, enter the method of payment used: Credito (R) or Contado (C) '),
            "product":product
        }
        if client.get('payment_method')!= 'R' and client.get('payment_method')!= 'C':
            print('That option is not valid, please enter one of these options: R or C')
        break
    return client

def get_iva(products_dict, client):
    iva=0
    if client.get('product')=='Q':
        iva+= products_dict.get(client.get('product')).get('price')*0.12
    if client.get('product')=='B':
        iva+= products_dict.get(client.get('product')).get('price')*0.12
    #real_amount_is= productsdict.get(client.get('product')).get('price')-iva
    return iva

##def real_amount(productsdict, iva, client):
##    
##    return real_amount_is

def get_receipt(client, iva):
    print('*****Receipt*****')
    print(f'The code of the client is rif', client.get('rif'))
    print(f'iva is: {iva}')
    # client.get('payment_method'), product, iva)

main()