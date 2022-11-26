import requests
import json
from Equipo import Equipo
from Estadio import Estadio
from Partido import Partido
from Restaurants import Restaurant
from Products import Product
#from prueba import printings
from Client import Client
from Ticket import Ticket
import random


###Añadir más comentarios, más propiedades de los objetos y entrelazarlos

def Team_Converter(teams_data, equipos):
    ##Convertir los equipos en objetos
    for x in teams_data:
        equipos.append(Equipo(x["name"], x["fifa_code"], x["group"], x["id"]))
#   for i in equipos:
#        print(i.name)
    return equipos

def Products_Converter(stadium_data, products):
    for x in stadium_data:
        for y in x["restaurants"]:
            for z in y["products"]:
                products.append(Product(z["name"], z["price"], z["type"], z["adicional"]))
    return products

def Restaurants_Converter(stadium_data, restaurants, products):
    products_list=[]
    for x in stadium_data:
        for y in x["restaurants"]:
            last=y["products"][-1]["name"]
            for z in y["products"]:
                for w in products:
                    if z["name"]==w.name:
                        products_list.append(w)
                        break
                if w.name==last:
                    restaurants.append(Restaurant(y["name"], products_list))
                    products_list=[]
                    break
                    

    return restaurants, products_list

def Stadium_Converter(stadium_data, estadios, restaurants):
    ##Convertir los estadios en objetos
    restaurant_list=[]
    for y in stadium_data:
        for z in y["restaurants"]:
            last=y["restaurants"][-1]["name"]
            for x in restaurants:
                if x.name==z["name"]:
                    restaurant_list.append(x)
                    break
            if x.name==last:
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
                lteam=y
            elif z["away_team"]==y.name:
                vteam=y
        for x in estadios:
            if z["stadium_id"]==x.id:
                stadium=x
        date_hour=z["date"].split(" ")
        date=date_hour[0]
        hour=date_hour[1]
        
        juegos.append(Partido(lteam, vteam, date, hour, stadium, z["id"]))
#    for i in juegos:
#        print(i.vteam)
    return juegos

def Búsqueda_por_equipos(juegos, equipos):
    #Búsqueda de partidos por equipo
    team=input("Escribe un equipo, en ingles, el cual quieras ver sus partidos: ")
    i=0
    for x in equipos:
        if x.name.casefold()==team.casefold():
            print(f"El equipo {x.name} jugará en los siguientes partidos:")
            for y in juegos:
                if y.lteam==x:
                    print(f"Partido del {y.date} a las {y.hour} en el estadio {y.estadio.name}, contra {y.vteam.name}")
                    i+=1
                elif y.vteam==x:
                    print(f"Partido del {y.date} a las {y.hour} en el estadio {y.estadio.name}, contra {y.lteam.name}")
                    i+=1
    if i==0:
        print("No hubo ningún partido con ese equipo")
    print("============================================")

def Búsqueda_por_estadios(juegos, estadios):
    #Búsqueda de partidos por equipo
    i=0
    estadio=input("Escribe un estadio el cual quieras ver sus partidos: ")
    for x in estadios:
        if x.name.casefold()==estadio.casefold():
            print(f"El estadio {x.name} se usará en los siguientes partidos:")
            for y in juegos:
                if y.estadio==x:
                    print(f"Partido del {y.date} a las {y.hour}. El equipo {y.lteam.name} contra {y.vteam.name}")
                    i+=1
    if i==0:
        print("No hubo ningún partido en ese estadio")
    print("============================================")

def Búsqueda_por_fecha(juegos):
    #Búsqueda de partidos por equipo
    i=0
    fecha=input("Escribe la fecha de la que quieras ver sus partidos de la sig. manera mes/día/año\n--> ")
    print(f"Los siguientes partidos se jugaran en la fecha {fecha}:")
    for x in juegos:
        if x.date==fecha:
            print(f"Partido en el estadio {x.estadio.name}. El equipo {x.lteam.name} contra {x.vteam.name}")
            i+=1
    if i==0:
        print("No hubo ningún partido en esa fecha")
    print("============================================")        

