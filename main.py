from calcular_cuadruplas import calcular_cuadruplas
from calcular_lineas_compatibles import calcular_lineas_compatibles
from calcular_soluciones import resolver

cuadruplas = calcular_cuadruplas()
print(f"{len(cuadruplas)} cuadruplas")
for t in cuadruplas:
    print(t)

conjuntos_lineas = calcular_lineas_compatibles(cuadruplas)
print(f"{len(conjuntos_lineas)} conjuntos de líneas compatibles")
for t in conjuntos_lineas:
    print(t)

soluciones = resolver(conjuntos_lineas)
print(f"{len(soluciones)} soluciones")
for sol in soluciones:
    print(sol)
