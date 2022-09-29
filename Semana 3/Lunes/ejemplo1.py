squares_2=[x**2 for x in range (9) if x%2 ==0]
squares=[]
for x in range (9):
    if x%2==0:
        squares.append(x)
        print(x)