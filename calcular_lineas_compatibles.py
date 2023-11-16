
conjuntos_solucion = []
memoria_de_cota = [0 for _ in range(12)]
solucion_incompleta = []

def funcion_cota(t):
    # Comprobamos que no hay tres lineas distintas con el mismo digito
    for k in t:
        if memoria_de_cota[k] == 2:
            return False
    # Comprobamos que t tiene dos elementos distintos en comparación del resto
    # de lineas de la solucion incompleta
    for s in solucion_incompleta:
        i=j=0
        n_elementos_iguales = 0
        while i<4 and j<4:
            if t[i]<s[j]:
                i+=1
            elif t[i]>s[j]:
                j+=1
            else:
                i+=1
                j+=1
                n_elementos_iguales+=1
                if n_elementos_iguales==2:
                    return False
    return True

def avanzar_solucion(t):
    for d in t:
        memoria_de_cota[d]+=1
    solucion_incompleta.append(t)

def retroceder_solucion():
    t = solucion_incompleta.pop()
    for d in t:
        memoria_de_cota[d]-=1

def backtracking(cuadruplas, i):
    nivel = len(solucion_incompleta)
    num_cuadruplas = len(cuadruplas)
    if nivel == 6:
        # Solucion completa
        sol = tuple(solucion_incompleta)
        conjuntos_solucion.append(sol)
        return
    for j in range(i+1, num_cuadruplas):
        t = cuadruplas[j]
        es_factible = funcion_cota(t)
        if es_factible:
            avanzar_solucion(t)
            backtracking(cuadruplas, j)
            retroceder_solucion()

def calcular_lineas_compatibles(cuadruplas):
    backtracking(cuadruplas, -1)
    return conjuntos_solucion
