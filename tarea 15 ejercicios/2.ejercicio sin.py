class Guerrero:

    def init(self, vida, ataque, defensa, estados):
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.estados = estados


def ejecutar_ronda(g1, g2):

    while g1.vida > 0 and g2.vida > 0:

        dano1 = g1.ataque - g2.defensa

        if dano1 < 0:
            dano1 = 0

        g2.vida -= dano1

        if g2.vida <= 0:
            print("Gana guerrero 1")
            break

        dano2 = g2.ataque - g1.defensa

        if dano2 < 0:
            dano2 = 0

        g1.vida -= dano2

        if g1.vida <= 0:
            print("Gana guerrero 2")


g1 = Guerrero(100, 30, 10, ("furia",))
g2 = Guerrero(90, 25, 5, ("veneno",))

ejecutar_ronda(g1, g2)
