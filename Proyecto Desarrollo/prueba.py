def printings(num_rows, num_cols):
     
    number = 10
    letter2 = 'A'
    asientos=[]
    for row in range(num_rows): 
       letter2='A' 
       for col in range(num_cols):
          print(f"{letter2}{number}", end=' ')
          asiento="{letter2}+{number}"
          asientos.append(asiento)
          letter2 = chr(ord(letter2) + 1)
       print("")
       number+=1
    return asientos
      