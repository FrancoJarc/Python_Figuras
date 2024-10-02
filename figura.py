from abc import ABC, abstractmethod

class Figura(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass