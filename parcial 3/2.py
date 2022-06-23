c = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
linea = ''
partir = 5
for i in range(len(c)):
    linea = linea + c[i]
    if len(linea) == 4:
        print(linea)
        linea = ''
if len(linea) > 1:
    print(linea)