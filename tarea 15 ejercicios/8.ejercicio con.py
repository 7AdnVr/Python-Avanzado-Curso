class Vuelo:

    def __init__(self, numero, asientos):
        self.numero = numero
        self.asientos = asientos

def reservar_asiento(vuelo, dato):

    asiento, tarifa = dato

    if asiento not in vuelo.asientos:

        vuelo.asientos.add(asiento)
        print("Reservado")
        print("Tarifa: ", tarifa)

    else:
        print("Asiento no disponible")

v = Vuelo("AV123", set())
reservar_asiento(v, ("1A", 100))