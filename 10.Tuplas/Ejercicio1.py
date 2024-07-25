tupla = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

mes = int(input("Ingresa un numero del 1 al 12: ")) - 1
if mes <= 12:
    print("Se corresponde al mes de: ", tupla[mes])
else:
    print("Solo hay 12 meses")
