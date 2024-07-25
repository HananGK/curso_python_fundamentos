candidato = input("Elige entre el candidato A, B o C:")

if candidato.upper() == "A":
    print("Ha votado por el partido rojo")
elif candidato.upper() == "B":
    print("Ha votado por el candidato verde")
elif candidato.upper() == "C":
    print("Ha votado por el candidato azul")
else:
    print("Opción errónea")
