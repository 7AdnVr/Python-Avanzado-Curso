class ProductoCarrito:

    def __init__(self, nombre, paso, precio):
        self.nombre = nombre
        self.paso = paso
        self.precio = precio

tarifas = {
    "normal": 10
}

def checkout_final(lista):

    total = 0
    peso_total = 0

    for producto in lista:

        total += producto.precio
        peso_total += producto.paso

    if total < 100:
        total += tarifas["normal"] * peso_total

    print(f"Total a pagar: {total}")
    print(f"Peso total: {peso_total}")

p1 = ProductoCarrito("Producto A", 2, 30)
p2 = ProductoCarrito("Producto B", 3, 50)

lista = [p1, p2]

checkout_final(lista)