from itertools import permutations

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

conjunto_soluciones = []
def resolver_varias(conjunto_lineas):
    # Condiciones iniciales
    a, *resto = conjunto_lineas[0]
    perms = []
    for (b,c,d) in permutations(resto, 3):
        perms.append((a,b,c,d))
        perms.append((b,a,c,d))
    for perm in perms:
        (a,b,c,d) = perm
        if resolver_hueco(a,b,conjunto_lineas) == None:
            continue
        elif resolver_hueco(a,d,conjunto_lineas) == None:
            continue
        elif resolver_hueco(b,c,conjunto_lineas) == None:
            continue
        elif resolver_hueco(c,d,conjunto_lineas) == None:
            continue
        # Resolvemos
        solucion = resolver_una(a,b,c,d,conjunto_lineas)
        conjunto_soluciones.append(solucion)

def resolver(conjuntos_lineas):
    for conjunto_lineas in conjuntos_lineas:
        resolver_varias(conjunto_lineas)
    return conjunto_soluciones
