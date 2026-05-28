from abc import ABC, abstractmethod
import math

# Clase abstracta
class Figura(ABC):
    @abstractmethod
    def calcularArea(self):
        pass


# Clase Circulo
class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def calcularArea(self):
        return math.pi * self.radio ** 2


# Clase Rectangulo
class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcularArea(self):
        return self.base * self.altura


# Clase Triangulo
class Triangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

