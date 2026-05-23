class Empleado:

    def __init__(self, nombre, bruto, contrato):
        self.nombre = nombre
        self.bruto = bruto
        self.contrato = contrato

impuestos = {
    "fijo": 0.10,
    "temporal": 0.05
}

def liquidar_nomina(lista):

    for empleado in lista:

        descuento = empleado.bruto * impuestos[empleado.contrato]
        neto = empleado.bruto - descuento

        if empleado.bruto > 100:
            neto -= 200

        print(empleado.nombre, neto)

e1 = Empleado("Juan", 150, "fijo")
e2 = Empleado("Ana", 80, "temporal")

lista = [e1, e2]

liquidar_nomina(lista)