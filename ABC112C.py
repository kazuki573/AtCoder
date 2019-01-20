n = int(input())
infolist = []
for i in range(n):
    infolist.append([int(x) for x in input().split()])
center = []
for x in infolist:
    if x[2] != 0:
        x1, y1, h1 = x
        break
for i in range(101):
    for j in range(101):
        H = h1 + abs(x1-i) + abs(y1-j)
        if all(h == max((H - abs(x-i) - abs(y-j)) ,0) for x, y, h in infolist):
            print(i, j, H)
