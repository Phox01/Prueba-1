from horse import Horse
class Race:
    def __init__(self, number, horse_list):
        self.number = number
        self.horse_list= horse_list
    def start_race(self):
        print('Partidaaaaaaaaaaaaa')
        print('Salieron los competidores')
        for horse in self.horse_list:
            print(horse.name)
