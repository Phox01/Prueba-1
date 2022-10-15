trimestre2=[]
trimestre1=[]
students=[]
trimestre0=[]
prom1, prom2, prom0=0, 0, 0
def main():
    print("*** Bienvenido ***\n")
    #while True:
    y=get_student_data()
    trimestre(y, trimestre2, trimestre1, students, trimestre0)
    printing(y)
    quantity_students(students, trimestre1, trimestre2, trimestre0)
    promedio(prom1, prom2, prom0, y)
        #if input('Ingrese n para salir, otro caracter para continuar: ')=='n':
        #    print('')
        #    break

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
        students.append(student)
        if input('Ingrese n para salir, otro caracter para continuar: ')=='n':
            print('')
            break
        print('')
    return student, students


def trimestre(student, trimestre2, trimestre1, students, trimestre0):
    for student in students:
        #x=student.get('nombre')
        if student.get('promedio de notas')>= 18:
            trimestre2.append(student)
            student['trimestre']=2

        elif student.get('promedio de notas')< 18 and student.get('promedio de notas')>= 12:
            trimestre1.append(student)
            student['trimestre']=1
            
        if student.get('promedio de notas')< 12:
            trimestre0.append(student)
            student['trimestre']='Rechazade'
    return trimestre1, trimestre2, student, trimestre0


def printing(student):
    for student in students:
        print('La información del estudiante es:')
        print (f'Cédula: ', student.get("cédula"))
        print (f'Nombre: ', student.get("nombre"))
        print (f'Promedio de notas:', student.get("promedio de notas"))
        print (f'Su trimestre es:', student.get("trimestre"))
        print('')

def quantity_students(students, trimestre1, trimestre2, trimestre0):
    print('La cantidad de estudiantes que aplicaron es de:', len(students), '\n - En trimestre 2:', len(trimestre2), '\n -En trimestre 1:', len(trimestre1), '\n Rechazados:', len(trimestre0), '\n')
    return 

def promedio(prom1, prom2, prom0, student):
    for student in trimestre2:
        prom2+=student.get('promedio de notas')
        if prom2> 18*len(trimestre2):
            print(f'El promedio del trimestre 2 es de: {prom2/len(trimestre2)}')
    for student in trimestre1:
        prom1+=student.get('promedio de notas')
        if prom1> 12*len(trimestre1):
            print(f'El promedio del trimestre 1 es de: {prom1/len(trimestre1)}')
    for student in trimestre0:
        prom0+=student.get('promedio de notas')
        if prom0> 1*len(trimestre0):
            print(f'El promedio de los estudiantes rechazados es de: {prom0/len(trimestre0)}')
    return prom2, prom1, prom0, student, trimestre2, trimestre1, trimestre0
            
main()