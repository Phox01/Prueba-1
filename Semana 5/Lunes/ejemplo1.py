def print_welcome():
    print('*****Welcome*****')

def get_option(studies):
    for key, value in studies.items():
        for key_interno, value_interno in value.items():
            print(f'{key}-{value_interno}', end= '')
            print('')
            return input('Please, enter an option:')

        
def get_net_amount(client, discount, studies):
    return studies.get(client.get("study")).get("price") - discount

def get_client_data(study):
    client={
        'id':input('Enter the client id: '),
        'age':input('Enter the client age: '),
        'gender':input('Enter the client gender: m or f'),
        'study':study
    }
    return client

def get_discounts(client, studies, client_number):
    discount=0
    if client.get('gender')== 'f' and int(client.get('age'))>55:
        discount += studies.get(client.get('study')).get('price') *0.25
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
    total_discounts=0
    total_net_amount=0
    total_net_amountU=0
    total_net_amountR=0
    total_net_amountT=0
    print_welcome()
    while True:
        option= get_option(studies_dict)
        client= get_client_data(option)
        clients.append(client)
        discount= get_discounts(client, studies_dict,len(client))
        print(discount)
        print_invoice(client, studies_dict, discount)
        total_discounts += discount
        total = get_net_amount(client,discount,studies_dict)
        total_net_amount += total
        if input("Do you want to continue Y-Yes or N-No") == "Y":
            break

def print_invoice(client, studies, net_amount):
    print('*****Receipt*****')
    print('id card:', client.get('id'))
    print('Age:', client.get('age'))
    print('gender:', client.get('gender'))
    print('study:', studies.get(client.get('study')).get('description'))
    print('net amount:', net_amount)
    client['total']=net_amount
    print('Net amount:', net_amount)

main()