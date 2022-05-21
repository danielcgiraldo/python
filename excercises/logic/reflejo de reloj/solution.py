hora = int(input())
min = int(input())

if(hora % 6 != 0):
    hora = 12 - hora
    
if(min != 0):
    hora = hora - 1
    min = 60 - min

if(hora == 0):
    hora = 12

print(f"{hora}:{min}")