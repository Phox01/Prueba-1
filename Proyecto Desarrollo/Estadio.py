class Estadio:
    def __init__(self, name, location, id, capacity, restaurant):
        self.name=name
        self.location=location
        self.id=id
        self.capacity=capacity
        self.restaurant=restaurant

    def printings(self, selections):
     
        number = "10"
        letter2 = 'A'
        asientos=[]
        for row in range(self.capacity[0]):
            letter2='A' 
            for col in range(self.capacity[1]):
                i=0
                asiento=letter2+number
                for x in selections:
                    if x ==asiento:
                        print("[X]", end=' ')
                        letter2 = chr(ord(letter2) + 1)
                        asiento=letter2+number
                        #i+=1
                        i+=1
                        #self.capacity[1]
                        break
                if i==1:
                    pass
                else:
                    print(asiento, end=' ')
                    asientos.append(asiento)
                    letter2 = chr(ord(letter2) + 1)
                
                
            print("")
            number=int(number)
            number+=1
            number=str(number)
            #self.capacity[1]+=i
        return asientos

