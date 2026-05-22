class Paquete:

    def __init__(self, id, volumen, fragil):
        self.id = id
        self.volumen = volumen
        self.fragil = fragil


def cargar_camiones(paquetes):

    camion = []
    fragiles = []

    total = 0

    for p in paquetes:

        if total + p.volumen <= 100:

            camion.append(p.id)
            total += p.volumen

        if p.fragil:
            fragiles.append(p.id)

    print(camion)
    print(fragiles)


p1 = Paquete(1, 20, True)
p2 = Paquete(2, 50, False)
p3 = Paquete(3, 40, True)

lista = [p1, p2, p3]

cargar_camiones(lista)