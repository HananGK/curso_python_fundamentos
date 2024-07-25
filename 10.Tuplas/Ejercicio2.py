tupla = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")

letra = int(input("Ingresa un número: ")) - 1

if letra < len(tupla):
    print("Se corresponde con la letra {} del abecedario".format(tupla[letra]))
else:
    print("No hay tantas letras")
