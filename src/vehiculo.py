class Vehiculo:
    def __init__(self, marca: str):
        self.marca = marca

    def __str__(self):
        return f"Vehículo: {self.marca}"