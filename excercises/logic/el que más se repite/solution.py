from itertools import count
import re

a = input()
matchs = []
result = []
cant = 0
for i in range(int(input())):
    matchs.append(int(input()))

matchs.sort(reverse=True)

while len(matchs) > 0:
    if(matchs.count(matchs[len(matchs) - 1]) > cant):
        result = [matchs[len(matchs) - 1]]
        cant = matchs.count(matchs[len(matchs) - 1])
    elif(matchs.count(matchs[len(matchs) - 1]) == cant):
        result.append(matchs[len(matchs) - 1])
    matchs.remove(matchs[len(matchs) - 1])

for i in result:
    print(i)