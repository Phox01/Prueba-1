def print_welcome():
    print('*****Welcome*****')

def get_option(studies):
    while True:
        for key, value in studies.items():
            for key_interno, value_interno in value.items():
                print(f'{key}-{value_interno}', end= '')
                print('')
        study=input('Please, enter an option in uppercase (U, T or R): ')
        if study!= 'U' and study!= 'T' and study!= 'R':
            print('That option is not valid, please enter one of these options: U, T, R')
        break
    return study

def get_net_amount(client, discount, studies):
    return studies.get(client.get("study")).get("price") - discount

def get_client_data(study):
    client={
        'id':input('Enter the client id: '),
        'age':input('Enter the client age: '),
        'gender':input('Enter the client gender (m or f): '),
        'study':study
    }
    return client

def get_discounts(client, studies, client_number):
    discount=0
    if client.get('gender')== 'f' and int(client.get('age'))>55:
        discount += studies.get(client.get('study')).get('price') *0.25
        #Ejemplo para entrar en diccionario dentro de diccionario
        # res = test_dict.get('Gfg', {}).get('is')
    
    elif client.get('gender')== 'm' and int(client.get('age'))>65:
        discount += studies.get(client.get('study')).get('price') *0.25
    if client_number %2 != 0:
        discount += studies.get(client.get('study')).get('price') *0.02
    return discount

def main():
    studies_dict = {
    'U':{
        'description':'ultrasonido', 
    'price':8900
    },
    'T': {
        'description':'tomografía', 
    'price':12640
    },
    'R': {
        'description':'resonancia', 
    'price':15600
    }
}   
    clients=[]
    clientsU=[]
    clientsR=[]
    clientsT=[]
    total_discounts=0
    total_net_amount=0

    print_welcome()
    while True:
        option= get_option(studies_dict)
        client= get_client_data(option)
        clients.append(client)
        if client.get('study')=='U':
            clientsU.append(client)
        if client.get('study')=='R':
            clientsR.append(client)
        if client.get('study')=='T':
            clientsT.append(client)
        discount= get_discounts(client, studies_dict, clients.index(client))
        total = get_net_amount(client,discount,studies_dict)
        print(discount)
        print_invoice(client, studies_dict, discount, total)
        total_discounts += discount
        total_net_amount += total
        if input("Do you want to quit?\nPress Y to quit, other to continue: ") == "Y":
            break
    countings(clientsU, clientsR, clientsT, total_discounts, total_net_amount, clients)

def print_invoice(client, studies, net_amount, total):
    print('**************Receipt*****************')
    print('id card:', client.get('id'))
    print('Age:', client.get('age'))
    print('gender:', client.get('gender'))
    print('study:', studies.get(client.get('study')).get('description'))
    print('Price with discount:', total)
    client['total']=total
    print('Discount:', net_amount)

def countings(clientsU, clientsR, clientsT, total_discounts, total_net_amount, clients):
    print(f'The amount of clients in Ultrasonido are:  {len(clientsU)}\nThe amount of clients in Resonancia are:  {len(clientsR)}\nThe amount of clients in Tomografía are:  {len(clientsT)}')
    print(f'The total of net amount payed is: {total_net_amount}\nThe total of discounts are: {total_discounts}')
    print(f'The average of net amount payed is: {total_net_amount/len(clients)}')
        

main()