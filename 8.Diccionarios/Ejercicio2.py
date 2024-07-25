diccionario = {1 : "Casillas", 15 : "Ramos", 3 : "Pique", 5 : "Puyol", 11 : "Capdevila", 14 : "Xabi Alonso", 16 : "Busquets", 8 : "Xavi Hernandez", 18 : "Pedrito", 6 : "Iniesta", 7 : "Villa"}

numero= int(input("Ingresa un número del 1 al 20: "))
if numero in diccionario:
    print("El nombre del jugador es: ", diccionario[numero])
else:
    print("El número no se encuentra en el diccionario")