##Numeros oblongos
n=1
while True:
    p_number=int(input('Please enter a number'))
    if p_number%n==0:
        x=n*(n+1)
        if p_number==x:
            print(f'The number {p_number} is a pronic number')
            break
    else:
        n+=1
