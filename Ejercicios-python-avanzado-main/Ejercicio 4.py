import math
from abc import ABC, abstractmethod

print("Ejercicio 4: Abstractas y Métodos Abstractos\n")

class FiguraGeometrica(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

class Circulo(FiguraGeometrica):
    def __init__(self, radio: float):
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio ** 2
    
    def calcular_perimetro(self):
        return 2 * math.pi * self.radio
    
class Rectangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

mi_circulo = Circulo(5)
mi_rectangulo = Rectangulo(4, 6)
print("Área del círculo:", mi_circulo.calcular_area())
print("Perímetro del círculo:", mi_circulo.calcular_perimetro())
print("Área del rectángulo:", mi_rectangulo.calcular_area())
print("Perímetro del rectángulo:", mi_rectangulo.calcular_perimetro())
print("\n")
