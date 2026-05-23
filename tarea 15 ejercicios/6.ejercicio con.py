class videojuego:

    def __init__(self, titulo, plataforma, horas):
        self.titulo = titulo
        self.plataforma = plataforma
        self.horas = horas

def obtener_favoritos(lista):

    favoritos = []

    for juego in lista:

        if juego["horas"] > 100:
            favoritos.append(juego["titulo"])
    return favoritos

juegos = [
    {"titulo": "Minecraft", "plataforma": "PC", "horas": 150},
    {"titulo": "Fortnite", "plataforma": "PC", "horas": 50},
    {"titulo": "The Legend of Zelda: Breath of the Wild", "plataforma": "Nintendo Switch", "horas": 200}
]

print(obtener_favoritos(juegos))
