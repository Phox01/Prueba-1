import requests
from clases import Equipo, Estadio, Partido

###Añadir más comentarios, más propiedades de los objetos y entrelazarlos

def Team_Converter(name, flag, group, equipos, edd, code):
    ##Convertir los equipos en objetos
    for i in edd:
        for key, value in i.items():
            if key=="name":
                name=value
            if key=="flag":
                flag=value
            if key=="code":
                code=value
            if key=="group":
                group=value
        equipos.append(Equipo(name, flag, code, group))
    for i in equipos:
        print(i.name)
    return equipos

def Stadium_Converter(name, location, edd2, estadios):
    ##Convertir los estadios en objetos
    for i in edd2:
        for key, value in i.items():
            if key=="name":
                name=value
            if key=="location":
                location=value
        estadios.append(Estadio(name,location))
    for i in estadios:
        print(i.name)
    return estadios

def Game_Converter(lteam,vteam, date_hour, estadio, edd3, juegos):
    ##Convertir los estadios en objetos
    for i in edd3:
        for key, value in i.items():
            if key=="home_team":
                lteam=value
            if key=="away_team":
                vteam=value
            if key=="date":
                date_hour=value
            if key=="stadium_id":
                estadio=value
        juegos.append(Partido(lteam, vteam, date_hour, estadio))
    for i in juegos:
        print(i.vteam)
    return juegos

def main():
    name=""
    flag=""
    code=""
    group=""
    location=""
    lteam=""
    vteam=""
    date_hour=""
    estadio=""
    equipos=[]
    estadios=[]
    juegos=[]
    link= "https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/teams.json"
    link2= "https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/stadiums.json"
    link3="https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/matches.json"
    r= requests.get(link)
    edd= r.json()
    
    s= requests.get(link2)
    edd2= s.json()

    t= requests.get(link3)
    edd3= t.json()

    Team_Converter(name, flag, group, equipos, edd, code)
    Stadium_Converter(name, location, edd2, estadios)
    Game_Converter(lteam,vteam, date_hour, estadio, edd3, juegos)


main()

