class Universidad():
    def __init__(self, nombreU):
        self._nombreU = nombreU

    @property
    def nombreU(self):
        return self._nombreU

class Carrera():
    def __init__(self, especialidad):
        self._especialidad = especialidad

    @property
    def especialidad(self):
        return self._especialidad

class Estudiante():
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre
    
class Persona(Universidad, Carrera, Estudiante):
    def __init__(self, nombreU, especialidad, edad, nombre):
        Universidad.__init__(self, nombreU)
        Carrera.__init__(self, especialidad)
        Estudiante.__init__(self, nombre, edad)

    def imprimir(self):
        print("Universidad: {}\nCarrera: {}\nNombre: {}\nEdad: {}".format(self.nombreU, self.especialidad, self.nombre, self._edad))

persona=Persona("UNIVERSIDAD","ESPECIALIDAD","EDAD","NOMBRE")
persona.imprimir()



