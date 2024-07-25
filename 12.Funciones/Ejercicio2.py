import math
def factorial():
    num = int(input("Ingresa un número entero positivo: "))
    if num>0:
        print(math.factorial(num))

        '''factorial=1
            for i in range(1, num+1):
                factorial = factorial * i
            print(factorial)'''
        
    else:
        print("El factorial de un número negativo no existe")

factorial()