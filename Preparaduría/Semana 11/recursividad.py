lista = [ 
    ["DOWN","RIGHT","RIGHT","RIGHT","RIGHT","RIGHT","DOWN"],
    ["DOWN","DOWN","LEFT","LEFT","LEFT","LEFT","LEFT"], 
    ["DOWN","WALL","RIGHT","DOWN","DOWN","LEFT","LEFT"],
    ["RIGHT","RIGHT","UP","DOWN","DOWN","RIGHT","DOWN"], 
    ["WALL","DOWN","LEFT","LEFT","RIGHT","UP","DOWN"],
    ["UP","RIGHT","RIGHT","RIGHT","RIGHT","RIGHT","DOWN"],
    ["UP","LEFT","LEFT","LEFT","LEFT","LEFT","EXIT"]
]


def recorrer(lista, x, y):
    if lista[x][y]=="RIGHT":
        print("YOU MOVED RIGHT")
        return recorrer(lista, x, y+1)
    elif lista[x][y]=="LEFT":
        print("YOU MOVED LEFT")
        return recorrer(lista, x, y-1)
    elif lista[x][y] == "DOWN":
        print("YOU MOVED DOWN")
        return recorrer(lista, x+1, y)
    elif lista[x][y] == "UP":
        print("YOU MOVED UP")
        return recorrer(lista, x-1, y)
    elif lista[x][y]=="WALL":
        print("STOP, THERE IS NO WAY HERE")
    elif lista[x][y]=="EXIT":
        print("YOU DID IT")

recorrer(lista, 0, 0)