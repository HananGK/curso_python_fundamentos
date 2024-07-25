def comparar():
    num1 = float(input("Ingresa un numero: "))
    num2 = float(input("Ingresa otro numero: "))

    if num1 > num2:
        return 1
    elif num2 > num1:
        return -1
    else:
        return 0
    
print(comparar())