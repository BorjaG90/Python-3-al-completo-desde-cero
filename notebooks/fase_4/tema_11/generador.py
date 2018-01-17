import random
import math

def leer_numero(init, end, msg):
    while True:
        try:
            r = int( input(msg) )
        except:
            pass
        else:
            if r >= init and r <= end:
                break
    return r

def generador():
    numeros = leer_numero(1,20,"¿Cuantos números quieres generar? [1-20]: ")
    modo = leer_numero(1,3,"¿Cómo quieres redondear los números? [1]Al alza [2]A la baja [3]Normal: ")

    lista=[]
    for i in range(numeros):
        n = random.uniform(0,101)
        if modo == 1:
            print("Antes: {}, despues:{}".format(n,math.ceil(n)))
            n = math.ceil(n)
        elif modo == 2:
            print("Antes: {}, despues:{}".format(n,math.floor(n)))
            n = math.floor(n)
        else:
            print("Antes: {}, despues:{}".format(n,round(n)))
            n = round(n)
        lista.append(n)
    return lista

generador()