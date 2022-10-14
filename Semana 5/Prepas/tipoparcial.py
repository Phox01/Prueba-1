def main():
    trimestre2=[]
    trimestre1=[]
    trim=0
    print_welcome()
    y=get_student_data(trim)
    trimestre2, trimestre1, trim = trimestre(y, trimestre2, trimestre1, trim)
    printing(y)

def print_welcome():
    print("*** Bienvenido ***")

def get_student_data(trim):
    while True:
        student = {
        "cédula":input("Ingrese su cédula: "),
        "nombre":input("Ingrese su nombre y apellido: "),
        "promedio de notas":float(input('Ingrese su promedio: ')),
        "trimestre": trim
        }
        if input('Ingrese n para salir, otra cosa para continuar: ')=='n':
            break 
    return student


def trimestre(student, trimestre2, trimestre1, trim):
    x = student.get('nombre')
    if student.get('promedio de notas')>= 18:
        trimestre2.append(student)
        #print(f'El estudiante {x} está en el trimestre 2' )
        trim=2
    elif student.get('promedio de notas')>= 12:
        trimestre1.append(student)
        #print(f'El estudiante {x} está en el trimestre 1' )
        trim=1
    if student.get('promedio de notas')< 18:
        print(f'El estudiante {x} está rechazado' )
    return trimestre1, trimestre2, trim

def printing(student):
    print('La información del estudiante es:')
    print (f'Cédula: ', student.get("cédula"))
    print (f'Nombre: ', student.get("nombre"))
    print (f'Promedio de notas:', student.get("promedio de notas"))
    print (f'Su trimestre es:', student.get("trimestre"))



####def promedio(prom):
####    while True:
####        notas_indv=input('Ingrese sus notas seguidas por una coma (,)')
####        for item in notas_indv.split(','):
####             prom=item/notas_indv.split.index
####
####             return prom
            
main()