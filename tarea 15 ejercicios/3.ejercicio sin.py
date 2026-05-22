class Equipo:

    def init(self, nombre, puntos):
        self.nombre = nombre
        self.puntos = puntos


def generar_emparejamientos(lista):

    lista.sort(key=lambda x: x.puntos, reverse=True)

    emparejamientos = {}

    i = 0

    while i < len(lista) - 1:

        emparejamientos[lista[i].nombre] = lista[i + 1].nombre

        i += 2

    return emparejamientos


e1 = Equipo("A", 20)
e2 = Equipo("B", 15)
e3 = Equipo("C", 10)
e4 = Equipo("D", 5)

lista = [e1, e2, e3, e4]

print(generar_emparejamientos(lista))