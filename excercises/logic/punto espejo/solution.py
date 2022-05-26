
lista = []
for i in range(int(input())):
    lista.append(float(input()))
puntos = 0
for i in range(1, len(lista)):
    sum_a = 0
    sum_b = 0
    for a in range(i):
        sum_a += lista[a]
    for b in range(i, len(lista)):
        sum_b += lista[b]
    if(sum_a == sum_b):
        puntos += 1
print(puntos)