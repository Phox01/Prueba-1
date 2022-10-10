##Numeros oblongos
while True:
    p_number=int(input('Please enter a number'))
    numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9]
    for n in numbers:
        x=int(n*(n+1))
        if p_number==x:
            print(f'The number {p_number} is a pronic number')
        else:
            continue
