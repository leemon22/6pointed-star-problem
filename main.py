from calcular_cuadruplas import calcular_cuadruplas
from calcular_lineas_compatibles import calcular_lineas_compatibles
from calcular_soluciones import resolver
from time import time_ns

t_inicio = time_ns()

cuadruplas = calcular_cuadruplas()
conjuntos_lineas = calcular_lineas_compatibles(cuadruplas)
soluciones = resolver(conjuntos_lineas)

t_fin = time_ns()
t_total = (t_fin - t_inicio)/10**6

soluciones = sorted(soluciones)

print(f"{len(soluciones)} soluciones en {t_total} ms")
i = 0
for sol in soluciones:
    print(f"solución número {i}: {sol}")
    i+=1
