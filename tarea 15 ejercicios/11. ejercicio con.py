class Mascota:

    def __init__(self, nombre, especie, urgencia):
        self.nombre = nombre
        self.especie = especie
        self.urgencia = urgencia

def asignar_consultorio(lista):

    usados = set()

    lista.sort(key=lambda x: x.urgencia, reverse=True)

    for mascota in lista:
        
        numero = len(usados) + 1

        usados.add(numero)

        print(f"{mascota.nombre} asignada al consultorio {numero}")

m1 = Mascota("Firulais", "perro", 5)
m2 = Mascota("Michi", "gato", 8)

lista = [m1, m2]

asignar_consultorio(lista)