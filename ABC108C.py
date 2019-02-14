n, k = [int(x) for x in input().split()]
count = 0
a = int(n / k)
count += (a + a * (a-1) * 3 + a * (a-1) * (a-2))
if k % 2 == 0:
    b = int(n / (int(k / 2))) - a
    count += (b + b * (b-1) * 3 + b * (b-1) * (b-2))
print(count)
