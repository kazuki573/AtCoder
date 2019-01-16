def difftemp_with_a(height_i):
    return abs((t - height_i * 0.006) - a)

n = int(input())
t, a = [int(x) for x in input().split()]
height = [int(x) for x in input().split()]
print(temp_i.index(min(height), key = difftemp_with_a) + 1)
