n, m, c = [int(x) for x in input().split()]
blist = [int(x) for x in input().split()]
alists = []
count = 0
for i in range(n):
    alists.append([int(x) for x in input().split()])
for alist in alists:
    clist = [x * y for (x, y) in zip(alist, blist)]
    if sum(clist) > c * (-1):
        count += 1
print(count)
