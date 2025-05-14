from vehiculo import Vehiculo
from motor import Motor

class Camion(Vehiculo):
    def __init__(self, marca: str, carga_maxima: float, motor: Motor):
        super().__init__(marca)
        self.carga_maxima = carga_maxima
        self.motor = motor  

    def __str__(self):
        return f"Camión: {self.marca} | Carga: {self.carga_maxima}kg | {self.motor}"