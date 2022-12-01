import requests
import json
from Equipo import Equipo
from Estadio import Estadio
from Partido import Partido
from Restaurants import Restaurant
from Products import Product, Beverage, Food
#from prueba import printings
from Client import Client
from Ticket import Ticket
import random
from itertools import permutations

###Añadir más comentarios, más propiedades de los objetos y entrelazarlos

def Team_Converter(teams_data, equipos):
    ##Convertir los equipos en objetos
    for x in teams_data:
        equipos.append(Equipo(x["name"], x["fifa_code"], x["group"], x["id"]))
    return equipos

def Products_Converter(stadium_data, products):
    ##Convertir los productos en objetos
    for x in stadium_data:
        for y in x["restaurants"]:
            for z in y["products"]:
                if z["type"]=="beverages":
                    products.append(Beverage(z["name"], z["quantity"], z["price"]*0.16+z["price"], z["type"], z["adicional"], y["name"], 0))
                elif z["type"]=="food":
                    products.append(Food(z["name"], z["quantity"], z["price"]*0.16+z["price"], z["type"], z["adicional"], y["name"], 0))
    return products

def Restaurants_Converter(stadium_data, restaurants, products):
    products_list=[] ##Lista para guardar los nombres de cada producto, como referencia
    ##para no meter un objeto completo dentro de otro objeto

    for x in stadium_data:
        for y in x["restaurants"]:
            last=y["products"][-1]["name"] ##"last" es una variable para saber cuál
            ##es el último producto de un restaurant
            for z in y["products"]:
                for w in products:
                    if z["name"]==w.name:
                        products_list.append(w.name)
                        break
                if w.name==last: ##si "last" es igual al nombre del producto actual,
                    ##guarda la lista dentro del objeto
                    restaurants.append(Restaurant(y["name"], products_list))
                    products_list=[]
                    break
                    

    return restaurants, products_list

def Stadium_Converter(stadium_data, estadios, restaurants):
    ##Convertir los estadios en objetos
    restaurant_list=[]##Lista para guardar los nombres de cada producto, como referencia
    ##para no meter un objeto completo dentro de otro objeto
    for y in stadium_data:
        for z in y["restaurants"]:
            last=y["restaurants"][-1]["name"]##"last" es una variable para saber cuál
            ##es el último producto de un restaurant
            for x in restaurants:
                if x.name==z["name"]:
                    restaurant_list.append(x.name)
                    break
            if x.name==last:##si "last" es igual al nombre del producto actual,
            ##guarda la lista dentro del objeto
                estadios.append(Estadio(y["name"], y["location"], y["id"], y["capacity"], restaurant_list, seats=[], occupied_seats=[]))
                restaurant_list=[]
                break
#    for i in estadios:
#       print(i.name)
    return estadios

def Game_Converter(games_data, juegos, equipos, estadios):
    ##Convertir los juegos en objetos
    for z in games_data:
        for y in equipos:
            if z["home_team"]==y.name:
                lteam=y.name ##para no guardar el objeto completo
            elif z["away_team"]==y.name:
                vteam=y.name ##para no guardar el objeto completo
        for x in estadios:
            if z["stadium_id"]==x.id:
                stadium=x.name ##para no guardar el objeto completo
        date_hour=z["date"].split(" ")
        date=date_hour[0]
        hour=date_hour[1]
        
        juegos.append(Partido(lteam, vteam, date, hour, stadium, z["id"], 0))
#    for i in juegos:
#        print(i.vteam)
    return juegos

def Búsqueda_por_equipos(juegos, equipos):
    #Búsqueda de partidos por equipo
    team=input("Escribe un equipo, en ingles, el cual quieras ver sus partidos: ")
    i=0 ##contador para saber si encontró o no el equipo que juega
    for x in equipos:
        if x.name.casefold()==team.casefold():
            print(f"El equipo {x.name} jugará en los siguientes partidos:")
            for y in juegos:
                if y.lteam==x.name:
                    print(f"Partido del {y.date} a las {y.hour} en el estadio {y.estadio}, contra {y.vteam}")
                    i+=1
                elif y.vteam==x.name:
                    print(f"Partido del {y.date} a las {y.hour} en el estadio {y.estadio}, contra {y.lteam}")
                    i+=1
    if i==0:
        print("No hubo ningún partido con ese equipo")
    print("---------------------------------------------------")

