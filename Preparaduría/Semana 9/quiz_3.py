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
                if i=='washer':
                    code=w
                elif y=='price':
                    precio=w
                elif y=='brand':
                    marca=w
                elif y=="color":
                    color=w
                elif y=="capacity":
                    capacidad=w
                elif y=="digital":
                    control=w
                elif y=="cooler":
                    inc_congelador=w
                elif y=="comp":
                    compartimientos=w
                elif y=="cup":
                    material_vaso=w
                elif y=="speeds":
                    velocidades=w

                
            if i=="washer":
                inventario.append(Lavadora(code, precio, marca, color, capacidad))
                
            elif i=="microwave":
                inventario.append(Horno_Microondas(code, precio, marca, color, control))
                
            elif i=="fridge":
                inventario.append(Nevera(code, precio, marca, color, inc_congelador, compartimientos))
                
            elif i=="blender":
                inventario.append(Licuadora(code, precio, marca, color, material_vaso, velocidades))
                
            
    print(inventario)
    return inventario
    
def leer(inventario):
    for n in inventario:
        if type(n)==Lavadora:
            print(f'El producto es una lavadora \nTiene código:{n.codigo_producto}\nPrecio:{n.precio}\nMarca:{n.marca}\nColor:{n.color}\nCapcidad:{n.capacidad}')
        elif type(n)==Horno_Microondas:
            print(f'El producto es un Horno \nTiene código:{n.codigo_producto}\nPrecio:{n.precio}\nMarca:{n.marca}\nColor:{n.color}\nControl{n.control}')
        elif type(n)==Nevera:
            print(f'El producto es una Nevera \nTiene código:{n.codigo_producto}\nPrecio:{n.precio}\nMarca:{n.marca}\nColor:{n.color}\nInc congelador{n.inc_congelador}\nCompartimientos{n.compartimiento}')
        elif type(n)==Licuadora:
            print(f'El producto es un Licuadora \nTiene código:{n.codigo_producto}\nPrecio:{n.precio}\nMarca:{n.marca}\nColor:{n.color}\nMaterial del vaso{n.material_vaso}\nVelocidades{n.velocidades}')


            





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
    leer(inventario)





main()