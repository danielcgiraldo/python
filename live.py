from datetime import datetime



for i in range(int(input())):
    count = 0
    data = input().split(' ')
    date = data[0].split('/')
    date[0] = int(date[0])
    date[1] = int(date[1])
    date[2] = int(date[2])
    for a in range(1, int(data[1]) + 1):
        if(datetime(date[0] + a, date[1], date[2]).strftime('%A') == 'Monday'):
            count += 1
    print(count)
        