from abc import ABC, abstractmethod
from circulo import Circulo
from cuadrado import Cuadrado
from figura import Figura

cuadrado= Cuadrado ("rojo",2)
circulo= Circulo("rojo",2)

print(cuadrado.area())
print(cuadrado.perimetro())
print(circulo.area())
print(circulo.perimetro())