import json

edd={"variable1":1, "var":2}

with open("edd.json", "w") as w:
    c=json.dumps(edd, indent="  ")
    w.write(c)
    w.close()

with open("cargar.json", "r") as r:
    read=r.read()
    c=json.loads(read)
    print(c)