class Partido:
    def __init__(self, lteam, vteam, date, hour, estadio, id):
        self.lteam=lteam
        self.vteam=vteam
        self.date=date
        self.hour=hour
        self.estadio=estadio
        self.id=id
    def Show(self):
        print(f"{self.lteam.name} vs {self.vteam.name} en el {self.estadio.name} (Id:{self.id})\nFecha:{self.date} Hora:{self.hour}")
        print("==========================")