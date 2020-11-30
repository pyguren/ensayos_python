class Coche:

    color = "Rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 500
    puestos = 2

    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad += 1

    def getVelocidad(self):
        return self.velocidad

    def setColor(self, color):
        self.color = amarill

    def getColor(self)
    return self.color

# fin definicion de la clase


coche = Coche()
print(coche.marca, coche.color)
print("velocidad actual: ", coche.velocidad)
