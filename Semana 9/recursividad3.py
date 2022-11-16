##invertir una palabra recursivamente

def recursividad(word, index):
    if index==0:
        return word[index]
    else:
        return word[index]+recursividad(word, index-1)    



def main():
    word=input('Ingrese una palabra: ')
    x=recursividad(word, len(word)-1)
    print(x)

main()