class Estudiante:

    def __init__(self, matricula, nombre, notas):
        self.matricula = matricula
        self.nombre = nombre
        self.notas = notas

def generar_actas(lista):

    for estudiante in lista:

        suma = 0

        for nota in estudiante.notas:
            suma += nota

        promedio = suma / len(estudiante.notas)

        if promedio >= 10:
            print(f"{estudiante.nombre} Aprobado")
        else:
            print(f"{estudiante.nombre} Reprobado")
e1 = Estudiante("2024-001", "Juan", [12, 14, 9])
e2 = Estudiante("2024-002", "Maria", [8, 7, 9])

lista = [e1, e2]

generar_actas(lista)