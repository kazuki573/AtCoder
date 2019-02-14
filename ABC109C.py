import fractions
from functools import reduce

n, x = [int(x) for x in input().split()]
xlist = [int(x) for x in input().split()]
xlist.append(x)
xlist.sort()
distlist = []
for i in range(len(xlist) - 1):
    distlist.append(xlist[i+1] - xlist[i])

def gcd(numbers):
    return reduce(fractions.gcd, numbers)

print(gcd(distlist))
