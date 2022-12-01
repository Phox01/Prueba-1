def factorial(number, count):
    if number>1:
        count*=number*(number-1)
        return factorial(number-2, count)
    elif number==1 or number==0:
        print(count)

count=1
factorial(6, count)



