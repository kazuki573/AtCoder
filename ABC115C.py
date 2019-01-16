n, k = [int(x) for x in input().split()]
hlist = []
for i in range(n):
    hlist.append(int(input()))
hlist.sort()
print(min([hlist[i+k-1] - hlist[i] for i in range(n-k+1)]))
