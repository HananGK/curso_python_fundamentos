P1 = float(input("Ingresa la nota de la primera práctica: "))
P2 = float(input("Ingresa la nota de la segunda práctica: "))
P3 = float(input("Ingresa la nota de la tercera práctica: "))
EP = float(input("Ingresa la nota del examen parcial: "))
EF = float(input("Ingresa la nota del examen final: "))

#promedio prácticas
PP = (P1+P2+P3)/3

#promedio curso
PROM = (PP+(2*EP)+(3*EF))/6

print("El promedio del alumno en este curso es de: ", PROM)