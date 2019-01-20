s = input()
if s[0] != "A":
    print("WA")
elif s[2:-1].count("C") != 1:
    print("WA")
else:
    flag = True
    s = s.replace("A", "").replace("C", "")
    if s.islower() != True:
        print("WA")
    else:
        print("AC")
