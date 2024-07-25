palabra1 = input("Ingresa una palabra: ")
palabra2 = input("Ingresa una segunda palabra: ")

if len(palabra1) < 3 or len(palabra2) < 3:
    print ("No rima, porque tienen menmos de 3 caracteres")
elif palabra1[-3: ] == palabra2[-3: ]:
    print("Las palabras riman")
elif palabra1[-2: ] == palabra2[-2: ]:
    print("Las palabras riman un poco")
else:
    print("Las palabras no riman")