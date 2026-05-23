class Credencial:

    def __init__(self, servicio, password):
        self.servicio = servicio
        self.password = password

def validar_fortaleza(credencial):

    mayus = False
    numero = False

    for letra in credencial.password:

        if letra.isupper():
            mayus = True

        if letra.isdigit():
            numero = True

    if mayus and numero and len(credencial.password) >= 8:
        return True
    
    return False

c1 = Credencial("Facebook", "12345678")

print(validar_fortaleza(c1))