def Búsqueda_por_estadios(juegos, estadios):
    #Búsqueda de partidos por equipo
    i=0
    estadio=input("Escribe un estadio el cual quieras ver sus partidos: ")
    for x in estadios:
        if x.name.casefold()==estadio.casefold():
            print(f"El estadio {x.name} se usará en los siguientes partidos:")
            for y in juegos:
                if y.estadio==x.name:
                    print(f"Partido del {y.date} a las {y.hour}. El equipo {y.lteam} contra {y.vteam}")
                    i+=1
    if i==0:
        print("No hubo ningún partido en ese estadio")
    print("---------------------------------------------------")

def Búsqueda_por_fecha(juegos):
    #Búsqueda de partidos por equipo
    i=0
    fecha=input("Escribe la fecha de la que quieras ver sus partidos de la sig. manera mes/día/año\n--> ")
    print(f"Los siguientes partidos se jugaran en la fecha {fecha}:")
    for x in juegos:
        if x.date==fecha:
            print(f"Partido en el estadio {x.estadio}. El equipo {x.lteam} contra {x.vteam}")
            i+=1
    if i==0:
        print("No hubo ningún partido en esa fecha")
    print("---------------------------------------------------")        

def Búsqueda_nombres_productos(products, election, bought_products, restaurants, client, your_bought_products, data):
    #Búsqueda de productos por nombre
    while True:
        i=0
        nombre=input("Escribe el nombre del producto en inglés que quieras ver\n--> ")
 
        for y in election.products:
            if y.casefold()==nombre.casefold():
                for z in products:
                    if z.name==y and election.name==z.restaurant:
                        z.Show()
                        i+=1
                        break
                break
            break
        buy1=input("Cuántos quieres comprar?")
        if i==0:
            print("No hubo ningún producto con ese nombre")
        elif buy1.isnumeric()==False or int(buy1)>z.quantity:
            print(f"La cantidad debe ser un número menor a {z.quantity}. Vuelva a ingresarla")
        elif int(client.age)<18 and z.aditional=="alcoholic":
            print("No puedes comprar este producto por ser menor de edad")
        else:
            if input(f"Quieres comprar {buy1} de este producto? {z.name} Y para comprar, otro para seguir buscando y anular ese: ")=="Y":
                buy1=int(buy1)
                data[0]+=z.price*buy1
                z.bought+=buy1
                z.quantity-=buy1
                bought_products.append(z)
                your_bought_products[z]=buy1
                print("---------------------------------------------------")
                break
            else:
                continue
    return bought_products, data, your_bought_products, products

def Búsqueda_tipos_productos(products, election, bought_products, restaurants, client, your_bought_products, data):
    #Búsqueda de productos por nombre
    while True:
        i=0
        beverages=[]
        foods=[]
        tipo=input("Escribe el tipo del producto que quieres ver\n1-Bebidas\n2-Comidas\n--> ")
    
        for y in election.products:
            for z in products:
                if z.name==y and election.name==z.restaurant:
                    if int(tipo)==1 and z.type=="beverages":
                        beverages.append(z)
                        z.Show()
                    elif int(tipo)==2 and z.type=="food":
                        foods.append(z)
                        z.Show()

        if int(tipo)==1:
            bebida=input("Escoge una de las bebidas: ")
            for x in beverages:
                if x.name.casefold()==bebida.casefold():
                    i+=1
                    break
        elif int(tipo)==2:
            comida=input("Escoge una de las comidas: ")
            for x in foods:
                if x.name.casefold()==comida.casefold():
                    i+=1
                    break
        elif tipo.isnumeric()==False or int(tipo)>3 or int(tipo)<1:
            print("Escoge una de las selecciones en números del 1 al 2")

        elif i==0:
            print("No hubo ningún producto con ese nombre")

        elif int(client.age)<18 and x.aditional=="alcoholic":
            print("No puedes comprar este producto por ser menor de edad")

        else:
            buy2=input("Cuántos quieres comprar?")
            if buy2.isnumeric()==False or int(buy2)>x.quantity:
                print(f"La cantidad debe ser un número menor a {x.quantity}. Vuelva a ingresarla")
            else:
                if input(f"Quieres comprar {buy2} de este producto? {x.name} Y para comprar, otro para seguir buscando y anular esa compra: ")=="Y":
                    buy2=int(buy2)
                    data[0]+=x.price*buy2
                    x.bought+=buy2
                    x.quantity-=buy2
                    bought_products.append(x)
                    your_bought_products[x]=buy2
                    print("---------------------------------------------------")
                    break
                else:
                    continue

    return bought_products, data, your_bought_products, products

