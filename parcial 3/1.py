# __judge42__id__ = W99hpGGnuHVLYuRM
    
dates = {}
for i in range(int(input())):
    x = input().strip().split(" ")
    dias = x[1].split("-")
    if not x[0] in list(dates.keys()):
        dates[x[0]] = 0
    for a in range(2, len(x)):
        for d in dias:
            if x[a][-1] == d:
                dates[x[0]] += 1


items = list(dates.items())
for item in items:
    date = item[0].split("/")
    print(f"20{date[2]}-{date[1]}-{date[0]}", "=", item[1])
