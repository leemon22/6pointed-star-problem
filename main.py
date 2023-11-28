from calcular_cuadruplas import calcular_cuadruplas
from calcular_lineas_compatibles import calcular_lineas_compatibles
from calcular_soluciones import resolver
from time import time_ns

t_inicio = time_ns()

'''
Calcula las posibles cuadruplas (a,b,c,d) tales que: 
    - a,b,c,d son enteros entre el 0 y el 11, ambos incluidos
    - a<b<c<d
    - a+b+c+d=22
Estas cuadruplas son los conjuntos de números que pueden haber en una línea de la estrella
'''
cuadruplas = calcular_cuadruplas()

'''
De entre todos los posibles conjuntos de 6 líneas, tomamos los que cumplen estas 2 condiciones,
basadas en la geometría de la estrella:
    - Cada número desde el 0 hasta el 11, ambos incluidos, no aparecen más de 2 veces repetidos.
    - Ningún par de líneas puede compartir más de 1 valor.
Como tenemos conjuntos de 6 líneas y cada línea tiene 4 valores, en total tenemos 24 valores en 
el conjunto de 6 líneas. Aplicando la primera propiedad, se tiene que cada valor aparece
exactamente 2 veces en cada conjunto de 6 líneas, como se deseaba en un primer momento.
'''
conjuntos_lineas = calcular_lineas_compatibles(cuadruplas)

'''
Com ya los conjuntos de 6 líneas calculados, obtenemos la solución final.
Ver el README.md para ver el formato de las soluciones.
'''
soluciones = resolver(conjuntos_lineas)

t_fin = time_ns()
t_total = (t_fin - t_inicio)/10**6

'''
Ordenamos las soluciones para mostrarlas mejor por pantalla y comprobar que no hay repetidas.
'''
soluciones = sorted(soluciones)

print(f"{len(soluciones)} soluciones en {t_total} ms")
i = 0
for sol in soluciones:
    print(f"solución número {i}: {sol}")
    i+=1
