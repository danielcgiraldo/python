def generar_julianachi(max):
    julianachi = [1, 2]
    num = 2
    while num<max:
        divisores = 2
        for i in range(2, julianachi[-1] // 2 + 1):
            if(julianachi[-1] % i == 0):
                divisores += 1
        julianachi.append(julianachi[-1] + divisores)
        num = julianachi[-1]
    return julianachi

while 6>5:
    x = int(input())
    if(x == 0):
        break
    if x in generar_julianachi(x):
        print('Pertenece a la serie de Julianachi')
    else:
        print("No pertenece a la serie de Julianachi")