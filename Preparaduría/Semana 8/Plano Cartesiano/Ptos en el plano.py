### Problema 1 (5pts):
#En este ejercicio vas a trabajar el concepto de puntos, 
#coordenadas y vectores sobre el plano cartesiano y cómo 
# la programación Orientada a Objetos puede ser una excelente aliada para trabajar 
# con ellos. No está pensado para que hagas ningún tipo de cálculo sino para que practiques 
# la automatización de tareas.
#- Crea una clase llamada Punto con sus dos coordenadas X e Y.
#- Añade un método constructor para crear puntos fácilmente. Si no se recibe alguna coordenad
# a, su valor será cero.
#- Sobreescribe el método string, para que al imprimir por pantalla un punto aparezca en formato (X,Y)
#- Añade un método llamado cuadrante que indique a qué cuadrante pertenece el punto, teniendo
#  en cuenta que si X == 0 e Y != 0 se sitúa sobre el eje Y, si X != 0 e Y == 0 se sitúa sobre
#  el eje X y si X == 0 e Y == 0 está sobre el origen.
#- Añade un método llamado vector, que tome otro punto y calcule el vector resultante entre los dos 
# puntos.

class Punto:
    def __init__(self, X, Y):
        self.X=X
        self.Y=Y
        

    def printing(self):
        printings=(self.X, self.Y)
        print(f'El punto en el plano es {printings})')
        
        return printings

    def Cuadrante(self, printings):
        if  self.X == 0 and self.Y !=0:
            print(f'El punto {printings} está sobre el eje Y')
        elif  self.X != 0 and self.Y ==0:
            print(f'El punto {printings} está sobre el eje X')
        elif  self.X == 0 and self.Y ==0:
            print(f'El punto {printings} está en el origen')
        elif self.X>0:
            if self.Y>0:
                print(f'El punto {printings} está en el cuadrante 1')
            else:
                print(f'El punto {printings} está en el cuadrante 4')
        else:
            if self.Y>0:
                print(f'El punto {printings} está en el cuadrante 2')
            else:
                print(f'El punto {printings} está en el cuadrante 3')


def Ingreso():
        X=int(input('Ingrese coordenada en X: '))
        Y=int(input('Ingrese coordenada en Y: '))
        if X=='':
            X=0
        if Y=='':
            Y=0
        pto= Punto(X, Y)
        
        return pto

def Vector(pto1, pto2):
    newX=pto2.X-pto1.X
    newY=pto2.Y-pto1.Y
    print(f'El vector será conformado por {pto2.X}-{pto1.X}, {pto2.Y}-{pto1.Y}')
    vector= Punto(newX, newY)
    return vector

def main():
    
    pto=Ingreso()
    print('Éste será su primer punto')
    pto2=Ingreso()
    print('Éste será su segundo punto')
    printings=pto.printing()
    pto.Cuadrante(printings)
    print('----------------')
    printings2=pto2.printing()
    pto2.Cuadrante(printings2)
    print('----------------')
    vector=Vector(pto, pto2)
    printings3=vector.printing()
    vector.Cuadrante(printings3)


main()
