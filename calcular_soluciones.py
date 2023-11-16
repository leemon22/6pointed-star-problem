from itertools import permutations

def rotar(solucion):
    pos0 = solucion.index(0)
    if pos0%2 == 1:
        pos0-=1
    sol_rotada = []
    for i in range(12):
        d = solucion[(i+pos0)%12]
        sol_rotada.append(d)
    return tuple(sol_rotada)

# Función que aplica una reflexión en el eje con dirección pasando por el 0 y el centro
# Se supone que el 0 esta en las posiciones 0 o 1
def reflejar(solucion):
    s = list(solucion)
    pos0 = solucion.index(0)
    if pos0 == 0:
        for i in range(1,6):
            s[i], s[12-i] = s[12-i], s[i]
    else:
        s[0], s[2] = s[2], s[0]
        for i in range(1,5):
            s[7-i], s[7+i] = s[7+i], s[7-i]
    return tuple(s)

# Formateo la solucion de tal forma que el 1 está entre los 6 primeros valores
# Si el 1 está en la esquina opuesta del 0, el 2 debe estar en los 5 primeros
def formatear(solucion):
    solucion = rotar(solucion)
    pos0 = solucion.index(0)
    if pos0 == 0:
        pos1 = solucion.index(1)
        if pos1 > 6:
            solucion = reflejar(solucion)
        elif pos1 == 6:
            pos2 = solucion.index(2)
            if pos2 > 6:
                solucion = reflejar(solucion)
    if pos0 == 1:
        pos1 = solucion.index(1)
        if pos1 > 7 or pos1==0:
            solucion = reflejar(solucion)
        elif pos1 == 7:
            pos2 = solucion.index(2)
            if pos2 > 7 or pos2==0:
                solucion = reflejar(solucion)
    return solucion

conjunto_soluciones = set()

# a,b deben pertenecer a por lo menos 1 linea para que
# tenga sentido la operacion
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

def resolver_varias(conjunto_lineas):
    cl = conjunto_lineas[0]
    # Condiciones iniciales
    for perm in permutations(cl, 4):
        (a,b,c,d) = perm
        if resolver_hueco(a,b,conjunto_lineas) == None:
            continue
        elif resolver_hueco(a,d,conjunto_lineas) == None:
            continue
        elif resolver_hueco(b,c,conjunto_lineas) == None:
            continue
        elif resolver_hueco(c,d,conjunto_lineas) == None:
            continue
        solucion = resolver_una(a,b,c,d,conjunto_lineas)
        solucion = formatear(solucion)
        conjunto_soluciones.add(solucion)

def resolver(conjuntos_lineas):
    for conjunto_lineas in conjuntos_lineas:
        resolver_varias(conjunto_lineas)
    return conjunto_soluciones
