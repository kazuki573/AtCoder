n = int(input())
anslist = []
for i in range(n):
    yakusu = []
    if (i+1) % 2 != 0:
        for j in range(n):
            if (i+1) % (j+1) == 0:
                yakusu.append(j+1)
        if len(yakusu) == 8:
            anslist.append(i+1)
print(len(anslist))
