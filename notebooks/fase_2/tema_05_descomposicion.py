import sys
if len(sys.argv) == 2:
	if int(sys.argv[1])>0:
		cad = str(sys.argv[1])
		num = len(cad)
		for n in range(num):
			print( "{:04d}".format( int(cad[num-1-n]) * 10 ** n ))
	else:
		print("El argumento es erroneo")
		print("Procura que sea un entero positivo")
else:
	print("Error, introduce los argumentos correctamente")
	print("Ejemplo: descomposicion.py [0-9999]")