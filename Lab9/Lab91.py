from abc import ABC, abstractmethod

# Interfaz / Clase abstracta
class Animal(ABC):
    @abstractmethod
    def hacer_sonido(self):
        pass

# Clase que implementa la interfaz
class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"

# Prueba
p = Perro()
print(p.hacer_sonido())
