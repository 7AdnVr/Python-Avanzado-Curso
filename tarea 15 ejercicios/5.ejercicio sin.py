class Evento:

    def __init__(self, nombre, capacidad, invitados):
        self.nombre = nombre
        self.capacidad = capacidad
        self.invitados = invitados


vips = {"Carlos", "Maria"}


def ingresar_asistente(evento, nombre):

    if len(evento.invitados) < evento.capacidad:

        if nombre in vips:
            evento.invitados[nombre] = "VIP"
        else:
            evento.invitados[nombre] = "Normal"

        print("Ingreso permitido")

    else:
        print("Evento lleno")


evento = Evento("Concierto", 3, {})

ingresar_asistente(evento, "Carlos")
ingresar_asistente(evento, "Luis")

print(evento.invitados)