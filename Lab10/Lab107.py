from abc import ABC, abstractmethod
import math

# Clase abstracta
class FuncionMatematica(ABC):
    @abstractmethod
    def evaluar(self, x):
        pass


# Función Lineal: f(x) = mx + b
class FuncionLineal(FuncionMatematica):
    def __init__(self, m, b):
        self.m = m
        self.b = b

    def evaluar(self, x):
        return self.m * x + self.b


# Función Cuadrática: f(x) = ax^2 + bx + c
class FuncionCuadratica(FuncionMatematica):
