from coche import Coche
from camion import Camion
from motor import Motor

motor_v8 = Motor("V8")
motor_diesel = Motor("Diésel")

mi_coche = Coche("Toyota", "Corolla", motor_v8)
mi_camion = Camion("Volvo", 5000.0, motor_diesel)

print(mi_coche)
print(mi_camion)