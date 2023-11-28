'''
En este paso he usado un algoritmo de Backtracking para obtener los conjuntos de líneas.
En esta sección, a lo que llamabamos cuádruplas vamos a llamarlo líneas. Previamente he 
construido una lista con las tuplas ordenadas de tal manera que pueda usar un algoritmo 
de este tipo.

Para alguien que no está familiarizado con este tipo de algoritmos lo único que de
saber es lo siguiente:

    - Backtracking consiste en ver el conjunto de todas las posibles soluciones incompletas 
    como un árbol (grafo dirigido conexo sin ciclos). La raíz del árbol es la solución vacía, 
    de cada nodo intermedio salen nodos tales que a la solución se le ha añadido un elemento
    y las hojas del árbol son soluciones completas, en nuestro caso conjuntos de 6 líneas.

    - Como las líneas están ordenadas en un cierto orden en el vector cuadruplas, entonces
    vamos a aprovechar dicho orden para obtener las soluciones (a,b,c,d,e,f) tales que
    a<b<c<d<e<f, donde < indica el orden de las líneas dentro del vector de cuadruplas.
    Con esto ya podamos una muy gran parte del árbol de soluciones.

    - Entonces vamos recorriendo el árbol de tal forma que, si estamos en un nodo (solución 
    incompleta, o completa si estamos en una hoja), vamos recorriendo en orden las soluciones
    hijas (si existen) volveremos hacia atrás en el árbol de tal forma que lleguemos a una
    solución no explorada. Si la solución incompleta acaba en el elemento i-ésimo de cuádruplas,
    los nodos hijos son las soluciones incompletas añadiendole un único elemento que esté entre
    el (i+1)-ésimo y el último elemento de cuadruplas.
    Este recorrido es virtual, en ningún momento creamos un árbol a través de código porque esto
    supone un gran gasto computacional. En su lugar nos apoyamos en un vector de soluciones
    incompletas y funciones recursivas para movernos por el árbol.

    - Antes de añadir una línea a una solución incompleta, nos vamos a asegurar que cumple las
    siguientes dos condiciones:
        - Cada uno de los elementos de la línea a insertar no puede aparecer 2 veces en la 
        solución incompleta. Tenemos en cuenta que todavía no hemos metido dicha línea.
        - La línea que queremos insertar no puede compartir más de dos valores con cualquier línea
        de la solución incompleta.
    Estas condiciones suponen una "poda" del árbol de soluciones, por lo que este tipo de funciones
    que determinan que parte del árbol de soluciones en un algoritmo backtracking no explorar
    se suelen llamar funciones de poda. Esta función devuelve True si se cumplen las condiciones,
    False en caso contrario.
    
    - Para mayor eficiencia y simplificidad, me he apoyado para implementar la condición 1 de 
    la función de poda en una estructura de datos auxiliar llamada memoria_de_cota. Esta
    estructura es una lista de 12 valores inicializados todos a 0 donde el valor i-ésimo
    representa cuántas veces se ha repetido el valor i para la solución incompleta actual.
    Este tipo de estructura no se encuentran en todos los algoritmos backtracking, pero son
    útiles en ciertos casos.

    - Si para cierta línea se verifica la función de poda, se inserta en la solución. Luego se 
    se sigue el algoritmo con los hijos a través de la función recursiva. Finalmente se saca la 
    la línea de la solución y continua el algoritmo. El la inserción y eliminación, además de
    modificar la solución incompleta, se modifica también la memoria_de_cota.

    - Si se llega a una solución con 6 valores (hoja), se ha llegado a un conjunto de líneas 
    que puede albergar una potencial solución. Se inserta la solución incompleta en la lista de 
    conjuntos_solucion. Previamente se pasa la solución incompleta, que era una lista, a una
    tupla por cuestiones técnicas.

    - Tras terminar el algoritmo de backtracking, tendremos en conjuntos_solucion todas los 
    posibles conjuntos de líneas que tienen capacidad de formar una solución. Por la forma en
    la que hemos recorrido y podado el árbol, las soluciones respetan y quedan ordenadas por el
    mismo orden en el que están ordenadas la líneas en vector de cuádruplas, por lo que esto
    asegura que los conjuntos de líneas son distintos unos de otros.

Tras aplicar el algoritmo de backtracking devolvemos conjuntos_solucion.

Se que se puede implementar un backtracking que pode mejor para este problema, pero esta
implementación es sencilla y relativamente rápida. Si crees que puedes mejorar este código
te invito a hacerlo.
'''

# Estructuras de datos usadas en el algoritmo de backtracking, descritas anteriormente
conjuntos_solucion = []
memoria_de_cota = [0 for _ in range(12)]
solucion_incompleta = []

# Función de poda
def funcion_poda(linea):
    # Comprobamos que no cada elemento de linea no esta repetido dos veces
    # en la solución incompleta. Usamos memoria_de_cota por eficiencia y simplidad
    for e in linea:
        if memoria_de_cota[e] == 2:
            return False
    # Comprobamos que la línea tiene dos elementos distintos en comparación del resto
    # de líneas de la solucion incompleta
    for s in solucion_incompleta:
        i=j=0
        n_elementos_iguales = 0
        while i<4 and j<4:
            if linea[i]<s[j]:
                i+=1
            elif linea[i]>s[j]:
                j+=1
            else:
                i+=1
                j+=1
                n_elementos_iguales+=1
                if n_elementos_iguales==2:
                    return False
    return True

# Función que añade la línea a la solución incompleta
def avanzar_solucion(linea):
    for e in linea:
        memoria_de_cota[e]+=1
    solucion_incompleta.append(linea)

# Función para quitar el último elemento de la solución incompleta
def retroceder_solucion():
    linea = solucion_incompleta.pop()
    for e in linea:
        memoria_de_cota[e]-=1

# Función recursiva del backtracking
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
        es_factible = funcion_poda(t)
        if es_factible:
            avanzar_solucion(t)
            backtracking(cuadruplas, j)
            retroceder_solucion()

# Interfaz para ejecutar el backtracking y obtener el conjunto de posibles soluciones.
def calcular_lineas_compatibles(cuadruplas):
    backtracking(cuadruplas, -1)
    return conjuntos_solucion
