import sys
if len(sys.argv) == 3:
	if int(sys.argv[1])>0 and int(sys.argv[1])<10 and int(sys.argv[2])>0 and int(sys.argv[2])<10:
		rows = int(sys.argv[1])
		cols = int(sys.argv[2])
		for row in range(rows):
			for col in range(cols):
				print(" * ", end='')
	else:
		print("Error. Alguno de los argumentos no está entre 1 y 9")
else:
	print("Error, introduce los argumentos correctamente")
	print("Ejemplo: tabla.py 4 5")
