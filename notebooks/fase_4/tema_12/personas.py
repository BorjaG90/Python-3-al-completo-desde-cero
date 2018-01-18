from io import open

fichero = open('personas.txt','r', encoding="utf8")
lineas = fichero.readlines()
fichero.close()
personas = []
for linea in lineas:
    linea = linea.replace("\n", "")
    persona = {
        'id':linea.split(';')[0],
        'nombre':linea.split(';')[1],
        'apellido':linea.split(';')[2],
        'nacimiento':linea.split(';')[3]
    }
    personas.append(persona)
for p in personas:
    print("Id: {} - {} {}, {}".format(p['id'],p['nombre'],p['apellido'],p['nacimiento']))



