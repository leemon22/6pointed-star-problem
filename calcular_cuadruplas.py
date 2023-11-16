from math import ceil

# esta funcion devuelve las cuadruplas (a,b,c,d) de numeros de 0 al 11
# tales que a<b<c<d y a+b+c+d=22
def calcular_cuadruplas():
    s = 22
    total = []

    # 4+5+6+7=22
    for i in range(0,5):
        # i+j+(j+1)+(j+2) <= 22 <=> j <= (19-i)/3
        max_j = ceil((19-i)/3)+1
        for j in range(i+1,max_j):
            # i+j+k+(k+1) <= 22 <=> k <= (21-i-j)/2
            max_k = ceil((21-i-j)/2)+1
            for k in range(j+1,max_k):
                l = s-i-j-k
                if(k==l or l>11): continue
                tupla = (i,j,k,l)
                total.append(tupla)
    return total
