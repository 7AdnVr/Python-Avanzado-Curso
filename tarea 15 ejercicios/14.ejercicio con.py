class RegistroClima:

    def __init__(self, fecha, temperaturas):
        self.fecha = fecha
        self.temperaturas= temperaturas

def detectar_anomalias(lista):

    anomalias = set()

    for registro in lista:

        suma = 0

        for temp in registro.temperaturas:
            suma += temp

        media = suma / len(registro.temperaturas)

        if media > 30:
            anomalias.add(registro.fecha)

    print(anomalias)

r1 = RegistroClima("2024-01-01", [28, 29, 31, 30])
r2 = RegistroClima("2024-01-02", [25, 27, 26, 24])
r3 = RegistroClima("2024-01-03", [32, 33, 31, 34])

lista = [r1, r2, r3]

detectar_anomalias(lista)
