i = 0
numero = int(input("Ingresa un número entero: "))
mult = 0

while i<10:
    i += 1
    mult = numero * i
    print(" {} x {} = {}".format(numero, i, mult))