number=int(input('Enter a number: '))
x=1
count=0
def is_primo(count, number, x):
    while True:
        if number%x==0:
            count+=1
        
        if x>number:
            print(f'The {number} is not primo')
            break
        if count==2:
            print(f'The {number} is primo')
            break
        x+=1
is_primo(count, number, x)

