
def comprobar_solucion(solucion):
    (e0,e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11) = solucion
    if e0+e1+e3+e4 != 22:
        return False
    if e0+e8+e9+e11 != 22:
        return False
    if e1+e2+e11+e10 != 22:
        return False
    if e2+e3+e5+e6 != 22:
        return False
    if e4+e5+e7+e8 != 22:
        return False
    if e6+e7+e9+e10 != 22:
        return False
    return True
