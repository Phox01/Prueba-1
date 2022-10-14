trimestre2=[]
trimestre1=[]
students=[]
def main():
    print("*** Bienvenido ***")
    y=get_student_data()
    trimestre(y, trimestre2, trimestre1)
    printing(y)
    quantity_students(y, students)

def get_student_data():
    while True:
        try:
            student = {
            "cédula":int(input("Ingrese su cédula: ")),
            "nombre":input("Ingrese su nombre y apellido: "),
            "promedio de notas":float(input('Ingrese su promedio: ')),
            "trimestre": 0
            }
        except SyntaxError:
            print('Ingrese valores válidos')
        except:
            print('Ingrese de nuevo sus datos sin error')
        #students.append(student)
        if input('Ingrese n para salir, otra cosa para continuar: ')=='n':
            break
        
    return student


def trimestre(student, trimestre2, trimestre1):
    #for student in students:
    x=student.get('nombre')
    if student.get('promedio de notas')>= 18:
        trimestre2.append(student)
        student['trimestre']=2
    elif student.get('promedio de notas')>= 12:
        trimestre1.append(student)
        student['trimestre']=1
    if student.get('promedio de notas')< 18:
        print(f'El estudiante {x} está rechazado' )
    return trimestre1, trimestre2, student


def printing(student):
    #for student in students:
    print('La información del estudiante es:')
    print (f'Cédula: ', student.get("cédula"))
    print (f'Nombre: ', student.get("nombre"))
    print (f'Promedio de notas:', student.get("promedio de notas"))
    print (f'Su trimestre es:', student.get("trimestre"))

def quantity_students(student, students):
    students.append(student)
    print('La cantidad de estudiantes que aplicaron son:', len(students))
    return students, student

####def promedio(prom):
####    while True:
####        notas_indv=input('Ingrese sus notas seguidas por una coma (,)')
####        for item in notas_indv.split(','):
####             prom=item/notas_indv.split.index
####
####             return prom
            
main()