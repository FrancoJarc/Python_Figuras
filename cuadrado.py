from abc import ABC, abstractmethod
from figura import Figura

class Cuadrado(Figura):
    def __init__(self, color, lado):
        super().__init__(color)  # Llama al constructor de Figura
        self.lado = lado

    def area(self):
        return self.lado*self.lado

    def perimetro(self):
        return self.lado*4