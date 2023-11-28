from math import ceil

'''
Esta funcion devuelve las cuadruplas (a,b,c,d) de numeros de 0 al 11
tales que a<b<c<d y a+b+c+d=22.
Devuelve una lista de tuplas de cuatro elementos, en concreto una lista de 33 elementos.
'''
def calcular_cuadruplas():
    s = 22
    total = []
    
    # Los comentarios de antes de los bucles indican optimizaciones a los bucles
    # 4+5+6+7=22
    for i in range(0,5):
        # i+j+(j+1)+(j+2) <= 22 <=> j <= (19-i)/3
        max_j = ceil((19-i)/3)+1
        for j in range(i+1,max_j):
            # i+j+k+11=22 <=> k=11-i-j
            min_k=max(11-i-j,j+1)
            # i+j+k+(k+1) <= 22 <=> k <= (21-i-j)/2
            max_k = ceil((21-i-j)/2)+1
            for k in range(min_k,max_k):
                l = s-i-j-k
                if(k==l): continue # No he encontrado optimización para evitar usar esto. Avanza al siguiente valor del bucle si j==k
                tupla = (i,j,k,l)
                total.append(tupla)
    return total