def Búsqueda_precios_productos(products, election, bought_products, restaurants, client, your_bought_products, data):
    #Búsqueda de productos por nombre
    while True:

        i=0
        j=0
        precio=input("Escribe el rango del precio del producto que quieres ver de la siguiente forma: mínimo,máximo así 0,1\n--> ")
        precio=precio.split(",")
        minimun=precio[0]
        maximun=precio[1]
        counting_products=[]
        for y in election.products:
            for z in products:
                if z.name==y and election.name==z.restaurant:
                    if z.price>int(minimun) and z.price<int(maximun):
                        counting_products.append(z)
                        z.Show()
                        i+=1
        nombre=input("Escribe el nombre del producto en inglés que quieras ver\n--> ")
        for a in counting_products:
            if a.name.casefold()==nombre.casefold():
                j+=1
                break

        buy3=input("Cuántos quieres comprar?")
        if i==0 or j==0:
            print("No hubo ningún producto con ese nombre o con ese rango de precio")
        elif buy3.isnumeric()==False or int(buy3)>a.quantity:
            print(f"La cantidad debe ser un número menor a {a.quantity}. Vuelva a ingresarla")
        elif int(client.age)<18 and a.aditional=="alcoholic":
            print("No puedes comprar este producto por ser menor de edad")
        elif minimun.isnumeric()==False or maximun.isnumeric()==False:
            print("Recuerda que deben ser dos números y una coma, así: 0,1")
        else:
            if input(f"Quieres comprar {buy3} de este producto? {a.name} Y para comprar, otro para seguir buscando y cancelar ese: ")=="Y":
                buy3=int(buy3)
                data[0]+=a.price*buy3
                a.bought+=buy3
                a.quantity-=buy3
                bought_products.append(a)
                your_bought_products[a]=buy3

                print("---------------------------------------------------")
                break
            else:
                continue
    return bought_products, data, your_bought_products, products

def recibo(data, your_bought_products, client):
    discount=0
    print("-----------------Verificación de compra--------------\nTus productos comprados son:")
    for i, j in your_bought_products.items():
        print(f"{i.name} cantidad {j}-----------------{i.price*int(j)}$")
    
    if perfect_number(int(client.cedula))==True:
        discount=data[0]*0.15

    
    print(f"-------------------------FACTURA---------------------------\nmonto total-------------------------------------->{data[0]}$\niva-------------------------------------------------->{data[0]*0.16}$\ndescuento-------------------------------------------->{discount}$")
    print("---------------------------------------------------")
    print(f"-------------------------FINAL-------------------------\n------------------------------------------------------>{data[0]-discount} $")
    if input("¿Quieres realizar tu compra? Escribe Y para confirmar la compra: ")=="Y":
        print("----------------¡Comprado!------------------------")
        print("---------------------------------------------------")    
        client.monto=data[0]-discount
        return client

def Validación(bought_tickets):
    print("¡Bienvenido a la validación de tickets!")    
    while True:
        selection=input("Para validar el ticket, ingrese el código de su boleto: ")
        i=0
        for x in bought_tickets:
            if int(selection)==x.code:
                if x.validate!=True:
                    print("¡Felicidades! Tu ticket ha sido conseguido. Será validado próximamente")
                    print("---------------------------------------------------")
                    x.validate=True
                    i+=1
        if i==0 or selection.isnumeric()==False or int(selection)>999 or int(selection)<100:
            print("Disculpa, ese ticket no existe o ya está ocupado.\nEscoja otro para validar")

        elif input("¿Quiere seguir validando? Escriba Y para continuar validando, otro para salir: ")!="Y":
            break
        else: 
            continue
    return bought_tickets

def Get_Client_data():
    while True:
        print("-----¡Bienvenido al sistema de compra de tickets!---------")
        nombre=input("Ingrese su nombre: ")
        cedula=input("Ingrese su cédula: ")
        edad=input("Ingrese su edad: ")
        monto=0

    ##validación
        if nombre.isnumeric()==True or cedula.isnumeric()==False or edad.isnumeric()==False:
            print("Recuerda que tu nombre debe ser puras letras, y la cédula y la edad son números")
        else:
            print("---------------------------------------------------")
            break
    data=[nombre, cedula, edad, monto]
    return data

