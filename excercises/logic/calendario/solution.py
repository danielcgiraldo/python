from calendar import monthrange
from datetime import datetime


for i in range(int(input())):
    x = input().split('/')
    info = monthrange(int(x[2]), int(x[1]))
    calendar = []
    count = 1
    for a in range(6):
        calendar.append([])
        for b in range(7):
            if((a == 0 and b >= info[0]) or (a != 0 and count <= info[1])):
                calendar[a].append(count)
                count+=1
            else: calendar[a].append(0)
    print("lun\tmar\tmie\tjue\tvie\tsab\tdom")
    for a in range(len(calendar)):
        line = ''
        if(a != 0 and calendar[a][0] == 0):
            break
        for b in range(len(calendar[0])):
            if(calendar[a][b] != 0):
                line += str(calendar[a][b]) + '\t'
            else:
                line += '\t'
        print(line.rstrip())
    print()