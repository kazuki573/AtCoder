H, W = [int(x) for x in input().split()]
h, w = [int(x) for x in input().split()]
print(H*W - h*W - w*H + h*w)
