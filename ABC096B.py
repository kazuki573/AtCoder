abclist = [int(x) for x in input().split()]
k = int(input())
abclist.sort(reverse=True)
abclist[0] = abclist[0] * (2**k)
print(sum(abclist))
