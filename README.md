# Problema de la suma de la estrella de las 6 puntas

## Problema

Dada la siguiente estrella
```
      c
     / \
a---b---d---e
 \ /     \ /
  l       f
 / \     / \
k---j---h---g
     \ /
      i
```

Poner en esta estrella los números del 0 al 11 sin repeticiones de tal forma que la suma de los números que hay en una línea sumen lo mismo en todas las líneas. Si se suma una cantidad k en todos los elementos de la estrella se sigue conservando esta propiedad, por lo que hay un isomorfismo entre las soluciones de este problema con el de soluciones de números del 1 al 12.

## Resolución

Vamos a dividir la solución en 3 partes:
- Obtener las posibles líneas (llamadas cuádruplas en el código).
- Obtener los conjuntos de 6 líneas.
- Resolver cada uno de esos conjuntos.

### Obtención de líneas/cuádruplas
En primer lugar tomo el sistema de ecuaciones que se cumple, donde $x$ sabemos que es constante:
- $a+b+d+e=x$
- $a+i+j+l=x$
- $b+c+k+l=x$
- $c+d+f+g=x$
- $e+f+h+i=x$
- $g+h+j+k=x$

Sumando todas estas ecuaciones se tiene que:
$2(a+b+c+d+e+f+g+h+i+j+k) = 2(\sum_{n=0}^{11} n) = 2 \frac{(11(11+1)}{2} = 11 · 12 = 132 = 6x \implies x = \frac{132}{6} = 22$

Luego la suma de cualquiera de las líneas es 22.

En esta fase obtendremos las líneas, cuádruplas de números,tales que la suma de todos sus elementos da 22. En código esto se traducirá en tener tuplas `(a,b,c,d)` de cuatro elementos, que son números del 0 al 11 distintos entre sí, tales que $a+b+c+d=22$. Para optimizar esta búsqueda, impondremos que $a < b < c < d$.
En esta fase salen 33 cuadruplas.

### Conjuntos de 6 líneas
Fijémonos en el dibujo de la estrella. Cada solución al problema cumple que por cada número pasan solo 2 líneas y que dos líneas cualesquiera comparten como mucho un único elemento.

Luego, por un algoritmo de backtracking, podemos obtener los conjuntos de 6 líneas tales que se cumplen estas dos condiciones. También le impondremos al algoritmo que las soluciones queden de forma ordenada según el orden en el que se han obtenido las cuádruplas en el paso anterior. Esta es una condición muy típica en este tipo de algoritmos y muy fácil de implementar dado ya el backtracking y el vector de cuádruplas. En este caso salen 20 de estos conjuntos.

Hay que también tener en cuenta que todos los conjuntos solución tendrán al principio de sus dos primeros elementos 0.

### Resolución de conjuntos

Dado un conjunto de líneas que cumple las condiciones impuestas en el paso anterior, puedo definir las siguientes operaciones:

#### Resolver Hueco:
Dada una línea $l$, tomemos dos elementos $a,b \in l$. Entonces resolver hueco consiste en tomar la otra línea en la que aparece $a$, la otra línea en la que aparece $b$ y hacer la intersección. Esta intersección puede ser vacía si las líneas son paralelas, o contiene un único elemento si se cruzan.
Esta operación es claramente conmutativa. Vamos a denotarla como $a*b$.

#### Resolver Línea:
Dado elementos $a,b,c$, resolver línea consiste en localizar la línea $l$ tal que $a,b,c \in l$ y obtener el elemento $d \in l$ tal que $d \not= a,b,c$. Si no existe dicha $l$, definimos el resultado como vacío.
Esta operación también es conmutativa y la denotaremos como $[a,b,c]$.

#### Condiciones iniciales

Para cada conjunto de líneas, podemos ordenar la primera línea de $4! = 24$ formas diferentes, pero esto nos daría soluciones repetidas ya que aparecerían reflexiones. Luego fijaremos que el 0 esté en la posición 0 o en la 1, luego nos quedan 12 posibles soluciones por cada conjunto de líneas. Si la primera línea la ordenamos como $(a,b,d,e)$, he comprobado por fuerza bruta que si existen $a*b,a*e,b*d,d*e$, entonces puedo resolver la estrella de la siguiente forma:
- $c = b*d$
- $l = a*b$
- $f = d*e$
- $i = a*e$
- $k = [b,c,l]$
- $g = [c,d,f]$
- $j = k*l$
- $h = f*g$

La solución se muestra entonces en formato `(a,b,c,d,e,d,e,f,g,h,i,j,k,l)`, donde estos valores representan el siguiente esquema:
```
      c
     / \
a---b---d---e
 \ /     \ /
  l       f
 / \     / \
k---j---h---g
     \ /
      i
```

Antes de devolver estas soluciones, se aplican las reflexiones necesarias para que se muestre en uno de los sigientes cuatro formatos:
```
      1
     / \
0---1---1---1
 \ /     \ /
  x       1
 / \     / \
x---x---x---x
     \ /
      x

      2
     / \
0---2---2---2
 \ /     \ /
  x       2
 / \     / \
x---x---x---1
     \ /
      x

      1
     / \
x---0---1---1
 \ /     \ /
  x       1
 / \     / \
x---x---x---1
     \ /
      x

      2
     / \
x---0---2---2
 \ /     \ /
  x       2
 / \     / \
x---x---1---2
     \ /
      x

```
En este formato:
- Si un número está repetido, esto significa que debe estar en algunas de las posiciones donde aparece.
- Las x simbolizan cualquier otro número.

De esta manera se tiene todas las 80 soluciones únicas a este problema.
