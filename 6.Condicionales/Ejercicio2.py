numero = int(input("Ingresa un número entero: "))

if numero >= 0:
    print("El valor absoluto de {} es {}".format(numero, numero))
else:
    print("El valor absoluto de {} es {}".format(numero, numero*(-1)))