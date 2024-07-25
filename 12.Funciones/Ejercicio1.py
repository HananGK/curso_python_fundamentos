lista = []
numero = 0

def llenarLista():
    i=0
    while i<=5:
        numero = float(input("Ingresa un número: "))
        lista.append(numero)
        i += 1

def ordenar():
    lista.sort()
    listaPar = []
    listaImpar = []
    for i in lista:
        if i % 2 == 0:
            listaPar.append(i)
        else:
            listaImpar.append(i)
    print("Numeros pares: ", listaPar)
    print("Numeros impares: ", listaImpar)

llenarLista()
print(lista)
ordenar()

