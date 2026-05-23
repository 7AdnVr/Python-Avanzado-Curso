class Articulo: 

    def __init__(self, nombre, categoria, precio): 
        self.nombre = nombre 
        self.categoria = categoria 
        self.precio = precio

descuentos = {
    "tecnologia": 0.8,
    "ropa": 0.5,
}

def procesar_carrito(lista):

    total = 0

    for articulo in lista:

        total += articulo.precio * descuentos[articulo.categoria]

        print(total)

a1 = Articulo("Laptop", "tecnologia", 1000)
a2 = Articulo("Camisa", "ropa", 50)

lista = [a1, a2]

procesar_carrito(lista)