class Motor:
    def __init__(self, tipo: str):
        self.tipo = tipo

    def __str__(self):
        return f"Motor: {self.tipo}"