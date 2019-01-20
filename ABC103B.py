s = input()
t = input()
flag = False
for i in range(len(s)):
    s = s[-1] + s[:-1]
    if s == t:
        flag = True
        break
if flag == True:
    print('Yes')
else:
    print('No')
