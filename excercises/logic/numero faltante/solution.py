suma = 0
x = int(input())
for i in range(x - 1):
    suma += int(input())
print("La ficha faltante es la", ((x * (x + 1)) // 2) - suma)