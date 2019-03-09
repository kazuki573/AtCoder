n, m = [int(x) for x in input().split()]
ablist = []
for i in range(n):
    ablist.append([int(x) for x in input().split()])
ablist.sort()
count = 0
cost = 0
for i in range(n):
    count += ablist[i][1]
    cost += ablist[i][0] * ablist[i][1]
    if count >= m:
        cost -= ablist[i][0] * (count - m)
        break
print(cost)
