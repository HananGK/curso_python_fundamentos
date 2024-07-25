class Calculadora():
  
    def __init__(self):
        self._num1  = int(input("Ingresa un número: "))
        self._num2 = int(input("Ingresa otro número: "))
        
    @property
    def num1(self):
        return self._num1
    
    @num1.setter
    def num1(self, num1):
        self._num1 = num1

    @property
    def num2(self):
        return self._num2

    def suma(self):
        return self._num1 + self._num2
    
    def resta(self):
        return self._num1 - self._num2
    
    def multiplicacion(self):
        return self._num1 * self._num2
    
    def division(self):
        if self._num2 == 0:
            return "No se puede dividir por 0"
        else:
            return self._num1 / self._num2
        
    def resultados(self):
        print("La suma es: ", self.suma())
        print("La resta es: ", self.resta())
        print("La multiplicacion es: ", self.multiplicacion())
        print("La division es: ", self.division())
        

calculadora = Calculadora()

calculadora.resultados()

