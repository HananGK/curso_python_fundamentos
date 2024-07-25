class Estudiante():

    def __init__(self, nombre, nota):
        self._nombre = nombre
        self._nota = nota

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    
    @property
    def nota(self):
        return self._nota

    @nota.setter
    def nota(self, nota):
        self._nota = nota

    def imprimir(self):
        print("Nombre:{} \nNota: {}".format(self.nombre, self.nota))

    def resultado(self):
        if self._nota >= 5:
            print("El/la estudiante {} ha aprobado con un {}".format(self.nombre, self.nota))
        else:
            print("El/la estudiante {} ha suspendido con un {}".format(self.nombre, self.nota))

estudiante = Estudiante("Hanan", 9)
estudiante.imprimir()
estudiante.resultado()

estudiante2 = Estudiante("Ángel", 3)
estudiante2.imprimir()
estudiante2.resultado()