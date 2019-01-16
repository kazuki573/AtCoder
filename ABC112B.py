n, t = [int(x) for x in input().split()]
costlist = []
for i in range(n):
    ci, ti = [int(x) for x in input().split()]
    if ti <= t:
        costlist.append(ci)
if costlist == []:
    print('TLE')
else:
    print(min(costlist))
