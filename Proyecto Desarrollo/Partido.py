class Partido:
    def __init__(self, lteam, vteam, date, hour, estadio, id, asistencia):
        self.lteam=lteam
        self.vteam=vteam
        self.date=date
        self.hour=hour
        self.estadio=estadio
        self.id=id
        self.asistencia=asistencia
    def Show(self):
        print(f"{self.lteam} vs {self.vteam} en el {self.estadio} (Id:{self.id})\nFecha:{self.date} Hora:{self.hour}")
        print("---------------------------------------------------")