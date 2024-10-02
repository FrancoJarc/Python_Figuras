from abc import ABC, abstractmethod
from figura import Figura

class Circulo(Figura):
    def __init__(self, color, radio):
        super().__init__(color)  # Llama al constructor de Figura
        self.radio = radio

    def area(self):
        return 3.14*(self.radio*self.radio)

    def perimetro(self):
        return (2*3.14*self.radio)