nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))

if nombre == "Hanan":
    if edad >= 18:
        print("Tu eres Hanan y eres mayor de edad")
    else:
        print("Tu eres Hanan y eres menor de edad")
else:
    print("Tu no eres Hanan")