def get_id(juegos):
    while True:
        i=0
        o=input("Ingrese el id del partido al que quiere comprar tickets\nAntes, seleccione 1 para ver las opciones:")
        ##validación
        if int(o)!=1 or o.isnumeric()==False:
            print("Escribe 1 para mostrar")
        else: 
            for x in juegos:
                x.Show()
            id_partido=input("-->")
            for y in juegos:
                if id_partido.isnumeric()==False:
                    print("Debes poner un número acá. Vuelva a ingresar sus datos correctamente")
                elif y.id==str(id_partido):
                    print(f"¡Hemos encontrado tu partido! Es el {y.lteam} vs {y.vteam} en {y.estadio}")
                    i+=1
                    break
            if y.id!=str(id_partido):
                print("Disculpa, no hemos encontrado tu partido. Vuelva a ingresar sus datos correctamente")
            elif i==1:
                print("---------------------------------------------------")
                break
    return id_partido

def get_tickets(juegos, estadios, bought_tickets, clients, id_partido, data, get_number_vampire, your_tickets_id, codes):
    iva=0
    descuento=0
    while True:
        ticket=input("Ingrese: \n1-Para comprar el ticket general (50$)\n2-Para el ticket VIP (120$). Con este ticket podrá disfrutar del restaurante del estadio\n-->")
        ##validación
        if ticket.isnumeric()==False or int(ticket)<1 or int(ticket)>2:
            print("El ticket debe ser un número entre el 1 y el 2. Vuelva a ingresar sus datos correctamente")
        
        else:
            if int(ticket)==1:
                vip_or_general="GENERAL"
                data[-1]+=50

            elif int(ticket)==2:
                vip_or_general="VIP"
                data[-1]+=120

            for y1 in juegos:
                if y1.id==str(id_partido):
                    for z in estadios:
                        if z.name==y1.estadio: ##se trae al objeto al buscar su nombre
                            z.printings()
                            break

            selection_made=str(input("Ingresa el puesto que quieres: -->"))
            i=0
            j=0
            
            for a in z.occupied_seats: 
                if a==selection_made: ##si encuentra la selección 
                    ##en los asientos ocupados
                    i+=1
                    break
            for a in z.seats:
                if a==selection_made: ##si encuentra la selección en
                    ##los asientos que existen
                    j+=1
                    break
            if i>=1 or j<=0:
                print("Disculpa, ese puesto no existe o ya está ocupado.\nEscoja otro puesto luego de ingresar sus datos nuevamente")
            else: ##continúa
                z.occupied_seats.append(selection_made)
                print("---------------------------------------------------")

                while True: ##bucle para generar códigos únicos
                    unique_code=random.randint(100,999)
                    for code in codes:
                        if unique_code==code:
                            continue
                        else:
                            codes.append(unique_code)
                            break
                    break
                        


                print(f"El id único de tu boleto es {unique_code}")
                your_ticket=Ticket(id_partido, vip_or_general, selection_made, data[1], unique_code, False, z.name)

                bought_tickets.append(your_ticket)
                your_tickets_id.append(your_ticket.code)
                if input("¿Quiere seguir comprando en el mismo estadio? Escriba Y para continuar con su compra, otro para salir: ")=="Y":
                    continue
                else:
                    if input("¿Quiere comprar tickets en otro estadio? Escriba Y para continuar con su compra, otro para salir: ")=="Y":
                        
                        get_tickets(juegos, bought_tickets, clients, get_id(juegos), data, get_number_vampire)
                    else:
                        break
                
    if get_number_vampire==True:
        descuento=data[-1]*0.5
        print(f"¡Felicidades, tienes un descuento de {descuento}$ por que tu cédula es un número vampiro!")
    iva=Iva(data[-1])
    Purchase_Confirmation(your_tickets_id, bought_tickets, data, clients, descuento, iva)    
    
    return clients, bought_tickets, codes

def Purchase_Confirmation(your_tickets_id, bought_tickets, data, clients, descuento, iva):

    print("-----------------Verificación de compra--------------\nTus tickets comprados son:")
    for i in your_tickets_id:
        for j in bought_tickets:
            if i==j.code:
                print(f"Ticket {j.code}\nPuesto {j.seat}, tipo {j.type}")
    print(f"-------------------------FACTURA---------------------------\nmonto principal-------------------------------------->{data[-1]}$\niva-------------------------------------------------->{iva}$\ndescuento-------------------------------------------->{descuento}$")
    print("---------------------------------------------------")
    print(f"-------------------------TOTAL-------------------------\n------------------------------------------------------>{data[-1] +iva- descuento} $")
    if input("¿Quieres realizar tu compra? Escribe Y para confirmar la compra: ")=="Y":
        print("----------------¡Comprado!------------------------")
        print("---------------------------------------------------")    
        client=Client(data[0], data[1], data[2], data[-1], your_tickets_id)
        clients.append(client)

        return clients
    else:
        print("Se ha anulado la compra")

