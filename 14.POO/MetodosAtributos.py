class FabricaTelefonos():
    marca = "Huawei"
    color = "Negro"
    memoriaRam = 32
    almacenamiento = 128

    def llamar(self, mensaje):
        return mensaje
    
    def escuharMusica(self):
        print("Estás escuchando música")

telefono= FabricaTelefonos()
'''print(telefono)''' #nos muestra el espacio de  memoria que ocupa
print(telefono.marca, telefono.color, telefono.memoriaRam, telefono.almacenamiento)

print(telefono.llamar("Hola, ¿Con quién hablo?"))
telefono.escuharMusica()