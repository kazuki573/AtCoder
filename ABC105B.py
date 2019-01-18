n = int(input())
a = int(100 / 4)
b = int(100 / 7)
flag = False
for i in range(a+1):
    for j in range(b+1):
        if (i) * 4 + (j) * 7 == n:
            flag = True
            break
    else:
        continue
    break
if flag == True:
    print('Yes')
else:
    print('No')
