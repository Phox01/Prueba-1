class Ticket:
    def __init__(self, id, type, seat, owner, code, validate, estadio):
        self.id=id
        self.type=type
        self.seat=seat
        self.owner=owner
        self.code=code
        self.validate=False
        self.estadio=estadio