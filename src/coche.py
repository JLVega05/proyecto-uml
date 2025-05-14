from vehiculo import Vehiculo
from motor import Motor

class Coche(Vehiculo):
    def __init__(self, marca: str, modelo: str, motor: Motor):
        super().__init__(marca)
        self.modelo = modelo
        self.motor = motor 

    def __str__(self):
        return f"Coche: {self.marca} {self.modelo} | {self.motor}"