def Get_Client_data(juegos, bought_tickets, clients):
    while True:
        print("-----¡Bienvenido al sistema de compra de tickets!---------")
        nombre=input("Ingrese su nombre: ")
        cedula=input("Ingrese su cédula: ")
        edad=input("Ingrese su edad: ")
        monto=0
        your_games=[]
        your_seats=[]
        your_tickets_id=[]
        boolean=True
        if nombre.isnumeric()==True or cedula.isnumeric()==False or edad.isnumeric()==False:
            print("Recuerda que tu nombre debe ser puras letras, y la cédula y la edad son números")
        else:
            print("============================")
            break
    while boolean:
        while True:
            i=0
            o=input("Ingrese el id del partido al que quiere comprar tickets\nAntes, seleccione 1 para ver las opciones:")
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
                        print("¡Hemos encontrado tu partido!")
                        i+=1
                        break
                if y.id!=str(id_partido):
                    print("Disculpa, no hemos encontrado tu partido. Vuelva a ingresar sus datos correctamente")
                elif i==1:
                    print("============================")
                    #your_games.append(id_partido)
                    break

        while True:
            ticket=input("Ingrese 1 para comprar el ticket general (50$), o 2 para el ticket VIP (120$). Con este ticket podrá disfrutar del restaurante del estadio\n-->")
            if ticket.isnumeric()==False or int(ticket)<1 or int(ticket)>2:
                print("El ticket debe ser un número entre el 1 y el 2. Vuelva a ingresar sus datos correctamente")
            else:
                if int(ticket)==1:
                    vip_or_general="GENERAL"
                    #print("El monto añadido fue de 50$")
                    monto+=50
                elif int(ticket)==2:
                    vip_or_general="VIP"
                    ##print("El monto añadido fue de 120$")
                    monto+=120
                y.estadio.printings()
                selection_made=str(input("Ingresa el puesto que quieres: -->"))
                i=0
                j=0
                for z in y.estadio.occupied_seats:
                    if z==selection_made:
                        i+=1
                        break
                for a in y.estadio.seats:
                    if a==selection_made:
                        j+=1
                        break
                if i>=1 or j<=0:
                    print("Disculpa, ese puesto no existe o ya está ocupado.\nEscoja otro puesto luego de ingresar sus datos nuevamente")
                else:
                    y.estadio.occupied_seats.append(selection_made)
                    print("============================\n----------------¡Comprado!------------------------")
                    unique_code=random.randint(10000000,99999999)
                    print(f"El id de tu boleto es {unique_code}")
                    your_ticket=Ticket(id_partido, vip_or_general, selection_made, nombre, unique_code)
                    bought_tickets.append(your_ticket)
                    your_tickets_id.append(your_ticket.code)
                    ##print("Los puestos que compró fueron:")
                    ##for x in your_seats:
                    ##    print(x, end=" ")
                    ##print("")
                    if input("¿Quiere seguir comprando en el mismo estadio? Escriba Y para continuar con su compra, otro para salir: ")=="Y":
                        continue
                    else:
                        if input("¿Quieres comprar tickets en otro estadio? Escriba Y para continuar con su compra, otro para salir: ")=="Y":
                            break
                        else:
                            boolean=False
                            break
    print("========================================")    
    client=Client(nombre, cedula, edad, monto, your_tickets_id)
    clients.append(client)
    return clients, bought_tickets

def Iva(ammount):
    iva+=ammount*0,16
    return Iva

def es_vampiro_o_no(cedula):
    if len(cedula)%2!=0:
        print(f"{cedula} no es un número vampiro")
    else:
        


    

def main():
    equipos=[]
    estadios=[]
    juegos=[]
    restaurants=[]
    products=[]
    bought_tickets=[]
    clients=[]
    value=True
    value1=True
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
    while value1:
        try:
            print("----------Bienvenido al sistema de la FIFA QATAR 2022----------")
            election=int(input("Por favor, escoge una de las siguientes opciones: \n1-Búsqueda por filtros\n2-Compra de tickets\n3-Búsqueda de partidos por fecha\n4-Mostrar equipos\n5-Mostrar partidos\n6-Mostrar fechas\n7-Salir\n-->"))
            print("============================================")
            if election==1:
                print("--------------¡Bienvenido a la página de búsqueda de partidos!----------")
                while value:
                    try:
                        election=int(input("Escoge una de las siguientes opciones: \n1-Búsqueda de partidos por equipos\n2-Búsqueda de partidos por estadios\n3-Búsqueda de partidos por fecha\n4-Mostrar equipos\n5-Mostrar partidos\n6-Mostrar fechas\n7-Salir de este menú\n-->"))
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
                             value=False
                        else:
                            print("Recuerda que deben ser opciones numéricas del 1 al 7")
                    except SyntaxError and ValueError:
                        print('Recuerda que deben ser opciones numéricas del 1 al 7')
            elif election==2:
                Get_Client_data(juegos, bought_tickets, clients)

        except SyntaxError and ValueError:
            print('Recuerda que deben ser opciones numéricas del 1 al 7')
    

main()

