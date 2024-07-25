'''while True:
    try:
        num1 = int(input("Ingresa un número: "))
        resultado = 100 / num1
        print("El resultado es: ", resultado)
        break
    except ZeroDivisionError:
        print("No se puede dividir por 0")'''

'''while True:
    try:
        edad = int(input("Ingresa tu edad: "))
        print("Tu edad es: ", edad)
        break
    except ValueError:
        print("Has colocado un valor erróneo")'''

while True:
    try:
        edad = int(input("Ingresa tu edad: "))
        print("Tu edad es: ", edad)
        break
    except KeyboardInterrupt:
        print("\nHas cancelado la ejecución")
        break

