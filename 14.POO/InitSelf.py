'''class FabricaTelefonos():
    marca = "Samsung"

    def ElaborarHuawei(self):
        self.marca = "Huawei"

telefono = FabricaTelefonos()

print(telefono.marca)

telefono.ElaborarHuawei()
print(telefono.marca)'''

class FabricaTelefonos:
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color

telefono = FabricaTelefonos("Huawei", "Negro")
print(telefono.marca)


