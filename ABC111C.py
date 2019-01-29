import collections

n = int(input())
v_list = [int(x) for x in input().split()]
v_oddlist = v_list[::2]
v_evenlist = v_list[1::2]
c_odd = collections.Counter(v_oddlist)
c_even = collections.Counter(v_evenlist)
if c_odd.most_common()[0][0] != c_even.most_common()[0][0]:
    print(n - c_odd.most_common()[0][1] - c_even.most_common()[0][1])
elif len(c_odd.most_common()) == 1 and len(c_even.most_common()) == 1:
    print(n - c_odd.most_common()[0][1])
else:
    a = c_odd.most_common()[0][1] + c_even.most_common()[1][1]
    b = c_odd.most_common()[1][1] + c_even.most_common()[0][1]
    if a > b:
        print(n - a)
    else:
        print(n - b)
