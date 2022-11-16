#======================================================
# Nombre del Estudiante: Joseph Ruiz
# Carnet: 20221110023
#======================================================
# correo a enviar: ja.teixeira@correo.unimet.edu.ve

from quiz_2 import Electrodoméstico, Nevera, Lavadora, Horno_Microondas, Licuadora


def convert(edd, code, precio, marca, color, capacidad, control, inc_congelador, compartimientos, material_vaso, velocidades, inventario):
    for i, j in edd.items():
        for x in j:
            for y, w in x.items():
               ## if y=='cod_p':
               ##     code=w
               ## elif y=='price':
               ##     precio=w
               ## elif y=='brand':
               ##     marca=w
               ## elif y=="color":
               ##     color=w
               ## elif y=="capacity":
               ##     capacidad=w
               ## elif y=="digital":
               ##     control=w
               ## elif y=="cooler":
               ##     inc_congelador=w
               ## elif y=="comp":
               ##     compartimientos=w
               ## elif y=="cup":
               ##     material_vaso=w
               ## elif y=="speeds":
               ##     velocidades=w

                
                if i=="washer":
                    inventario.append(Lavadora(y['cod_p'], y["price"], y["brand"], y["color"], y["capacity"]))
                if i=="microwave":
                    inventario.append(Horno_Microondas(y['cod_p'], y["price"], y["brand"], y["color"], y["digital"]))
                if i=="fridge":
                    inventario.append(Nevera(y['cod_p'], y["price"], y["brand"], y["color"], y["cooler"], y["comp"]))
                if i=="blender":
                    inventario.append(Licuadora(y['cod_p'], y["price"], y["brand"], y["color"], y["cup"], y["speeds"]))
            inventario.append(i)
    print(inventario)
    return inventario
    





            





def main():
    inventario=[]
    code=''
    precio=0
    marca=''
    color=''
    capacidad=0
    control=True
    inc_congelador=True
    compartimientos=0
    material_vaso=''
    velocidades=0

    edd = {
        "washer":
        [
            {"cod_p": "AEX-200918", "price": 551.99, "brand": "Whirlpool", "color": "Blanca", "capacity": 17},
            {"cod_p": "GHT-191214", "price": 409.00, "brand": "LG", "color": "Gris", "capacity": 15}
        ],
        "microwave":
        [
            {"cod_p": "FGE-220708", "price": 109.01, "brand": "Daewoo", "color": "Blanco", "digital": False},
            {"cod_p": "PEP-210123", "price": 201.50, "brand": "Frigilux", "color": "Negro", "digital": True}
        ],
        "fridge":
        [
            {"cod_p": "HYW-180909", "price": 280.98, "brand": "Electrolux", "color": "Plateado", "cooler": False, "comp": 5},
            {"cod_p": "IUO-201020", "price": 405.99, "brand": "Samsung", "color": "Azul pastel y rosado", "cooler": True, "comp": 8}
        ],
        "blender":
        [
            {"cod_p": "OWO-191111", "price": 42.05, "brand": "Oster", "color": "Plateado", "cup": "Cristal", "speeds": 3},
            {"cod_p": "XAT-221230", "price": 17.99, "brand": "Philips", "color": "Blanco", "cup": "Plastico", "speeds": 2}
        ]
    }

    convert(edd, code, precio, marca, color, capacidad, control, inc_congelador, compartimientos, material_vaso, velocidades, inventario)






main()