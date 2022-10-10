#======================================================
# Nombre del Estudiante: Joseph Ruiz
# Carnet: 20221110023
#======================================================
# correo a enviar: ja.teixeira@correo.unimet.edu.ve
anime = {
    "Demon Slayer": {
        "Temporada 1": [
        {
            "cap": 1,
            "name": "Crueldad",
            "duration": "23:39"
        },
        {
            "cap": 4,
            "name": "Selección final",
            "duration": "23:40"
        },
        {
            "cap": 19,
            "name": "Dios del fuego",
            "duration": "23:40"
        },
        {
            "cap": 26,
            "name": "Una nueva misión",
            "duration": "24:10"
        }
    ],
        "Temporada 2": [
        {
            "cap": 26,
            "name": "Un sueño profundo",
            "duration": "22:55"
        },
        {
            "cap": 43,
            "name": "¡No me rendiré!",
            "duration": "23:40"
        }
    ]
 
        },
    "Spy × Family": {
       
        "Temporada 1":[
        {
            "cap": 4,
            "name": "Objetivo: pasar la entrevista",
            "duration": "24:10"
        },
        {
            "cap": 7,
            "name": "El segundo hijo del objetivo",
            "duration": "24:10"
        }
    ]
    },
    "Attack on Titan": {
        "Temporada 3": [
            {
                "cap": 46,
                "name": "La reina de la muralla",
                "duration": "23:55"
            },
            {
                "cap": 54,
                "name": "Héroe",
                "duration": "23:55"
            }
    ],
        "Temporada 4":[
            {
                "cap": 60,
                "name": "Al otro lado del mar",
                "duration": "23:55"
            },
            {
                "cap": 72,
                "name": "Los hijos del bosque",
                "duration": "23:55"
            }
        ]
        }
}
historial=[]
while True:
    option=int(input('Selecciona una opción:\n 1: Seleccionar una serie \n 2:Consultar historial de vistos\n 3:Menú principal\n 4:Salir \n'))
    if option==1:
        series={1:"Demon Slayer", 2:"Spy × Family", 3:"Attack on Titan"}
        value=0
        serie=int(input('Por favor, ingrese uno de estos animes que quiere ver:\n 1:Demon Slayer\n 2:Spy × Family\n 3:Attack on Titan\n'))
        
        print(series.get(serie))
        for value, data in anime.items():
            for temp, inf in data.items():
                print(temp)
                for caps in inf:
                   d=caps.get("cap")
                   e=caps.get("name")
                   f=caps.get("duration")
                    #print(caps)
                    #for cap, info in caps.items():

    #if option ==2:                 
    if option==4:
        break
    if option>4:
        print('Esa opción no está disponible')
    #if option.isnumeric() is False:
        #print('Esa opción no es un número')

