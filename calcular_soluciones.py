from itertools import permutations

# Aplicamos una reflexión distinta dependiendo si el 0 está en la posición 0 o 1
# El eje de reflexión pasa por el 0 y el centro de la estrella
def reflejar(solucion):
    sol = list(solucion)
    if sol[0] == 0:
        for i in range(1,5):
            sol[i], sol[12-i] = sol[12-i], sol[i]
    else:
        sol[0], sol[2] = sol[2], sol[0]
        for i in range(1,4):
            sol[7+i], sol[7-i] = sol[7-i], sol[7+i]
    return tuple(sol)

# Le damos el formato descrito en el README.md
def formatear(solucion):
    # buscamos poner el 1 a la derecha del 0
    pos1 = solucion.index(1)
    if solucion[0] == 0:
        if pos1 > 6:
            solucion = reflejar(solucion)
        elif pos1 == 6:
            # si el 1 es el opuesto del 0 en la estrella, entonces ponemos el 2 a la derecha del 0
            pos2 = solucion.index(2)
            if pos2 > 6:
                solucion = reflejar(solucion)
    else:
        if pos1 > 7 or pos1 == 0:
            solucion = reflejar(solucion)
        elif pos1 == 7:
            pos2 = solucion.index(2)
            if pos2 > 7 or pos2 == 0:
                solucion = reflejar(solucion)
    return solucion

# a,b deben pertenecer a por lo menos 1 linea para que
# tenga sentido la operacion. Invito a hacer esta operación más eficiente.
def resolver_hueco(a,b,conjunto_lineas):
    sa = set()
    sb = set()
    for l in conjunto_lineas:
        s = set(l)
        if (a in s) and (b in s):
            continue
        if a in s:
            sa = s
        if b in s:
            sb = s
    interseccion = sa.intersection(sb)
    return None if not interseccion else interseccion.pop()

# a,b,c deben pertenecer todos a la misma linea
def resolver_linea(a,b,c,conjunto_lineas):
    for l in conjunto_lineas:
        s = set(l)
        if a in s and b in s and c in s:
            s.remove(a)
            s.remove(b)
            s.remove(c)
            return s.pop()

# Algoritmo para resolver una estrella dadas las condiciones iniciales y el conjunto de líneas.
def resolver_una(a,b,c,d,conjunto_lineas):
    ab = resolver_hueco(a,b,conjunto_lineas)
    bc = resolver_hueco(b,c,conjunto_lineas)
    cd = resolver_hueco(c,d,conjunto_lineas)
    ad = resolver_hueco(a,d,conjunto_lineas)

    x = resolver_linea(bc,b,ab,conjunto_lineas)
    y = resolver_linea(bc,c,cd,conjunto_lineas)

    x_ab = resolver_hueco(ab,x,conjunto_lineas)
    y_cd = resolver_hueco(cd,y,conjunto_lineas)

    return (a,b,bc,c,d,cd,y,y_cd,ad,x_ab,x,ab)

# Lista de soluciones. Modificado por resolver_varias y devuelto al main por resolver.
# Si no estás seguro de que las soluciones no son únicas transformalo en un set.
conjunto_soluciones = []

# Obtengo todas las posibles soluciones
def resolver_varias(conjunto_lineas):
    # Condiciones iniciales.
    # Nos aseguramos de que las soluciones sean únicas, es decir, que no haya soluciones
    # repetidas al darles formato. Tenemos en cuenta que las líneas están ordenadas en el 
    # conjunto de líneas, por lo que la primera línea empieza forzosamente por 0.
    # Metemos dicho 0 en la posición 0 o 1 de la línea de condiciones iniciales y generamos
    # el resto de permutaciones iniciales en dicha línea.
    a, *resto = conjunto_lineas[0]
    perms = []
    for (b,c,d) in permutations(resto, 3):
        perms.append((a,b,c,d))
        perms.append((b,a,c,d))
    for perm in perms:
        (a,b,c,d) = perm
        # Si no podemos aplicar la operación resolver_hueco en estos casos, no podemos sacar
        # una solución
        if resolver_hueco(a,b,conjunto_lineas) == None:
            continue
        elif resolver_hueco(a,d,conjunto_lineas) == None:
            continue
        elif resolver_hueco(b,c,conjunto_lineas) == None:
            continue
        elif resolver_hueco(c,d,conjunto_lineas) == None:
            continue
        # Fin de las condiciones iniciales, resolvemos, damos formato y guardamos.
        solucion = resolver_una(a,b,c,d,conjunto_lineas)
        solucion = formatear(solucion)
        conjunto_soluciones.append(solucion)

# Devuelve una lista con todas las soluciones
def resolver(conjuntos_lineas):
    # Para cada conjunto de líneas obtengo todas las soluciones posibles
    for conjunto_lineas in conjuntos_lineas:
        resolver_varias(conjunto_lineas)
    return conjunto_soluciones
