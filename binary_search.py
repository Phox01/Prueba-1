from selection import selection 

def main ():
    lista =[6, 5, 3, 1, 8, 7, 2, 4]
    lista= selection(lista)
    number= int(input('Please, enter a number: '))
    if binary_search(lista, number) !=-1:


def binary_search(lista, number):
    start=0
    final=len(lista)-1
    middle= (start + final)//2
    if len(lista)==1:
        if lista[0]==number:
            return number
        else:
            return -1
    if number >