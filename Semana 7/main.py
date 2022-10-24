from horse import Horse
from valida import Valid
from carrera import Race
def main():
    valids=int(input('how many valids do you want: '))
    races=int(input('how many races do you want for each valid: '))
    horse1=Horse('El rayo veloz', 1)
    horse2=Horse('Ivan', 2)  
    horse3=Horse('Bernardo', 3)  
    horse4=Horse('Ornaldo', 4)  
    horse5=Horse('Juan', 5)  
    horse6=Horse('Manolo', 6)
    horse_list=[horse1, horse2, horse3, horse4, horse5, horse6]
    for valid in range(valids):
        race_list=[]
        
        for race in range(races):
            
            race_objetc= Race(race, horse_list)
            race_list
main()