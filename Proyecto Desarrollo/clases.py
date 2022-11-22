class Equipo:
    def __init__(self, name, flag, code, group):
        self.name=name
        self.flag=flag
        self.code=code
        self.group=group

class Estadio:
    def __init__(self, name, location):
        self.name=name
        self.location=location

class Partido:
    def __init__(self, lteam, vteam, date_hour, estadio):
        self.lteam=lteam
        self.vteam=vteam
        self.date_hour=date_hour
        self.estadio=estadio
        
