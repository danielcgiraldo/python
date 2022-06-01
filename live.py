a = open('./resources/haiku.txt', 'a')
print('Hola\nMundo', end='', file=a)
a.close()