##Los números de la suceción de Fibonacci son: 1, 1, 2, 3, 5, 8, 13, 21, 34...
a=0
b=1
while True:
    f_number=int(input('Please enter a integer number: '))
    while True:
        f = int(a + b)
        #s= f
        if f_number==f:
                print(f'The number {f_number} is a number of the fibonacci sequence')
                break
        else:
            a=b
            b=f
    if input('Do you wanna exit? Type "y" to exit, else to continue, \n ')=='y':
        break 
    f=0
    a=0
    b=1
    continue