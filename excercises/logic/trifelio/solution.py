a = open('trifelios.txt', 'r')
word = []
for renglon in a:
    word.append((renglon.strip()).lower())
a.close()

for w in word:
    words = w.split('-')
    flag = False
    for a in range(1, len(words[0])):
        result = ""
        for i in range(len(words[0]) - a, 0, -1):
            result += words[0][-i]
        for i in range(a):
            result += words[0][i]
        if(result == words[1]):
            flag = True
            break
    if(flag):
        print("Es trifelio")
    else:
        print("No es trifelio")