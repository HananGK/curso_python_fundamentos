class A():
    def __init__(self):
        self._cuenta = 0
        self._contador = 0

    @property #metodo get q puede ser llamado como si fuera un atributo
    def cuenta(self):
        return self._cuenta
    
    @property
    def contador(self):
        return self._contador

a = A ()

print(a.cuenta)
print(a.contador)