def Iva(ammount):
    iva=0
    iva+=ammount*0.16
    return iva

def colmillos(cedula_str):
    permutating = permutations(cedula_str, len(cedula_str))
    for num_list in permutating:
        v = ''.join(num_list)
        x, y = v[:int(len(v)/2)], v[int(len(v)/2):]
        if x[-1] == '0' and y[-1] == '0':
            continue
        product=int(x) * int(y)
        if product == int(cedula_str):
            return x,y
    return False

def is_vampire_or_not(cedula_int):
    cedula_str = str(cedula_int)
    if len(cedula_str) % 2 == 1:
        return False
    fangs = colmillos(cedula_str)
    if not fangs:
        return False
    return True

def get_number_vampire(data):
    cedula=data[1]
    if is_vampire_or_not(cedula):
        ##print ("El número {} es un número vampiro".format(cedula))
        return True
    else:
        ##print("El número {cedula} no es vampiro 😥")
        return False

def perfect_number(number):
    i=0
    number2=1
    while True: 
        if number%number2==0:
            i+=number2
            if i==number:
                print(f"Su número {number} es perfecto")
                return True
        number2+=1

        if number2==number:
            print(f"Su número {number} no es perfecto")
            return False

def main():
    equipos=[]
    estadios=[]
    juegos=[]
    restaurants=[]
    products=[]
    bought_products=[]
    bought_tickets=[]
    clients=[]
    codes=[]

    link= "https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/teams.json"
    link2= "https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/stadiums.json"
    link3="https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/matches.json"
    
    r= requests.get(link)
    teams_data= r.json()
    
    
    s= requests.get(link2)
    stadium_data= s.json()

    t= requests.get(link3)
    games_data= t.json()

    Team_Converter(teams_data, equipos)
    Products_Converter(stadium_data, products)
    Restaurants_Converter(stadium_data, restaurants, products)
    Stadium_Converter(stadium_data, estadios, restaurants)
    Game_Converter(games_data, juegos, equipos, estadios)
    

    while True:
            print("----------Bienvenido al sistema de la FIFA QATAR 2022----------")
            election=input("Por favor, escoge una de las siguientes opciones: \n1-Búsqueda por filtros\n2-Compra de tickets\n3-Validar un ticket\n4-Búsqueda y compra de productos\n5-Salir\n-->")
            print("---------------------------------------------------")
            if election.isnumeric()==False or int(election)>5:
                print("Recuerda que deben ser opciones numéricas del 1 al 7")
            else:
                election=int(election)

                if election==1:
                    print("--------------¡Bienvenido a la página de búsqueda de partidos!---------------")
                    while True:
                            election=input("Escoge una de las siguientes opciones: \n1-Búsqueda de partidos por equipos\n2-Búsqueda de partidos por estadios\n3-Búsqueda de partidos por fecha\n4-Mostrar equipos\n5-Mostrar partidos\n6-Mostrar fechas\n7-Salir de este menú\n-->")
                            if election.isnumeric()==False or int(election)>7:
                                print("Recuerda que deben ser opciones numéricas del 1 al 7")
                            else:
                                election=int(election)
                                if election==1:
                                    Búsqueda_por_equipos(juegos, equipos)
                                elif election==2:
                                    Búsqueda_por_estadios(juegos, estadios)
                                elif election==3:
                                    Búsqueda_por_fecha(juegos)
                                elif election==4:
                                    print("Los equipos son:")
                                    for x in equipos:
                                        print(x.name)
                                elif election==5:
                                    print("Los estadios son:")
                                    for x in estadios:
                                        print(x.name)
                                elif election==6:
                                    print("Las fechas son:")
                                    for x in juegos:
                                        print(x.date_hour)
                                elif election==7:
                                     break

                elif election==2:
                    your_tickets_id=[]
                    data=Get_Client_data()
                    get_tickets(juegos, estadios, bought_tickets, clients, get_id(juegos), data, get_number_vampire(data), your_tickets_id, codes)
                    
                elif election==3:
                    Validación(bought_tickets)

                elif election==4:
                    monto=0
                    print("--------------¡Bienvenido a la página de compra de productos!---------------")
                    data=input("Para empezar, ingrese el número de su cédula: ")
                    VIPtickets=[]
                    restaurants_used=[]
                    options_of_products=[]
                    i=0
                    if data.isnumeric()==False:
                        print("Recuerda que tu nombre debe ser puras letras, y la cédula y la edad son números")
                    
                    else:
                        print(f"Los tickets VIP que compraste tienen la siguiente ID")
                        for client in clients:
                            if client.cedula==data:
                                for x in bought_tickets:
                                    for y in client.tickets:
                                        if x.code==y:
                                            if x.type=="VIP":
                                                print(x.code)
                                                i+=1
                                                VIPtickets.append(x.estadio)
                        if i==0:
                            print("No se encontró ningún ticket VIP. Recuerda que debes comprar uno de este tipo para poder comprar en el restaurant")
                        else:
                            i=0
                            for estadio in estadios:
                                for estadios_comprados in VIPtickets:
                                    if estadio.name==estadios_comprados:
                                        for restaurant in restaurants:
                                            for restaurants1 in estadio.restaurant:
                                                if restaurants1==restaurant.name:
                                                    restaurants_used.append(restaurant.name)
                                                    i+=1

                            if i==0:
                                print("No se encontró nada")
                            else:
                                your_bought_products={}
                                while True:

                                    i=0
                                    print("---------------------------------------------------")
                                    print("Podrás comprar en los siguientes restaurantes: ")
                                    for x in restaurants_used:
                                        print(x)
                                    election=input("Copie y pegue el nombre del restaurante en el que quiere comprar: ")

                                    for y in restaurants:
                                        if election.casefold()==y.name.casefold():
                                            i+=1
                                            break
                                    if i==0:
                                        print("No se encontró el restaurante, escribalo de nuevo por favor")
                                    else: 
                                        print(f"Usted escogió el restaurant: {y.name}")
                                        election=y
                                        break
                                data=[]
                                data.append(monto)
                                while True:
                                    print("---------------------------------------------------")
                                    selection=input("Escoge una de las siguientes opciones: \n1-Búsqueda de productos por nombre\n2-Búsqueda de productos por rango de precios\n3-Búsqueda de productos por tipo\n4-Salir de este menú\n-->")
                                    if selection.isnumeric()==False or int(selection)>4:
                                        print("Recuerda que deben ser opciones numéricas del 1 al 7")
                                    elif int(selection)==1:
                                        Búsqueda_nombres_productos(products, election, bought_products, restaurants, client, your_bought_products, data)
                                    elif int(selection)==2:
                                        Búsqueda_precios_productos(products, election, bought_products, restaurants, client, your_bought_products, data)
                                    elif int(selection)==3:
                                        Búsqueda_tipos_productos(products, election, bought_products, restaurants, client, your_bought_products, data)
                                    elif int(selection)==4:
                                        break
                                recibo(data, your_bought_products, client)
                elif election==5:
                    promedio=0
                    clientesVIP=0
                    clientesGENERAL=0
                    print("El promedio de gastos de clientes VIP es de: ")
                    for a in clients:
                        for b in a.tickets:
                            for c in bought_tickets:
                                if c.code==b:
                                    if c.type=="VIP":
                                        promedio+=a.monto
                                        clientesVIP+=1
                                    elif c.type=="GENERAL":
                                        clientesGENERAL+=1
                    print(f"{promedio-(50*clientesGENERAL+50*clientesGENERAL*0.16)/clientesVIP} $")
                    
                    print("Tabla de asistencia en cada partido")
                    for a in juegos:
                        for b in bought_tickets:
                            if a.id==b.id:
                                if b.validate==True:
                                    a.asistencia+=1
                    juegos=sorted(juegos, key=lambda partido: partido.asistencia, reverse=True)
                    print(f"Los primeros 3 partidos tienen los sig id: 1. {juegos[0].id} 2. {juegos[1].id} 3.{juegos[3].id}")
                    clients=sorted(clients, key=lambda cliente: len(cliente.tickets), reverse=True)
                    print(f"Los primeros 3 clientes tienen los sig nombres: 1. {clients[0].name} 2. {clients[1].name} 3.{clients[2].name}")

                    #juegos.sort(for i in juegos, key=i.asistencia)



                    
                    

                                
                                

            

main()

