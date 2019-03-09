a, b = [int(x) for x in input().split()]

if b > 3:
    if a <= 1:
        s_c = 1
    else:
        s_c = 0

    a_keta = len(str(bin(a))) - 2
    b_keta = len(str(bin(b))) - 2
    m_a = (2 ** a_keta - a) % 4
    m_b = (b - (2 ** (b_keta-1)) + 1) % 4
    #print(m_a)
    #print(m_b)

    if m_a == 0:
        s_a = 0
    elif m_a == 1:
        s_a = a
    elif m_a == 2:
        s_a = 1
    elif m_a == 3:
        s_a = a - 1

    if m_b == 0:
        s_b = 0
    elif m_b == 1:
        s_b = b
    elif m_b == 2:
        s_b = 1
    elif m_b == 3:
        s_b = b + 1
    print(s_a ^ s_b ^ s_c)
else:
    if a == 0 and b == 0:
        print(0)
    if a == 0 and b == 1:
        print(1)
    if a == 0 and b == 2:
        print(3)
    if a == 0 and b == 3:
        print(0)
    if a == 1 and b == 1:
        print(1)
    if a == 1 and b == 2:
        print(3)
    if a == 1 and b == 3:
        print(0)
    if a == 2 and b == 2:
        print(2)
    if a == 2 and b == 3:
        print(1)
    if a == 3 and b == 3:
        print(3)
