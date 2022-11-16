##Exponencial

def exponencial(base, exponente):
    
    count=1
    if exponente==0:
        return 1
    return base*exponencial(base, exponente-1)

def main():
    base=int(input('Por favor, ingrese una base'))
    exponente=int(input('Por favor, ingrese un exponente'))
    exponencial(base, exponente)

main()