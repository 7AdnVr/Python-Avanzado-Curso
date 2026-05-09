class Estudiante:

    def __init__(self, edad, cedula, año="desconocido"):
        self.edad = edad
        self.cedula = cedula
        self.año = año

    def mostrar_info(self):
        print(f"Edad -> {self.edad}")
        print(f"Cedula -> {self.cedula}")
        print(f"Año -> {self.año}")

marcelo = Estudiante(16, 31006943, año="secundaria")
juan = Estudiante(10, 32054345, año="primer")

marcelo.mostrar_info()
juan.mostrar_info()