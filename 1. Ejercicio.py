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

class EstudianteDeportista(Estudiante):

    def __init__(self, edad, cedula, año="desconocido", deporte="desconocido"):
        super().__init__(edad, cedula, año)
        self.deporte = deporte

    def club(self):
        print(f"Estoy en el club deportivo de -> {self.deporte}.")

    def entrenar(self):
        print(f"Estoy entrenando -> {self.deporte}.")

class EstudianteNota(Estudiante):

    def __init__(self, edad, cedula, año="desconocido", nota="desconocido"):
        super().__init__(edad, cedula, año)
        self.nota = nota

    def calificacion(self):
        print(f"Mi promedio es -> {self.nota}")

    def estudiar(self):
        print("Estoy estudiando para mejorar mi nota.")

maria = EstudianteDeportista(16, 12345678, "secundaria", "voleibol")
pedro = EstudianteNota(15, 87654321, "secundaria", 18)

maria.club()
maria.entrenar()

pedro.calificacion()
pedro.estudiar()