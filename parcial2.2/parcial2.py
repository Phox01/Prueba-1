from cliente import Cliente
from herramientas import Herramienta, Carpintería, Plomería, Herrería

def get_client_data():
    while True:
        nombre=input("Por favor, ingrese su nombre: ")
        edad=input("Por favor, ingrese su edad: ")
        cedula=input("Por favor, ingrese su cédula: ")
        telefono=input("Por favor, ingrese su telefono: ")
        data=[nombre, edad, cedula, telefono]
        if nombre.isnumeric()==True or edad.isnumeric()==False or cedula.isnumeric()==False or telefono.isnumeric()==False:
            print("Vuelve a ingresar los datos, por favor")
        else:
            #buying(productos, your_products,)
            
            break
    return data

def buying(productos, data, your_products, clients):
    while True:
        tipo=input("Ingrese el tipo de producto que quieres comprar:\n1-Plomería\n2-Herrería\n3-Carpintería\n")
        if tipo.isnumeric()==False or int(tipo)>3 or int(tipo)<1:
            print("Recuerde que debe ser en número y del 1 al 3")
        else:
            marca=input("Ingrese la marca del producto: ")
            color=input("Ingrese el color del producto: ")
            if marca.isnumeric()==True or color.isnumeric==True:
                print("Vuelva a ingresar los datos, recuerda que no deben ser números")
            else:
                if int(tipo)==1:
                    while True:
                        pulgadas=input("Ingrese las pulgadas del producto: ")
                        ajustable=input("¿Es ajustable?\n1-Sí\n2-No\n")
                        mantenimiento=input("¿Requiere de mantenimiento?\n1-Sí\n2-No\n")
                        if pulgadas.isnumeric==False or ajustable.isnumeric==False or mantenimiento.isnumeric==False:
                            print("Vuelva a ingresar los datos, recuerda que deben ser números")
                        else:
                            if ajustable==1:
                                ajustable=True
                            elif ajustable==2:
                                ajustable==False
                            elif mantenimiento==1:
                                mantenimiento=True
                            elif mantenimiento==2:
                                mantenimiento=False

                            producto=Plomería(marca, color, 50, pulgadas, ajustable, mantenimiento)
                            productos.append(producto)
                            your_products.append(producto)
                            break

                elif int(tipo)==2:
                    while True:
                        grados=input("Cuantos grados soporta?")
                        if grados.isnumeric==False:
                            print("Recuerda que deben ser números")
                        else:
                            producto=Herrería(marca, color, 40, grados)
                            productos.append(producto)
                            your_products.append(producto)
                            break

                elif int(tipo)==3:
                    while True:
                        añosgarantía=input("Cuantos años de garantía tiene?")
                        if añosgarantía.isnumeric==False:
                            print("Recuerda que deben ser números")
                        else:
                            producto=Herrería(marca, color, 30, añosgarantía)
                            productos.append(producto)
                            your_products.append(producto)
                            break
                ##productos.append(producto)
                
                
                if input("Quiere seguir comprando? Escribe Y para continuar, otro para salir")=="Y":
                    continue

                else:
                    client=Cliente(data[0], data[1], data[2], data[3], your_products, monto=0)
                    recibo(client)
                    ##abundante(client, i=0)
                    
                    ##if primo(client)==True:
                    ##    client.monto-=client.monto*0.1
                    ##    print(f"Su nuevo monto es de {client.monto}")
                    ##else:
                    ##    continue
                    clients.append(client)
                    break

    return clients, productos

def recibo(client):
    client.recibo()
    for x in client.productos:
        x.printing()
        client.monto+=x.precio
    print(f"Su monto final es {client.monto}")
    return client

def abundante(client, i):
    i=1
    counting=0
    if int(client.edad)%i==0:
        counting+=i
        if counting>int(client.edad):
            print("Tu edad es un numero abundante")
        else:
            abundante(client, i+1)
        
    elif i>client:
        print("Tu número no es abundante")
        
def primo(client):
    n=1
    count=0
    while True:
        if int(client.edad)%n==0:
            count+=1
            
        elif n>int(client.edad):
            print("Su número no es primo")
            is_primo=False
            break
        elif count==2:
            print("Su número es primo")
            is_primo=True
            break
    return is_primo
    

                




def main():
    clients=[]
    productos=[]
    your_products=[]
    plomero=0
    carpintero=0
    herrero=0
    while True:
        selection=input("ingrese 1 para registrarte como cliente y comprar, 2 para salir")
        if int(selection)==1:
            buying(productos, get_client_data(), your_products, clients)
        elif int(selection)==2:
            break
    print(f"Compraron {len(clients)} clientes")
    for x in productos:
        if type(x)==Plomería:
            plomero+=1
        elif type(x)==Herrería:
            herrero+=1
        elif type(x)==Carpintería:
            carpintero+=1
    print(f"Fueron {plomero} cantidad de productos de plomería, {herrero} cantidad de productos de herrería y {carpintero} cantidad de productos de carpintería")
        


    
main()