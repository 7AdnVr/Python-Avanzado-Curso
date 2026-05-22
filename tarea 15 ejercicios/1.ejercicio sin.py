class Cuenta:

    def __init__(self, numero, titular, saldo):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.historial = []


cuentas = {}


def ejecutar_transferencia(origen, destino, monto):

    if origen in cuentas and destino in cuentas:

        if cuentas[origen].saldo >= monto:

            cuentas[origen].saldo -= monto
            cuentas[destino].saldo += monto

            cuentas[origen].historial.append(monto)
            cuentas[destino].historial.append(monto)

            print("Transferencia realizada")

        else:
            print("Saldo insuficiente")

    else:
        print("Cuenta no encontrada")


c1 = Cuenta(1, "Juan", 500)
c2 = Cuenta(2, "Ana", 300)

cuentas[1] = c1
cuentas[2] = c2

ejecutar_transferencia(1, 2, 200)
