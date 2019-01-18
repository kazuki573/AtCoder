n = int(input())
wlist = []
for i in range(n):
    wlist.append(input())
if len(wlist) != len(set(wlist)):
    print('No')
else:
    flag = True
    for i in range(n-1):
        flag = flag and (wlist[i][-1] == wlist[i+1][0])
    if flag == False:
        print('No')
    else:
        print('Yes')
