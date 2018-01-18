from io import open

fichero = open('contador.txt','a+', encoding="utf8")
fichero.seek(0)
texto = fichero.readline()

if len(texto) == 0:
    texto = "0"
    fichero.write(texto)

fichero.close()
try:
    contador = int(texto)

    if len(sys.argv) == 2:
        if sys.argv[1] == "inc":
            contador += 1
        elif sys.argv[1] == "dec":
            contador -= 1

    print(contador)

    fichero = open("contador.txt", "w", encoding="utf8")
    fichero.write( str(contador) )
    fichero.close()
except:
    print("Error: Fichero corrupto.")