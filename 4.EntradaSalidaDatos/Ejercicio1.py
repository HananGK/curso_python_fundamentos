a = float(input("Ingresa el valor de a: "))
b = float(input("Ingresa el valor de b: "))
c = float(input("Ingresa el valor de c: "))

solucion1 = ((-b)+(((b**2)-(4*a*c))**0.5))/(2*a)
solucion2 = ((-b)-(((b**2)-(4*a*c))**0.5))/(2*a)

print("Las soluciones son: ", solucion1, " y ", solucion2)