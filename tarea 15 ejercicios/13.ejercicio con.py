class Candidato:

    def __init__(self, nombre, partido):
        self.nombre = nombre
        self.votos = partido

def escrutar_votos(votos):
    
    resultados = {}

    for voto in votos:

        if voto in resultados:
            resultados[voto] += 1
        else:
            resultados[voto] = 1

    ganador = max(resultados, key=resultados.get)

    print(resultados)
    print(f"El ganador es: {ganador}")

votos = ["Candidato A", "Candidato B", "Candidato A", "Candidato C", "Candidato B", "Candidato A"]

escrutar_votos(votos)