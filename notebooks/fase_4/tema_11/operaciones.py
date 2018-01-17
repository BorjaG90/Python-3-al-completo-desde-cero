def sumar(a,b):
    try:
        r = a+b
    except TypeError:
        print("Error. Tipo de dato no válido.")
    else:
        return r
def restar(a,b):
    try:
        r = a-b
    except TypeError:
        print("Error. Tipo de dato no válido.")
    else:
        return r
def multiplicar(a,b):
    try:
        r = a*b
    except TypeError:
        print("Error. Tipo de dato no válido.")
    else:
        return r
def dividir(a,b):
    try:
        r = a/b
    except TypeError:
        print("Error. Tipo de dato no válido.")
    except ZeroDivisionError:
        print("Error. No es posible dividir entre cero.")
    else:
        return r
