class Humano: 

    def __init__(self, ojos, cabello, piel, altura, peso, genero="desconocido"):

        self.ojos = ojos
        self.caballo = cabello
        self.piel = piel
        self.altura = altura
        self.peso = peso

    def hablar(self):
        print("Hola, soy un humano y hablo")


gringo = Humano("marrones", "negro", "clara", 1.75, 70, "masculino")
chino = Humano("marrones", "negro", "amarillo", 1.65, 60, "masculino")

