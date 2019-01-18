n, m, x, y = [int(x) for x in input().split()]
xlist = [int(x) for x in input().split()]
ylist = [int(x) for x in input().split()]

if max(xlist) >= min(ylist):
    print('War')
elif min(ylist) <= x or y < min(ylist):
    print('War')
else:
    print('No War')
