a = open('cadena.txt', 'r')
word = []
for renglon in a:
    word.append(renglon.strip())
a.close()

for w in word:
    splited = w.split(' ')
    count = 0
    for i in range(len(splited)):
        if(i + 1 < len(splited)):
            left = splited[i][-1]
            right = splited[i + 1][0]
            for a in range(1, min(len(splited[i]), len(splited[i + 1]))): # Desde 1 porque que tengan la primera y ultima letra no mas no se vale
                left += splited[i][-a - 1]
                right += splited[i + 1][a]
                if(left[::-1] == right):
                    count += 1
                    break
    if(count == len(splited) - 1):
        print('cadena completa')
    else:
        print('cadena rota')