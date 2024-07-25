class Fabrica():
    def __init__(self, llantas, color, precio):
        self._llantas = llantas
        self._color = color
        self._precio = precio

    @property
    def llantas(self):
        return self._llantas
    
    @property
    def color(self):
        return self._color
    
    @property
    def precio(self):
        return self._precio
    
    @llantas.setter
    def llantas(self, llantas):
        self._llantas = llantas

    @color.setter
    def color(self, color):
        self._color = color

    @precio.setter
    def precio(self, precio):
        self._precio = precio

    def caracteristicas(self):
        print("Llantas: {}".format(self._llantas))
        print("Color: {}".format(self._color))
        print("Precio: {}".format(self._precio))

class Moto(Fabrica):
    pass

class Coche(Fabrica):
    pass

moto=Moto(2,"Rojo",10000)
moto.caracteristicas()

coche=Coche(4,"Azul",20000)
coche.caracteristicas()