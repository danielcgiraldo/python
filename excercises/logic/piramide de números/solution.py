def check(num):
    if((-1 + (1 + 8 * num) ** (1 / 2)) / 2 % 1 == 0):
        print("Puede ser un racimo ideal")
    else:
        print("No puede ser un racimo ideal")

x = 2
while x != 0:
    x = int(input())
    if(x != 0):
        check(x)